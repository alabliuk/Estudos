using Dapper;
using readJsonLogs.Models;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace readJsonLogs.Repository
{
    public class ResponseB2bRepository
    {
        static readonly string strConnectionString = "Server=GRU3WVSQLDEV1;Database=B2BGETNETSAP_LOGFILE;trusted_connection=true;";

        public static List<ResponseB2b> GetLogs()
        {
            List<ResponseB2b> groupMeetingsList = new List<ResponseB2b>();
            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();

                groupMeetingsList = con.Query<ResponseB2b>("readJsonLogs_GetAll").ToList();
            }
            return groupMeetingsList;
        }
    }
}