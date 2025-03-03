import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-page-visualisation',
  standalone: true,
  imports: [],
  templateUrl: './page-visualisation.component.html',
  styleUrl: './page-visualisation.component.css'
})
export class PageVisualisationComponent {

  result="";
  done=false;
  constructor(private router: Router) {
  }


  consulter(){
    if(this.done){
      this.result="here's the test result";
    }else{
      this.result="test is running, no current result";
    }
  }

  topagecla(){
    this.router.navigate(['/menu']);
  }
}
