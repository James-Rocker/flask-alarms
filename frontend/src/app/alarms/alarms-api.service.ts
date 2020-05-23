import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import {API_URL} from '../env';
import {Alarms} from './alarms.model';

@Injectable()
export class AlarmsApiService {

  constructor(private http: HttpClient) {
  }

  // GET list of public, future events
  getAlarms(): Observable<Alarms[]> {
    return this.http.get<Alarms[]>(`${API_URL}/alarms`).pipe(catchError(this.errorHandler));
  }
    errorHandler(err: HttpErrorResponse | any) {
    return catchError(err.message || 'Error: Unable to complete request.');
  }
}
