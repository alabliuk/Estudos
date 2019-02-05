using Newtonsoft.Json.Linq;
using readJsonLogs.Models;
using readJsonLogs.Repository;
using System.Web.Mvc;

namespace readJsonLogs.Controllers
{
    public class ResponseB2bController : Controller
    {
        // GET: ResponseB2b
        public ActionResult Index()
        {
            return View(ResponseB2bRepository.GetLogs());
        }
    }
}