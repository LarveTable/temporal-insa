import { Routes } from '@angular/router';
import { PageClassificationComponent } from './component/page-classification/page-classification.component';
import { PageVisualisationComponent } from './component/page-visualisation/page-visualisation.component';

export const routes: Routes = [
    { path: 'menu', component: PageClassificationComponent }, 
    { path: 'board', component: PageVisualisationComponent},
    {path: '',
    redirectTo: '/menu', // auto redirect to /aroute
    pathMatch: 'full'
    }
];
