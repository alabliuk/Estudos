using Dapper;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.Hosting;

namespace WebApp.Models
{
    public class Aluno
    {
        public int id { get; set; }
        public string nome { get; set; }
        public string sobrenome { get; set; }
        public string telefone { get; set; }
        public int ra { get; set; }

        public List<Aluno> ListarAluno()
        {
            List<Aluno> Alunolist = new List<Aluno>();
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["dapperConnection"].ConnectionString))
            {
                Alunolist = db.Query<Aluno>("Select * From aluno").ToList();
            }
            return Alunolist;
        }

        public Aluno Inserir(Aluno _aluno)
        {
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["dapperConnection"].ConnectionString))
            {
                string sqlQuery = "Insert Into aluno (nome, sobrenome, telefone, ra) Values('" + _aluno.nome + "','" + _aluno.sobrenome + "','" + _aluno.telefone + "','" + _aluno.ra + "')";

                int rowsAffected = db.Execute(sqlQuery);
            }
            return _aluno;
        }

        public Aluno Atualizar(int id, Aluno _aluno)
        {
            var listaAlunos = this.ListarAluno();

            var itemIndex = listaAlunos.FindIndex(p => p.id == id);
            if (itemIndex >= 0)
            {
                using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["dapperConnection"].ConnectionString))
                {
                    string sqlQuery = "update aluno set nome='" + _aluno.nome + "',sobrenome='" + _aluno.sobrenome + "',telefone='" + _aluno.telefone + "',ra='" + _aluno.ra + "' where id=" + _aluno.id;
                    int rowsAffected = db.Execute(sqlQuery);
                }
            }
            else
            {
                return null;
            }
            return _aluno;
        }

        public bool Deletar(int id)
        {
            var listaAlunos = this.ListarAluno();
            
            var itemIndex = listaAlunos.FindIndex(p => p.id == id);
            if (itemIndex >= 0)
            {
                using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["dapperConnection"].ConnectionString))
                {
                    string sqlQuery = "Delete From aluno WHERE id = " + id;
                    int rowsAffected = db.Execute(sqlQuery);
                }
            }
            else
            {
                return false;
            }

            return true;
        }

    }
}