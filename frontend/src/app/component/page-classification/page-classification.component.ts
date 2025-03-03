import { Component } from '@angular/core';
import { DataServiceService } from '../../service/data-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-page-classification',
  standalone: true,
  imports: [],
  templateUrl: './page-classification.component.html',
  styleUrl: './page-classification.component.css'
})
export class PageClassificationComponent {
  init=false;


  constructor(private router: Router,public service:DataServiceService) {
  }

  start(){
    this.init=true;
  }

  topagevis(){
    this.router.navigate(['/board']);
  }
}
