using Dapper;
using GroupMeetingASP.NETCoreWebApp.Models;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace GroupMeetingASP.NETCoreWebApp.Repository
{
    public class GroupMeetingRepository
    {
        static string strConnectionString = "Server=localhost;Database=ProjectMeeting;Trusted_Connection=True;";

        public static IEnumerable<GroupMeeting> GetGroupMeetings()
        {
            List<GroupMeeting> groupMeetingsList = new List<GroupMeeting>();

            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();

                groupMeetingsList = con.Query<GroupMeeting>("GetGroupMeetingDetails").ToList();
            }

            return groupMeetingsList;
        }

        public static GroupMeeting GetGroupMeetingById(int? id)
        {
            GroupMeeting groupMeeting = new GroupMeeting();
            if (id == null)
                return groupMeeting;

            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();

                DynamicParameters parameter = new DynamicParameters();
                parameter.Add("@Id", id);
                groupMeeting = con.Query<GroupMeeting>("GetGroupMeetingByID", parameter, commandType: CommandType.StoredProcedure).FirstOrDefault();
            }

            return groupMeeting;
        }

        public static int AddGroupMeeting(GroupMeeting groupMeeting)
        {
            int rowAffected = 0;
            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();

                DynamicParameters parameters = new DynamicParameters();
                parameters.Add("@ProjectName", groupMeeting.ProjectName);
                parameters.Add("@GroupMeetingLeadName", groupMeeting.GroupMeetingLeadName);
                parameters.Add("@TeamLeadName", groupMeeting.TeamLeadName);
                parameters.Add("@Description", groupMeeting.Description);
                parameters.Add("@GroupMeetingDate", groupMeeting.GroupMeetingDate);

                rowAffected = con.Execute("InsertGroupMeeting", parameters, commandType: CommandType.StoredProcedure);
            }

            return rowAffected;
        }

        public static int UpdateGroupMeeting(GroupMeeting groupMeeting)
        {
            int rowAffected = 0;

            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();

                DynamicParameters parameters = new DynamicParameters();
                parameters.Add("@Id", groupMeeting.Id);
                parameters.Add("@ProjectName", groupMeeting.ProjectName);
                parameters.Add("@GroupMeetingLeadName", groupMeeting.GroupMeetingLeadName);
                parameters.Add("@TeamLeadName", groupMeeting.TeamLeadName);
                parameters.Add("@Description", groupMeeting.Description);
                parameters.Add("@GroupMeetingDate", groupMeeting.GroupMeetingDate);
                rowAffected = con.Execute("UpdateGroupMeeting", parameters, commandType: CommandType.StoredProcedure);
            }

            return rowAffected;
        }

        public static int DeleteGroupMeeting(int id)
        {
            int rowAffected = 0;
            using (IDbConnection con = new SqlConnection(strConnectionString))
            {
                if (con.State == ConnectionState.Closed)
                    con.Open();
                DynamicParameters parameters = new DynamicParameters();
                parameters.Add("@Id", id);
                rowAffected = con.Execute("DeleteGroupMeeting", parameters, commandType: CommandType.StoredProcedure);

            }

            return rowAffected;
        }
    }
}
