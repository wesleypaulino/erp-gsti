import { Component, OnInit } from '@angular/core';
import { TecnicoService } from './services/tecnico.service';
import { Tecnico } from './models/tecnico';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  tecnico = {} as Tecnico;
  tecnicos: Tecnico[] = [];

  constructor(private TecnicoService: TecnicoService) {}
  
  ngOnInit() {
    this.getTecnicos();
  }

  // defini se um tecnico será criado ou atualizado
  saveCar(form: NgForm) {
    if (this.tecnico.id !== undefined) {
      this.TecnicoService.updateTecnico(this.tecnico).subscribe(() => {
        this.cleanForm(form);
      });
    } else {
      this.TecnicoService.saveTecnico(this.tecnico).subscribe(() => {
        this.cleanForm(form);
      });
    }
  }

  // Chama o serviço para obtém todos os tecnicos
  getTecnicos() {
    this.TecnicoService.getTecnicos().subscribe((tecnicos: Tecnico[]) => {
      this.tecnicos = tecnicos;
    });
  }

  // deleta um tecnico
  deleteTecnico(tecnico: Tecnico) {
    this.TecnicoService.deleteTecnico(tecnico).subscribe(() => {
      /*this.getTecnicos()*/
      alert('Tecnico deletado');
    });
  }

  // copia o carro para ser editado.
  editTecnico(tecnico: Tecnico) {
    /* 
    this.tecnico = { ...tecnico }
    */
   alert('Tecnico editado');
  }

  // limpa o formulario
  cleanForm(form: NgForm) {
    this.getTecnicos();
    form.resetForm();
    this.tecnico = {} as Tecnico;
  }

}