import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {AlarmsApiService} from './alarms/alarms-api.service';
import {Alarms} from './alarms/alarms.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  alarmsListSubs: Subscription;
  alarmList: Alarms[];

  constructor(private alarmsApi: AlarmsApiService) {
  }

  ngOnInit() {
    this.alarmsListSubs = this.alarmsApi
      .getAlarms()
      .subscribe(res => {
          this.alarmList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.alarmsListSubs.unsubscribe();
  }
}
