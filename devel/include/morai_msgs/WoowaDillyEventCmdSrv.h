// Generated by gencpp from file morai_msgs/WoowaDillyEventCmdSrv.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_WOOWADILLYEVENTCMDSRV_H
#define MORAI_MSGS_MESSAGE_WOOWADILLYEVENTCMDSRV_H

#include <ros/service_traits.h>


#include <morai_msgs/WoowaDillyEventCmdSrvRequest.h>
#include <morai_msgs/WoowaDillyEventCmdSrvResponse.h>


namespace morai_msgs
{

struct WoowaDillyEventCmdSrv
{

typedef WoowaDillyEventCmdSrvRequest Request;
typedef WoowaDillyEventCmdSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct WoowaDillyEventCmdSrv
} // namespace morai_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrv > {
  static const char* value()
  {
    return "1955b6d4c59847467e59b20a60d97dee";
  }

  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrv&) { return value(); }
};

template<>
struct DataType< ::morai_msgs::WoowaDillyEventCmdSrv > {
  static const char* value()
  {
    return "morai_msgs/WoowaDillyEventCmdSrv";
  }

  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrv&) { return value(); }
};


// service_traits::MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrvRequest> should match
// service_traits::MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrv >
template<>
struct MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::WoowaDillyEventCmdSrvRequest> should match
// service_traits::DataType< ::morai_msgs::WoowaDillyEventCmdSrv >
template<>
struct DataType< ::morai_msgs::WoowaDillyEventCmdSrvRequest>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::WoowaDillyEventCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrvResponse> should match
// service_traits::MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrv >
template<>
struct MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::WoowaDillyEventCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::WoowaDillyEventCmdSrvResponse> should match
// service_traits::DataType< ::morai_msgs::WoowaDillyEventCmdSrv >
template<>
struct DataType< ::morai_msgs::WoowaDillyEventCmdSrvResponse>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::WoowaDillyEventCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::WoowaDillyEventCmdSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_WOOWADILLYEVENTCMDSRV_H