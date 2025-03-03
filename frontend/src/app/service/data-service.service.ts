import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  constructor() { }
  
  ListAlgo:string[]=["Rocket","Resnet"];
  ListDataset:string[]=["set1","set2"];
}
