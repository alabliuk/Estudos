using GroupMeetingASP.NETCoreWebApp.Models;
using GroupMeetingASP.NETCoreWebApp.Repository;
using Microsoft.AspNetCore.Mvc;

namespace GroupMeetingASP.NETCoreWebApp.Controllers
{
    public class GroupMeetingController : Controller
    {
        public IActionResult Index()
        {
            return View(GroupMeetingRepository.GetGroupMeetings());
        }

        [HttpGet]
        public IActionResult AddGroupMeeting()
        {
            return View();
        }

        [HttpPost]
        public IActionResult AddGroupMeeting([Bind] GroupMeeting groupMeeting)
        {
            if (ModelState.IsValid)
            {
                if (GroupMeetingRepository.AddGroupMeeting(groupMeeting) > 0)
                {
                    return RedirectToAction("Index");
                }
            }
            return View(groupMeeting);
        }

        [HttpGet]
        public IActionResult EditMeeting(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }
            GroupMeeting group = GroupMeetingRepository.GetGroupMeetingById(id);
            if (group == null)
                return NotFound();
            return View(group);
        }

        [HttpPost]
        public IActionResult EditMeeting(int id, [Bind] GroupMeeting groupMeeting)
        {
            if (id != groupMeeting.Id)
                return NotFound();

            if (ModelState.IsValid)
            {
                GroupMeetingRepository.UpdateGroupMeeting(groupMeeting);
                return RedirectToAction("Index");
            }
            return View(groupMeeting);
        }

        public IActionResult DeleteMeeting(int id)
        {
            GroupMeeting group = GroupMeetingRepository.GetGroupMeetingById(id);
            if (group == null)
            {
                return NotFound();
            }

            return View(group);
        }
        [HttpPost]
        public IActionResult DeleteMeeting(int id, GroupMeeting groupMeeting)
        {
            if (GroupMeetingRepository.DeleteGroupMeeting(id) > 0)
            {
                return RedirectToAction("Index");
            }
            return View(groupMeeting);
        }
    }
}