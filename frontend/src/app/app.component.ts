import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PageClassificationComponent } from './component/page-classification/page-classification.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,PageClassificationComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'prototype for time serie classification';
}
