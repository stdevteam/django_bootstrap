import { Component, OnInit, Input } from '@angular/core';

import { ItemModel } from 'src/app/models/item.model';
import { ItemsService } from 'src/app/services/items.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.scss']
})
export class ItemComponent implements OnInit {

  @Input() itemData: ItemModel;

  constructor(
    private itemsService: ItemsService
  ) { }

  ngOnInit() {
  }

  public onCheck($event) {
    this.itemData.value = $event.target.checked;
    if (this.itemData.isCreated) {
      this.itemsService.editItem(this.itemData.id, this.itemData.value).subscribe(
        res => {},
        (err: HttpErrorResponse) => {
          console.log(err);
          $event.target.checked = !$event.target.checked;
        }
      );
    } else {
      this.itemData.isCreated = true;
      this.itemsService.additem(this.itemData).subscribe(
        (res: ItemModel) => {
          this.itemData.id = res.id;
        },
        (err: HttpErrorResponse) => {
          this.itemData.isCreated = false;
          $event.target.checked = !$event.target.checked;
        }
      );
    }
  }

}
