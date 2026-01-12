\# HTTP — notatki (Dzień 3)



\## Metody

\- GET — odczyt

\- POST — tworzenie

\- PUT — pełna aktualizacja

\- PATCH — częściowa aktualizacja

\- DELETE — usuwanie



\## Statusy (must-know)

\- 200 OK

\- 201 Created

\- 204 No Content

\- 400 Bad Request

\- 401 Unauthorized

\- 403 Forbidden

\- 404 Not Found

\- 409 Conflict

\- 422 Unprocessable Entity (częste w FastAPI/Pydantic)

\- 500 Internal Server Error



\## Nagłówki (najważniejsze)

\- Content-Type: application/json

\- Accept: application/json

\- Authorization: Bearer <token>

\- User-Agent



\## Cookies vs tokeny (security)



\### Cookies

\- przeglądarka wysyła automatycznie

\- często do sesji

\- ryzyko: CSRF (bo idą automatycznie)

\- zabezpieczenia: HttpOnly, Secure, SameSite



\### Tokeny (np. JWT w Authorization)

\- klient wysyła jawnie (Bearer)

\- ryzyko: wyciek tokena (np. XSS / logi)

\- plus: wygodne dla API, mobile, integracji



\### Ściąga

\- cookie-session: wygodne dla web (ale CSRF)

\- bearer token: wygodne dla API (ale chroń przed wyciekiem)



