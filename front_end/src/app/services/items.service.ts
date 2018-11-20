import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ItemModel } from '../models/item.model';

@Injectable({
    providedIn: 'root'
})
export class ItemsService {

    constructor(private http: HttpClient) {
    }

    public getitems(): Observable<ItemModel[]> {
        return this.http.get<ItemModel[]>(`${environment.api}checkmarks/`);
    }

    public editItem(id: number, value: boolean): Observable<any> {
        return this.http.patch(`${environment.api}checkmarks/${id}/`, {value});
    }

    public additem(item: ItemModel): Observable<any> {
        return this.http.post(`${environment.api}checkmarks/`, item);
    }
}
