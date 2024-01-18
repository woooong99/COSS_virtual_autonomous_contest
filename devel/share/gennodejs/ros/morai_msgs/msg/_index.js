
"use strict";

let SetTrafficLight = require('./SetTrafficLight.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');
let TrafficLight = require('./TrafficLight.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let CtrlCmd = require('./CtrlCmd.js');
let WaitForTick = require('./WaitForTick.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let VehicleCollision = require('./VehicleCollision.js');
let SkateboardCtrlCmd = require('./SkateboardCtrlCmd.js');
let SkidSteer6wUGVCtrlCmd = require('./SkidSteer6wUGVCtrlCmd.js');
let IntscnTL = require('./IntscnTL.js');
let FaultInjection_Controller = require('./FaultInjection_Controller.js');
let FaultStatusInfo = require('./FaultStatusInfo.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let IntersectionControl = require('./IntersectionControl.js');
let SyncModeAddObject = require('./SyncModeAddObject.js');
let PRStatus = require('./PRStatus.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');
let ReplayInfo = require('./ReplayInfo.js');
let FaultInjection_Tire = require('./FaultInjection_Tire.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let FaultStatusInfo_Sensor = require('./FaultStatusInfo_Sensor.js');
let ObjectStatusExtended = require('./ObjectStatusExtended.js');
let FaultInjection_Response = require('./FaultInjection_Response.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let GhostMessage = require('./GhostMessage.js');
let EgoVehicleStatusExtended = require('./EgoVehicleStatusExtended.js');
let PREvent = require('./PREvent.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let SkateboardStatus = require('./SkateboardStatus.js');
let WoowaDillyStatus = require('./WoowaDillyStatus.js');
let PRCtrlCmd = require('./PRCtrlCmd.js');
let SyncModeRemoveObject = require('./SyncModeRemoveObject.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');
let SVADC = require('./SVADC.js');
let VehicleSpec = require('./VehicleSpec.js');
let FaultInjection_Sensor = require('./FaultInjection_Sensor.js');
let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let ObjectStatusListExtended = require('./ObjectStatusListExtended.js');
let CollisionData = require('./CollisionData.js');
let GPSMessage = require('./GPSMessage.js');
let SkidSteer6wUGVStatus = require('./SkidSteer6wUGVStatus.js');
let ObjectStatus = require('./ObjectStatus.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let MultiEgoSetting = require('./MultiEgoSetting.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let DillyCmd = require('./DillyCmd.js');
let DillyCmdResponse = require('./DillyCmdResponse.js');
let EgoDdVehicleStatus = require('./EgoDdVehicleStatus.js');
let RadarDetections = require('./RadarDetections.js');
let EventInfo = require('./EventInfo.js');
let SensorPosControl = require('./SensorPosControl.js');
let MultiPlayEventRequest = require('./MultiPlayEventRequest.js');
let ERP42Info = require('./ERP42Info.js');
let FaultStatusInfo_Vehicle = require('./FaultStatusInfo_Vehicle.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let RadarDetection = require('./RadarDetection.js');
let MapSpec = require('./MapSpec.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let FaultStatusInfo_Overall = require('./FaultStatusInfo_Overall.js');
let SaveSensorData = require('./SaveSensorData.js');
let MultiPlayEventResponse = require('./MultiPlayEventResponse.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let DdCtrlCmd = require('./DdCtrlCmd.js');
let Lamps = require('./Lamps.js');

module.exports = {
  SetTrafficLight: SetTrafficLight,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
  TrafficLight: TrafficLight,
  WaitForTickResponse: WaitForTickResponse,
  CtrlCmd: CtrlCmd,
  WaitForTick: WaitForTick,
  SyncModeCmd: SyncModeCmd,
  VehicleCollision: VehicleCollision,
  SkateboardCtrlCmd: SkateboardCtrlCmd,
  SkidSteer6wUGVCtrlCmd: SkidSteer6wUGVCtrlCmd,
  IntscnTL: IntscnTL,
  FaultInjection_Controller: FaultInjection_Controller,
  FaultStatusInfo: FaultStatusInfo,
  ScenarioLoad: ScenarioLoad,
  IntersectionControl: IntersectionControl,
  SyncModeAddObject: SyncModeAddObject,
  PRStatus: PRStatus,
  NpcGhostInfo: NpcGhostInfo,
  MoraiSimProcStatus: MoraiSimProcStatus,
  MoraiSimProcHandle: MoraiSimProcHandle,
  ReplayInfo: ReplayInfo,
  FaultInjection_Tire: FaultInjection_Tire,
  SyncModeInfo: SyncModeInfo,
  IntersectionStatus: IntersectionStatus,
  GetTrafficLightStatus: GetTrafficLightStatus,
  FaultStatusInfo_Sensor: FaultStatusInfo_Sensor,
  ObjectStatusExtended: ObjectStatusExtended,
  FaultInjection_Response: FaultInjection_Response,
  NpcGhostCmd: NpcGhostCmd,
  GhostMessage: GhostMessage,
  EgoVehicleStatusExtended: EgoVehicleStatusExtended,
  PREvent: PREvent,
  MoraiSrvResponse: MoraiSrvResponse,
  SkateboardStatus: SkateboardStatus,
  WoowaDillyStatus: WoowaDillyStatus,
  PRCtrlCmd: PRCtrlCmd,
  SyncModeRemoveObject: SyncModeRemoveObject,
  MoraiTLIndex: MoraiTLIndex,
  SVADC: SVADC,
  VehicleSpec: VehicleSpec,
  FaultInjection_Sensor: FaultInjection_Sensor,
  EgoVehicleStatus: EgoVehicleStatus,
  ObjectStatusListExtended: ObjectStatusListExtended,
  CollisionData: CollisionData,
  GPSMessage: GPSMessage,
  SkidSteer6wUGVStatus: SkidSteer6wUGVStatus,
  ObjectStatus: ObjectStatus,
  MoraiTLInfo: MoraiTLInfo,
  MultiEgoSetting: MultiEgoSetting,
  SyncModeResultResponse: SyncModeResultResponse,
  SyncModeCmdResponse: SyncModeCmdResponse,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  VehicleCollisionData: VehicleCollisionData,
  DillyCmd: DillyCmd,
  DillyCmdResponse: DillyCmdResponse,
  EgoDdVehicleStatus: EgoDdVehicleStatus,
  RadarDetections: RadarDetections,
  EventInfo: EventInfo,
  SensorPosControl: SensorPosControl,
  MultiPlayEventRequest: MultiPlayEventRequest,
  ERP42Info: ERP42Info,
  FaultStatusInfo_Vehicle: FaultStatusInfo_Vehicle,
  VehicleSpecIndex: VehicleSpecIndex,
  RadarDetection: RadarDetection,
  MapSpec: MapSpec,
  ObjectStatusList: ObjectStatusList,
  FaultStatusInfo_Overall: FaultStatusInfo_Overall,
  SaveSensorData: SaveSensorData,
  MultiPlayEventResponse: MultiPlayEventResponse,
  SyncModeSetGear: SyncModeSetGear,
  MapSpecIndex: MapSpecIndex,
  DdCtrlCmd: DdCtrlCmd,
  Lamps: Lamps,
};
