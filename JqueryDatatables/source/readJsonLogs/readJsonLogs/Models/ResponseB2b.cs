using System;
using System.ComponentModel.DataAnnotations;

namespace readJsonLogs.Models
{
    public class ResponseB2b
    {
        [Display(Name = "Data")]
        public DateTime Date { get; set; }
        [Display(Name = "Serviço")]
        public string RequestName { get; set; }
        [Display(Name = "OS")]
        public string ClientProcessOrder { get; set; }
        [Display(Name = "Json")]
        public string Json { get; set; }
    }
}