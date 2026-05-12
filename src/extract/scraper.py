import requests
import pandas as pd
import time
from datetime import datetime
from tqdm import tqdm
from typing import Optional
from pathlib import Path

ROOT_PATH = Path("../").resolve()
SAVE_PATH = ROOT_PATH / "dataset"

class ScraperError(Exception):
    pass


class Scraper:

    # ------------------------------------------------------------------
    # Constants
    # ------------------------------------------------------------------

    BASE_URL = "https://beta-api.sub100.com.br/api/properties"

    CITY_ID = "e430c297-02f1-42b6-ae35-57b8d94b499a"

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept":  "application/json",
        "Referer": "https://sub100.com.br/",
        "Origin":  "https://sub100.com.br",
    }

    MAPA_TIPOS = {
        "residencial":              "9321def4-9c0f-4088-a9c8-4cf5e5fb3643",
        "comerciais":               "7699479b-f111-49b8-b114-1149419b4111",
        "negocios-e-investimentos": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
        "imoveis-para-lazer":       "b2c3d4e5-f6g7-h8i9-j0k1-l2m3n4o5p6q7",
        "terrenos-e-areas":         "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    }

    MAPA_NEGOCIO = {
        "venda":   "289fbbf4-6fd3-47db-85fe-e72772efd6c0",
        "locacao": "9e867846-fb2b-491e-954d-bbe68a1b88eb",
    }

    COLUMNS = [
        "suites", "rooms", "dorms", "bwc", "parking_spaces",
        "private_area", "total_area", "total", "variation",
        "apartment", "floor", "dream_property", "mcmv",
        "academic_regions", "digital_fair", "subtype_name",
        "lot", "block", "tags", "royalty_value",
        "latitude", "longitude",
        "address.complete", "address.street", "address.number",
        "address.neighborhood", "address.city", "address.uf",
        "address.complement", "condo.name", "advertise.name"
    ]

    REQUEST_DELAY = 0.5
    REQUEST_TIMEOUT = 20

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _resolve_uuids(self, tipo: str, finalidade: str) -> tuple[str, str]:
        tipo_uuid    = self.MAPA_TIPOS.get(tipo.lower(),      self.MAPA_TIPOS["residencial"])
        negocio_uuid = self.MAPA_NEGOCIO.get(finalidade.lower(), self.MAPA_NEGOCIO["venda"])

        if tipo.lower() not in self.MAPA_TIPOS:
            print(f"[AVISO] Tipo '{tipo}' nao mapeado. Usando 'residencial'.")
        if finalidade.lower() not in self.MAPA_NEGOCIO:
            print(f"[AVISO] Finalidade '{finalidade}' nao mapeada. Usando 'venda'.")

        return tipo_uuid, negocio_uuid

    def _build_url(
        self,
        local: str,
        finalidade: str,
        tipo_uuid: str,
        negocio_uuid: str,
        pagina: int,
    ) -> str:
        empty_range = "%7B%22min%22:%22%22,%22max%22:%22%22%7D"
        empty_dorms = "%7B%22suites%22:%22%22,%22dorms%22:%22%22%7D"

        return (
            f"{self.BASE_URL}?"
            f"value={empty_range}&"
            f"dorms={empty_dorms}&"
            f"condo_value={empty_range}&"
            f"installmentValues={empty_range}&"
            f"pax=&page={pagina}&exact=false&order=relevants&"
            f"business_type={negocio_uuid}&"
            f"business={finalidade.lower()}&"
            f"type={tipo_uuid}&"
            f"city={local.lower()}&"
            f"local={self.CITY_ID}"
        )

    def _fetch_page(self, url: str, pagina: int) -> Optional[list]:
        try:
            response = requests.get(url, headers=self.HEADERS, timeout=self.REQUEST_TIMEOUT)

            if response.status_code == 200:
                data = response.json().get("data", [])
                return data if data else None

            print(f"[ERRO] Status {response.status_code} na página {pagina}.")
            return None

        except requests.exceptions.Timeout:
            print(f"[ERRO] Timeout na página {pagina}.")
            return None
        except requests.exceptions.ConnectionError:
            print(f"[ERRO] Falha de conexão na página {pagina}.")
            return None
        except Exception as e:
            print(f"[ERRO] Falha inesperada na página {pagina}: {e}")
            return None

    def _parse_response(self, all_data: list) -> pd.DataFrame:
        if not all_data:
            raise ScraperError("Nenhum dado coletado. Verifique os parametros da busca.")

        df = pd.json_normalize(all_data)

        missing = [col for col in self.COLUMNS if col not in df.columns]
        if missing:
            print(f"[AVISO] Colunas ausentes na resposta: {missing}")

        available = [col for col in self.COLUMNS if col in df.columns]
        return df[available]
    
    def _save_full_csv(self, all_data:list, local:str, tipo:str, finalidade:str) -> pd.DataFrame:
        if not all_data:
            raise ScraperError("Não foi possível salvar o dataset completo.")
        
        df = pd.json_normalize(all_data)
        data = datetime.today().strftime("%Y-%m-%d")
        return df.to_csv(SAVE_PATH / f"{local}/{tipo}/{finalidade}/{data}")
        
    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def sub_cem(
        self,
        local: str = "maringa-pr",
        tipo: str = "residencial",
        finalidade: str = "venda",
        n_pages: int = 5,
    ) -> pd.DataFrame:
        tipo_uuid, negocio_uuid = self._resolve_uuids(tipo, finalidade)
        all_data: list = []

        desc = f"Coletando {tipo} ({finalidade}) em {local}"
        for pagina in tqdm(range(1, n_pages + 1), desc=desc):
            url  = self._build_url(local, finalidade, tipo_uuid, negocio_uuid, pagina)
            data = self._fetch_page(url, pagina)

            if data is None:
                print(f"[INFO] Coleta encerrada na página {pagina}.")
                break

            all_data.extend(data)
            time.sleep(self.REQUEST_DELAY)

        print(f"[OK] {len(all_data)} imóveis coletados em {pagina} páginas.")
        self._save_full_csv(all_data, self.local, self.local, self.finalidade)
        return self._parse_response(all_data)