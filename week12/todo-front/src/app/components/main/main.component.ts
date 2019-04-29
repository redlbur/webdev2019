import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../../models/models';
import {ProviderService} from '../../services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];
  public name = '';
  public taskName = '';
  public taskStatus = '';
  public targetTaskList: TaskList;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }
  getTaskOfTaskList(taskList: TaskList) {
    this.targetTaskList = taskList;
    this.provider.getTasks(taskList.id).then(res => {this.tasks = res; });
  }

  createTaskList() {
      if (this.name !== '') {
        this.provider.createTaskList(this.name).then(res => {
          this.name = '';
          this.taskLists.push(res);
        });
      }
  }

  updateTaskList(taskList: TaskList) {
    this.provider.updateTaskList(taskList).then(res => {});
  }

  deleteTaskList(taskList: TaskList) {
    this.provider.deleteTaskList(taskList).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }

  updateTask(task: Task) {
    this.provider.updateTask(task).then(res => {});
  }

  deleteTask(task: Task) {
    this.provider.deleteTask(task).then(res => {
      this.provider.getTasks(task.task_list.id).then(r => {
        this.tasks = r;
      });
    });
  }

  /*createTask() {
    let createdTask: Task;
    createdTask.name = this.name;
    createdTask.status = this.taskStatus;
    createdTask.created_at = Date.now();
    createdTask.due_on = Date.now() + (1000 * 60 * 60 * 24);
    createdTask.task_list = this.targetTaskList;
    this.provider.createTask(createdTask).then(res => {
      this.taskName = '';
      this.taskStatus = '';
    });
  }*/
}
