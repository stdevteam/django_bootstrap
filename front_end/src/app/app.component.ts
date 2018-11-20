import { Component, OnInit } from '@angular/core';
import { ItemsService } from './services/items.service';
import { ItemModel } from './models/item.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  public items: ItemModel[][] = [
    [
      {
        id: 1,
        name: 'Name1',
        type: 'readings',
        isCreated: false,
        value: false
      },
      {
        id: 2,
        name: 'Name2',
        type: 'questions',
        isCreated: false,
        value: false
      },
      {
        id: 3,
        name: 'Name3',
        type: 'readings',
        isCreated: false,
        value: false
      },
      {
        id: 4,
        name: 'Name4',
        type: 'questions',
        isCreated: false,
        value: false
      },
    ],
    [
      {
        id: 5,
        name: 'Name5',
        type: 'readings',
        isCreated: false,
        value: false
      },
      {
        id: 6,
        name: 'Name6',
        type: 'questions',
        isCreated: false,
        value: false
      },
      {
        id: 7,
        name: 'Name7',
        type: 'readings',
        isCreated: false,
        value: false
      },
      {
        id: 8,
        name: 'Name8',
        type: 'questions',
        isCreated: false,
        value: false
      }
    ]
  ];

  constructor(private itemsService: ItemsService) {}

  ngOnInit() {
    this.itemsService.getitems().subscribe(
      (dataFromBack: ItemModel[]) => {
        dataFromBack.forEach((itemFromBack: ItemModel) => {
          this.items.map((section: ItemModel[]) => {
            const existingItem: ItemModel = section.find((sectionItem: ItemModel) => sectionItem.name === itemFromBack.name);
            if (existingItem) {
              existingItem.id = itemFromBack.id;
              existingItem.isCreated = true;
              existingItem.value = itemFromBack.value;
            }
          });
        });
      }
    );
  }
}
