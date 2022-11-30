import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { Tecnico } from '../models/tecnico';

@Injectable({
  providedIn: 'root'
})
export class TecnicoService {

  url = 'http://127.0.0.1:8000/tecnicos'; // api rest fake

  // injetando o HttpClient
  constructor(private httpClient: HttpClient) { }

  // Headers
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  // Obtem todos os carros
  getTecnicos(): Observable<Tecnico[]> {
    return this.httpClient.get<Tecnico[]>(this.url)
      .pipe(
        retry(2),
        catchError(this.handleError))
  }

  // Obtem tecncio id
  getTecnicosById(id: number): Observable<Tecnico> {
    return this.httpClient.get<Tecnico>(this.url + '/' + id)
      .pipe(
        retry(2),
        catchError(this.handleError)
      )
  }

  // salva um carro
  saveTecnico(tecnico: Tecnico): Observable<Tecnico> {
    return this.httpClient.post<Tecnico>(this.url, JSON.stringify(tecnico), this.httpOptions)
      .pipe(
        retry(2),
        catchError(this.handleError)
      )
  }

  // utualiza um carro
  updateTecnico(tecnico: Tecnico): Observable<Tecnico> {
    return this.httpClient.put<Tecnico>(this.url + '/' + tecnico.id, JSON.stringify(tecnico), this.httpOptions)
      .pipe(
        retry(1),
        catchError(this.handleError)
      )
  }

  // deleta um carro
  deleteTecnico(tecnico: Tecnico) {
    return this.httpClient.delete<Tecnico>(this.url + '/' + tecnico.id, this.httpOptions)
      .pipe(
        retry(1),
        catchError(this.handleError)
      )
  }

  // Manipulação de erros
  handleError(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Erro ocorreu no lado do client
      errorMessage = error.error.message;
    } else {
      // Erro ocorreu no lado do servidor
      errorMessage = `Código do erro: ${error.status}, ` + `menssagem: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  };

}