# SNMP MIB module (ECRESO-FM-TRANS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\worldcastsystems\ECRESO-FM-TRANS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:23 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysLocation",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

transmitter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2)
)
if mibBuilder.loadTexts:
    transmitter.setRevisions(
        ("2023-01-10 10:47",
         "2022-12-05 13:19",
         "2022-10-11 15:00",
         "2022-07-27 14:20",
         "2022-06-28 12:00",
         "2022-06-24 13:52",
         "2021-01-26 14:13",
         "2021-01-25 14:43",
         "2021-01-20 12:09",
         "2020-08-06 13:22",
         "2020-08-06 10:02",
         "2020-08-06 08:04",
         "2020-08-06 07:43",
         "2020-08-05 07:16",
         "2020-03-17 15:35",
         "2018-07-05 16:51",
         "2018-06-19 09:27",
         "2018-06-06 13:01",
         "2018-06-01 08:10",
         "2018-05-30 16:01",
         "2017-06-02 17:42",
         "2017-05-17 09:12",
         "2017-02-21 15:53",
         "2017-02-17 10:20",
         "2017-02-15 14:00",
         "2016-05-13 08:30",
         "2016-04-11 18:46",
         "2016-04-11 08:18",
         "2016-04-07 09:47",
         "2016-02-24 09:41",
         "2016-01-19 08:59",
         "2015-01-30 12:48",
         "2014-12-02 15:54",
         "2014-09-24 10:08",
         "2014-07-18 08:04",
         "2014-03-04 11:01",
         "2013-11-07 14:41",
         "2013-10-25 14:55",
         "2013-10-24 09:31",
         "2013-09-26 09:53",
         "2013-09-11 14:34",
         "2013-08-08 09:09",
         "2013-07-18 14:56",
         "2013-07-17 13:34",
         "2013-07-03 13:54",
         "2013-06-25 13:56",
         "2013-06-06 16:27",
         "2013-04-22 09:51",
         "2013-03-18 08:33",
         "2013-02-26 14:09",
         "2013-02-08 14:24",
         "2012-12-13 16:03",
         "2012-07-11 15:04",
         "2012-01-10 11:32")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ecreso_ObjectIdentity = ObjectIdentity
ecreso = _Ecreso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404)
)
if mibBuilder.loadTexts:
    ecreso.setStatus("current")
_Transv3_ObjectIdentity = ObjectIdentity
transv3 = _Transv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3)
)
if mibBuilder.loadTexts:
    transv3.setStatus("current")
_Fm_ObjectIdentity = ObjectIdentity
fm = _Fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1)
)
if mibBuilder.loadTexts:
    fm.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0)
)
if mibBuilder.loadTexts:
    events.setStatus("current")
_EventBindings_ObjectIdentity = ObjectIdentity
eventBindings = _EventBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eventBindings.setStatus("current")
_EventTxLocalModeBindings_ObjectIdentity = ObjectIdentity
eventTxLocalModeBindings = _EventTxLocalModeBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eventTxLocalModeBindings.setStatus("current")
_EventTimeStampTxLocalMode_Type = DateAndTime
_EventTimeStampTxLocalMode_Object = MibScalar
eventTimeStampTxLocalMode = _EventTimeStampTxLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 1, 1),
    _EventTimeStampTxLocalMode_Type()
)
eventTimeStampTxLocalMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxLocalMode.setStatus("current")
_EventTxAl3dBBindings_ObjectIdentity = ObjectIdentity
eventTxAl3dBBindings = _EventTxAl3dBBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eventTxAl3dBBindings.setStatus("current")
_EventTimeStampTxAl3dB_Type = DateAndTime
_EventTimeStampTxAl3dB_Object = MibScalar
eventTimeStampTxAl3dB = _EventTimeStampTxAl3dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 2, 1),
    _EventTimeStampTxAl3dB_Type()
)
eventTimeStampTxAl3dB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAl3dB.setStatus("current")
_EventTxAlFaultBindings_ObjectIdentity = ObjectIdentity
eventTxAlFaultBindings = _EventTxAlFaultBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eventTxAlFaultBindings.setStatus("current")
_EventTimeStampTxAlFault_Type = DateAndTime
_EventTimeStampTxAlFault_Object = MibScalar
eventTimeStampTxAlFault = _EventTimeStampTxAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 3, 1),
    _EventTimeStampTxAlFault_Type()
)
eventTimeStampTxAlFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAlFault.setStatus("current")
_EventTxAlWarningBindings_ObjectIdentity = ObjectIdentity
eventTxAlWarningBindings = _EventTxAlWarningBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    eventTxAlWarningBindings.setStatus("current")
_EventTimeStampTxAlWarning_Type = DateAndTime
_EventTimeStampTxAlWarning_Object = MibScalar
eventTimeStampTxAlWarning = _EventTimeStampTxAlWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 4, 1),
    _EventTimeStampTxAlWarning_Type()
)
eventTimeStampTxAlWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAlWarning.setStatus("current")
_EventTxAlVSWRBindings_ObjectIdentity = ObjectIdentity
eventTxAlVSWRBindings = _EventTxAlVSWRBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    eventTxAlVSWRBindings.setStatus("current")
_EventTimeStampTxAlVSWR_Type = DateAndTime
_EventTimeStampTxAlVSWR_Object = MibScalar
eventTimeStampTxAlVSWR = _EventTimeStampTxAlVSWR_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 5, 1),
    _EventTimeStampTxAlVSWR_Type()
)
eventTimeStampTxAlVSWR.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAlVSWR.setStatus("current")
_EventTxAlInterlockAntBindings_ObjectIdentity = ObjectIdentity
eventTxAlInterlockAntBindings = _EventTxAlInterlockAntBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    eventTxAlInterlockAntBindings.setStatus("current")
_EventTimeStampTxAlInterlockAnt_Type = DateAndTime
_EventTimeStampTxAlInterlockAnt_Object = MibScalar
eventTimeStampTxAlInterlockAnt = _EventTimeStampTxAlInterlockAnt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 6, 1),
    _EventTimeStampTxAlInterlockAnt_Type()
)
eventTimeStampTxAlInterlockAnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAlInterlockAnt.setStatus("current")
_EventTxAlInterlockLoadBindings_ObjectIdentity = ObjectIdentity
eventTxAlInterlockLoadBindings = _EventTxAlInterlockLoadBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    eventTxAlInterlockLoadBindings.setStatus("obsolete")
_EventTimeStampTxAlInterlockLoad_Type = DateAndTime
_EventTimeStampTxAlInterlockLoad_Object = MibScalar
eventTimeStampTxAlInterlockLoad = _EventTimeStampTxAlInterlockLoad_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 7, 1),
    _EventTimeStampTxAlInterlockLoad_Type()
)
eventTimeStampTxAlInterlockLoad.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAlInterlockLoad.setStatus("obsolete")
_EventTxRfOpmodeBindings_ObjectIdentity = ObjectIdentity
eventTxRfOpmodeBindings = _EventTxRfOpmodeBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    eventTxRfOpmodeBindings.setStatus("current")
_EventTimeStampTxRfOpmode_Type = DateAndTime
_EventTimeStampTxRfOpmode_Object = MibScalar
eventTimeStampTxRfOpmode = _EventTimeStampTxRfOpmode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 8, 1),
    _EventTimeStampTxRfOpmode_Type()
)
eventTimeStampTxRfOpmode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxRfOpmode.setStatus("current")
_EventTxRfRFPresentBindings_ObjectIdentity = ObjectIdentity
eventTxRfRFPresentBindings = _EventTxRfRFPresentBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    eventTxRfRFPresentBindings.setStatus("current")
_EventTimeStampTxRfRFPresent_Type = DateAndTime
_EventTimeStampTxRfRFPresent_Object = MibScalar
eventTimeStampTxRfRFPresent = _EventTimeStampTxRfRFPresent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 9, 1),
    _EventTimeStampTxRfRFPresent_Type()
)
eventTimeStampTxRfRFPresent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxRfRFPresent.setStatus("current")
_EventAcReserveControlBindings_ObjectIdentity = ObjectIdentity
eventAcReserveControlBindings = _EventAcReserveControlBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    eventAcReserveControlBindings.setStatus("current")
_EventTimeStampAcReserveControl_Type = DateAndTime
_EventTimeStampAcReserveControl_Object = MibScalar
eventTimeStampAcReserveControl = _EventTimeStampAcReserveControl_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 10, 1),
    _EventTimeStampAcReserveControl_Type()
)
eventTimeStampAcReserveControl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcReserveControl.setStatus("current")
_EventAcLocalModeBindings_ObjectIdentity = ObjectIdentity
eventAcLocalModeBindings = _EventAcLocalModeBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    eventAcLocalModeBindings.setStatus("current")
_EventTimeStampAcLocalMode_Type = DateAndTime
_EventTimeStampAcLocalMode_Object = MibScalar
eventTimeStampAcLocalMode = _EventTimeStampAcLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 11, 1),
    _EventTimeStampAcLocalMode_Type()
)
eventTimeStampAcLocalMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcLocalMode.setStatus("current")
_EventAcFaultBindings_ObjectIdentity = ObjectIdentity
eventAcFaultBindings = _EventAcFaultBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    eventAcFaultBindings.setStatus("current")
_EventTimeStampAcFault_Type = DateAndTime
_EventTimeStampAcFault_Object = MibScalar
eventTimeStampAcFault = _EventTimeStampAcFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 12, 1),
    _EventTimeStampAcFault_Type()
)
eventTimeStampAcFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcFault.setStatus("current")
_EventAcSwitchOverBindings_ObjectIdentity = ObjectIdentity
eventAcSwitchOverBindings = _EventAcSwitchOverBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    eventAcSwitchOverBindings.setStatus("current")
_EventTimeStampAcSwitchOver_Type = DateAndTime
_EventTimeStampAcSwitchOver_Object = MibScalar
eventTimeStampAcSwitchOver = _EventTimeStampAcSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 13, 1),
    _EventTimeStampAcSwitchOver_Type()
)
eventTimeStampAcSwitchOver.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcSwitchOver.setStatus("current")
_EventSysWarningBindings_ObjectIdentity = ObjectIdentity
eventSysWarningBindings = _EventSysWarningBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 14)
)
if mibBuilder.loadTexts:
    eventSysWarningBindings.setStatus("current")
_EventTimeStampSysWarning_Type = DateAndTime
_EventTimeStampSysWarning_Object = MibScalar
eventTimeStampSysWarning = _EventTimeStampSysWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 14, 1),
    _EventTimeStampSysWarning_Type()
)
eventTimeStampSysWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysWarning.setStatus("current")
_EventSysFaultBindings_ObjectIdentity = ObjectIdentity
eventSysFaultBindings = _EventSysFaultBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    eventSysFaultBindings.setStatus("current")
_EventTimeStampSysFault_Type = DateAndTime
_EventTimeStampSysFault_Object = MibScalar
eventTimeStampSysFault = _EventTimeStampSysFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 15, 1),
    _EventTimeStampSysFault_Type()
)
eventTimeStampSysFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysFault.setStatus("current")
_EventSysAlAmbBindings_ObjectIdentity = ObjectIdentity
eventSysAlAmbBindings = _EventSysAlAmbBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 16)
)
if mibBuilder.loadTexts:
    eventSysAlAmbBindings.setStatus("current")
_EventTimeStampSysAlAmb_Type = DateAndTime
_EventTimeStampSysAlAmb_Object = MibScalar
eventTimeStampSysAlAmb = _EventTimeStampSysAlAmb_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 16, 1),
    _EventTimeStampSysAlAmb_Type()
)
eventTimeStampSysAlAmb.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlAmb.setStatus("current")
_EventSysAlVoltAuxBindings_ObjectIdentity = ObjectIdentity
eventSysAlVoltAuxBindings = _EventSysAlVoltAuxBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    eventSysAlVoltAuxBindings.setStatus("current")
_EventTimeStampSysAlVoltAux_Type = DateAndTime
_EventTimeStampSysAlVoltAux_Object = MibScalar
eventTimeStampSysAlVoltAux = _EventTimeStampSysAlVoltAux_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 17, 1),
    _EventTimeStampSysAlVoltAux_Type()
)
eventTimeStampSysAlVoltAux.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlVoltAux.setStatus("current")
_EventSysAlRelayBindings_ObjectIdentity = ObjectIdentity
eventSysAlRelayBindings = _EventSysAlRelayBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 18)
)
if mibBuilder.loadTexts:
    eventSysAlRelayBindings.setStatus("current")
_EventTimeStampSysAlRelay_Type = DateAndTime
_EventTimeStampSysAlRelay_Object = MibScalar
eventTimeStampSysAlRelay = _EventTimeStampSysAlRelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 18, 1),
    _EventTimeStampSysAlRelay_Type()
)
eventTimeStampSysAlRelay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlRelay.setStatus("current")
_EventSysAlReserveBindings_ObjectIdentity = ObjectIdentity
eventSysAlReserveBindings = _EventSysAlReserveBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    eventSysAlReserveBindings.setStatus("current")
_EventTimeStampSysAlReserve_Type = DateAndTime
_EventTimeStampSysAlReserve_Object = MibScalar
eventTimeStampSysAlReserve = _EventTimeStampSysAlReserve_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 19, 1),
    _EventTimeStampSysAlReserve_Type()
)
eventTimeStampSysAlReserve.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlReserve.setStatus("current")
_EventInSeAlrInputSwitchBindings_ObjectIdentity = ObjectIdentity
eventInSeAlrInputSwitchBindings = _EventInSeAlrInputSwitchBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    eventInSeAlrInputSwitchBindings.setStatus("current")
_EventTimeStampInSeAlrInputSwitch_Type = DateAndTime
_EventTimeStampInSeAlrInputSwitch_Object = MibScalar
eventTimeStampInSeAlrInputSwitch = _EventTimeStampInSeAlrInputSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 20, 1),
    _EventTimeStampInSeAlrInputSwitch_Type()
)
eventTimeStampInSeAlrInputSwitch.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInSeAlrInputSwitch.setStatus("current")
_EventTxAl1dBBindings_ObjectIdentity = ObjectIdentity
eventTxAl1dBBindings = _EventTxAl1dBBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    eventTxAl1dBBindings.setStatus("current")
_EventTimeStampTxAl1dB_Type = DateAndTime
_EventTimeStampTxAl1dB_Object = MibScalar
eventTimeStampTxAl1dB = _EventTimeStampTxAl1dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 21, 1),
    _EventTimeStampTxAl1dB_Type()
)
eventTimeStampTxAl1dB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxAl1dB.setStatus("current")
_EventTxGnGlStandbyBindings_ObjectIdentity = ObjectIdentity
eventTxGnGlStandbyBindings = _EventTxGnGlStandbyBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 22)
)
if mibBuilder.loadTexts:
    eventTxGnGlStandbyBindings.setStatus("current")
_EventTimeStampTxGnGlStandby_Type = DateAndTime
_EventTimeStampTxGnGlStandby_Object = MibScalar
eventTimeStampTxGnGlStandby = _EventTimeStampTxGnGlStandby_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 22, 1),
    _EventTimeStampTxGnGlStandby_Type()
)
eventTimeStampTxGnGlStandby.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxGnGlStandby.setStatus("current")
_EventInAlLine1Bindings_ObjectIdentity = ObjectIdentity
eventInAlLine1Bindings = _EventInAlLine1Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 23)
)
if mibBuilder.loadTexts:
    eventInAlLine1Bindings.setStatus("current")
_EventTimeStampInAlLine1_Type = DateAndTime
_EventTimeStampInAlLine1_Object = MibScalar
eventTimeStampInAlLine1 = _EventTimeStampInAlLine1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 23, 1),
    _EventTimeStampInAlLine1_Type()
)
eventTimeStampInAlLine1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlLine1.setStatus("current")
_EventInAlLine2Bindings_ObjectIdentity = ObjectIdentity
eventInAlLine2Bindings = _EventInAlLine2Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 24)
)
if mibBuilder.loadTexts:
    eventInAlLine2Bindings.setStatus("current")
_EventTimeStampInAlLine2_Type = DateAndTime
_EventTimeStampInAlLine2_Object = MibScalar
eventTimeStampInAlLine2 = _EventTimeStampInAlLine2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 24, 1),
    _EventTimeStampInAlLine2_Type()
)
eventTimeStampInAlLine2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlLine2.setStatus("current")
_EventInAlMpx1Bindings_ObjectIdentity = ObjectIdentity
eventInAlMpx1Bindings = _EventInAlMpx1Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 25)
)
if mibBuilder.loadTexts:
    eventInAlMpx1Bindings.setStatus("current")
_EventTimeStampInAlMpx1_Type = DateAndTime
_EventTimeStampInAlMpx1_Object = MibScalar
eventTimeStampInAlMpx1 = _EventTimeStampInAlMpx1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 25, 1),
    _EventTimeStampInAlMpx1_Type()
)
eventTimeStampInAlMpx1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlMpx1.setStatus("current")
_EventInAlMpx2Bindings_ObjectIdentity = ObjectIdentity
eventInAlMpx2Bindings = _EventInAlMpx2Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 26)
)
if mibBuilder.loadTexts:
    eventInAlMpx2Bindings.setStatus("current")
_EventTimeStampInAlMpx2_Type = DateAndTime
_EventTimeStampInAlMpx2_Object = MibScalar
eventTimeStampInAlMpx2 = _EventTimeStampInAlMpx2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 26, 1),
    _EventTimeStampInAlMpx2_Type()
)
eventTimeStampInAlMpx2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlMpx2.setStatus("current")
_EventInAlPlayerBindings_ObjectIdentity = ObjectIdentity
eventInAlPlayerBindings = _EventInAlPlayerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 27)
)
if mibBuilder.loadTexts:
    eventInAlPlayerBindings.setStatus("current")
_EventTimeStampInAlPlayer_Type = DateAndTime
_EventTimeStampInAlPlayer_Object = MibScalar
eventTimeStampInAlPlayer = _EventTimeStampInAlPlayer_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 27, 1),
    _EventTimeStampInAlPlayer_Type()
)
eventTimeStampInAlPlayer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlPlayer.setStatus("current")
_EventSysAlInvalidDataBindings_ObjectIdentity = ObjectIdentity
eventSysAlInvalidDataBindings = _EventSysAlInvalidDataBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 28)
)
if mibBuilder.loadTexts:
    eventSysAlInvalidDataBindings.setStatus("current")
_EventTimeStampSysAlInvalidData_Type = DateAndTime
_EventTimeStampSysAlInvalidData_Object = MibScalar
eventTimeStampSysAlInvalidData = _EventTimeStampSysAlInvalidData_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 28, 1),
    _EventTimeStampSysAlInvalidData_Type()
)
eventTimeStampSysAlInvalidData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlInvalidData.setStatus("current")
_EventAcGnAlInterlockAntBindings_ObjectIdentity = ObjectIdentity
eventAcGnAlInterlockAntBindings = _EventAcGnAlInterlockAntBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 29)
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockAntBindings.setStatus("current")
_EventTimeStampAcGnAlInterlockAnt_Type = DateAndTime
_EventTimeStampAcGnAlInterlockAnt_Object = MibScalar
eventTimeStampAcGnAlInterlockAnt = _EventTimeStampAcGnAlInterlockAnt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 29, 1),
    _EventTimeStampAcGnAlInterlockAnt_Type()
)
eventTimeStampAcGnAlInterlockAnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcGnAlInterlockAnt.setStatus("current")
_EventAcGnAlInterlockLoadBindings_ObjectIdentity = ObjectIdentity
eventAcGnAlInterlockLoadBindings = _EventAcGnAlInterlockLoadBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 30)
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockLoadBindings.setStatus("current")
_EventTimeStampAcGnAlInterlockLoad_Type = DateAndTime
_EventTimeStampAcGnAlInterlockLoad_Object = MibScalar
eventTimeStampAcGnAlInterlockLoad = _EventTimeStampAcGnAlInterlockLoad_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 30, 1),
    _EventTimeStampAcGnAlInterlockLoad_Type()
)
eventTimeStampAcGnAlInterlockLoad.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampAcGnAlInterlockLoad.setStatus("current")
_EventSysAl24vBindings_ObjectIdentity = ObjectIdentity
eventSysAl24vBindings = _EventSysAl24vBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 31)
)
if mibBuilder.loadTexts:
    eventSysAl24vBindings.setStatus("current")
_EventTimeStampSysAl24v_Type = DateAndTime
_EventTimeStampSysAl24v_Object = MibScalar
eventTimeStampSysAl24v = _EventTimeStampSysAl24v_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 31, 1),
    _EventTimeStampSysAl24v_Type()
)
eventTimeStampSysAl24v.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAl24v.setStatus("current")
_EventSysAlCommBindings_ObjectIdentity = ObjectIdentity
eventSysAlCommBindings = _EventSysAlCommBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 32)
)
if mibBuilder.loadTexts:
    eventSysAlCommBindings.setStatus("current")
_EventTimeStampSysAlComm_Type = DateAndTime
_EventTimeStampSysAlComm_Object = MibScalar
eventTimeStampSysAlComm = _EventTimeStampSysAlComm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 32, 1),
    _EventTimeStampSysAlComm_Type()
)
eventTimeStampSysAlComm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSysAlComm.setStatus("current")
_EventEquipmentOnBindings_ObjectIdentity = ObjectIdentity
eventEquipmentOnBindings = _EventEquipmentOnBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 33)
)
if mibBuilder.loadTexts:
    eventEquipmentOnBindings.setStatus("current")
_EventTimeStampEquipmentOn_Type = DateAndTime
_EventTimeStampEquipmentOn_Object = MibScalar
eventTimeStampEquipmentOn = _EventTimeStampEquipmentOn_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 33, 1),
    _EventTimeStampEquipmentOn_Type()
)
eventTimeStampEquipmentOn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampEquipmentOn.setStatus("current")
_EventEquipmentOnDownTime_Type = Integer32
_EventEquipmentOnDownTime_Object = MibScalar
eventEquipmentOnDownTime = _EventEquipmentOnDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 33, 2),
    _EventEquipmentOnDownTime_Type()
)
eventEquipmentOnDownTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventEquipmentOnDownTime.setStatus("current")
_EventHeartBeatBindings_ObjectIdentity = ObjectIdentity
eventHeartBeatBindings = _EventHeartBeatBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 34)
)
if mibBuilder.loadTexts:
    eventHeartBeatBindings.setStatus("current")
_EventTimeStampHeartBeat_Type = DateAndTime
_EventTimeStampHeartBeat_Object = MibScalar
eventTimeStampHeartBeat = _EventTimeStampHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 34, 1),
    _EventTimeStampHeartBeat_Type()
)
eventTimeStampHeartBeat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampHeartBeat.setStatus("current")
_EventConfigChangedBindings_ObjectIdentity = ObjectIdentity
eventConfigChangedBindings = _EventConfigChangedBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 35)
)
if mibBuilder.loadTexts:
    eventConfigChangedBindings.setStatus("current")
_EventTimeStampConfigChanged_Type = DateAndTime
_EventTimeStampConfigChanged_Object = MibScalar
eventTimeStampConfigChanged = _EventTimeStampConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 35, 1),
    _EventTimeStampConfigChanged_Type()
)
eventTimeStampConfigChanged.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampConfigChanged.setStatus("current")
_EventEquipmentFaultBindings_ObjectIdentity = ObjectIdentity
eventEquipmentFaultBindings = _EventEquipmentFaultBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 36)
)
if mibBuilder.loadTexts:
    eventEquipmentFaultBindings.setStatus("obsolete")
_EventTimeStampEquipmentFault_Type = DateAndTime
_EventTimeStampEquipmentFault_Object = MibScalar
eventTimeStampEquipmentFault = _EventTimeStampEquipmentFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 36, 1),
    _EventTimeStampEquipmentFault_Type()
)
eventTimeStampEquipmentFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampEquipmentFault.setStatus("obsolete")


class _EventEquipmentFaultError_Type(DisplayString):
    """Custom type eventEquipmentFaultError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventEquipmentFaultError_Type.__name__ = "DisplayString"
_EventEquipmentFaultError_Object = MibScalar
eventEquipmentFaultError = _EventEquipmentFaultError_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 36, 2),
    _EventEquipmentFaultError_Type()
)
eventEquipmentFaultError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventEquipmentFaultError.setStatus("obsolete")
_EventInAlFaultBindings_ObjectIdentity = ObjectIdentity
eventInAlFaultBindings = _EventInAlFaultBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 37)
)
if mibBuilder.loadTexts:
    eventInAlFaultBindings.setStatus("current")
_EventTimeStampInAlFault_Type = DateAndTime
_EventTimeStampInAlFault_Object = MibScalar
eventTimeStampInAlFault = _EventTimeStampInAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 37, 1),
    _EventTimeStampInAlFault_Type()
)
eventTimeStampInAlFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlFault.setStatus("current")
_EventMoSfAlarmBindings_ObjectIdentity = ObjectIdentity
eventMoSfAlarmBindings = _EventMoSfAlarmBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 38)
)
if mibBuilder.loadTexts:
    eventMoSfAlarmBindings.setStatus("current")
_EventTimeStampMoSfAlarm_Type = DateAndTime
_EventTimeStampMoSfAlarm_Object = MibScalar
eventTimeStampMoSfAlarm = _EventTimeStampMoSfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 38, 1),
    _EventTimeStampMoSfAlarm_Type()
)
eventTimeStampMoSfAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampMoSfAlarm.setStatus("current")
_EventMoSfSwitch10MAlarmBindings_ObjectIdentity = ObjectIdentity
eventMoSfSwitch10MAlarmBindings = _EventMoSfSwitch10MAlarmBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 39)
)
if mibBuilder.loadTexts:
    eventMoSfSwitch10MAlarmBindings.setStatus("current")
_EventTimeStampMoSfSwitch10MAlarm_Type = DateAndTime
_EventTimeStampMoSfSwitch10MAlarm_Object = MibScalar
eventTimeStampMoSfSwitch10MAlarm = _EventTimeStampMoSfSwitch10MAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 39, 1),
    _EventTimeStampMoSfSwitch10MAlarm_Type()
)
eventTimeStampMoSfSwitch10MAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampMoSfSwitch10MAlarm.setStatus("current")
_EventSyAlLoggingBindings_ObjectIdentity = ObjectIdentity
eventSyAlLoggingBindings = _EventSyAlLoggingBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 40)
)
if mibBuilder.loadTexts:
    eventSyAlLoggingBindings.setStatus("current")
_EventTimeStampSyAlLogging_Type = DateAndTime
_EventTimeStampSyAlLogging_Object = MibScalar
eventTimeStampSyAlLogging = _EventTimeStampSyAlLogging_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 40, 1),
    _EventTimeStampSyAlLogging_Type()
)
eventTimeStampSyAlLogging.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyAlLogging.setStatus("current")
_EventInAlMpx3Bindings_ObjectIdentity = ObjectIdentity
eventInAlMpx3Bindings = _EventInAlMpx3Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 41)
)
if mibBuilder.loadTexts:
    eventInAlMpx3Bindings.setStatus("current")
_EventTimeStampInAlMpx3_Type = DateAndTime
_EventTimeStampInAlMpx3_Object = MibScalar
eventTimeStampInAlMpx3 = _EventTimeStampInAlMpx3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 41, 1),
    _EventTimeStampInAlMpx3_Type()
)
eventTimeStampInAlMpx3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlMpx3.setStatus("current")
_EventInAlMpx4Bindings_ObjectIdentity = ObjectIdentity
eventInAlMpx4Bindings = _EventInAlMpx4Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 42)
)
if mibBuilder.loadTexts:
    eventInAlMpx4Bindings.setStatus("current")
_EventTimeStampInAlMpx4_Type = DateAndTime
_EventTimeStampInAlMpx4_Object = MibScalar
eventTimeStampInAlMpx4 = _EventTimeStampInAlMpx4_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 42, 1),
    _EventTimeStampInAlMpx4_Type()
)
eventTimeStampInAlMpx4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlMpx4.setStatus("current")
_EventTxSfStActBindings_ObjectIdentity = ObjectIdentity
eventTxSfStActBindings = _EventTxSfStActBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 43)
)
if mibBuilder.loadTexts:
    eventTxSfStActBindings.setStatus("current")
_EventTimeStampTxSfStAct_Type = DateAndTime
_EventTimeStampTxSfStAct_Object = MibScalar
eventTimeStampTxSfStAct = _EventTimeStampTxSfStAct_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 43, 1),
    _EventTimeStampTxSfStAct_Type()
)
eventTimeStampTxSfStAct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxSfStAct.setStatus("current")
_EventTxSfStAlarmBindings_ObjectIdentity = ObjectIdentity
eventTxSfStAlarmBindings = _EventTxSfStAlarmBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 44)
)
if mibBuilder.loadTexts:
    eventTxSfStAlarmBindings.setStatus("current")
_EventTimeStampTxSfStAlarm_Type = DateAndTime
_EventTimeStampTxSfStAlarm_Object = MibScalar
eventTimeStampTxSfStAlarm = _EventTimeStampTxSfStAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 44, 1),
    _EventTimeStampTxSfStAlarm_Type()
)
eventTimeStampTxSfStAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampTxSfStAlarm.setStatus("current")
_EventSyLiAlRdsBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlRdsBindings = _EventSyLiAlRdsBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 45)
)
if mibBuilder.loadTexts:
    eventSyLiAlRdsBindings.setStatus("current")
_EventTimeStampSyLiAlRds_Type = DateAndTime
_EventTimeStampSyLiAlRds_Object = MibScalar
eventTimeStampSyLiAlRds = _EventTimeStampSyLiAlRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 45, 1),
    _EventTimeStampSyLiAlRds_Type()
)
eventTimeStampSyLiAlRds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlRds.setStatus("current")
_EventSyLiAlSoundProcBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlSoundProcBindings = _EventSyLiAlSoundProcBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 46)
)
if mibBuilder.loadTexts:
    eventSyLiAlSoundProcBindings.setStatus("current")
_EventTimeStampSyLiAlSoundProc_Type = DateAndTime
_EventTimeStampSyLiAlSoundProc_Object = MibScalar
eventTimeStampSyLiAlSoundProc = _EventTimeStampSyLiAlSoundProc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 46, 1),
    _EventTimeStampSyLiAlSoundProc_Type()
)
eventTimeStampSyLiAlSoundProc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlSoundProc.setStatus("current")
_EventSyLiAlSfmBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlSfmBindings = _EventSyLiAlSfmBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 47)
)
if mibBuilder.loadTexts:
    eventSyLiAlSfmBindings.setStatus("current")
_EventTimeStampSyLiAlSfm_Type = DateAndTime
_EventTimeStampSyLiAlSfm_Object = MibScalar
eventTimeStampSyLiAlSfm = _EventTimeStampSyLiAlSfm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 47, 1),
    _EventTimeStampSyLiAlSfm_Type()
)
eventTimeStampSyLiAlSfm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlSfm.setStatus("current")
_EventSyLiAlActivationBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlActivationBindings = _EventSyLiAlActivationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 48)
)
if mibBuilder.loadTexts:
    eventSyLiAlActivationBindings.setStatus("current")
_EventTimeStampSyLiAlActivation_Type = DateAndTime
_EventTimeStampSyLiAlActivation_Object = MibScalar
eventTimeStampSyLiAlActivation = _EventTimeStampSyLiAlActivation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 48, 1),
    _EventTimeStampSyLiAlActivation_Type()
)
eventTimeStampSyLiAlActivation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlActivation.setStatus("current")
_EventInAlAes1Bindings_ObjectIdentity = ObjectIdentity
eventInAlAes1Bindings = _EventInAlAes1Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 49)
)
if mibBuilder.loadTexts:
    eventInAlAes1Bindings.setStatus("current")
_EventTimeStampInAlAes1_Type = DateAndTime
_EventTimeStampInAlAes1_Object = MibScalar
eventTimeStampInAlAes1 = _EventTimeStampInAlAes1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 49, 1),
    _EventTimeStampInAlAes1_Type()
)
eventTimeStampInAlAes1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlAes1.setStatus("current")
_EventInAlAes2Bindings_ObjectIdentity = ObjectIdentity
eventInAlAes2Bindings = _EventInAlAes2Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 50)
)
if mibBuilder.loadTexts:
    eventInAlAes2Bindings.setStatus("current")
_EventTimeStampInAlAes2_Type = DateAndTime
_EventTimeStampInAlAes2_Object = MibScalar
eventTimeStampInAlAes2 = _EventTimeStampInAlAes2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 50, 1),
    _EventTimeStampInAlAes2_Type()
)
eventTimeStampInAlAes2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlAes2.setStatus("current")
_EventInAlAes3Bindings_ObjectIdentity = ObjectIdentity
eventInAlAes3Bindings = _EventInAlAes3Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 51)
)
if mibBuilder.loadTexts:
    eventInAlAes3Bindings.setStatus("current")
_EventTimeStampInAlAes3_Type = DateAndTime
_EventTimeStampInAlAes3_Object = MibScalar
eventTimeStampInAlAes3 = _EventTimeStampInAlAes3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 51, 1),
    _EventTimeStampInAlAes3_Type()
)
eventTimeStampInAlAes3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlAes3.setStatus("current")
_EventInAlAna1Bindings_ObjectIdentity = ObjectIdentity
eventInAlAna1Bindings = _EventInAlAna1Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 52)
)
if mibBuilder.loadTexts:
    eventInAlAna1Bindings.setStatus("current")
_EventTimeStampInAlAna1_Type = DateAndTime
_EventTimeStampInAlAna1_Object = MibScalar
eventTimeStampInAlAna1 = _EventTimeStampInAlAna1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 52, 1),
    _EventTimeStampInAlAna1_Type()
)
eventTimeStampInAlAna1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlAna1.setStatus("current")
_EventInAlAoipBindings_ObjectIdentity = ObjectIdentity
eventInAlAoipBindings = _EventInAlAoipBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 53)
)
if mibBuilder.loadTexts:
    eventInAlAoipBindings.setStatus("current")
_EventTimeStampInAlAoip_Type = DateAndTime
_EventTimeStampInAlAoip_Object = MibScalar
eventTimeStampInAlAoip = _EventTimeStampInAlAoip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 53, 1),
    _EventTimeStampInAlAoip_Type()
)
eventTimeStampInAlAoip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampInAlAoip.setStatus("current")
_EventLossOfEth0Bindings_ObjectIdentity = ObjectIdentity
eventLossOfEth0Bindings = _EventLossOfEth0Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 54)
)
if mibBuilder.loadTexts:
    eventLossOfEth0Bindings.setStatus("current")
_EventTimeStampLossOfEth0_Type = DateAndTime
_EventTimeStampLossOfEth0_Object = MibScalar
eventTimeStampLossOfEth0 = _EventTimeStampLossOfEth0_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 54, 1),
    _EventTimeStampLossOfEth0_Type()
)
eventTimeStampLossOfEth0.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampLossOfEth0.setStatus("current")
_EventLossOfEth1Bindings_ObjectIdentity = ObjectIdentity
eventLossOfEth1Bindings = _EventLossOfEth1Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 55)
)
if mibBuilder.loadTexts:
    eventLossOfEth1Bindings.setStatus("current")
_EventTimeStampLossOfEth1_Type = DateAndTime
_EventTimeStampLossOfEth1_Object = MibScalar
eventTimeStampLossOfEth1 = _EventTimeStampLossOfEth1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 55, 1),
    _EventTimeStampLossOfEth1_Type()
)
eventTimeStampLossOfEth1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampLossOfEth1.setStatus("current")
_EventSyLiAlAoipdecoderBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlAoipdecoderBindings = _EventSyLiAlAoipdecoderBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 56)
)
if mibBuilder.loadTexts:
    eventSyLiAlAoipdecoderBindings.setStatus("current")
_EventTimeStampSyLiAlAoipdecoder_Type = DateAndTime
_EventTimeStampSyLiAlAoipdecoder_Object = MibScalar
eventTimeStampSyLiAlAoipdecoder = _EventTimeStampSyLiAlAoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 56, 1),
    _EventTimeStampSyLiAlAoipdecoder_Type()
)
eventTimeStampSyLiAlAoipdecoder.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlAoipdecoder.setStatus("current")
_EventSyLiAlMpxoipdecoderBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlMpxoipdecoderBindings = _EventSyLiAlMpxoipdecoderBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 57)
)
if mibBuilder.loadTexts:
    eventSyLiAlMpxoipdecoderBindings.setStatus("current")
_EventTimeStampSyLiAlMpxoipdecoder_Type = DateAndTime
_EventTimeStampSyLiAlMpxoipdecoder_Object = MibScalar
eventTimeStampSyLiAlMpxoipdecoder = _EventTimeStampSyLiAlMpxoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 57, 1),
    _EventTimeStampSyLiAlMpxoipdecoder_Type()
)
eventTimeStampSyLiAlMpxoipdecoder.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlMpxoipdecoder.setStatus("current")
_EventSyLiAlSurestreamBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlSurestreamBindings = _EventSyLiAlSurestreamBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 58)
)
if mibBuilder.loadTexts:
    eventSyLiAlSurestreamBindings.setStatus("current")
_EventTimeStampSyLiAlSurestream_Type = DateAndTime
_EventTimeStampSyLiAlSurestream_Object = MibScalar
eventTimeStampSyLiAlSurestream = _EventTimeStampSyLiAlSurestream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 58, 1),
    _EventTimeStampSyLiAlSurestream_Type()
)
eventTimeStampSyLiAlSurestream.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlSurestream.setStatus("current")
_EventSyLiAlSynchrostreamBindings_ObjectIdentity = ObjectIdentity
eventSyLiAlSynchrostreamBindings = _EventSyLiAlSynchrostreamBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 59)
)
if mibBuilder.loadTexts:
    eventSyLiAlSynchrostreamBindings.setStatus("current")
_EventTimeStampSyLiAlSynchrostream_Type = DateAndTime
_EventTimeStampSyLiAlSynchrostream_Object = MibScalar
eventTimeStampSyLiAlSynchrostream = _EventTimeStampSyLiAlSynchrostream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 1, 59, 1),
    _EventTimeStampSyLiAlSynchrostream_Type()
)
eventTimeStampSyLiAlSynchrostream.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStampSyLiAlSynchrostream.setStatus("current")
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    groups.setStatus("current")
_EventsParams_ObjectIdentity = ObjectIdentity
eventsParams = _EventsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eventsParams.setStatus("current")
_EventTxLocalModeParams_ObjectIdentity = ObjectIdentity
eventTxLocalModeParams = _EventTxLocalModeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    eventTxLocalModeParams.setStatus("current")


class _EventTxLocalModePriority_Type(Gauge32):
    """Custom type eventTxLocalModePriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxLocalModePriority_Type.__name__ = "Gauge32"
_EventTxLocalModePriority_Object = MibScalar
eventTxLocalModePriority = _EventTxLocalModePriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 1, 1),
    _EventTxLocalModePriority_Type()
)
eventTxLocalModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxLocalModePriority.setStatus("current")


class _EventTxLocalModeEnable_Type(Integer32):
    """Custom type eventTxLocalModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxLocalModeEnable_Type.__name__ = "Integer32"
_EventTxLocalModeEnable_Object = MibScalar
eventTxLocalModeEnable = _EventTxLocalModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 1, 2),
    _EventTxLocalModeEnable_Type()
)
eventTxLocalModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxLocalModeEnable.setStatus("current")


class _TxLocalModeSignalSuppression_Type(Integer32):
    """Custom type txLocalModeSignalSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TxLocalModeSignalSuppression_Type.__name__ = "Integer32"
_TxLocalModeSignalSuppression_Object = MibScalar
txLocalModeSignalSuppression = _TxLocalModeSignalSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 1, 3),
    _TxLocalModeSignalSuppression_Type()
)
txLocalModeSignalSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txLocalModeSignalSuppression.setStatus("current")
_EventTxAl3dBParams_ObjectIdentity = ObjectIdentity
eventTxAl3dBParams = _EventTxAl3dBParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    eventTxAl3dBParams.setStatus("current")


class _EventTxAl3dBPriority_Type(Gauge32):
    """Custom type eventTxAl3dBPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAl3dBPriority_Type.__name__ = "Gauge32"
_EventTxAl3dBPriority_Object = MibScalar
eventTxAl3dBPriority = _EventTxAl3dBPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 2, 1),
    _EventTxAl3dBPriority_Type()
)
eventTxAl3dBPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAl3dBPriority.setStatus("current")


class _EventTxAl3dBEnable_Type(Integer32):
    """Custom type eventTxAl3dBEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAl3dBEnable_Type.__name__ = "Integer32"
_EventTxAl3dBEnable_Object = MibScalar
eventTxAl3dBEnable = _EventTxAl3dBEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 2, 2),
    _EventTxAl3dBEnable_Type()
)
eventTxAl3dBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAl3dBEnable.setStatus("current")
_EventTxAlFaultParams_ObjectIdentity = ObjectIdentity
eventTxAlFaultParams = _EventTxAlFaultParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    eventTxAlFaultParams.setStatus("current")


class _EventTxAlFaultPriority_Type(Gauge32):
    """Custom type eventTxAlFaultPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAlFaultPriority_Type.__name__ = "Gauge32"
_EventTxAlFaultPriority_Object = MibScalar
eventTxAlFaultPriority = _EventTxAlFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 3, 1),
    _EventTxAlFaultPriority_Type()
)
eventTxAlFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlFaultPriority.setStatus("current")


class _EventTxAlFaultEnable_Type(Integer32):
    """Custom type eventTxAlFaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAlFaultEnable_Type.__name__ = "Integer32"
_EventTxAlFaultEnable_Object = MibScalar
eventTxAlFaultEnable = _EventTxAlFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 3, 2),
    _EventTxAlFaultEnable_Type()
)
eventTxAlFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlFaultEnable.setStatus("current")
_EventTxAlWarningParams_ObjectIdentity = ObjectIdentity
eventTxAlWarningParams = _EventTxAlWarningParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    eventTxAlWarningParams.setStatus("current")


class _EventTxAlWarningPriority_Type(Gauge32):
    """Custom type eventTxAlWarningPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAlWarningPriority_Type.__name__ = "Gauge32"
_EventTxAlWarningPriority_Object = MibScalar
eventTxAlWarningPriority = _EventTxAlWarningPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 4, 1),
    _EventTxAlWarningPriority_Type()
)
eventTxAlWarningPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlWarningPriority.setStatus("current")


class _EventTxAlWarningEnable_Type(Integer32):
    """Custom type eventTxAlWarningEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAlWarningEnable_Type.__name__ = "Integer32"
_EventTxAlWarningEnable_Object = MibScalar
eventTxAlWarningEnable = _EventTxAlWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 4, 2),
    _EventTxAlWarningEnable_Type()
)
eventTxAlWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlWarningEnable.setStatus("current")
_EventTxAlVSWRParams_ObjectIdentity = ObjectIdentity
eventTxAlVSWRParams = _EventTxAlVSWRParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    eventTxAlVSWRParams.setStatus("current")


class _EventTxAlVSWRPriority_Type(Gauge32):
    """Custom type eventTxAlVSWRPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAlVSWRPriority_Type.__name__ = "Gauge32"
_EventTxAlVSWRPriority_Object = MibScalar
eventTxAlVSWRPriority = _EventTxAlVSWRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 5, 1),
    _EventTxAlVSWRPriority_Type()
)
eventTxAlVSWRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlVSWRPriority.setStatus("current")


class _EventTxAlVSWREnable_Type(Integer32):
    """Custom type eventTxAlVSWREnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAlVSWREnable_Type.__name__ = "Integer32"
_EventTxAlVSWREnable_Object = MibScalar
eventTxAlVSWREnable = _EventTxAlVSWREnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 5, 2),
    _EventTxAlVSWREnable_Type()
)
eventTxAlVSWREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlVSWREnable.setStatus("current")
_EventTxAlInterlockAntParams_ObjectIdentity = ObjectIdentity
eventTxAlInterlockAntParams = _EventTxAlInterlockAntParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    eventTxAlInterlockAntParams.setStatus("current")


class _EventTxAlInterlockAntPriority_Type(Gauge32):
    """Custom type eventTxAlInterlockAntPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAlInterlockAntPriority_Type.__name__ = "Gauge32"
_EventTxAlInterlockAntPriority_Object = MibScalar
eventTxAlInterlockAntPriority = _EventTxAlInterlockAntPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 6, 1),
    _EventTxAlInterlockAntPriority_Type()
)
eventTxAlInterlockAntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlInterlockAntPriority.setStatus("current")


class _EventTxAlInterlockAntEnable_Type(Integer32):
    """Custom type eventTxAlInterlockAntEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAlInterlockAntEnable_Type.__name__ = "Integer32"
_EventTxAlInterlockAntEnable_Object = MibScalar
eventTxAlInterlockAntEnable = _EventTxAlInterlockAntEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 6, 2),
    _EventTxAlInterlockAntEnable_Type()
)
eventTxAlInterlockAntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlInterlockAntEnable.setStatus("current")
_EventTxAlInterlockLoadParams_ObjectIdentity = ObjectIdentity
eventTxAlInterlockLoadParams = _EventTxAlInterlockLoadParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    eventTxAlInterlockLoadParams.setStatus("obsolete")


class _EventTxAlInterlockLoadPriority_Type(Gauge32):
    """Custom type eventTxAlInterlockLoadPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAlInterlockLoadPriority_Type.__name__ = "Gauge32"
_EventTxAlInterlockLoadPriority_Object = MibScalar
eventTxAlInterlockLoadPriority = _EventTxAlInterlockLoadPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 7, 1),
    _EventTxAlInterlockLoadPriority_Type()
)
eventTxAlInterlockLoadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlInterlockLoadPriority.setStatus("obsolete")


class _EventTxAlInterlockLoadEnable_Type(Integer32):
    """Custom type eventTxAlInterlockLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAlInterlockLoadEnable_Type.__name__ = "Integer32"
_EventTxAlInterlockLoadEnable_Object = MibScalar
eventTxAlInterlockLoadEnable = _EventTxAlInterlockLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 7, 2),
    _EventTxAlInterlockLoadEnable_Type()
)
eventTxAlInterlockLoadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAlInterlockLoadEnable.setStatus("obsolete")
_EventTxRfOpmodeParams_ObjectIdentity = ObjectIdentity
eventTxRfOpmodeParams = _EventTxRfOpmodeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    eventTxRfOpmodeParams.setStatus("current")


class _EventTxRfOpmodePriority_Type(Gauge32):
    """Custom type eventTxRfOpmodePriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxRfOpmodePriority_Type.__name__ = "Gauge32"
_EventTxRfOpmodePriority_Object = MibScalar
eventTxRfOpmodePriority = _EventTxRfOpmodePriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 8, 1),
    _EventTxRfOpmodePriority_Type()
)
eventTxRfOpmodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxRfOpmodePriority.setStatus("current")


class _EventTxRfOpmodeEnable_Type(Integer32):
    """Custom type eventTxRfOpmodeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxRfOpmodeEnable_Type.__name__ = "Integer32"
_EventTxRfOpmodeEnable_Object = MibScalar
eventTxRfOpmodeEnable = _EventTxRfOpmodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 8, 2),
    _EventTxRfOpmodeEnable_Type()
)
eventTxRfOpmodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxRfOpmodeEnable.setStatus("current")
_EventTxRfRFPresentParams_ObjectIdentity = ObjectIdentity
eventTxRfRFPresentParams = _EventTxRfRFPresentParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    eventTxRfRFPresentParams.setStatus("current")


class _EventTxRfRFPresentPriority_Type(Gauge32):
    """Custom type eventTxRfRFPresentPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxRfRFPresentPriority_Type.__name__ = "Gauge32"
_EventTxRfRFPresentPriority_Object = MibScalar
eventTxRfRFPresentPriority = _EventTxRfRFPresentPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 9, 1),
    _EventTxRfRFPresentPriority_Type()
)
eventTxRfRFPresentPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxRfRFPresentPriority.setStatus("current")


class _EventTxRfRFPresentEnable_Type(Integer32):
    """Custom type eventTxRfRFPresentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxRfRFPresentEnable_Type.__name__ = "Integer32"
_EventTxRfRFPresentEnable_Object = MibScalar
eventTxRfRFPresentEnable = _EventTxRfRFPresentEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 9, 2),
    _EventTxRfRFPresentEnable_Type()
)
eventTxRfRFPresentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxRfRFPresentEnable.setStatus("current")
_EventAcReserveControlParams_ObjectIdentity = ObjectIdentity
eventAcReserveControlParams = _EventAcReserveControlParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    eventAcReserveControlParams.setStatus("current")


class _EventAcReserveControlPriority_Type(Gauge32):
    """Custom type eventAcReserveControlPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcReserveControlPriority_Type.__name__ = "Gauge32"
_EventAcReserveControlPriority_Object = MibScalar
eventAcReserveControlPriority = _EventAcReserveControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 10, 1),
    _EventAcReserveControlPriority_Type()
)
eventAcReserveControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcReserveControlPriority.setStatus("current")


class _EventAcReserveControlEnable_Type(Integer32):
    """Custom type eventAcReserveControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcReserveControlEnable_Type.__name__ = "Integer32"
_EventAcReserveControlEnable_Object = MibScalar
eventAcReserveControlEnable = _EventAcReserveControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 10, 2),
    _EventAcReserveControlEnable_Type()
)
eventAcReserveControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcReserveControlEnable.setStatus("current")
_EventAcLocalModeParams_ObjectIdentity = ObjectIdentity
eventAcLocalModeParams = _EventAcLocalModeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    eventAcLocalModeParams.setStatus("current")


class _EventAcLocalModePriority_Type(Gauge32):
    """Custom type eventAcLocalModePriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcLocalModePriority_Type.__name__ = "Gauge32"
_EventAcLocalModePriority_Object = MibScalar
eventAcLocalModePriority = _EventAcLocalModePriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 11, 1),
    _EventAcLocalModePriority_Type()
)
eventAcLocalModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcLocalModePriority.setStatus("current")


class _EventAcLocalModeEnable_Type(Integer32):
    """Custom type eventAcLocalModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcLocalModeEnable_Type.__name__ = "Integer32"
_EventAcLocalModeEnable_Object = MibScalar
eventAcLocalModeEnable = _EventAcLocalModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 11, 2),
    _EventAcLocalModeEnable_Type()
)
eventAcLocalModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcLocalModeEnable.setStatus("current")


class _AcLocalModeSignalSuppression_Type(Integer32):
    """Custom type acLocalModeSignalSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AcLocalModeSignalSuppression_Type.__name__ = "Integer32"
_AcLocalModeSignalSuppression_Object = MibScalar
acLocalModeSignalSuppression = _AcLocalModeSignalSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 11, 3),
    _AcLocalModeSignalSuppression_Type()
)
acLocalModeSignalSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLocalModeSignalSuppression.setStatus("current")
_EventAcFaultParams_ObjectIdentity = ObjectIdentity
eventAcFaultParams = _EventAcFaultParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 12)
)
if mibBuilder.loadTexts:
    eventAcFaultParams.setStatus("current")


class _EventAcFaultPriority_Type(Gauge32):
    """Custom type eventAcFaultPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcFaultPriority_Type.__name__ = "Gauge32"
_EventAcFaultPriority_Object = MibScalar
eventAcFaultPriority = _EventAcFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 12, 1),
    _EventAcFaultPriority_Type()
)
eventAcFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcFaultPriority.setStatus("current")


class _EventAcFaultEnable_Type(Integer32):
    """Custom type eventAcFaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcFaultEnable_Type.__name__ = "Integer32"
_EventAcFaultEnable_Object = MibScalar
eventAcFaultEnable = _EventAcFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 12, 2),
    _EventAcFaultEnable_Type()
)
eventAcFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcFaultEnable.setStatus("current")
_EventAcSwitchOverParams_ObjectIdentity = ObjectIdentity
eventAcSwitchOverParams = _EventAcSwitchOverParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 13)
)
if mibBuilder.loadTexts:
    eventAcSwitchOverParams.setStatus("current")


class _EventAcSwitchOverPriority_Type(Gauge32):
    """Custom type eventAcSwitchOverPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcSwitchOverPriority_Type.__name__ = "Gauge32"
_EventAcSwitchOverPriority_Object = MibScalar
eventAcSwitchOverPriority = _EventAcSwitchOverPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 13, 1),
    _EventAcSwitchOverPriority_Type()
)
eventAcSwitchOverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcSwitchOverPriority.setStatus("current")


class _EventAcSwitchOverEnable_Type(Integer32):
    """Custom type eventAcSwitchOverEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcSwitchOverEnable_Type.__name__ = "Integer32"
_EventAcSwitchOverEnable_Object = MibScalar
eventAcSwitchOverEnable = _EventAcSwitchOverEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 13, 2),
    _EventAcSwitchOverEnable_Type()
)
eventAcSwitchOverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcSwitchOverEnable.setStatus("current")
_EventSysWarningParams_ObjectIdentity = ObjectIdentity
eventSysWarningParams = _EventSysWarningParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 14)
)
if mibBuilder.loadTexts:
    eventSysWarningParams.setStatus("current")


class _EventSysWarningPriority_Type(Gauge32):
    """Custom type eventSysWarningPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysWarningPriority_Type.__name__ = "Gauge32"
_EventSysWarningPriority_Object = MibScalar
eventSysWarningPriority = _EventSysWarningPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 14, 1),
    _EventSysWarningPriority_Type()
)
eventSysWarningPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysWarningPriority.setStatus("current")


class _EventSysWarningEnable_Type(Integer32):
    """Custom type eventSysWarningEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysWarningEnable_Type.__name__ = "Integer32"
_EventSysWarningEnable_Object = MibScalar
eventSysWarningEnable = _EventSysWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 14, 2),
    _EventSysWarningEnable_Type()
)
eventSysWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysWarningEnable.setStatus("current")
_EventSysFaultParams_ObjectIdentity = ObjectIdentity
eventSysFaultParams = _EventSysFaultParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 15)
)
if mibBuilder.loadTexts:
    eventSysFaultParams.setStatus("current")


class _EventSysFaultPriority_Type(Gauge32):
    """Custom type eventSysFaultPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysFaultPriority_Type.__name__ = "Gauge32"
_EventSysFaultPriority_Object = MibScalar
eventSysFaultPriority = _EventSysFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 15, 1),
    _EventSysFaultPriority_Type()
)
eventSysFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysFaultPriority.setStatus("current")


class _EventSysFaultEnable_Type(Integer32):
    """Custom type eventSysFaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysFaultEnable_Type.__name__ = "Integer32"
_EventSysFaultEnable_Object = MibScalar
eventSysFaultEnable = _EventSysFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 15, 2),
    _EventSysFaultEnable_Type()
)
eventSysFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysFaultEnable.setStatus("current")
_EventSysAlAmbParams_ObjectIdentity = ObjectIdentity
eventSysAlAmbParams = _EventSysAlAmbParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 16)
)
if mibBuilder.loadTexts:
    eventSysAlAmbParams.setStatus("current")


class _EventSysAlAmbPriority_Type(Gauge32):
    """Custom type eventSysAlAmbPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlAmbPriority_Type.__name__ = "Gauge32"
_EventSysAlAmbPriority_Object = MibScalar
eventSysAlAmbPriority = _EventSysAlAmbPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 16, 1),
    _EventSysAlAmbPriority_Type()
)
eventSysAlAmbPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlAmbPriority.setStatus("current")


class _EventSysAlAmbEnable_Type(Integer32):
    """Custom type eventSysAlAmbEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlAmbEnable_Type.__name__ = "Integer32"
_EventSysAlAmbEnable_Object = MibScalar
eventSysAlAmbEnable = _EventSysAlAmbEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 16, 2),
    _EventSysAlAmbEnable_Type()
)
eventSysAlAmbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlAmbEnable.setStatus("current")
_EventSysAlVoltAuxParams_ObjectIdentity = ObjectIdentity
eventSysAlVoltAuxParams = _EventSysAlVoltAuxParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 17)
)
if mibBuilder.loadTexts:
    eventSysAlVoltAuxParams.setStatus("current")


class _EventSysAlVoltAuxPriority_Type(Gauge32):
    """Custom type eventSysAlVoltAuxPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlVoltAuxPriority_Type.__name__ = "Gauge32"
_EventSysAlVoltAuxPriority_Object = MibScalar
eventSysAlVoltAuxPriority = _EventSysAlVoltAuxPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 17, 1),
    _EventSysAlVoltAuxPriority_Type()
)
eventSysAlVoltAuxPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlVoltAuxPriority.setStatus("current")


class _EventSysAlVoltAuxEnable_Type(Integer32):
    """Custom type eventSysAlVoltAuxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlVoltAuxEnable_Type.__name__ = "Integer32"
_EventSysAlVoltAuxEnable_Object = MibScalar
eventSysAlVoltAuxEnable = _EventSysAlVoltAuxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 17, 2),
    _EventSysAlVoltAuxEnable_Type()
)
eventSysAlVoltAuxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlVoltAuxEnable.setStatus("current")
_EventSysAlRelayParams_ObjectIdentity = ObjectIdentity
eventSysAlRelayParams = _EventSysAlRelayParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 18)
)
if mibBuilder.loadTexts:
    eventSysAlRelayParams.setStatus("current")


class _EventSysAlRelayPriority_Type(Gauge32):
    """Custom type eventSysAlRelayPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlRelayPriority_Type.__name__ = "Gauge32"
_EventSysAlRelayPriority_Object = MibScalar
eventSysAlRelayPriority = _EventSysAlRelayPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 18, 1),
    _EventSysAlRelayPriority_Type()
)
eventSysAlRelayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlRelayPriority.setStatus("current")


class _EventSysAlRelayEnable_Type(Integer32):
    """Custom type eventSysAlRelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlRelayEnable_Type.__name__ = "Integer32"
_EventSysAlRelayEnable_Object = MibScalar
eventSysAlRelayEnable = _EventSysAlRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 18, 2),
    _EventSysAlRelayEnable_Type()
)
eventSysAlRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlRelayEnable.setStatus("current")
_EventSysAlReserveParams_ObjectIdentity = ObjectIdentity
eventSysAlReserveParams = _EventSysAlReserveParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 19)
)
if mibBuilder.loadTexts:
    eventSysAlReserveParams.setStatus("current")


class _EventSysAlReservePriority_Type(Gauge32):
    """Custom type eventSysAlReservePriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlReservePriority_Type.__name__ = "Gauge32"
_EventSysAlReservePriority_Object = MibScalar
eventSysAlReservePriority = _EventSysAlReservePriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 19, 1),
    _EventSysAlReservePriority_Type()
)
eventSysAlReservePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlReservePriority.setStatus("current")


class _EventSysAlReserveEnable_Type(Integer32):
    """Custom type eventSysAlReserveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlReserveEnable_Type.__name__ = "Integer32"
_EventSysAlReserveEnable_Object = MibScalar
eventSysAlReserveEnable = _EventSysAlReserveEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 19, 2),
    _EventSysAlReserveEnable_Type()
)
eventSysAlReserveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlReserveEnable.setStatus("current")
_EventInSeAlrInputSwitchParams_ObjectIdentity = ObjectIdentity
eventInSeAlrInputSwitchParams = _EventInSeAlrInputSwitchParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 20)
)
if mibBuilder.loadTexts:
    eventInSeAlrInputSwitchParams.setStatus("current")


class _EventInSeAlrInputSwitchPriority_Type(Gauge32):
    """Custom type eventInSeAlrInputSwitchPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInSeAlrInputSwitchPriority_Type.__name__ = "Gauge32"
_EventInSeAlrInputSwitchPriority_Object = MibScalar
eventInSeAlrInputSwitchPriority = _EventInSeAlrInputSwitchPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 20, 1),
    _EventInSeAlrInputSwitchPriority_Type()
)
eventInSeAlrInputSwitchPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInSeAlrInputSwitchPriority.setStatus("current")


class _EventInSeAlrInputSwitchEnable_Type(Integer32):
    """Custom type eventInSeAlrInputSwitchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInSeAlrInputSwitchEnable_Type.__name__ = "Integer32"
_EventInSeAlrInputSwitchEnable_Object = MibScalar
eventInSeAlrInputSwitchEnable = _EventInSeAlrInputSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 20, 2),
    _EventInSeAlrInputSwitchEnable_Type()
)
eventInSeAlrInputSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInSeAlrInputSwitchEnable.setStatus("current")
_EventTxAl1dBParams_ObjectIdentity = ObjectIdentity
eventTxAl1dBParams = _EventTxAl1dBParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 21)
)
if mibBuilder.loadTexts:
    eventTxAl1dBParams.setStatus("current")


class _EventTxAl1dBPriority_Type(Gauge32):
    """Custom type eventTxAl1dBPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxAl1dBPriority_Type.__name__ = "Gauge32"
_EventTxAl1dBPriority_Object = MibScalar
eventTxAl1dBPriority = _EventTxAl1dBPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 21, 1),
    _EventTxAl1dBPriority_Type()
)
eventTxAl1dBPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAl1dBPriority.setStatus("current")


class _EventTxAl1dBEnable_Type(Integer32):
    """Custom type eventTxAl1dBEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxAl1dBEnable_Type.__name__ = "Integer32"
_EventTxAl1dBEnable_Object = MibScalar
eventTxAl1dBEnable = _EventTxAl1dBEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 21, 2),
    _EventTxAl1dBEnable_Type()
)
eventTxAl1dBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxAl1dBEnable.setStatus("current")
_EventTxGnGlStandbyParams_ObjectIdentity = ObjectIdentity
eventTxGnGlStandbyParams = _EventTxGnGlStandbyParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 22)
)
if mibBuilder.loadTexts:
    eventTxGnGlStandbyParams.setStatus("current")


class _EventTxGnGlStandbyPriority_Type(Gauge32):
    """Custom type eventTxGnGlStandbyPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxGnGlStandbyPriority_Type.__name__ = "Gauge32"
_EventTxGnGlStandbyPriority_Object = MibScalar
eventTxGnGlStandbyPriority = _EventTxGnGlStandbyPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 22, 1),
    _EventTxGnGlStandbyPriority_Type()
)
eventTxGnGlStandbyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxGnGlStandbyPriority.setStatus("current")


class _EventTxGnGlStandbyEnable_Type(Integer32):
    """Custom type eventTxGnGlStandbyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxGnGlStandbyEnable_Type.__name__ = "Integer32"
_EventTxGnGlStandbyEnable_Object = MibScalar
eventTxGnGlStandbyEnable = _EventTxGnGlStandbyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 22, 2),
    _EventTxGnGlStandbyEnable_Type()
)
eventTxGnGlStandbyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxGnGlStandbyEnable.setStatus("current")
_EventInAlLine1Params_ObjectIdentity = ObjectIdentity
eventInAlLine1Params = _EventInAlLine1Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 23)
)
if mibBuilder.loadTexts:
    eventInAlLine1Params.setStatus("current")


class _EventInAlLine1Priority_Type(Gauge32):
    """Custom type eventInAlLine1Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlLine1Priority_Type.__name__ = "Gauge32"
_EventInAlLine1Priority_Object = MibScalar
eventInAlLine1Priority = _EventInAlLine1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 23, 1),
    _EventInAlLine1Priority_Type()
)
eventInAlLine1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlLine1Priority.setStatus("current")


class _EventInAlLine1Enable_Type(Integer32):
    """Custom type eventInAlLine1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlLine1Enable_Type.__name__ = "Integer32"
_EventInAlLine1Enable_Object = MibScalar
eventInAlLine1Enable = _EventInAlLine1Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 23, 2),
    _EventInAlLine1Enable_Type()
)
eventInAlLine1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlLine1Enable.setStatus("current")
_EventInAlLine2Params_ObjectIdentity = ObjectIdentity
eventInAlLine2Params = _EventInAlLine2Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 24)
)
if mibBuilder.loadTexts:
    eventInAlLine2Params.setStatus("current")


class _EventInAlLine2Priority_Type(Gauge32):
    """Custom type eventInAlLine2Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlLine2Priority_Type.__name__ = "Gauge32"
_EventInAlLine2Priority_Object = MibScalar
eventInAlLine2Priority = _EventInAlLine2Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 24, 1),
    _EventInAlLine2Priority_Type()
)
eventInAlLine2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlLine2Priority.setStatus("current")


class _EventInAlLine2Enable_Type(Integer32):
    """Custom type eventInAlLine2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlLine2Enable_Type.__name__ = "Integer32"
_EventInAlLine2Enable_Object = MibScalar
eventInAlLine2Enable = _EventInAlLine2Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 24, 2),
    _EventInAlLine2Enable_Type()
)
eventInAlLine2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlLine2Enable.setStatus("current")
_EventInAlMpx1Params_ObjectIdentity = ObjectIdentity
eventInAlMpx1Params = _EventInAlMpx1Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 25)
)
if mibBuilder.loadTexts:
    eventInAlMpx1Params.setStatus("current")


class _EventInAlMpx1Priority_Type(Gauge32):
    """Custom type eventInAlMpx1Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlMpx1Priority_Type.__name__ = "Gauge32"
_EventInAlMpx1Priority_Object = MibScalar
eventInAlMpx1Priority = _EventInAlMpx1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 25, 1),
    _EventInAlMpx1Priority_Type()
)
eventInAlMpx1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx1Priority.setStatus("current")


class _EventInAlMpx1Enable_Type(Integer32):
    """Custom type eventInAlMpx1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlMpx1Enable_Type.__name__ = "Integer32"
_EventInAlMpx1Enable_Object = MibScalar
eventInAlMpx1Enable = _EventInAlMpx1Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 25, 2),
    _EventInAlMpx1Enable_Type()
)
eventInAlMpx1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx1Enable.setStatus("current")
_EventInAlMpx2Params_ObjectIdentity = ObjectIdentity
eventInAlMpx2Params = _EventInAlMpx2Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 26)
)
if mibBuilder.loadTexts:
    eventInAlMpx2Params.setStatus("current")


class _EventInAlMpx2Priority_Type(Gauge32):
    """Custom type eventInAlMpx2Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlMpx2Priority_Type.__name__ = "Gauge32"
_EventInAlMpx2Priority_Object = MibScalar
eventInAlMpx2Priority = _EventInAlMpx2Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 26, 1),
    _EventInAlMpx2Priority_Type()
)
eventInAlMpx2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx2Priority.setStatus("current")


class _EventInAlMpx2Enable_Type(Integer32):
    """Custom type eventInAlMpx2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlMpx2Enable_Type.__name__ = "Integer32"
_EventInAlMpx2Enable_Object = MibScalar
eventInAlMpx2Enable = _EventInAlMpx2Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 26, 2),
    _EventInAlMpx2Enable_Type()
)
eventInAlMpx2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx2Enable.setStatus("current")
_EventInAlPlayerParams_ObjectIdentity = ObjectIdentity
eventInAlPlayerParams = _EventInAlPlayerParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 27)
)
if mibBuilder.loadTexts:
    eventInAlPlayerParams.setStatus("current")


class _EventInAlPlayerPriority_Type(Gauge32):
    """Custom type eventInAlPlayerPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlPlayerPriority_Type.__name__ = "Gauge32"
_EventInAlPlayerPriority_Object = MibScalar
eventInAlPlayerPriority = _EventInAlPlayerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 27, 1),
    _EventInAlPlayerPriority_Type()
)
eventInAlPlayerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlPlayerPriority.setStatus("current")


class _EventInAlPlayerEnable_Type(Integer32):
    """Custom type eventInAlPlayerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlPlayerEnable_Type.__name__ = "Integer32"
_EventInAlPlayerEnable_Object = MibScalar
eventInAlPlayerEnable = _EventInAlPlayerEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 27, 2),
    _EventInAlPlayerEnable_Type()
)
eventInAlPlayerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlPlayerEnable.setStatus("current")
_EventSysAlInvalidDataParams_ObjectIdentity = ObjectIdentity
eventSysAlInvalidDataParams = _EventSysAlInvalidDataParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 28)
)
if mibBuilder.loadTexts:
    eventSysAlInvalidDataParams.setStatus("current")


class _EventSysAlInvalidDataPriority_Type(Gauge32):
    """Custom type eventSysAlInvalidDataPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlInvalidDataPriority_Type.__name__ = "Gauge32"
_EventSysAlInvalidDataPriority_Object = MibScalar
eventSysAlInvalidDataPriority = _EventSysAlInvalidDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 28, 1),
    _EventSysAlInvalidDataPriority_Type()
)
eventSysAlInvalidDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlInvalidDataPriority.setStatus("current")


class _EventSysAlInvalidDataEnable_Type(Integer32):
    """Custom type eventSysAlInvalidDataEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlInvalidDataEnable_Type.__name__ = "Integer32"
_EventSysAlInvalidDataEnable_Object = MibScalar
eventSysAlInvalidDataEnable = _EventSysAlInvalidDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 28, 2),
    _EventSysAlInvalidDataEnable_Type()
)
eventSysAlInvalidDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlInvalidDataEnable.setStatus("current")
_EventAcGnAlInterlockAntParams_ObjectIdentity = ObjectIdentity
eventAcGnAlInterlockAntParams = _EventAcGnAlInterlockAntParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 29)
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockAntParams.setStatus("current")


class _EventAcGnAlInterlockAntPriority_Type(Gauge32):
    """Custom type eventAcGnAlInterlockAntPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcGnAlInterlockAntPriority_Type.__name__ = "Gauge32"
_EventAcGnAlInterlockAntPriority_Object = MibScalar
eventAcGnAlInterlockAntPriority = _EventAcGnAlInterlockAntPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 29, 1),
    _EventAcGnAlInterlockAntPriority_Type()
)
eventAcGnAlInterlockAntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcGnAlInterlockAntPriority.setStatus("current")


class _EventAcGnAlInterlockAntEnable_Type(Integer32):
    """Custom type eventAcGnAlInterlockAntEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcGnAlInterlockAntEnable_Type.__name__ = "Integer32"
_EventAcGnAlInterlockAntEnable_Object = MibScalar
eventAcGnAlInterlockAntEnable = _EventAcGnAlInterlockAntEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 29, 2),
    _EventAcGnAlInterlockAntEnable_Type()
)
eventAcGnAlInterlockAntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcGnAlInterlockAntEnable.setStatus("current")
_EventAcGnAlInterlockLoadParams_ObjectIdentity = ObjectIdentity
eventAcGnAlInterlockLoadParams = _EventAcGnAlInterlockLoadParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 30)
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockLoadParams.setStatus("current")


class _EventAcGnAlInterlockLoadPriority_Type(Gauge32):
    """Custom type eventAcGnAlInterlockLoadPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventAcGnAlInterlockLoadPriority_Type.__name__ = "Gauge32"
_EventAcGnAlInterlockLoadPriority_Object = MibScalar
eventAcGnAlInterlockLoadPriority = _EventAcGnAlInterlockLoadPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 30, 1),
    _EventAcGnAlInterlockLoadPriority_Type()
)
eventAcGnAlInterlockLoadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcGnAlInterlockLoadPriority.setStatus("current")


class _EventAcGnAlInterlockLoadEnable_Type(Integer32):
    """Custom type eventAcGnAlInterlockLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventAcGnAlInterlockLoadEnable_Type.__name__ = "Integer32"
_EventAcGnAlInterlockLoadEnable_Object = MibScalar
eventAcGnAlInterlockLoadEnable = _EventAcGnAlInterlockLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 30, 2),
    _EventAcGnAlInterlockLoadEnable_Type()
)
eventAcGnAlInterlockLoadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAcGnAlInterlockLoadEnable.setStatus("current")
_EventSysAl24vParams_ObjectIdentity = ObjectIdentity
eventSysAl24vParams = _EventSysAl24vParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 31)
)
if mibBuilder.loadTexts:
    eventSysAl24vParams.setStatus("current")


class _EventSysAl24vPriority_Type(Gauge32):
    """Custom type eventSysAl24vPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAl24vPriority_Type.__name__ = "Gauge32"
_EventSysAl24vPriority_Object = MibScalar
eventSysAl24vPriority = _EventSysAl24vPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 31, 1),
    _EventSysAl24vPriority_Type()
)
eventSysAl24vPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAl24vPriority.setStatus("current")


class _EventSysAl24vEnable_Type(Integer32):
    """Custom type eventSysAl24vEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAl24vEnable_Type.__name__ = "Integer32"
_EventSysAl24vEnable_Object = MibScalar
eventSysAl24vEnable = _EventSysAl24vEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 31, 2),
    _EventSysAl24vEnable_Type()
)
eventSysAl24vEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAl24vEnable.setStatus("current")
_EventSysAlCommParams_ObjectIdentity = ObjectIdentity
eventSysAlCommParams = _EventSysAlCommParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 32)
)
if mibBuilder.loadTexts:
    eventSysAlCommParams.setStatus("current")


class _EventSysAlCommPriority_Type(Gauge32):
    """Custom type eventSysAlCommPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSysAlCommPriority_Type.__name__ = "Gauge32"
_EventSysAlCommPriority_Object = MibScalar
eventSysAlCommPriority = _EventSysAlCommPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 32, 1),
    _EventSysAlCommPriority_Type()
)
eventSysAlCommPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlCommPriority.setStatus("current")


class _EventSysAlCommEnable_Type(Integer32):
    """Custom type eventSysAlCommEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSysAlCommEnable_Type.__name__ = "Integer32"
_EventSysAlCommEnable_Object = MibScalar
eventSysAlCommEnable = _EventSysAlCommEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 32, 2),
    _EventSysAlCommEnable_Type()
)
eventSysAlCommEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSysAlCommEnable.setStatus("current")
_EventEquipmentOnParams_ObjectIdentity = ObjectIdentity
eventEquipmentOnParams = _EventEquipmentOnParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 33)
)
if mibBuilder.loadTexts:
    eventEquipmentOnParams.setStatus("current")


class _EventEquipmentOnPriority_Type(Gauge32):
    """Custom type eventEquipmentOnPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventEquipmentOnPriority_Type.__name__ = "Gauge32"
_EventEquipmentOnPriority_Object = MibScalar
eventEquipmentOnPriority = _EventEquipmentOnPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 33, 1),
    _EventEquipmentOnPriority_Type()
)
eventEquipmentOnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEquipmentOnPriority.setStatus("current")


class _EventEquipmentOnEnable_Type(Integer32):
    """Custom type eventEquipmentOnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventEquipmentOnEnable_Type.__name__ = "Integer32"
_EventEquipmentOnEnable_Object = MibScalar
eventEquipmentOnEnable = _EventEquipmentOnEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 33, 2),
    _EventEquipmentOnEnable_Type()
)
eventEquipmentOnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEquipmentOnEnable.setStatus("current")
_EventHeartBeatParams_ObjectIdentity = ObjectIdentity
eventHeartBeatParams = _EventHeartBeatParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 34)
)
if mibBuilder.loadTexts:
    eventHeartBeatParams.setStatus("current")


class _EventHeartBeatPriority_Type(Gauge32):
    """Custom type eventHeartBeatPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventHeartBeatPriority_Type.__name__ = "Gauge32"
_EventHeartBeatPriority_Object = MibScalar
eventHeartBeatPriority = _EventHeartBeatPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 34, 1),
    _EventHeartBeatPriority_Type()
)
eventHeartBeatPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventHeartBeatPriority.setStatus("current")


class _EventHeartBeatEnable_Type(Integer32):
    """Custom type eventHeartBeatEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventHeartBeatEnable_Type.__name__ = "Integer32"
_EventHeartBeatEnable_Object = MibScalar
eventHeartBeatEnable = _EventHeartBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 34, 2),
    _EventHeartBeatEnable_Type()
)
eventHeartBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventHeartBeatEnable.setStatus("current")
_EventConfigChangedParams_ObjectIdentity = ObjectIdentity
eventConfigChangedParams = _EventConfigChangedParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 35)
)
if mibBuilder.loadTexts:
    eventConfigChangedParams.setStatus("current")


class _EventConfigChangedPriority_Type(Gauge32):
    """Custom type eventConfigChangedPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventConfigChangedPriority_Type.__name__ = "Gauge32"
_EventConfigChangedPriority_Object = MibScalar
eventConfigChangedPriority = _EventConfigChangedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 35, 1),
    _EventConfigChangedPriority_Type()
)
eventConfigChangedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigChangedPriority.setStatus("current")


class _EventConfigChangedEnable_Type(Integer32):
    """Custom type eventConfigChangedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventConfigChangedEnable_Type.__name__ = "Integer32"
_EventConfigChangedEnable_Object = MibScalar
eventConfigChangedEnable = _EventConfigChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 35, 2),
    _EventConfigChangedEnable_Type()
)
eventConfigChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigChangedEnable.setStatus("current")
_EventEquipmentFaultParams_ObjectIdentity = ObjectIdentity
eventEquipmentFaultParams = _EventEquipmentFaultParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 36)
)
if mibBuilder.loadTexts:
    eventEquipmentFaultParams.setStatus("obsolete")


class _EventEquipmentFaultPriority_Type(Gauge32):
    """Custom type eventEquipmentFaultPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventEquipmentFaultPriority_Type.__name__ = "Gauge32"
_EventEquipmentFaultPriority_Object = MibScalar
eventEquipmentFaultPriority = _EventEquipmentFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 36, 1),
    _EventEquipmentFaultPriority_Type()
)
eventEquipmentFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEquipmentFaultPriority.setStatus("obsolete")


class _EventEquipmentFaultEnable_Type(Integer32):
    """Custom type eventEquipmentFaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventEquipmentFaultEnable_Type.__name__ = "Integer32"
_EventEquipmentFaultEnable_Object = MibScalar
eventEquipmentFaultEnable = _EventEquipmentFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 36, 2),
    _EventEquipmentFaultEnable_Type()
)
eventEquipmentFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEquipmentFaultEnable.setStatus("obsolete")
_EventInAlFaultParams_ObjectIdentity = ObjectIdentity
eventInAlFaultParams = _EventInAlFaultParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 37)
)
if mibBuilder.loadTexts:
    eventInAlFaultParams.setStatus("obsolete")


class _EventInAlFaultPriority_Type(Gauge32):
    """Custom type eventInAlFaultPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlFaultPriority_Type.__name__ = "Gauge32"
_EventInAlFaultPriority_Object = MibScalar
eventInAlFaultPriority = _EventInAlFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 37, 1),
    _EventInAlFaultPriority_Type()
)
eventInAlFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlFaultPriority.setStatus("current")


class _EventInAlFaultEnable_Type(Integer32):
    """Custom type eventInAlFaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlFaultEnable_Type.__name__ = "Integer32"
_EventInAlFaultEnable_Object = MibScalar
eventInAlFaultEnable = _EventInAlFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 37, 2),
    _EventInAlFaultEnable_Type()
)
eventInAlFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlFaultEnable.setStatus("current")
_EventMoSfAlarmParams_ObjectIdentity = ObjectIdentity
eventMoSfAlarmParams = _EventMoSfAlarmParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 38)
)
if mibBuilder.loadTexts:
    eventMoSfAlarmParams.setStatus("current")


class _EventMoSfAlarmPriority_Type(Gauge32):
    """Custom type eventMoSfAlarmPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventMoSfAlarmPriority_Type.__name__ = "Gauge32"
_EventMoSfAlarmPriority_Object = MibScalar
eventMoSfAlarmPriority = _EventMoSfAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 38, 1),
    _EventMoSfAlarmPriority_Type()
)
eventMoSfAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventMoSfAlarmPriority.setStatus("current")


class _EventMoSfAlarmEnable_Type(Integer32):
    """Custom type eventMoSfAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventMoSfAlarmEnable_Type.__name__ = "Integer32"
_EventMoSfAlarmEnable_Object = MibScalar
eventMoSfAlarmEnable = _EventMoSfAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 38, 2),
    _EventMoSfAlarmEnable_Type()
)
eventMoSfAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventMoSfAlarmEnable.setStatus("current")
_EventMoSfSwitch10MAlarmParams_ObjectIdentity = ObjectIdentity
eventMoSfSwitch10MAlarmParams = _EventMoSfSwitch10MAlarmParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 39)
)
if mibBuilder.loadTexts:
    eventMoSfSwitch10MAlarmParams.setStatus("current")


class _EventMoSfSwitch10MAlarmPriority_Type(Gauge32):
    """Custom type eventMoSfSwitch10MAlarmPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventMoSfSwitch10MAlarmPriority_Type.__name__ = "Gauge32"
_EventMoSfSwitch10MAlarmPriority_Object = MibScalar
eventMoSfSwitch10MAlarmPriority = _EventMoSfSwitch10MAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 39, 1),
    _EventMoSfSwitch10MAlarmPriority_Type()
)
eventMoSfSwitch10MAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventMoSfSwitch10MAlarmPriority.setStatus("current")


class _EventMoSfSwitch10MAlarmEnable_Type(Integer32):
    """Custom type eventMoSfSwitch10MAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventMoSfSwitch10MAlarmEnable_Type.__name__ = "Integer32"
_EventMoSfSwitch10MAlarmEnable_Object = MibScalar
eventMoSfSwitch10MAlarmEnable = _EventMoSfSwitch10MAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 39, 2),
    _EventMoSfSwitch10MAlarmEnable_Type()
)
eventMoSfSwitch10MAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventMoSfSwitch10MAlarmEnable.setStatus("current")
_EventSyAlLoggingParams_ObjectIdentity = ObjectIdentity
eventSyAlLoggingParams = _EventSyAlLoggingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 40)
)
if mibBuilder.loadTexts:
    eventSyAlLoggingParams.setStatus("current")


class _EventSyAlLoggingPriority_Type(Gauge32):
    """Custom type eventSyAlLoggingPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyAlLoggingPriority_Type.__name__ = "Gauge32"
_EventSyAlLoggingPriority_Object = MibScalar
eventSyAlLoggingPriority = _EventSyAlLoggingPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 40, 1),
    _EventSyAlLoggingPriority_Type()
)
eventSyAlLoggingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyAlLoggingPriority.setStatus("current")


class _EventSyAlLoggingEnable_Type(Integer32):
    """Custom type eventSyAlLoggingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyAlLoggingEnable_Type.__name__ = "Integer32"
_EventSyAlLoggingEnable_Object = MibScalar
eventSyAlLoggingEnable = _EventSyAlLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 40, 2),
    _EventSyAlLoggingEnable_Type()
)
eventSyAlLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyAlLoggingEnable.setStatus("current")
_EventInAlMpx3Params_ObjectIdentity = ObjectIdentity
eventInAlMpx3Params = _EventInAlMpx3Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 41)
)
if mibBuilder.loadTexts:
    eventInAlMpx3Params.setStatus("current")


class _EventInAlMpx3Priority_Type(Gauge32):
    """Custom type eventInAlMpx3Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlMpx3Priority_Type.__name__ = "Gauge32"
_EventInAlMpx3Priority_Object = MibScalar
eventInAlMpx3Priority = _EventInAlMpx3Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 41, 1),
    _EventInAlMpx3Priority_Type()
)
eventInAlMpx3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx3Priority.setStatus("current")


class _EventInAlMpx3Enable_Type(Integer32):
    """Custom type eventInAlMpx3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlMpx3Enable_Type.__name__ = "Integer32"
_EventInAlMpx3Enable_Object = MibScalar
eventInAlMpx3Enable = _EventInAlMpx3Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 41, 2),
    _EventInAlMpx3Enable_Type()
)
eventInAlMpx3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx3Enable.setStatus("current")
_EventInAlMpx4Params_ObjectIdentity = ObjectIdentity
eventInAlMpx4Params = _EventInAlMpx4Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 42)
)
if mibBuilder.loadTexts:
    eventInAlMpx4Params.setStatus("current")


class _EventInAlMpx4Priority_Type(Gauge32):
    """Custom type eventInAlMpx4Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlMpx4Priority_Type.__name__ = "Gauge32"
_EventInAlMpx4Priority_Object = MibScalar
eventInAlMpx4Priority = _EventInAlMpx4Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 42, 1),
    _EventInAlMpx4Priority_Type()
)
eventInAlMpx4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx4Priority.setStatus("current")


class _EventInAlMpx4Enable_Type(Integer32):
    """Custom type eventInAlMpx4Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlMpx4Enable_Type.__name__ = "Integer32"
_EventInAlMpx4Enable_Object = MibScalar
eventInAlMpx4Enable = _EventInAlMpx4Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 42, 2),
    _EventInAlMpx4Enable_Type()
)
eventInAlMpx4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlMpx4Enable.setStatus("current")
_EventTxSfStActParams_ObjectIdentity = ObjectIdentity
eventTxSfStActParams = _EventTxSfStActParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 43)
)
if mibBuilder.loadTexts:
    eventTxSfStActParams.setStatus("current")


class _EventTxSfStActPriority_Type(Gauge32):
    """Custom type eventTxSfStActPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxSfStActPriority_Type.__name__ = "Gauge32"
_EventTxSfStActPriority_Object = MibScalar
eventTxSfStActPriority = _EventTxSfStActPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 43, 1),
    _EventTxSfStActPriority_Type()
)
eventTxSfStActPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxSfStActPriority.setStatus("current")


class _EventTxSfStActEnable_Type(Integer32):
    """Custom type eventTxSfStActEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxSfStActEnable_Type.__name__ = "Integer32"
_EventTxSfStActEnable_Object = MibScalar
eventTxSfStActEnable = _EventTxSfStActEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 43, 2),
    _EventTxSfStActEnable_Type()
)
eventTxSfStActEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxSfStActEnable.setStatus("current")
_EventTxSfStAlarmParams_ObjectIdentity = ObjectIdentity
eventTxSfStAlarmParams = _EventTxSfStAlarmParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 44)
)
if mibBuilder.loadTexts:
    eventTxSfStAlarmParams.setStatus("current")


class _EventTxSfStAlarmPriority_Type(Gauge32):
    """Custom type eventTxSfStAlarmPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventTxSfStAlarmPriority_Type.__name__ = "Gauge32"
_EventTxSfStAlarmPriority_Object = MibScalar
eventTxSfStAlarmPriority = _EventTxSfStAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 44, 1),
    _EventTxSfStAlarmPriority_Type()
)
eventTxSfStAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxSfStAlarmPriority.setStatus("current")


class _EventTxSfStAlarmEnable_Type(Integer32):
    """Custom type eventTxSfStAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventTxSfStAlarmEnable_Type.__name__ = "Integer32"
_EventTxSfStAlarmEnable_Object = MibScalar
eventTxSfStAlarmEnable = _EventTxSfStAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 44, 2),
    _EventTxSfStAlarmEnable_Type()
)
eventTxSfStAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxSfStAlarmEnable.setStatus("current")
_EventSyLiAlRdsParams_ObjectIdentity = ObjectIdentity
eventSyLiAlRdsParams = _EventSyLiAlRdsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 45)
)
if mibBuilder.loadTexts:
    eventSyLiAlRdsParams.setStatus("current")


class _EventSyLiAlRdsPriority_Type(Gauge32):
    """Custom type eventSyLiAlRdsPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlRdsPriority_Type.__name__ = "Gauge32"
_EventSyLiAlRdsPriority_Object = MibScalar
eventSyLiAlRdsPriority = _EventSyLiAlRdsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 45, 1),
    _EventSyLiAlRdsPriority_Type()
)
eventSyLiAlRdsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlRdsPriority.setStatus("current")


class _EventSyLiAlRdsEnable_Type(Integer32):
    """Custom type eventSyLiAlRdsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlRdsEnable_Type.__name__ = "Integer32"
_EventSyLiAlRdsEnable_Object = MibScalar
eventSyLiAlRdsEnable = _EventSyLiAlRdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 45, 2),
    _EventSyLiAlRdsEnable_Type()
)
eventSyLiAlRdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlRdsEnable.setStatus("current")
_EventSyLiAlSoundProcParams_ObjectIdentity = ObjectIdentity
eventSyLiAlSoundProcParams = _EventSyLiAlSoundProcParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 46)
)
if mibBuilder.loadTexts:
    eventSyLiAlSoundProcParams.setStatus("current")


class _EventSyLiAlSoundProcPriority_Type(Gauge32):
    """Custom type eventSyLiAlSoundProcPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlSoundProcPriority_Type.__name__ = "Gauge32"
_EventSyLiAlSoundProcPriority_Object = MibScalar
eventSyLiAlSoundProcPriority = _EventSyLiAlSoundProcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 46, 1),
    _EventSyLiAlSoundProcPriority_Type()
)
eventSyLiAlSoundProcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSoundProcPriority.setStatus("current")


class _EventSyLiAlSoundProcEnable_Type(Integer32):
    """Custom type eventSyLiAlSoundProcEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlSoundProcEnable_Type.__name__ = "Integer32"
_EventSyLiAlSoundProcEnable_Object = MibScalar
eventSyLiAlSoundProcEnable = _EventSyLiAlSoundProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 46, 2),
    _EventSyLiAlSoundProcEnable_Type()
)
eventSyLiAlSoundProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSoundProcEnable.setStatus("current")
_EventSyLiAlSfmParams_ObjectIdentity = ObjectIdentity
eventSyLiAlSfmParams = _EventSyLiAlSfmParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 47)
)
if mibBuilder.loadTexts:
    eventSyLiAlSfmParams.setStatus("current")


class _EventSyLiAlSfmPriority_Type(Gauge32):
    """Custom type eventSyLiAlSfmPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlSfmPriority_Type.__name__ = "Gauge32"
_EventSyLiAlSfmPriority_Object = MibScalar
eventSyLiAlSfmPriority = _EventSyLiAlSfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 47, 1),
    _EventSyLiAlSfmPriority_Type()
)
eventSyLiAlSfmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSfmPriority.setStatus("current")


class _EventSyLiAlSfmEnable_Type(Integer32):
    """Custom type eventSyLiAlSfmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlSfmEnable_Type.__name__ = "Integer32"
_EventSyLiAlSfmEnable_Object = MibScalar
eventSyLiAlSfmEnable = _EventSyLiAlSfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 47, 2),
    _EventSyLiAlSfmEnable_Type()
)
eventSyLiAlSfmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSfmEnable.setStatus("current")
_EventSyLiAlActivationParams_ObjectIdentity = ObjectIdentity
eventSyLiAlActivationParams = _EventSyLiAlActivationParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 48)
)
if mibBuilder.loadTexts:
    eventSyLiAlActivationParams.setStatus("current")


class _EventSyLiAlActivationPriority_Type(Gauge32):
    """Custom type eventSyLiAlActivationPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlActivationPriority_Type.__name__ = "Gauge32"
_EventSyLiAlActivationPriority_Object = MibScalar
eventSyLiAlActivationPriority = _EventSyLiAlActivationPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 48, 1),
    _EventSyLiAlActivationPriority_Type()
)
eventSyLiAlActivationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlActivationPriority.setStatus("current")


class _EventSyLiAlActivationEnable_Type(Integer32):
    """Custom type eventSyLiAlActivationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlActivationEnable_Type.__name__ = "Integer32"
_EventSyLiAlActivationEnable_Object = MibScalar
eventSyLiAlActivationEnable = _EventSyLiAlActivationEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 48, 2),
    _EventSyLiAlActivationEnable_Type()
)
eventSyLiAlActivationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlActivationEnable.setStatus("current")
_EventInAlAes1Params_ObjectIdentity = ObjectIdentity
eventInAlAes1Params = _EventInAlAes1Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 49)
)
if mibBuilder.loadTexts:
    eventInAlAes1Params.setStatus("current")


class _EventInAlAes1Priority_Type(Gauge32):
    """Custom type eventInAlAes1Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlAes1Priority_Type.__name__ = "Gauge32"
_EventInAlAes1Priority_Object = MibScalar
eventInAlAes1Priority = _EventInAlAes1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 49, 1),
    _EventInAlAes1Priority_Type()
)
eventInAlAes1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes1Priority.setStatus("current")


class _EventInAlAes1Enable_Type(Integer32):
    """Custom type eventInAlAes1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlAes1Enable_Type.__name__ = "Integer32"
_EventInAlAes1Enable_Object = MibScalar
eventInAlAes1Enable = _EventInAlAes1Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 49, 2),
    _EventInAlAes1Enable_Type()
)
eventInAlAes1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes1Enable.setStatus("current")
_EventInAlAes2Params_ObjectIdentity = ObjectIdentity
eventInAlAes2Params = _EventInAlAes2Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 50)
)
if mibBuilder.loadTexts:
    eventInAlAes2Params.setStatus("current")


class _EventInAlAes2Priority_Type(Gauge32):
    """Custom type eventInAlAes2Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlAes2Priority_Type.__name__ = "Gauge32"
_EventInAlAes2Priority_Object = MibScalar
eventInAlAes2Priority = _EventInAlAes2Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 50, 1),
    _EventInAlAes2Priority_Type()
)
eventInAlAes2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes2Priority.setStatus("current")


class _EventInAlAes2Enable_Type(Integer32):
    """Custom type eventInAlAes2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlAes2Enable_Type.__name__ = "Integer32"
_EventInAlAes2Enable_Object = MibScalar
eventInAlAes2Enable = _EventInAlAes2Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 50, 2),
    _EventInAlAes2Enable_Type()
)
eventInAlAes2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes2Enable.setStatus("current")
_EventInAlAes3Params_ObjectIdentity = ObjectIdentity
eventInAlAes3Params = _EventInAlAes3Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 51)
)
if mibBuilder.loadTexts:
    eventInAlAes3Params.setStatus("current")


class _EventInAlAes3Priority_Type(Gauge32):
    """Custom type eventInAlAes3Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlAes3Priority_Type.__name__ = "Gauge32"
_EventInAlAes3Priority_Object = MibScalar
eventInAlAes3Priority = _EventInAlAes3Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 51, 1),
    _EventInAlAes3Priority_Type()
)
eventInAlAes3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes3Priority.setStatus("current")


class _EventInAlAes3Enable_Type(Integer32):
    """Custom type eventInAlAes3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlAes3Enable_Type.__name__ = "Integer32"
_EventInAlAes3Enable_Object = MibScalar
eventInAlAes3Enable = _EventInAlAes3Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 51, 2),
    _EventInAlAes3Enable_Type()
)
eventInAlAes3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAes3Enable.setStatus("current")
_EventInAlAna1Params_ObjectIdentity = ObjectIdentity
eventInAlAna1Params = _EventInAlAna1Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 52)
)
if mibBuilder.loadTexts:
    eventInAlAna1Params.setStatus("current")


class _EventInAlAna1Priority_Type(Gauge32):
    """Custom type eventInAlAna1Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlAna1Priority_Type.__name__ = "Gauge32"
_EventInAlAna1Priority_Object = MibScalar
eventInAlAna1Priority = _EventInAlAna1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 52, 1),
    _EventInAlAna1Priority_Type()
)
eventInAlAna1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAna1Priority.setStatus("current")


class _EventInAlAna1Enable_Type(Integer32):
    """Custom type eventInAlAna1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlAna1Enable_Type.__name__ = "Integer32"
_EventInAlAna1Enable_Object = MibScalar
eventInAlAna1Enable = _EventInAlAna1Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 52, 2),
    _EventInAlAna1Enable_Type()
)
eventInAlAna1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAna1Enable.setStatus("current")
_EventInAlAoipParams_ObjectIdentity = ObjectIdentity
eventInAlAoipParams = _EventInAlAoipParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 53)
)
if mibBuilder.loadTexts:
    eventInAlAoipParams.setStatus("current")


class _EventInAlAoipPriority_Type(Gauge32):
    """Custom type eventInAlAoipPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventInAlAoipPriority_Type.__name__ = "Gauge32"
_EventInAlAoipPriority_Object = MibScalar
eventInAlAoipPriority = _EventInAlAoipPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 53, 1),
    _EventInAlAoipPriority_Type()
)
eventInAlAoipPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAoipPriority.setStatus("current")


class _EventInAlAoipEnable_Type(Integer32):
    """Custom type eventInAlAoipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventInAlAoipEnable_Type.__name__ = "Integer32"
_EventInAlAoipEnable_Object = MibScalar
eventInAlAoipEnable = _EventInAlAoipEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 53, 2),
    _EventInAlAoipEnable_Type()
)
eventInAlAoipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventInAlAoipEnable.setStatus("current")
_EventLossOfEth0Params_ObjectIdentity = ObjectIdentity
eventLossOfEth0Params = _EventLossOfEth0Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 54)
)
if mibBuilder.loadTexts:
    eventLossOfEth0Params.setStatus("current")


class _EventLossOfEth0Priority_Type(Gauge32):
    """Custom type eventLossOfEth0Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventLossOfEth0Priority_Type.__name__ = "Gauge32"
_EventLossOfEth0Priority_Object = MibScalar
eventLossOfEth0Priority = _EventLossOfEth0Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 54, 1),
    _EventLossOfEth0Priority_Type()
)
eventLossOfEth0Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLossOfEth0Priority.setStatus("current")


class _EventLossOfEth0Enable_Type(Integer32):
    """Custom type eventLossOfEth0Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventLossOfEth0Enable_Type.__name__ = "Integer32"
_EventLossOfEth0Enable_Object = MibScalar
eventLossOfEth0Enable = _EventLossOfEth0Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 54, 2),
    _EventLossOfEth0Enable_Type()
)
eventLossOfEth0Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLossOfEth0Enable.setStatus("current")
_EventLossOfEth1Params_ObjectIdentity = ObjectIdentity
eventLossOfEth1Params = _EventLossOfEth1Params_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 55)
)
if mibBuilder.loadTexts:
    eventLossOfEth1Params.setStatus("current")


class _EventLossOfEth1Priority_Type(Gauge32):
    """Custom type eventLossOfEth1Priority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventLossOfEth1Priority_Type.__name__ = "Gauge32"
_EventLossOfEth1Priority_Object = MibScalar
eventLossOfEth1Priority = _EventLossOfEth1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 55, 1),
    _EventLossOfEth1Priority_Type()
)
eventLossOfEth1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLossOfEth1Priority.setStatus("current")


class _EventLossOfEth1Enable_Type(Integer32):
    """Custom type eventLossOfEth1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventLossOfEth1Enable_Type.__name__ = "Integer32"
_EventLossOfEth1Enable_Object = MibScalar
eventLossOfEth1Enable = _EventLossOfEth1Enable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 55, 2),
    _EventLossOfEth1Enable_Type()
)
eventLossOfEth1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLossOfEth1Enable.setStatus("current")
_EventSyLiAlAoipdecoderParams_ObjectIdentity = ObjectIdentity
eventSyLiAlAoipdecoderParams = _EventSyLiAlAoipdecoderParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 56)
)
if mibBuilder.loadTexts:
    eventSyLiAlAoipdecoderParams.setStatus("current")


class _EventSyLiAlAoipdecoderPriority_Type(Gauge32):
    """Custom type eventSyLiAlAoipdecoderPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlAoipdecoderPriority_Type.__name__ = "Gauge32"
_EventSyLiAlAoipdecoderPriority_Object = MibScalar
eventSyLiAlAoipdecoderPriority = _EventSyLiAlAoipdecoderPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 56, 1),
    _EventSyLiAlAoipdecoderPriority_Type()
)
eventSyLiAlAoipdecoderPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlAoipdecoderPriority.setStatus("current")


class _EventSyLiAlAoipdecoderEnable_Type(Integer32):
    """Custom type eventSyLiAlAoipdecoderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlAoipdecoderEnable_Type.__name__ = "Integer32"
_EventSyLiAlAoipdecoderEnable_Object = MibScalar
eventSyLiAlAoipdecoderEnable = _EventSyLiAlAoipdecoderEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 56, 2),
    _EventSyLiAlAoipdecoderEnable_Type()
)
eventSyLiAlAoipdecoderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlAoipdecoderEnable.setStatus("current")
_EventSyLiAlMpxoipdecoderParams_ObjectIdentity = ObjectIdentity
eventSyLiAlMpxoipdecoderParams = _EventSyLiAlMpxoipdecoderParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 57)
)
if mibBuilder.loadTexts:
    eventSyLiAlMpxoipdecoderParams.setStatus("current")


class _EventSyLiAlMpxoipdecoderPriority_Type(Gauge32):
    """Custom type eventSyLiAlMpxoipdecoderPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlMpxoipdecoderPriority_Type.__name__ = "Gauge32"
_EventSyLiAlMpxoipdecoderPriority_Object = MibScalar
eventSyLiAlMpxoipdecoderPriority = _EventSyLiAlMpxoipdecoderPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 57, 1),
    _EventSyLiAlMpxoipdecoderPriority_Type()
)
eventSyLiAlMpxoipdecoderPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlMpxoipdecoderPriority.setStatus("current")


class _EventSyLiAlMpxoipdecoderEnable_Type(Integer32):
    """Custom type eventSyLiAlMpxoipdecoderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlMpxoipdecoderEnable_Type.__name__ = "Integer32"
_EventSyLiAlMpxoipdecoderEnable_Object = MibScalar
eventSyLiAlMpxoipdecoderEnable = _EventSyLiAlMpxoipdecoderEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 57, 2),
    _EventSyLiAlMpxoipdecoderEnable_Type()
)
eventSyLiAlMpxoipdecoderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlMpxoipdecoderEnable.setStatus("current")
_EventSyLiAlSurestreamParams_ObjectIdentity = ObjectIdentity
eventSyLiAlSurestreamParams = _EventSyLiAlSurestreamParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 58)
)
if mibBuilder.loadTexts:
    eventSyLiAlSurestreamParams.setStatus("current")


class _EventSyLiAlSurestreamPriority_Type(Gauge32):
    """Custom type eventSyLiAlSurestreamPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlSurestreamPriority_Type.__name__ = "Gauge32"
_EventSyLiAlSurestreamPriority_Object = MibScalar
eventSyLiAlSurestreamPriority = _EventSyLiAlSurestreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 58, 1),
    _EventSyLiAlSurestreamPriority_Type()
)
eventSyLiAlSurestreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSurestreamPriority.setStatus("current")


class _EventSyLiAlSurestreamEnable_Type(Integer32):
    """Custom type eventSyLiAlSurestreamEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlSurestreamEnable_Type.__name__ = "Integer32"
_EventSyLiAlSurestreamEnable_Object = MibScalar
eventSyLiAlSurestreamEnable = _EventSyLiAlSurestreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 58, 2),
    _EventSyLiAlSurestreamEnable_Type()
)
eventSyLiAlSurestreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSurestreamEnable.setStatus("current")
_EventSyLiAlSynchrostreamParams_ObjectIdentity = ObjectIdentity
eventSyLiAlSynchrostreamParams = _EventSyLiAlSynchrostreamParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 59)
)
if mibBuilder.loadTexts:
    eventSyLiAlSynchrostreamParams.setStatus("current")


class _EventSyLiAlSynchrostreamPriority_Type(Gauge32):
    """Custom type eventSyLiAlSynchrostreamPriority based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EventSyLiAlSynchrostreamPriority_Type.__name__ = "Gauge32"
_EventSyLiAlSynchrostreamPriority_Object = MibScalar
eventSyLiAlSynchrostreamPriority = _EventSyLiAlSynchrostreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 59, 1),
    _EventSyLiAlSynchrostreamPriority_Type()
)
eventSyLiAlSynchrostreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSynchrostreamPriority.setStatus("current")


class _EventSyLiAlSynchrostreamEnable_Type(Integer32):
    """Custom type eventSyLiAlSynchrostreamEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EventSyLiAlSynchrostreamEnable_Type.__name__ = "Integer32"
_EventSyLiAlSynchrostreamEnable_Object = MibScalar
eventSyLiAlSynchrostreamEnable = _EventSyLiAlSynchrostreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 3, 59, 2),
    _EventSyLiAlSynchrostreamEnable_Type()
)
eventSyLiAlSynchrostreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSyLiAlSynchrostreamEnable.setStatus("current")
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    inputs.setStatus("current")
_InSource_ObjectIdentity = ObjectIdentity
inSource = _InSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    inSource.setStatus("current")
_InSoLine1_ObjectIdentity = ObjectIdentity
inSoLine1 = _InSoLine1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    inSoLine1.setStatus("current")


class _InSoL1Presence_Type(Integer32):
    """Custom type inSoL1Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("leftRight", 3),
          ("none", 4))
    )


_InSoL1Presence_Type.__name__ = "Integer32"
_InSoL1Presence_Object = MibScalar
inSoL1Presence = _InSoL1Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 1),
    _InSoL1Presence_Type()
)
inSoL1Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1Presence.setStatus("current")


class _InSoL1Type_Type(Integer32):
    """Custom type inSoL1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ana", 1),
          ("aes", 2),
          ("off", 3))
    )


_InSoL1Type_Type.__name__ = "Integer32"
_InSoL1Type_Object = MibScalar
inSoL1Type = _InSoL1Type_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 2),
    _InSoL1Type_Type()
)
inSoL1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1Type.setStatus("current")


class _InSoL1LeftPeakMax_Type(Integer32):
    """Custom type inSoL1LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL1LeftPeakMax_Type.__name__ = "Integer32"
_InSoL1LeftPeakMax_Object = MibScalar
inSoL1LeftPeakMax = _InSoL1LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 3),
    _InSoL1LeftPeakMax_Type()
)
inSoL1LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1LeftPeakMax.setUnits("dB/100")


class _InSoL1RightPeakMax_Type(Integer32):
    """Custom type inSoL1RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL1RightPeakMax_Type.__name__ = "Integer32"
_InSoL1RightPeakMax_Object = MibScalar
inSoL1RightPeakMax = _InSoL1RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 4),
    _InSoL1RightPeakMax_Type()
)
inSoL1RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1RightPeakMax.setUnits("dB/100")


class _InSoL1LeftPeak_Type(Integer32):
    """Custom type inSoL1LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL1LeftPeak_Type.__name__ = "Integer32"
_InSoL1LeftPeak_Object = MibScalar
inSoL1LeftPeak = _InSoL1LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 5),
    _InSoL1LeftPeak_Type()
)
inSoL1LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1LeftPeak.setUnits("dB/100")


class _InSoL1RightPeak_Type(Integer32):
    """Custom type inSoL1RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL1RightPeak_Type.__name__ = "Integer32"
_InSoL1RightPeak_Object = MibScalar
inSoL1RightPeak = _InSoL1RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 6),
    _InSoL1RightPeak_Type()
)
inSoL1RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1RightPeak.setUnits("dB/100")


class _InSoL1Level_Type(Integer32):
    """Custom type inSoL1Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoL1Level_Type.__name__ = "Integer32"
_InSoL1Level_Object = MibScalar
inSoL1Level = _InSoL1Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 7),
    _InSoL1Level_Type()
)
inSoL1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1Level.setUnits("dB/100")


class _InSoL1Drive_Type(Integer32):
    """Custom type inSoL1Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoL1Drive_Type.__name__ = "Integer32"
_InSoL1Drive_Object = MibScalar
inSoL1Drive = _InSoL1Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 8),
    _InSoL1Drive_Type()
)
inSoL1Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1Drive.setUnits("dB/100")


class _InSoL1Trim_Type(Integer32):
    """Custom type inSoL1Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoL1Trim_Type.__name__ = "Integer32"
_InSoL1Trim_Object = MibScalar
inSoL1Trim = _InSoL1Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 9),
    _InSoL1Trim_Type()
)
inSoL1Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoL1Trim.setUnits("dB/100")


class _InSoL1Filter_Type(Integer32):
    """Custom type inSoL1Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoL1Filter_Type.__name__ = "Integer32"
_InSoL1Filter_Object = MibScalar
inSoL1Filter = _InSoL1Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 10),
    _InSoL1Filter_Type()
)
inSoL1Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1Filter.setStatus("current")


class _InSoL1Preacc_Type(Integer32):
    """Custom type inSoL1Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoL1Preacc_Type.__name__ = "Integer32"
_InSoL1Preacc_Object = MibScalar
inSoL1Preacc = _InSoL1Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 11),
    _InSoL1Preacc_Type()
)
inSoL1Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1Preacc.setStatus("current")


class _InSoL1Lost_Type(Integer32):
    """Custom type inSoL1Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoL1Lost_Type.__name__ = "Integer32"
_InSoL1Lost_Object = MibScalar
inSoL1Lost = _InSoL1Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 12),
    _InSoL1Lost_Type()
)
inSoL1Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL1Lost.setStatus("current")


class _InSoL1AlarmTrig_Type(Integer32):
    """Custom type inSoL1AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoL1AlarmTrig_Type.__name__ = "Integer32"
_InSoL1AlarmTrig_Object = MibScalar
inSoL1AlarmTrig = _InSoL1AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 1, 13),
    _InSoL1AlarmTrig_Type()
)
inSoL1AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL1AlarmTrig.setStatus("current")
_InSoLine2_ObjectIdentity = ObjectIdentity
inSoLine2 = _InSoLine2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    inSoLine2.setStatus("current")


class _InSoL2Presence_Type(Integer32):
    """Custom type inSoL2Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("leftRight", 3),
          ("none", 4))
    )


_InSoL2Presence_Type.__name__ = "Integer32"
_InSoL2Presence_Object = MibScalar
inSoL2Presence = _InSoL2Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 1),
    _InSoL2Presence_Type()
)
inSoL2Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2Presence.setStatus("current")


class _InSoL2Type_Type(Integer32):
    """Custom type inSoL2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ana", 1),
          ("aes", 2),
          ("off", 3))
    )


_InSoL2Type_Type.__name__ = "Integer32"
_InSoL2Type_Object = MibScalar
inSoL2Type = _InSoL2Type_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 2),
    _InSoL2Type_Type()
)
inSoL2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2Type.setStatus("current")


class _InSoL2LeftPeakMax_Type(Integer32):
    """Custom type inSoL2LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL2LeftPeakMax_Type.__name__ = "Integer32"
_InSoL2LeftPeakMax_Object = MibScalar
inSoL2LeftPeakMax = _InSoL2LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 3),
    _InSoL2LeftPeakMax_Type()
)
inSoL2LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2LeftPeakMax.setUnits("dB/100")


class _InSoL2RightPeakMax_Type(Integer32):
    """Custom type inSoL2RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL2RightPeakMax_Type.__name__ = "Integer32"
_InSoL2RightPeakMax_Object = MibScalar
inSoL2RightPeakMax = _InSoL2RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 4),
    _InSoL2RightPeakMax_Type()
)
inSoL2RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2RightPeakMax.setUnits("dB/100")


class _InSoL2LeftPeak_Type(Integer32):
    """Custom type inSoL2LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL2LeftPeak_Type.__name__ = "Integer32"
_InSoL2LeftPeak_Object = MibScalar
inSoL2LeftPeak = _InSoL2LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 5),
    _InSoL2LeftPeak_Type()
)
inSoL2LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2LeftPeak.setUnits("dB/100")


class _InSoL2RightPeak_Type(Integer32):
    """Custom type inSoL2RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoL2RightPeak_Type.__name__ = "Integer32"
_InSoL2RightPeak_Object = MibScalar
inSoL2RightPeak = _InSoL2RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 6),
    _InSoL2RightPeak_Type()
)
inSoL2RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2RightPeak.setUnits("dB/100")


class _InSoL2Level_Type(Integer32):
    """Custom type inSoL2Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoL2Level_Type.__name__ = "Integer32"
_InSoL2Level_Object = MibScalar
inSoL2Level = _InSoL2Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 7),
    _InSoL2Level_Type()
)
inSoL2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2Level.setUnits("dB/100")


class _InSoL2Drive_Type(Integer32):
    """Custom type inSoL2Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoL2Drive_Type.__name__ = "Integer32"
_InSoL2Drive_Object = MibScalar
inSoL2Drive = _InSoL2Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 8),
    _InSoL2Drive_Type()
)
inSoL2Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2Drive.setUnits("dB/100")


class _InSoL2Trim_Type(Integer32):
    """Custom type inSoL2Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoL2Trim_Type.__name__ = "Integer32"
_InSoL2Trim_Object = MibScalar
inSoL2Trim = _InSoL2Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 9),
    _InSoL2Trim_Type()
)
inSoL2Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoL2Trim.setUnits("dB/100")


class _InSoL2Filter_Type(Integer32):
    """Custom type inSoL2Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoL2Filter_Type.__name__ = "Integer32"
_InSoL2Filter_Object = MibScalar
inSoL2Filter = _InSoL2Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 10),
    _InSoL2Filter_Type()
)
inSoL2Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2Filter.setStatus("current")


class _InSoL2Preacc_Type(Integer32):
    """Custom type inSoL2Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoL2Preacc_Type.__name__ = "Integer32"
_InSoL2Preacc_Object = MibScalar
inSoL2Preacc = _InSoL2Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 11),
    _InSoL2Preacc_Type()
)
inSoL2Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2Preacc.setStatus("current")


class _InSoL2Lost_Type(Integer32):
    """Custom type inSoL2Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoL2Lost_Type.__name__ = "Integer32"
_InSoL2Lost_Object = MibScalar
inSoL2Lost = _InSoL2Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 12),
    _InSoL2Lost_Type()
)
inSoL2Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoL2Lost.setStatus("current")


class _InSoL2AlarmTrig_Type(Integer32):
    """Custom type inSoL2AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoL2AlarmTrig_Type.__name__ = "Integer32"
_InSoL2AlarmTrig_Object = MibScalar
inSoL2AlarmTrig = _InSoL2AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 2, 13),
    _InSoL2AlarmTrig_Type()
)
inSoL2AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoL2AlarmTrig.setStatus("current")
_InSoMpx1_ObjectIdentity = ObjectIdentity
inSoMpx1 = _InSoMpx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    inSoMpx1.setStatus("current")


class _InSoM1Presence_Type(Integer32):
    """Custom type inSoM1Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mono", 1),
          ("monoRds", 2),
          ("monoRdsSca", 3),
          ("stereo", 4),
          ("stereoRds", 5),
          ("stereoRdsSca", 6),
          ("rdsSca", 7),
          ("rds", 8),
          ("sca", 9),
          ("none", 10))
    )


_InSoM1Presence_Type.__name__ = "Integer32"
_InSoM1Presence_Object = MibScalar
inSoM1Presence = _InSoM1Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 1),
    _InSoM1Presence_Type()
)
inSoM1Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM1Presence.setStatus("current")


class _InSoM1PeakMax_Type(Integer32):
    """Custom type inSoM1PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM1PeakMax_Type.__name__ = "Integer32"
_InSoM1PeakMax_Object = MibScalar
inSoM1PeakMax = _InSoM1PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 2),
    _InSoM1PeakMax_Type()
)
inSoM1PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM1PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoM1PeakMax.setUnits("dB/100")


class _InSoM1Peak_Type(Integer32):
    """Custom type inSoM1Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM1Peak_Type.__name__ = "Integer32"
_InSoM1Peak_Object = MibScalar
inSoM1Peak = _InSoM1Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 3),
    _InSoM1Peak_Type()
)
inSoM1Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM1Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoM1Peak.setUnits("dB/100")


class _InSoM1Level_Type(Integer32):
    """Custom type inSoM1Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_InSoM1Level_Type.__name__ = "Integer32"
_InSoM1Level_Object = MibScalar
inSoM1Level = _InSoM1Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 4),
    _InSoM1Level_Type()
)
inSoM1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM1Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoM1Level.setUnits("dB/100")


class _InSoM1Drive_Type(Integer32):
    """Custom type inSoM1Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoM1Drive_Type.__name__ = "Integer32"
_InSoM1Drive_Object = MibScalar
inSoM1Drive = _InSoM1Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 5),
    _InSoM1Drive_Type()
)
inSoM1Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM1Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoM1Drive.setUnits("dB/100")


class _InSoM1Lost_Type(Integer32):
    """Custom type inSoM1Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoM1Lost_Type.__name__ = "Integer32"
_InSoM1Lost_Object = MibScalar
inSoM1Lost = _InSoM1Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 6),
    _InSoM1Lost_Type()
)
inSoM1Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM1Lost.setStatus("current")


class _InSoM1AlarmTrig_Type(Integer32):
    """Custom type inSoM1AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoM1AlarmTrig_Type.__name__ = "Integer32"
_InSoM1AlarmTrig_Object = MibScalar
inSoM1AlarmTrig = _InSoM1AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 4, 7),
    _InSoM1AlarmTrig_Type()
)
inSoM1AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM1AlarmTrig.setStatus("current")
_InSoMpx2_ObjectIdentity = ObjectIdentity
inSoMpx2 = _InSoMpx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    inSoMpx2.setStatus("current")


class _InSoM2Presence_Type(Integer32):
    """Custom type inSoM2Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mono", 1),
          ("monoRds", 2),
          ("monoRdsSca", 3),
          ("stereo", 4),
          ("stereoRds", 5),
          ("stereoRdsSca", 6),
          ("rdsSca", 7),
          ("rds", 8),
          ("sca", 9),
          ("none", 10))
    )


_InSoM2Presence_Type.__name__ = "Integer32"
_InSoM2Presence_Object = MibScalar
inSoM2Presence = _InSoM2Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 1),
    _InSoM2Presence_Type()
)
inSoM2Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM2Presence.setStatus("current")


class _InSoM2PeakMax_Type(Integer32):
    """Custom type inSoM2PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM2PeakMax_Type.__name__ = "Integer32"
_InSoM2PeakMax_Object = MibScalar
inSoM2PeakMax = _InSoM2PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 2),
    _InSoM2PeakMax_Type()
)
inSoM2PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM2PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoM2PeakMax.setUnits("dB/100")


class _InSoM2Peak_Type(Integer32):
    """Custom type inSoM2Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM2Peak_Type.__name__ = "Integer32"
_InSoM2Peak_Object = MibScalar
inSoM2Peak = _InSoM2Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 3),
    _InSoM2Peak_Type()
)
inSoM2Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM2Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoM2Peak.setUnits("dB/100")


class _InSoM2Level_Type(Integer32):
    """Custom type inSoM2Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_InSoM2Level_Type.__name__ = "Integer32"
_InSoM2Level_Object = MibScalar
inSoM2Level = _InSoM2Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 4),
    _InSoM2Level_Type()
)
inSoM2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM2Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoM2Level.setUnits("dB/100")


class _InSoM2Drive_Type(Integer32):
    """Custom type inSoM2Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoM2Drive_Type.__name__ = "Integer32"
_InSoM2Drive_Object = MibScalar
inSoM2Drive = _InSoM2Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 5),
    _InSoM2Drive_Type()
)
inSoM2Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM2Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoM2Drive.setUnits("dB/100")


class _InSoM2Lost_Type(Integer32):
    """Custom type inSoM2Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoM2Lost_Type.__name__ = "Integer32"
_InSoM2Lost_Object = MibScalar
inSoM2Lost = _InSoM2Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 6),
    _InSoM2Lost_Type()
)
inSoM2Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM2Lost.setStatus("current")


class _InSoM2AlarmTrig_Type(Integer32):
    """Custom type inSoM2AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoM2AlarmTrig_Type.__name__ = "Integer32"
_InSoM2AlarmTrig_Object = MibScalar
inSoM2AlarmTrig = _InSoM2AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 5, 7),
    _InSoM2AlarmTrig_Type()
)
inSoM2AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM2AlarmTrig.setStatus("current")
_InSoPlayer_ObjectIdentity = ObjectIdentity
inSoPlayer = _InSoPlayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    inSoPlayer.setStatus("current")


class _InSoPlPresence_Type(Integer32):
    """Custom type inSoPlPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("leftRight", 3),
          ("none", 4))
    )


_InSoPlPresence_Type.__name__ = "Integer32"
_InSoPlPresence_Object = MibScalar
inSoPlPresence = _InSoPlPresence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 1),
    _InSoPlPresence_Type()
)
inSoPlPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlPresence.setStatus("current")


class _InSoPlLeftPeakMax_Type(Integer32):
    """Custom type inSoPlLeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoPlLeftPeakMax_Type.__name__ = "Integer32"
_InSoPlLeftPeakMax_Object = MibScalar
inSoPlLeftPeakMax = _InSoPlLeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 2),
    _InSoPlLeftPeakMax_Type()
)
inSoPlLeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlLeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlLeftPeakMax.setUnits("dB/100")


class _InSoPlRightPeakMax_Type(Integer32):
    """Custom type inSoPlRightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoPlRightPeakMax_Type.__name__ = "Integer32"
_InSoPlRightPeakMax_Object = MibScalar
inSoPlRightPeakMax = _InSoPlRightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 3),
    _InSoPlRightPeakMax_Type()
)
inSoPlRightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlRightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlRightPeakMax.setUnits("dB/100")


class _InSoPlLeftPeak_Type(Integer32):
    """Custom type inSoPlLeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoPlLeftPeak_Type.__name__ = "Integer32"
_InSoPlLeftPeak_Object = MibScalar
inSoPlLeftPeak = _InSoPlLeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 4),
    _InSoPlLeftPeak_Type()
)
inSoPlLeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlLeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlLeftPeak.setUnits("dB/100")


class _InSoPlRightPeak_Type(Integer32):
    """Custom type inSoPlRightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoPlRightPeak_Type.__name__ = "Integer32"
_InSoPlRightPeak_Object = MibScalar
inSoPlRightPeak = _InSoPlRightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 5),
    _InSoPlRightPeak_Type()
)
inSoPlRightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlRightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlRightPeak.setUnits("dB/100")


class _InSoPlLevel_Type(Integer32):
    """Custom type inSoPlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 0),
    )


_InSoPlLevel_Type.__name__ = "Integer32"
_InSoPlLevel_Object = MibScalar
inSoPlLevel = _InSoPlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 6),
    _InSoPlLevel_Type()
)
inSoPlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlLevel.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlLevel.setUnits("dB/100")


class _InSoPlDrive_Type(Integer32):
    """Custom type inSoPlDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoPlDrive_Type.__name__ = "Integer32"
_InSoPlDrive_Object = MibScalar
inSoPlDrive = _InSoPlDrive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 7),
    _InSoPlDrive_Type()
)
inSoPlDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlDrive.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlDrive.setUnits("dB/100")


class _InSoPlTrim_Type(Integer32):
    """Custom type inSoPlTrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoPlTrim_Type.__name__ = "Integer32"
_InSoPlTrim_Object = MibScalar
inSoPlTrim = _InSoPlTrim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 8),
    _InSoPlTrim_Type()
)
inSoPlTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlTrim.setStatus("current")
if mibBuilder.loadTexts:
    inSoPlTrim.setUnits("dB/100")


class _InSoPlFilter_Type(Integer32):
    """Custom type inSoPlFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoPlFilter_Type.__name__ = "Integer32"
_InSoPlFilter_Object = MibScalar
inSoPlFilter = _InSoPlFilter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 9),
    _InSoPlFilter_Type()
)
inSoPlFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlFilter.setStatus("current")


class _InSoPlPreacc_Type(Integer32):
    """Custom type inSoPlPreacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoPlPreacc_Type.__name__ = "Integer32"
_InSoPlPreacc_Object = MibScalar
inSoPlPreacc = _InSoPlPreacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 10),
    _InSoPlPreacc_Type()
)
inSoPlPreacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlPreacc.setStatus("current")


class _InSoPlSampling_Type(Integer32):
    """Custom type inSoPlSampling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v44kHz", 1),
          ("v48kHz", 2),
          ("v96kHz", 3))
    )


_InSoPlSampling_Type.__name__ = "Integer32"
_InSoPlSampling_Object = MibScalar
inSoPlSampling = _InSoPlSampling_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 11),
    _InSoPlSampling_Type()
)
inSoPlSampling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlSampling.setStatus("current")


class _InSoPlLost_Type(Integer32):
    """Custom type inSoPlLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoPlLost_Type.__name__ = "Integer32"
_InSoPlLost_Object = MibScalar
inSoPlLost = _InSoPlLost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 12),
    _InSoPlLost_Type()
)
inSoPlLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoPlLost.setStatus("current")


class _InSoPlAlarmTrig_Type(Integer32):
    """Custom type inSoPlAlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoPlAlarmTrig_Type.__name__ = "Integer32"
_InSoPlAlarmTrig_Object = MibScalar
inSoPlAlarmTrig = _InSoPlAlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 6, 13),
    _InSoPlAlarmTrig_Type()
)
inSoPlAlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoPlAlarmTrig.setStatus("current")
_InSoGenerator_ObjectIdentity = ObjectIdentity
inSoGenerator = _InSoGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    inSoGenerator.setStatus("current")


class _InSoGeState_Type(Integer32):
    """Custom type inSoGeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("off", 1),
          ("pilot", 2),
          ("left", 3),
          ("right", 4),
          ("leftRight", 5),
          ("leftMinusRight", 6))
    )


_InSoGeState_Type.__name__ = "Integer32"
_InSoGeState_Object = MibScalar
inSoGeState = _InSoGeState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 1),
    _InSoGeState_Type()
)
inSoGeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGeState.setStatus("current")


class _InSoGeLevel1_Type(Integer32):
    """Custom type inSoGeLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 1200),
    )


_InSoGeLevel1_Type.__name__ = "Integer32"
_InSoGeLevel1_Object = MibScalar
inSoGeLevel1 = _InSoGeLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 2),
    _InSoGeLevel1_Type()
)
inSoGeLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGeLevel1.setStatus("current")
if mibBuilder.loadTexts:
    inSoGeLevel1.setUnits("dB/100")


class _InSoGeLevel2_Type(Integer32):
    """Custom type inSoGeLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 1200),
    )


_InSoGeLevel2_Type.__name__ = "Integer32"
_InSoGeLevel2_Object = MibScalar
inSoGeLevel2 = _InSoGeLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 3),
    _InSoGeLevel2_Type()
)
inSoGeLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGeLevel2.setStatus("current")
if mibBuilder.loadTexts:
    inSoGeLevel2.setUnits("dB/100")


class _InSoGeFreq1_Type(Integer32):
    """Custom type inSoGeFreq1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_InSoGeFreq1_Type.__name__ = "Integer32"
_InSoGeFreq1_Object = MibScalar
inSoGeFreq1 = _InSoGeFreq1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 4),
    _InSoGeFreq1_Type()
)
inSoGeFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGeFreq1.setStatus("current")
if mibBuilder.loadTexts:
    inSoGeFreq1.setUnits("Hz/100")


class _InSoGeFreq2_Type(Integer32):
    """Custom type inSoGeFreq2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_InSoGeFreq2_Type.__name__ = "Integer32"
_InSoGeFreq2_Object = MibScalar
inSoGeFreq2 = _InSoGeFreq2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 5),
    _InSoGeFreq2_Type()
)
inSoGeFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGeFreq2.setStatus("current")
if mibBuilder.loadTexts:
    inSoGeFreq2.setUnits("Hz/100")


class _InSoGePreacc_Type(Integer32):
    """Custom type inSoGePreacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoGePreacc_Type.__name__ = "Integer32"
_InSoGePreacc_Object = MibScalar
inSoGePreacc = _InSoGePreacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 7, 6),
    _InSoGePreacc_Type()
)
inSoGePreacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoGePreacc.setStatus("current")
_InSoMpx3_ObjectIdentity = ObjectIdentity
inSoMpx3 = _InSoMpx3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    inSoMpx3.setStatus("current")


class _InSoM3Presence_Type(Integer32):
    """Custom type inSoM3Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mono", 1),
          ("monoRds", 2),
          ("monoRdsSca", 3),
          ("stereo", 4),
          ("stereoRds", 5),
          ("stereoRdsSca", 6),
          ("rdsSca", 7),
          ("rds", 8),
          ("sca", 9),
          ("none", 10))
    )


_InSoM3Presence_Type.__name__ = "Integer32"
_InSoM3Presence_Object = MibScalar
inSoM3Presence = _InSoM3Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 1),
    _InSoM3Presence_Type()
)
inSoM3Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM3Presence.setStatus("current")


class _InSoM3PeakMax_Type(Integer32):
    """Custom type inSoM3PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM3PeakMax_Type.__name__ = "Integer32"
_InSoM3PeakMax_Object = MibScalar
inSoM3PeakMax = _InSoM3PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 2),
    _InSoM3PeakMax_Type()
)
inSoM3PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM3PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoM3PeakMax.setUnits("dB/100")


class _InSoM3Peak_Type(Integer32):
    """Custom type inSoM3Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM3Peak_Type.__name__ = "Integer32"
_InSoM3Peak_Object = MibScalar
inSoM3Peak = _InSoM3Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 3),
    _InSoM3Peak_Type()
)
inSoM3Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM3Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoM3Peak.setUnits("dB/100")


class _InSoM3Level_Type(Integer32):
    """Custom type inSoM3Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_InSoM3Level_Type.__name__ = "Integer32"
_InSoM3Level_Object = MibScalar
inSoM3Level = _InSoM3Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 4),
    _InSoM3Level_Type()
)
inSoM3Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM3Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoM3Level.setUnits("dB/100")


class _InSoM3Drive_Type(Integer32):
    """Custom type inSoM3Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoM3Drive_Type.__name__ = "Integer32"
_InSoM3Drive_Object = MibScalar
inSoM3Drive = _InSoM3Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 5),
    _InSoM3Drive_Type()
)
inSoM3Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM3Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoM3Drive.setUnits("dB/100")


class _InSoM3Lost_Type(Integer32):
    """Custom type inSoM3Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoM3Lost_Type.__name__ = "Integer32"
_InSoM3Lost_Object = MibScalar
inSoM3Lost = _InSoM3Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 6),
    _InSoM3Lost_Type()
)
inSoM3Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM3Lost.setStatus("current")


class _InSoM3AlarmTrig_Type(Integer32):
    """Custom type inSoM3AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoM3AlarmTrig_Type.__name__ = "Integer32"
_InSoM3AlarmTrig_Object = MibScalar
inSoM3AlarmTrig = _InSoM3AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 8, 7),
    _InSoM3AlarmTrig_Type()
)
inSoM3AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM3AlarmTrig.setStatus("current")
_InSoMpx4_ObjectIdentity = ObjectIdentity
inSoMpx4 = _InSoMpx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9)
)
if mibBuilder.loadTexts:
    inSoMpx4.setStatus("current")


class _InSoM4Presence_Type(Integer32):
    """Custom type inSoM4Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mono", 1),
          ("monoRds", 2),
          ("monoRdsSca", 3),
          ("stereo", 4),
          ("stereoRds", 5),
          ("stereoRdsSca", 6),
          ("rdsSca", 7),
          ("rds", 8),
          ("sca", 9),
          ("none", 10))
    )


_InSoM4Presence_Type.__name__ = "Integer32"
_InSoM4Presence_Object = MibScalar
inSoM4Presence = _InSoM4Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 1),
    _InSoM4Presence_Type()
)
inSoM4Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM4Presence.setStatus("current")


class _InSoM4PeakMax_Type(Integer32):
    """Custom type inSoM4PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM4PeakMax_Type.__name__ = "Integer32"
_InSoM4PeakMax_Object = MibScalar
inSoM4PeakMax = _InSoM4PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 2),
    _InSoM4PeakMax_Type()
)
inSoM4PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM4PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoM4PeakMax.setUnits("dB/100")


class _InSoM4Peak_Type(Integer32):
    """Custom type inSoM4Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoM4Peak_Type.__name__ = "Integer32"
_InSoM4Peak_Object = MibScalar
inSoM4Peak = _InSoM4Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 3),
    _InSoM4Peak_Type()
)
inSoM4Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM4Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoM4Peak.setUnits("dB/100")


class _InSoM4Level_Type(Integer32):
    """Custom type inSoM4Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_InSoM4Level_Type.__name__ = "Integer32"
_InSoM4Level_Object = MibScalar
inSoM4Level = _InSoM4Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 4),
    _InSoM4Level_Type()
)
inSoM4Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM4Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoM4Level.setUnits("dB/100")


class _InSoM4Drive_Type(Integer32):
    """Custom type inSoM4Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoM4Drive_Type.__name__ = "Integer32"
_InSoM4Drive_Object = MibScalar
inSoM4Drive = _InSoM4Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 5),
    _InSoM4Drive_Type()
)
inSoM4Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM4Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoM4Drive.setUnits("dB/100")


class _InSoM4Lost_Type(Integer32):
    """Custom type inSoM4Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoM4Lost_Type.__name__ = "Integer32"
_InSoM4Lost_Object = MibScalar
inSoM4Lost = _InSoM4Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 6),
    _InSoM4Lost_Type()
)
inSoM4Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoM4Lost.setStatus("current")


class _InSoM4AlarmTrig_Type(Integer32):
    """Custom type inSoM4AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoM4AlarmTrig_Type.__name__ = "Integer32"
_InSoM4AlarmTrig_Object = MibScalar
inSoM4AlarmTrig = _InSoM4AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 9, 7),
    _InSoM4AlarmTrig_Type()
)
inSoM4AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoM4AlarmTrig.setStatus("current")
_InSoAes1_ObjectIdentity = ObjectIdentity
inSoAes1 = _InSoAes1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10)
)
if mibBuilder.loadTexts:
    inSoAes1.setStatus("current")


class _InSoAes1Presence_Type(Integer32):
    """Custom type inSoAes1Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftRight", 4),
          ("mono", 5),
          ("monoRds", 6),
          ("monoRdsSca", 7),
          ("stereo", 8),
          ("stereoRds", 9),
          ("stereoRdsSca", 10),
          ("rds", 11),
          ("rdsSca", 12))
    )


_InSoAes1Presence_Type.__name__ = "Integer32"
_InSoAes1Presence_Object = MibScalar
inSoAes1Presence = _InSoAes1Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 1),
    _InSoAes1Presence_Type()
)
inSoAes1Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1Presence.setStatus("current")


class _InSoAes1LeftPeakMax_Type(Integer32):
    """Custom type inSoAes1LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1LeftPeakMax_Type.__name__ = "Integer32"
_InSoAes1LeftPeakMax_Object = MibScalar
inSoAes1LeftPeakMax = _InSoAes1LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 2),
    _InSoAes1LeftPeakMax_Type()
)
inSoAes1LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1LeftPeakMax.setUnits("dB/100")


class _InSoAes1RightPeakMax_Type(Integer32):
    """Custom type inSoAes1RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1RightPeakMax_Type.__name__ = "Integer32"
_InSoAes1RightPeakMax_Object = MibScalar
inSoAes1RightPeakMax = _InSoAes1RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 3),
    _InSoAes1RightPeakMax_Type()
)
inSoAes1RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1RightPeakMax.setUnits("dB/100")


class _InSoAes1LeftPeak_Type(Integer32):
    """Custom type inSoAes1LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1LeftPeak_Type.__name__ = "Integer32"
_InSoAes1LeftPeak_Object = MibScalar
inSoAes1LeftPeak = _InSoAes1LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 4),
    _InSoAes1LeftPeak_Type()
)
inSoAes1LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1LeftPeak.setUnits("dB/100")


class _InSoAes1RightPeak_Type(Integer32):
    """Custom type inSoAes1RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1RightPeak_Type.__name__ = "Integer32"
_InSoAes1RightPeak_Object = MibScalar
inSoAes1RightPeak = _InSoAes1RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 5),
    _InSoAes1RightPeak_Type()
)
inSoAes1RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1RightPeak.setUnits("dB/100")


class _InSoAes1PeakMax_Type(Integer32):
    """Custom type inSoAes1PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1PeakMax_Type.__name__ = "Integer32"
_InSoAes1PeakMax_Object = MibScalar
inSoAes1PeakMax = _InSoAes1PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 6),
    _InSoAes1PeakMax_Type()
)
inSoAes1PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1PeakMax.setUnits("dB/100")


class _InSoAes1Peak_Type(Integer32):
    """Custom type inSoAes1Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes1Peak_Type.__name__ = "Integer32"
_InSoAes1Peak_Object = MibScalar
inSoAes1Peak = _InSoAes1Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 7),
    _InSoAes1Peak_Type()
)
inSoAes1Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1Peak.setUnits("dB/100")


class _InSoAes1Level_Type(Integer32):
    """Custom type inSoAes1Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoAes1Level_Type.__name__ = "Integer32"
_InSoAes1Level_Object = MibScalar
inSoAes1Level = _InSoAes1Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 8),
    _InSoAes1Level_Type()
)
inSoAes1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1Level.setUnits("dB/100")


class _InSoAes1Drive_Type(Integer32):
    """Custom type inSoAes1Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoAes1Drive_Type.__name__ = "Integer32"
_InSoAes1Drive_Object = MibScalar
inSoAes1Drive = _InSoAes1Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 9),
    _InSoAes1Drive_Type()
)
inSoAes1Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1Drive.setUnits("dB/100")


class _InSoAes1Trim_Type(Integer32):
    """Custom type inSoAes1Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoAes1Trim_Type.__name__ = "Integer32"
_InSoAes1Trim_Object = MibScalar
inSoAes1Trim = _InSoAes1Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 10),
    _InSoAes1Trim_Type()
)
inSoAes1Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes1Trim.setUnits("dB/100")


class _InSoAes1Filter_Type(Integer32):
    """Custom type inSoAes1Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoAes1Filter_Type.__name__ = "Integer32"
_InSoAes1Filter_Object = MibScalar
inSoAes1Filter = _InSoAes1Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 11),
    _InSoAes1Filter_Type()
)
inSoAes1Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1Filter.setStatus("current")


class _InSoAes1Preacc_Type(Integer32):
    """Custom type inSoAes1Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoAes1Preacc_Type.__name__ = "Integer32"
_InSoAes1Preacc_Object = MibScalar
inSoAes1Preacc = _InSoAes1Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 12),
    _InSoAes1Preacc_Type()
)
inSoAes1Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1Preacc.setStatus("current")


class _InSoAes1Lost_Type(Integer32):
    """Custom type inSoAes1Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoAes1Lost_Type.__name__ = "Integer32"
_InSoAes1Lost_Object = MibScalar
inSoAes1Lost = _InSoAes1Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 13),
    _InSoAes1Lost_Type()
)
inSoAes1Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes1Lost.setStatus("current")


class _InSoAes1AlarmTrig_Type(Integer32):
    """Custom type inSoAes1AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoAes1AlarmTrig_Type.__name__ = "Integer32"
_InSoAes1AlarmTrig_Object = MibScalar
inSoAes1AlarmTrig = _InSoAes1AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 10, 14),
    _InSoAes1AlarmTrig_Type()
)
inSoAes1AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes1AlarmTrig.setStatus("current")
_InSoAes2_ObjectIdentity = ObjectIdentity
inSoAes2 = _InSoAes2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    inSoAes2.setStatus("current")


class _InSoAes2Presence_Type(Integer32):
    """Custom type inSoAes2Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftRight", 4),
          ("mono", 5),
          ("monoRds", 6),
          ("monoRdsSca", 7),
          ("stereo", 8),
          ("stereoRds", 9),
          ("stereoRdsSca", 10),
          ("rds", 11),
          ("rdsSca", 12))
    )


_InSoAes2Presence_Type.__name__ = "Integer32"
_InSoAes2Presence_Object = MibScalar
inSoAes2Presence = _InSoAes2Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 1),
    _InSoAes2Presence_Type()
)
inSoAes2Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2Presence.setStatus("current")


class _InSoAes2LeftPeakMax_Type(Integer32):
    """Custom type inSoAes2LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2LeftPeakMax_Type.__name__ = "Integer32"
_InSoAes2LeftPeakMax_Object = MibScalar
inSoAes2LeftPeakMax = _InSoAes2LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 2),
    _InSoAes2LeftPeakMax_Type()
)
inSoAes2LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2LeftPeakMax.setUnits("dB/100")


class _InSoAes2RightPeakMax_Type(Integer32):
    """Custom type inSoAes2RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2RightPeakMax_Type.__name__ = "Integer32"
_InSoAes2RightPeakMax_Object = MibScalar
inSoAes2RightPeakMax = _InSoAes2RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 3),
    _InSoAes2RightPeakMax_Type()
)
inSoAes2RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2RightPeakMax.setUnits("dB/100")


class _InSoAes2LeftPeak_Type(Integer32):
    """Custom type inSoAes2LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2LeftPeak_Type.__name__ = "Integer32"
_InSoAes2LeftPeak_Object = MibScalar
inSoAes2LeftPeak = _InSoAes2LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 4),
    _InSoAes2LeftPeak_Type()
)
inSoAes2LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2LeftPeak.setUnits("dB/100")


class _InSoAes2RightPeak_Type(Integer32):
    """Custom type inSoAes2RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2RightPeak_Type.__name__ = "Integer32"
_InSoAes2RightPeak_Object = MibScalar
inSoAes2RightPeak = _InSoAes2RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 5),
    _InSoAes2RightPeak_Type()
)
inSoAes2RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2RightPeak.setUnits("dB/100")


class _InSoAes2PeakMax_Type(Integer32):
    """Custom type inSoAes2PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2PeakMax_Type.__name__ = "Integer32"
_InSoAes2PeakMax_Object = MibScalar
inSoAes2PeakMax = _InSoAes2PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 6),
    _InSoAes2PeakMax_Type()
)
inSoAes2PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2PeakMax.setUnits("dB/100")


class _InSoAes2Peak_Type(Integer32):
    """Custom type inSoAes2Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes2Peak_Type.__name__ = "Integer32"
_InSoAes2Peak_Object = MibScalar
inSoAes2Peak = _InSoAes2Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 7),
    _InSoAes2Peak_Type()
)
inSoAes2Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2Peak.setUnits("dB/100")


class _InSoAes2Level_Type(Integer32):
    """Custom type inSoAes2Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoAes2Level_Type.__name__ = "Integer32"
_InSoAes2Level_Object = MibScalar
inSoAes2Level = _InSoAes2Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 8),
    _InSoAes2Level_Type()
)
inSoAes2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2Level.setUnits("dB/100")


class _InSoAes2Drive_Type(Integer32):
    """Custom type inSoAes2Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoAes2Drive_Type.__name__ = "Integer32"
_InSoAes2Drive_Object = MibScalar
inSoAes2Drive = _InSoAes2Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 9),
    _InSoAes2Drive_Type()
)
inSoAes2Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2Drive.setUnits("dB/100")


class _InSoAes2Trim_Type(Integer32):
    """Custom type inSoAes2Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoAes2Trim_Type.__name__ = "Integer32"
_InSoAes2Trim_Object = MibScalar
inSoAes2Trim = _InSoAes2Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 10),
    _InSoAes2Trim_Type()
)
inSoAes2Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes2Trim.setUnits("dB/100")


class _InSoAes2Filter_Type(Integer32):
    """Custom type inSoAes2Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoAes2Filter_Type.__name__ = "Integer32"
_InSoAes2Filter_Object = MibScalar
inSoAes2Filter = _InSoAes2Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 11),
    _InSoAes2Filter_Type()
)
inSoAes2Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2Filter.setStatus("current")


class _InSoAes2Preacc_Type(Integer32):
    """Custom type inSoAes2Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoAes2Preacc_Type.__name__ = "Integer32"
_InSoAes2Preacc_Object = MibScalar
inSoAes2Preacc = _InSoAes2Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 12),
    _InSoAes2Preacc_Type()
)
inSoAes2Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2Preacc.setStatus("current")


class _InSoAes2Lost_Type(Integer32):
    """Custom type inSoAes2Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoAes2Lost_Type.__name__ = "Integer32"
_InSoAes2Lost_Object = MibScalar
inSoAes2Lost = _InSoAes2Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 13),
    _InSoAes2Lost_Type()
)
inSoAes2Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes2Lost.setStatus("current")


class _InSoAes2AlarmTrig_Type(Integer32):
    """Custom type inSoAes2AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoAes2AlarmTrig_Type.__name__ = "Integer32"
_InSoAes2AlarmTrig_Object = MibScalar
inSoAes2AlarmTrig = _InSoAes2AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 11, 14),
    _InSoAes2AlarmTrig_Type()
)
inSoAes2AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes2AlarmTrig.setStatus("current")
_InSoAes3_ObjectIdentity = ObjectIdentity
inSoAes3 = _InSoAes3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12)
)
if mibBuilder.loadTexts:
    inSoAes3.setStatus("current")


class _InSoAes3Presence_Type(Integer32):
    """Custom type inSoAes3Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftRight", 4),
          ("mono", 5),
          ("monoRds", 6),
          ("monoRdsSca", 7),
          ("stereo", 8),
          ("stereoRds", 9),
          ("stereoRdsSca", 10),
          ("rds", 11),
          ("rdsSca", 12))
    )


_InSoAes3Presence_Type.__name__ = "Integer32"
_InSoAes3Presence_Object = MibScalar
inSoAes3Presence = _InSoAes3Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 1),
    _InSoAes3Presence_Type()
)
inSoAes3Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3Presence.setStatus("current")


class _InSoAes3LeftPeakMax_Type(Integer32):
    """Custom type inSoAes3LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3LeftPeakMax_Type.__name__ = "Integer32"
_InSoAes3LeftPeakMax_Object = MibScalar
inSoAes3LeftPeakMax = _InSoAes3LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 2),
    _InSoAes3LeftPeakMax_Type()
)
inSoAes3LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3LeftPeakMax.setUnits("dB/100")


class _InSoAes3RightPeakMax_Type(Integer32):
    """Custom type inSoAes3RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3RightPeakMax_Type.__name__ = "Integer32"
_InSoAes3RightPeakMax_Object = MibScalar
inSoAes3RightPeakMax = _InSoAes3RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 3),
    _InSoAes3RightPeakMax_Type()
)
inSoAes3RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3RightPeakMax.setUnits("dB/100")


class _InSoAes3LeftPeak_Type(Integer32):
    """Custom type inSoAes3LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3LeftPeak_Type.__name__ = "Integer32"
_InSoAes3LeftPeak_Object = MibScalar
inSoAes3LeftPeak = _InSoAes3LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 4),
    _InSoAes3LeftPeak_Type()
)
inSoAes3LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3LeftPeak.setUnits("dB/100")


class _InSoAes3RightPeak_Type(Integer32):
    """Custom type inSoAes3RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3RightPeak_Type.__name__ = "Integer32"
_InSoAes3RightPeak_Object = MibScalar
inSoAes3RightPeak = _InSoAes3RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 5),
    _InSoAes3RightPeak_Type()
)
inSoAes3RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3RightPeak.setUnits("dB/100")


class _InSoAes3PeakMax_Type(Integer32):
    """Custom type inSoAes3PeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3PeakMax_Type.__name__ = "Integer32"
_InSoAes3PeakMax_Object = MibScalar
inSoAes3PeakMax = _InSoAes3PeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 6),
    _InSoAes3PeakMax_Type()
)
inSoAes3PeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3PeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3PeakMax.setUnits("dB/100")


class _InSoAes3Peak_Type(Integer32):
    """Custom type inSoAes3Peak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAes3Peak_Type.__name__ = "Integer32"
_InSoAes3Peak_Object = MibScalar
inSoAes3Peak = _InSoAes3Peak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 7),
    _InSoAes3Peak_Type()
)
inSoAes3Peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3Peak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3Peak.setUnits("dB/100")


class _InSoAes3Level_Type(Integer32):
    """Custom type inSoAes3Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoAes3Level_Type.__name__ = "Integer32"
_InSoAes3Level_Object = MibScalar
inSoAes3Level = _InSoAes3Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 8),
    _InSoAes3Level_Type()
)
inSoAes3Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3Level.setUnits("dB/100")


class _InSoAes3Drive_Type(Integer32):
    """Custom type inSoAes3Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoAes3Drive_Type.__name__ = "Integer32"
_InSoAes3Drive_Object = MibScalar
inSoAes3Drive = _InSoAes3Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 9),
    _InSoAes3Drive_Type()
)
inSoAes3Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3Drive.setUnits("dB/100")


class _InSoAes3Trim_Type(Integer32):
    """Custom type inSoAes3Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoAes3Trim_Type.__name__ = "Integer32"
_InSoAes3Trim_Object = MibScalar
inSoAes3Trim = _InSoAes3Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 10),
    _InSoAes3Trim_Type()
)
inSoAes3Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoAes3Trim.setUnits("dB/100")


class _InSoAes3Filter_Type(Integer32):
    """Custom type inSoAes3Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoAes3Filter_Type.__name__ = "Integer32"
_InSoAes3Filter_Object = MibScalar
inSoAes3Filter = _InSoAes3Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 11),
    _InSoAes3Filter_Type()
)
inSoAes3Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3Filter.setStatus("current")


class _InSoAes3Preacc_Type(Integer32):
    """Custom type inSoAes3Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoAes3Preacc_Type.__name__ = "Integer32"
_InSoAes3Preacc_Object = MibScalar
inSoAes3Preacc = _InSoAes3Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 12),
    _InSoAes3Preacc_Type()
)
inSoAes3Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3Preacc.setStatus("current")


class _InSoAes3Lost_Type(Integer32):
    """Custom type inSoAes3Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoAes3Lost_Type.__name__ = "Integer32"
_InSoAes3Lost_Object = MibScalar
inSoAes3Lost = _InSoAes3Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 13),
    _InSoAes3Lost_Type()
)
inSoAes3Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAes3Lost.setStatus("current")


class _InSoAes3AlarmTrig_Type(Integer32):
    """Custom type inSoAes3AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoAes3AlarmTrig_Type.__name__ = "Integer32"
_InSoAes3AlarmTrig_Object = MibScalar
inSoAes3AlarmTrig = _InSoAes3AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 12, 14),
    _InSoAes3AlarmTrig_Type()
)
inSoAes3AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAes3AlarmTrig.setStatus("current")
_InSoAna1_ObjectIdentity = ObjectIdentity
inSoAna1 = _InSoAna1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    inSoAna1.setStatus("current")


class _InSoAna1Presence_Type(Integer32):
    """Custom type inSoAna1Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftRight", 4),
          ("mono", 5),
          ("monoRds", 6),
          ("monoRdsSca", 7),
          ("stereo", 8),
          ("stereoRds", 9),
          ("stereoRdsSca", 10),
          ("rds", 11),
          ("rdsSca", 12))
    )


_InSoAna1Presence_Type.__name__ = "Integer32"
_InSoAna1Presence_Object = MibScalar
inSoAna1Presence = _InSoAna1Presence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 1),
    _InSoAna1Presence_Type()
)
inSoAna1Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1Presence.setStatus("current")


class _InSoAna1LeftPeakMax_Type(Integer32):
    """Custom type inSoAna1LeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAna1LeftPeakMax_Type.__name__ = "Integer32"
_InSoAna1LeftPeakMax_Object = MibScalar
inSoAna1LeftPeakMax = _InSoAna1LeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 2),
    _InSoAna1LeftPeakMax_Type()
)
inSoAna1LeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1LeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1LeftPeakMax.setUnits("dB/100")


class _InSoAna1RightPeakMax_Type(Integer32):
    """Custom type inSoAna1RightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAna1RightPeakMax_Type.__name__ = "Integer32"
_InSoAna1RightPeakMax_Object = MibScalar
inSoAna1RightPeakMax = _InSoAna1RightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 3),
    _InSoAna1RightPeakMax_Type()
)
inSoAna1RightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1RightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1RightPeakMax.setUnits("dB/100")


class _InSoAna1LeftPeak_Type(Integer32):
    """Custom type inSoAna1LeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAna1LeftPeak_Type.__name__ = "Integer32"
_InSoAna1LeftPeak_Object = MibScalar
inSoAna1LeftPeak = _InSoAna1LeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 4),
    _InSoAna1LeftPeak_Type()
)
inSoAna1LeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1LeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1LeftPeak.setUnits("dB/100")


class _InSoAna1RightPeak_Type(Integer32):
    """Custom type inSoAna1RightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAna1RightPeak_Type.__name__ = "Integer32"
_InSoAna1RightPeak_Object = MibScalar
inSoAna1RightPeak = _InSoAna1RightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 5),
    _InSoAna1RightPeak_Type()
)
inSoAna1RightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1RightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1RightPeak.setUnits("dB/100")


class _InSoAna1Level_Type(Integer32):
    """Custom type inSoAna1Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoAna1Level_Type.__name__ = "Integer32"
_InSoAna1Level_Object = MibScalar
inSoAna1Level = _InSoAna1Level_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 6),
    _InSoAna1Level_Type()
)
inSoAna1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1Level.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1Level.setUnits("dB/100")


class _InSoAna1Drive_Type(Integer32):
    """Custom type inSoAna1Drive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoAna1Drive_Type.__name__ = "Integer32"
_InSoAna1Drive_Object = MibScalar
inSoAna1Drive = _InSoAna1Drive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 7),
    _InSoAna1Drive_Type()
)
inSoAna1Drive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1Drive.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1Drive.setUnits("dB/100")


class _InSoAna1Trim_Type(Integer32):
    """Custom type inSoAna1Trim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoAna1Trim_Type.__name__ = "Integer32"
_InSoAna1Trim_Object = MibScalar
inSoAna1Trim = _InSoAna1Trim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 8),
    _InSoAna1Trim_Type()
)
inSoAna1Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1Trim.setStatus("current")
if mibBuilder.loadTexts:
    inSoAna1Trim.setUnits("dB/100")


class _InSoAna1Filter_Type(Integer32):
    """Custom type inSoAna1Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoAna1Filter_Type.__name__ = "Integer32"
_InSoAna1Filter_Object = MibScalar
inSoAna1Filter = _InSoAna1Filter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 9),
    _InSoAna1Filter_Type()
)
inSoAna1Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1Filter.setStatus("current")


class _InSoAna1Preacc_Type(Integer32):
    """Custom type inSoAna1Preacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoAna1Preacc_Type.__name__ = "Integer32"
_InSoAna1Preacc_Object = MibScalar
inSoAna1Preacc = _InSoAna1Preacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 10),
    _InSoAna1Preacc_Type()
)
inSoAna1Preacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1Preacc.setStatus("current")


class _InSoAna1Lost_Type(Integer32):
    """Custom type inSoAna1Lost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoAna1Lost_Type.__name__ = "Integer32"
_InSoAna1Lost_Object = MibScalar
inSoAna1Lost = _InSoAna1Lost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 11),
    _InSoAna1Lost_Type()
)
inSoAna1Lost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAna1Lost.setStatus("current")


class _InSoAna1AlarmTrig_Type(Integer32):
    """Custom type inSoAna1AlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoAna1AlarmTrig_Type.__name__ = "Integer32"
_InSoAna1AlarmTrig_Object = MibScalar
inSoAna1AlarmTrig = _InSoAna1AlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 13, 12),
    _InSoAna1AlarmTrig_Type()
)
inSoAna1AlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAna1AlarmTrig.setStatus("current")
_InSoType_ObjectIdentity = ObjectIdentity
inSoType = _InSoType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 14)
)
if mibBuilder.loadTexts:
    inSoType.setStatus("current")


class _InSoTySlot1_Type(Integer32):
    """Custom type inSoTySlot1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("aes1", 2),
          ("aes2", 3),
          ("aes1And2", 4))
    )


_InSoTySlot1_Type.__name__ = "Integer32"
_InSoTySlot1_Object = MibScalar
inSoTySlot1 = _InSoTySlot1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 14, 1),
    _InSoTySlot1_Type()
)
inSoTySlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoTySlot1.setStatus("current")


class _InSoTySlot2_Type(Integer32):
    """Custom type inSoTySlot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("aes", 2),
          ("ana", 3))
    )


_InSoTySlot2_Type.__name__ = "Integer32"
_InSoTySlot2_Object = MibScalar
inSoTySlot2 = _InSoTySlot2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 14, 2),
    _InSoTySlot2_Type()
)
inSoTySlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoTySlot2.setStatus("current")


class _InSoTySlot3_Type(Integer32):
    """Custom type inSoTySlot3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("mpx", 2))
    )


_InSoTySlot3_Type.__name__ = "Integer32"
_InSoTySlot3_Object = MibScalar
inSoTySlot3 = _InSoTySlot3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 14, 3),
    _InSoTySlot3_Type()
)
inSoTySlot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoTySlot3.setStatus("current")
_InSoAoip_ObjectIdentity = ObjectIdentity
inSoAoip = _InSoAoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15)
)
if mibBuilder.loadTexts:
    inSoAoip.setStatus("current")


class _InSoAoipPresence_Type(Integer32):
    """Custom type inSoAoipPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftRight", 4),
          ("mono", 5),
          ("monoRds", 6),
          ("monoRdsSca", 7),
          ("stereo", 8),
          ("stereoRds", 9),
          ("stereoRdsSca", 10),
          ("rds", 11),
          ("rdsSca", 12))
    )


_InSoAoipPresence_Type.__name__ = "Integer32"
_InSoAoipPresence_Object = MibScalar
inSoAoipPresence = _InSoAoipPresence_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 1),
    _InSoAoipPresence_Type()
)
inSoAoipPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipPresence.setStatus("current")


class _InSoAoipLeftPeakMax_Type(Integer32):
    """Custom type inSoAoipLeftPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipLeftPeakMax_Type.__name__ = "Integer32"
_InSoAoipLeftPeakMax_Object = MibScalar
inSoAoipLeftPeakMax = _InSoAoipLeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 2),
    _InSoAoipLeftPeakMax_Type()
)
inSoAoipLeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipLeftPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipLeftPeakMax.setUnits("dB/100")


class _InSoAoipRightPeakMax_Type(Integer32):
    """Custom type inSoAoipRightPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipRightPeakMax_Type.__name__ = "Integer32"
_InSoAoipRightPeakMax_Object = MibScalar
inSoAoipRightPeakMax = _InSoAoipRightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 3),
    _InSoAoipRightPeakMax_Type()
)
inSoAoipRightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipRightPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipRightPeakMax.setUnits("dB/100")


class _InSoAoipLeftPeak_Type(Integer32):
    """Custom type inSoAoipLeftPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipLeftPeak_Type.__name__ = "Integer32"
_InSoAoipLeftPeak_Object = MibScalar
inSoAoipLeftPeak = _InSoAoipLeftPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 4),
    _InSoAoipLeftPeak_Type()
)
inSoAoipLeftPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipLeftPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipLeftPeak.setUnits("dB/100")


class _InSoAoipRightPeak_Type(Integer32):
    """Custom type inSoAoipRightPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipRightPeak_Type.__name__ = "Integer32"
_InSoAoipRightPeak_Object = MibScalar
inSoAoipRightPeak = _InSoAoipRightPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 5),
    _InSoAoipRightPeak_Type()
)
inSoAoipRightPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipRightPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipRightPeak.setUnits("dB/100")


class _InSoAoipPeakMax_Type(Integer32):
    """Custom type inSoAoipPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipPeakMax_Type.__name__ = "Integer32"
_InSoAoipPeakMax_Object = MibScalar
inSoAoipPeakMax = _InSoAoipPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 6),
    _InSoAoipPeakMax_Type()
)
inSoAoipPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipPeakMax.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipPeakMax.setUnits("dB/100")


class _InSoAoipPeak_Type(Integer32):
    """Custom type inSoAoipPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_InSoAoipPeak_Type.__name__ = "Integer32"
_InSoAoipPeak_Object = MibScalar
inSoAoipPeak = _InSoAoipPeak_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 7),
    _InSoAoipPeak_Type()
)
inSoAoipPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipPeak.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipPeak.setUnits("dB/100")


class _InSoAoipLevel_Type(Integer32):
    """Custom type inSoAoipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 1800),
    )


_InSoAoipLevel_Type.__name__ = "Integer32"
_InSoAoipLevel_Object = MibScalar
inSoAoipLevel = _InSoAoipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 8),
    _InSoAoipLevel_Type()
)
inSoAoipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipLevel.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipLevel.setUnits("dB/100")


class _InSoAoipDrive_Type(Integer32):
    """Custom type inSoAoipDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_InSoAoipDrive_Type.__name__ = "Integer32"
_InSoAoipDrive_Object = MibScalar
inSoAoipDrive = _InSoAoipDrive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 9),
    _InSoAoipDrive_Type()
)
inSoAoipDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipDrive.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipDrive.setUnits("dB/100")


class _InSoAoipTrim_Type(Integer32):
    """Custom type inSoAoipTrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_InSoAoipTrim_Type.__name__ = "Integer32"
_InSoAoipTrim_Object = MibScalar
inSoAoipTrim = _InSoAoipTrim_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 10),
    _InSoAoipTrim_Type()
)
inSoAoipTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipTrim.setStatus("current")
if mibBuilder.loadTexts:
    inSoAoipTrim.setUnits("dB/100")


class _InSoAoipFilter_Type(Integer32):
    """Custom type inSoAoipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v0", 1),
          ("v15", 2),
          ("v16", 3),
          ("v17", 4))
    )


_InSoAoipFilter_Type.__name__ = "Integer32"
_InSoAoipFilter_Object = MibScalar
inSoAoipFilter = _InSoAoipFilter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 11),
    _InSoAoipFilter_Type()
)
inSoAoipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipFilter.setStatus("current")


class _InSoAoipPreacc_Type(Integer32):
    """Custom type inSoAoipPreacc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("v50us", 1),
          ("v75us", 2),
          ("off", 3))
    )


_InSoAoipPreacc_Type.__name__ = "Integer32"
_InSoAoipPreacc_Object = MibScalar
inSoAoipPreacc = _InSoAoipPreacc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 12),
    _InSoAoipPreacc_Type()
)
inSoAoipPreacc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipPreacc.setStatus("current")


class _InSoAoipLost_Type(Integer32):
    """Custom type inSoAoipLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_InSoAoipLost_Type.__name__ = "Integer32"
_InSoAoipLost_Object = MibScalar
inSoAoipLost = _InSoAoipLost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 13),
    _InSoAoipLost_Type()
)
inSoAoipLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSoAoipLost.setStatus("current")


class _InSoAoipAlarmTrig_Type(Integer32):
    """Custom type inSoAoipAlarmTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("fault", 2),
          ("warning", 3))
    )


_InSoAoipAlarmTrig_Type.__name__ = "Integer32"
_InSoAoipAlarmTrig_Object = MibScalar
inSoAoipAlarmTrig = _InSoAoipAlarmTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 1, 15, 14),
    _InSoAoipAlarmTrig_Type()
)
inSoAoipAlarmTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSoAoipAlarmTrig.setStatus("current")
_InSelect_ObjectIdentity = ObjectIdentity
inSelect = _InSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    inSelect.setStatus("current")
_InSeAudio_ObjectIdentity = ObjectIdentity
inSeAudio = _InSeAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    inSeAudio.setStatus("current")


class _InSeLine1Prio_Type(Gauge32):
    """Custom type inSeLine1Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeLine1Prio_Type.__name__ = "Gauge32"
_InSeLine1Prio_Object = MibScalar
inSeLine1Prio = _InSeLine1Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 1),
    _InSeLine1Prio_Type()
)
inSeLine1Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeLine1Prio.setStatus("current")


class _InSeLine2Prio_Type(Gauge32):
    """Custom type inSeLine2Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeLine2Prio_Type.__name__ = "Gauge32"
_InSeLine2Prio_Object = MibScalar
inSeLine2Prio = _InSeLine2Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 2),
    _InSeLine2Prio_Type()
)
inSeLine2Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeLine2Prio.setStatus("current")


class _InSeMpx1Prio_Type(Gauge32):
    """Custom type inSeMpx1Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeMpx1Prio_Type.__name__ = "Gauge32"
_InSeMpx1Prio_Object = MibScalar
inSeMpx1Prio = _InSeMpx1Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 3),
    _InSeMpx1Prio_Type()
)
inSeMpx1Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeMpx1Prio.setStatus("current")


class _InSeMpx2Prio_Type(Gauge32):
    """Custom type inSeMpx2Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeMpx2Prio_Type.__name__ = "Gauge32"
_InSeMpx2Prio_Object = MibScalar
inSeMpx2Prio = _InSeMpx2Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 4),
    _InSeMpx2Prio_Type()
)
inSeMpx2Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeMpx2Prio.setStatus("current")


class _InSePlayerPrio_Type(Gauge32):
    """Custom type inSePlayerPrio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_InSePlayerPrio_Type.__name__ = "Gauge32"
_InSePlayerPrio_Object = MibScalar
inSePlayerPrio = _InSePlayerPrio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 5),
    _InSePlayerPrio_Type()
)
inSePlayerPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSePlayerPrio.setStatus("current")


class _InSeCrossfade_Type(Gauge32):
    """Custom type inSeCrossfade based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InSeCrossfade_Type.__name__ = "Gauge32"
_InSeCrossfade_Object = MibScalar
inSeCrossfade = _InSeCrossfade_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 6),
    _InSeCrossfade_Type()
)
inSeCrossfade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeCrossfade.setStatus("current")
if mibBuilder.loadTexts:
    inSeCrossfade.setUnits("s/10")


class _InSeSelectAudio_Type(Integer32):
    """Custom type inSeSelectAudio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("auto", 1),
          ("line1", 2),
          ("line2", 3),
          ("aoip", 4),
          ("tuner", 5),
          ("mpx1", 6),
          ("mpx2", 7),
          ("aoip1", 8),
          ("aoip2", 9),
          ("tuner1", 10),
          ("tuner2", 11),
          ("player", 12),
          ("generator", 13),
          ("mpx3", 14),
          ("mpx4", 15),
          ("aes1", 17),
          ("aes2", 18),
          ("aes3", 19),
          ("ana1", 20))
    )


_InSeSelectAudio_Type.__name__ = "Integer32"
_InSeSelectAudio_Object = MibScalar
inSeSelectAudio = _InSeSelectAudio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 7),
    _InSeSelectAudio_Type()
)
inSeSelectAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSelectAudio.setStatus("current")


class _InSeCurrentAudio_Type(Integer32):
    """Custom type inSeCurrentAudio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("line1", 2),
          ("line2", 3),
          ("aoip", 4),
          ("tuner", 5),
          ("mpx1", 6),
          ("mpx2", 7),
          ("aoip1", 8),
          ("aoip2", 9),
          ("tuner1", 10),
          ("tuner2", 11),
          ("player", 12),
          ("generator", 13),
          ("mpx3", 14),
          ("mpx4", 15),
          ("aes1", 16),
          ("aes2", 17),
          ("aes3", 18),
          ("ana1", 19))
    )


_InSeCurrentAudio_Type.__name__ = "Integer32"
_InSeCurrentAudio_Object = MibScalar
inSeCurrentAudio = _InSeCurrentAudio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 8),
    _InSeCurrentAudio_Type()
)
inSeCurrentAudio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeCurrentAudio.setStatus("current")


class _InSeAlrInputSwitch_Type(Integer32):
    """Custom type inSeAlrInputSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeAlrInputSwitch_Type.__name__ = "Integer32"
_InSeAlrInputSwitch_Object = MibScalar
inSeAlrInputSwitch = _InSeAlrInputSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 9),
    _InSeAlrInputSwitch_Type()
)
inSeAlrInputSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeAlrInputSwitch.setStatus("current")


class _InSeFadein_Type(Gauge32):
    """Custom type inSeFadein based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InSeFadein_Type.__name__ = "Gauge32"
_InSeFadein_Object = MibScalar
inSeFadein = _InSeFadein_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 10),
    _InSeFadein_Type()
)
inSeFadein.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeFadein.setStatus("current")
if mibBuilder.loadTexts:
    inSeFadein.setUnits("s/10")


class _InSeMpx3Prio_Type(Gauge32):
    """Custom type inSeMpx3Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeMpx3Prio_Type.__name__ = "Gauge32"
_InSeMpx3Prio_Object = MibScalar
inSeMpx3Prio = _InSeMpx3Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 11),
    _InSeMpx3Prio_Type()
)
inSeMpx3Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeMpx3Prio.setStatus("current")


class _InSeMpx4Prio_Type(Gauge32):
    """Custom type inSeMpx4Prio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InSeMpx4Prio_Type.__name__ = "Gauge32"
_InSeMpx4Prio_Object = MibScalar
inSeMpx4Prio = _InSeMpx4Prio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 12),
    _InSeMpx4Prio_Type()
)
inSeMpx4Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeMpx4Prio.setStatus("current")
_InSeBackupsTable_Object = MibTable
inSeBackupsTable = _InSeBackupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 13)
)
if mibBuilder.loadTexts:
    inSeBackupsTable.setStatus("current")
_InSeBackupsEntry_Object = MibTableRow
inSeBackupsEntry = _InSeBackupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 13, 1)
)
inSeBackupsEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "inSeBackupsIndex"),
)
if mibBuilder.loadTexts:
    inSeBackupsEntry.setStatus("current")


class _InSeBackupsIndex_Type(Integer32):
    """Custom type inSeBackupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InSeBackupsIndex_Type.__name__ = "Integer32"
_InSeBackupsIndex_Object = MibTableColumn
inSeBackupsIndex = _InSeBackupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 13, 1, 1),
    _InSeBackupsIndex_Type()
)
inSeBackupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inSeBackupsIndex.setStatus("current")


class _InSeBackupsSource_Type(Integer32):
    """Custom type inSeBackupsSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("aes1", 2),
          ("aes2", 3),
          ("aes3", 4),
          ("ana1", 5),
          ("mpx1", 6),
          ("mpx2", 7),
          ("aoip", 8),
          ("player", 9),
          ("generator", 10),
          ("tuner", 11))
    )


_InSeBackupsSource_Type.__name__ = "Integer32"
_InSeBackupsSource_Object = MibTableColumn
inSeBackupsSource = _InSeBackupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 13, 1, 2),
    _InSeBackupsSource_Type()
)
inSeBackupsSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeBackupsSource.setStatus("current")


class _InSeAuBackupMode_Type(Integer32):
    """Custom type inSeAuBackupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("manu", 1),
          ("auto", 2))
    )


_InSeAuBackupMode_Type.__name__ = "Integer32"
_InSeAuBackupMode_Object = MibScalar
inSeAuBackupMode = _InSeAuBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 1, 14),
    _InSeAuBackupMode_Type()
)
inSeAuBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeAuBackupMode.setStatus("current")
_InSeThresholds_ObjectIdentity = ObjectIdentity
inSeThresholds = _InSeThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    inSeThresholds.setStatus("current")


class _InSeThLine1Th_Type(Integer32):
    """Custom type inSeThLine1Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-116, 24),
    )


_InSeThLine1Th_Type.__name__ = "Integer32"
_InSeThLine1Th_Object = MibScalar
inSeThLine1Th = _InSeThLine1Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 1),
    _InSeThLine1Th_Type()
)
inSeThLine1Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThLine1Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThLine1Th.setUnits("dB")


class _InSeThLine1Sil_Type(Integer32):
    """Custom type inSeThLine1Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThLine1Sil_Type.__name__ = "Integer32"
_InSeThLine1Sil_Object = MibScalar
inSeThLine1Sil = _InSeThLine1Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 2),
    _InSeThLine1Sil_Type()
)
inSeThLine1Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThLine1Sil.setStatus("current")


class _InSeThLine2Th_Type(Integer32):
    """Custom type inSeThLine2Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-116, 0),
    )


_InSeThLine2Th_Type.__name__ = "Integer32"
_InSeThLine2Th_Object = MibScalar
inSeThLine2Th = _InSeThLine2Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 3),
    _InSeThLine2Th_Type()
)
inSeThLine2Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThLine2Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThLine2Th.setUnits("dB")


class _InSeThLine2Sil_Type(Integer32):
    """Custom type inSeThLine2Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThLine2Sil_Type.__name__ = "Integer32"
_InSeThLine2Sil_Object = MibScalar
inSeThLine2Sil = _InSeThLine2Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 4),
    _InSeThLine2Sil_Type()
)
inSeThLine2Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThLine2Sil.setStatus("current")


class _InSeThPlayerTh_Type(Integer32):
    """Custom type inSeThPlayerTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-116, 0),
    )


_InSeThPlayerTh_Type.__name__ = "Integer32"
_InSeThPlayerTh_Object = MibScalar
inSeThPlayerTh = _InSeThPlayerTh_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 5),
    _InSeThPlayerTh_Type()
)
inSeThPlayerTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThPlayerTh.setStatus("current")
if mibBuilder.loadTexts:
    inSeThPlayerTh.setUnits("dB")


class _InSeThPlayerSil_Type(Integer32):
    """Custom type inSeThPlayerSil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThPlayerSil_Type.__name__ = "Integer32"
_InSeThPlayerSil_Object = MibScalar
inSeThPlayerSil = _InSeThPlayerSil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 6),
    _InSeThPlayerSil_Type()
)
inSeThPlayerSil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThPlayerSil.setStatus("current")


class _InSeThMpxTh_Type(Integer32):
    """Custom type inSeThMpxTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-114, 24),
    )


_InSeThMpxTh_Type.__name__ = "Integer32"
_InSeThMpxTh_Object = MibScalar
inSeThMpxTh = _InSeThMpxTh_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 7),
    _InSeThMpxTh_Type()
)
inSeThMpxTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThMpxTh.setStatus("obsolete")
if mibBuilder.loadTexts:
    inSeThMpxTh.setUnits("dB")


class _InSeThMpx1Th_Type(Integer32):
    """Custom type inSeThMpx1Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-114, 24),
    )


_InSeThMpx1Th_Type.__name__ = "Integer32"
_InSeThMpx1Th_Object = MibScalar
inSeThMpx1Th = _InSeThMpx1Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 8),
    _InSeThMpx1Th_Type()
)
inSeThMpx1Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThMpx1Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThMpx1Th.setUnits("dB")


class _InSeThMpx2Th_Type(Integer32):
    """Custom type inSeThMpx2Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-114, 24),
    )


_InSeThMpx2Th_Type.__name__ = "Integer32"
_InSeThMpx2Th_Object = MibScalar
inSeThMpx2Th = _InSeThMpx2Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 9),
    _InSeThMpx2Th_Type()
)
inSeThMpx2Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThMpx2Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThMpx2Th.setUnits("dB")


class _InSeThMpx3Th_Type(Integer32):
    """Custom type inSeThMpx3Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThMpx3Th_Type.__name__ = "Integer32"
_InSeThMpx3Th_Object = MibScalar
inSeThMpx3Th = _InSeThMpx3Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 10),
    _InSeThMpx3Th_Type()
)
inSeThMpx3Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThMpx3Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThMpx3Th.setUnits("dB")


class _InSeThMpx4Th_Type(Integer32):
    """Custom type inSeThMpx4Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThMpx4Th_Type.__name__ = "Integer32"
_InSeThMpx4Th_Object = MibScalar
inSeThMpx4Th = _InSeThMpx4Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 11),
    _InSeThMpx4Th_Type()
)
inSeThMpx4Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThMpx4Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThMpx4Th.setUnits("dB")


class _InSeThAes1Th_Type(Integer32):
    """Custom type inSeThAes1Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThAes1Th_Type.__name__ = "Integer32"
_InSeThAes1Th_Object = MibScalar
inSeThAes1Th = _InSeThAes1Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 12),
    _InSeThAes1Th_Type()
)
inSeThAes1Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes1Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThAes1Th.setUnits("dB")


class _InSeThAes1Sil_Type(Integer32):
    """Custom type inSeThAes1Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThAes1Sil_Type.__name__ = "Integer32"
_InSeThAes1Sil_Object = MibScalar
inSeThAes1Sil = _InSeThAes1Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 13),
    _InSeThAes1Sil_Type()
)
inSeThAes1Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes1Sil.setStatus("current")


class _InSeThAes2Th_Type(Integer32):
    """Custom type inSeThAes2Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThAes2Th_Type.__name__ = "Integer32"
_InSeThAes2Th_Object = MibScalar
inSeThAes2Th = _InSeThAes2Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 14),
    _InSeThAes2Th_Type()
)
inSeThAes2Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes2Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThAes2Th.setUnits("dB")


class _InSeThAes2Sil_Type(Integer32):
    """Custom type inSeThAes2Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThAes2Sil_Type.__name__ = "Integer32"
_InSeThAes2Sil_Object = MibScalar
inSeThAes2Sil = _InSeThAes2Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 15),
    _InSeThAes2Sil_Type()
)
inSeThAes2Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes2Sil.setStatus("current")


class _InSeThAes3Th_Type(Integer32):
    """Custom type inSeThAes3Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThAes3Th_Type.__name__ = "Integer32"
_InSeThAes3Th_Object = MibScalar
inSeThAes3Th = _InSeThAes3Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 16),
    _InSeThAes3Th_Type()
)
inSeThAes3Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes3Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThAes3Th.setUnits("dB")


class _InSeThAes3Sil_Type(Integer32):
    """Custom type inSeThAes3Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThAes3Sil_Type.__name__ = "Integer32"
_InSeThAes3Sil_Object = MibScalar
inSeThAes3Sil = _InSeThAes3Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 17),
    _InSeThAes3Sil_Type()
)
inSeThAes3Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAes3Sil.setStatus("current")


class _InSeThAna1Th_Type(Integer32):
    """Custom type inSeThAna1Th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThAna1Th_Type.__name__ = "Integer32"
_InSeThAna1Th_Object = MibScalar
inSeThAna1Th = _InSeThAna1Th_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 18),
    _InSeThAna1Th_Type()
)
inSeThAna1Th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAna1Th.setStatus("current")
if mibBuilder.loadTexts:
    inSeThAna1Th.setUnits("dB")


class _InSeThAna1Sil_Type(Integer32):
    """Custom type inSeThAna1Sil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThAna1Sil_Type.__name__ = "Integer32"
_InSeThAna1Sil_Object = MibScalar
inSeThAna1Sil = _InSeThAna1Sil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 19),
    _InSeThAna1Sil_Type()
)
inSeThAna1Sil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAna1Sil.setStatus("current")


class _InSeThAoipTh_Type(Integer32):
    """Custom type inSeThAoipTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_InSeThAoipTh_Type.__name__ = "Integer32"
_InSeThAoipTh_Object = MibScalar
inSeThAoipTh = _InSeThAoipTh_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 20),
    _InSeThAoipTh_Type()
)
inSeThAoipTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAoipTh.setStatus("current")
if mibBuilder.loadTexts:
    inSeThAoipTh.setUnits("dB")


class _InSeThAoipSil_Type(Integer32):
    """Custom type inSeThAoipSil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("left", 1),
          ("right", 2),
          ("any", 3),
          ("both", 4))
    )


_InSeThAoipSil_Type.__name__ = "Integer32"
_InSeThAoipSil_Object = MibScalar
inSeThAoipSil = _InSeThAoipSil_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 2, 21),
    _InSeThAoipSil_Type()
)
inSeThAoipSil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeThAoipSil.setStatus("current")
_InSeDelays_ObjectIdentity = ObjectIdentity
inSeDelays = _InSeDelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    inSeDelays.setStatus("current")


class _InSeDeLine1BackDelay_Type(Gauge32):
    """Custom type inSeDeLine1BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeLine1BackDelay_Type.__name__ = "Gauge32"
_InSeDeLine1BackDelay_Object = MibScalar
inSeDeLine1BackDelay = _InSeDeLine1BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 1),
    _InSeDeLine1BackDelay_Type()
)
inSeDeLine1BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeLine1BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeLine1BackDelay.setUnits("s")


class _InSeDeLine1Delay_Type(Gauge32):
    """Custom type inSeDeLine1Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeLine1Delay_Type.__name__ = "Gauge32"
_InSeDeLine1Delay_Object = MibScalar
inSeDeLine1Delay = _InSeDeLine1Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 2),
    _InSeDeLine1Delay_Type()
)
inSeDeLine1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeLine1Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeLine1Delay.setUnits("s")


class _InSeDeLine2BackDelay_Type(Gauge32):
    """Custom type inSeDeLine2BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeLine2BackDelay_Type.__name__ = "Gauge32"
_InSeDeLine2BackDelay_Object = MibScalar
inSeDeLine2BackDelay = _InSeDeLine2BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 3),
    _InSeDeLine2BackDelay_Type()
)
inSeDeLine2BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeLine2BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeLine2BackDelay.setUnits("s")


class _InSeDeLine2Delay_Type(Gauge32):
    """Custom type inSeDeLine2Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeLine2Delay_Type.__name__ = "Gauge32"
_InSeDeLine2Delay_Object = MibScalar
inSeDeLine2Delay = _InSeDeLine2Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 4),
    _InSeDeLine2Delay_Type()
)
inSeDeLine2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeLine2Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeLine2Delay.setUnits("s")


class _InSeDePlayerBackDelay_Type(Gauge32):
    """Custom type inSeDePlayerBackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDePlayerBackDelay_Type.__name__ = "Gauge32"
_InSeDePlayerBackDelay_Object = MibScalar
inSeDePlayerBackDelay = _InSeDePlayerBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 5),
    _InSeDePlayerBackDelay_Type()
)
inSeDePlayerBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDePlayerBackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDePlayerBackDelay.setUnits("s")


class _InSeDePlayerDelay_Type(Gauge32):
    """Custom type inSeDePlayerDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDePlayerDelay_Type.__name__ = "Gauge32"
_InSeDePlayerDelay_Object = MibScalar
inSeDePlayerDelay = _InSeDePlayerDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 6),
    _InSeDePlayerDelay_Type()
)
inSeDePlayerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDePlayerDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDePlayerDelay.setUnits("s")


class _InSeDeMpxBackDelay_Type(Gauge32):
    """Custom type inSeDeMpxBackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeMpxBackDelay_Type.__name__ = "Gauge32"
_InSeDeMpxBackDelay_Object = MibScalar
inSeDeMpxBackDelay = _InSeDeMpxBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 7),
    _InSeDeMpxBackDelay_Type()
)
inSeDeMpxBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpxBackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpxBackDelay.setUnits("s")


class _InSeDeMpxDelay_Type(Gauge32):
    """Custom type inSeDeMpxDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeMpxDelay_Type.__name__ = "Gauge32"
_InSeDeMpxDelay_Object = MibScalar
inSeDeMpxDelay = _InSeDeMpxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 8),
    _InSeDeMpxDelay_Type()
)
inSeDeMpxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpxDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpxDelay.setUnits("s")


class _InSeDeMpx34BackDelay_Type(Gauge32):
    """Custom type inSeDeMpx34BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeMpx34BackDelay_Type.__name__ = "Gauge32"
_InSeDeMpx34BackDelay_Object = MibScalar
inSeDeMpx34BackDelay = _InSeDeMpx34BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 9),
    _InSeDeMpx34BackDelay_Type()
)
inSeDeMpx34BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx34BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx34BackDelay.setUnits("s")


class _InSeDeMpx34Delay_Type(Gauge32):
    """Custom type inSeDeMpx34Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeMpx34Delay_Type.__name__ = "Gauge32"
_InSeDeMpx34Delay_Object = MibScalar
inSeDeMpx34Delay = _InSeDeMpx34Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 10),
    _InSeDeMpx34Delay_Type()
)
inSeDeMpx34Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx34Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx34Delay.setUnits("s")


class _InSeDeAes1BackDelay_Type(Gauge32):
    """Custom type inSeDeAes1BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeAes1BackDelay_Type.__name__ = "Gauge32"
_InSeDeAes1BackDelay_Object = MibScalar
inSeDeAes1BackDelay = _InSeDeAes1BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 11),
    _InSeDeAes1BackDelay_Type()
)
inSeDeAes1BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes1BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes1BackDelay.setUnits("s")


class _InSeDeAes1Delay_Type(Gauge32):
    """Custom type inSeDeAes1Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeAes1Delay_Type.__name__ = "Gauge32"
_InSeDeAes1Delay_Object = MibScalar
inSeDeAes1Delay = _InSeDeAes1Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 12),
    _InSeDeAes1Delay_Type()
)
inSeDeAes1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes1Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes1Delay.setUnits("s")


class _InSeDeAes2BackDelay_Type(Gauge32):
    """Custom type inSeDeAes2BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeAes2BackDelay_Type.__name__ = "Gauge32"
_InSeDeAes2BackDelay_Object = MibScalar
inSeDeAes2BackDelay = _InSeDeAes2BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 13),
    _InSeDeAes2BackDelay_Type()
)
inSeDeAes2BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes2BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes2BackDelay.setUnits("s")


class _InSeDeAes2Delay_Type(Gauge32):
    """Custom type inSeDeAes2Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeAes2Delay_Type.__name__ = "Gauge32"
_InSeDeAes2Delay_Object = MibScalar
inSeDeAes2Delay = _InSeDeAes2Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 14),
    _InSeDeAes2Delay_Type()
)
inSeDeAes2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes2Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes2Delay.setUnits("s")


class _InSeDeAes3BackDelay_Type(Gauge32):
    """Custom type inSeDeAes3BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeAes3BackDelay_Type.__name__ = "Gauge32"
_InSeDeAes3BackDelay_Object = MibScalar
inSeDeAes3BackDelay = _InSeDeAes3BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 15),
    _InSeDeAes3BackDelay_Type()
)
inSeDeAes3BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes3BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes3BackDelay.setUnits("s")


class _InSeDeAes3Delay_Type(Gauge32):
    """Custom type inSeDeAes3Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeAes3Delay_Type.__name__ = "Gauge32"
_InSeDeAes3Delay_Object = MibScalar
inSeDeAes3Delay = _InSeDeAes3Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 16),
    _InSeDeAes3Delay_Type()
)
inSeDeAes3Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAes3Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAes3Delay.setUnits("s")


class _InSeDeAna1BackDelay_Type(Gauge32):
    """Custom type inSeDeAna1BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeAna1BackDelay_Type.__name__ = "Gauge32"
_InSeDeAna1BackDelay_Object = MibScalar
inSeDeAna1BackDelay = _InSeDeAna1BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 17),
    _InSeDeAna1BackDelay_Type()
)
inSeDeAna1BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAna1BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAna1BackDelay.setUnits("s")


class _InSeDeAna1Delay_Type(Gauge32):
    """Custom type inSeDeAna1Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeAna1Delay_Type.__name__ = "Gauge32"
_InSeDeAna1Delay_Object = MibScalar
inSeDeAna1Delay = _InSeDeAna1Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 18),
    _InSeDeAna1Delay_Type()
)
inSeDeAna1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAna1Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAna1Delay.setUnits("s")


class _InSeDeMpx1BackDelay_Type(Gauge32):
    """Custom type inSeDeMpx1BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeMpx1BackDelay_Type.__name__ = "Gauge32"
_InSeDeMpx1BackDelay_Object = MibScalar
inSeDeMpx1BackDelay = _InSeDeMpx1BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 19),
    _InSeDeMpx1BackDelay_Type()
)
inSeDeMpx1BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx1BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx1BackDelay.setUnits("s")


class _InSeDeMpx1Delay_Type(Gauge32):
    """Custom type inSeDeMpx1Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeMpx1Delay_Type.__name__ = "Gauge32"
_InSeDeMpx1Delay_Object = MibScalar
inSeDeMpx1Delay = _InSeDeMpx1Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 20),
    _InSeDeMpx1Delay_Type()
)
inSeDeMpx1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx1Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx1Delay.setUnits("s")


class _InSeDeMpx2BackDelay_Type(Gauge32):
    """Custom type inSeDeMpx2BackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeMpx2BackDelay_Type.__name__ = "Gauge32"
_InSeDeMpx2BackDelay_Object = MibScalar
inSeDeMpx2BackDelay = _InSeDeMpx2BackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 21),
    _InSeDeMpx2BackDelay_Type()
)
inSeDeMpx2BackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx2BackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx2BackDelay.setUnits("s")


class _InSeDeMpx2Delay_Type(Gauge32):
    """Custom type inSeDeMpx2Delay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeMpx2Delay_Type.__name__ = "Gauge32"
_InSeDeMpx2Delay_Object = MibScalar
inSeDeMpx2Delay = _InSeDeMpx2Delay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 22),
    _InSeDeMpx2Delay_Type()
)
inSeDeMpx2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeMpx2Delay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeMpx2Delay.setUnits("s")


class _InSeDeAoipBackDelay_Type(Gauge32):
    """Custom type inSeDeAoipBackDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_InSeDeAoipBackDelay_Type.__name__ = "Gauge32"
_InSeDeAoipBackDelay_Object = MibScalar
inSeDeAoipBackDelay = _InSeDeAoipBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 23),
    _InSeDeAoipBackDelay_Type()
)
inSeDeAoipBackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAoipBackDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAoipBackDelay.setUnits("s")


class _InSeDeAoipDelay_Type(Gauge32):
    """Custom type inSeDeAoipDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InSeDeAoipDelay_Type.__name__ = "Gauge32"
_InSeDeAoipDelay_Object = MibScalar
inSeDeAoipDelay = _InSeDeAoipDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 3, 24),
    _InSeDeAoipDelay_Type()
)
inSeDeAoipDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeDeAoipDelay.setStatus("current")
if mibBuilder.loadTexts:
    inSeDeAoipDelay.setUnits("s")
_InSeSync_ObjectIdentity = ObjectIdentity
inSeSync = _InSeSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    inSeSync.setStatus("current")


class _InSeSyLine1_Type(Integer32):
    """Custom type inSeSyLine1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyLine1_Type.__name__ = "Integer32"
_InSeSyLine1_Object = MibScalar
inSeSyLine1 = _InSeSyLine1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 1),
    _InSeSyLine1_Type()
)
inSeSyLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyLine1.setStatus("current")


class _InSeSyLine2_Type(Integer32):
    """Custom type inSeSyLine2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyLine2_Type.__name__ = "Integer32"
_InSeSyLine2_Object = MibScalar
inSeSyLine2 = _InSeSyLine2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 2),
    _InSeSyLine2_Type()
)
inSeSyLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyLine2.setStatus("current")


class _InSeSyPlayer_Type(Integer32):
    """Custom type inSeSyPlayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyPlayer_Type.__name__ = "Integer32"
_InSeSyPlayer_Object = MibScalar
inSeSyPlayer = _InSeSyPlayer_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 3),
    _InSeSyPlayer_Type()
)
inSeSyPlayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyPlayer.setStatus("current")


class _InSeSyMpx34_Type(Integer32):
    """Custom type inSeSyMpx34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyMpx34_Type.__name__ = "Integer32"
_InSeSyMpx34_Object = MibScalar
inSeSyMpx34 = _InSeSyMpx34_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 4),
    _InSeSyMpx34_Type()
)
inSeSyMpx34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyMpx34.setStatus("current")


class _InSeSyAes1_Type(Integer32):
    """Custom type inSeSyAes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyAes1_Type.__name__ = "Integer32"
_InSeSyAes1_Object = MibScalar
inSeSyAes1 = _InSeSyAes1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 5),
    _InSeSyAes1_Type()
)
inSeSyAes1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyAes1.setStatus("current")


class _InSeSyAes2_Type(Integer32):
    """Custom type inSeSyAes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyAes2_Type.__name__ = "Integer32"
_InSeSyAes2_Object = MibScalar
inSeSyAes2 = _InSeSyAes2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 6),
    _InSeSyAes2_Type()
)
inSeSyAes2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyAes2.setStatus("current")


class _InSeSyAes3_Type(Integer32):
    """Custom type inSeSyAes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyAes3_Type.__name__ = "Integer32"
_InSeSyAes3_Object = MibScalar
inSeSyAes3 = _InSeSyAes3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 7),
    _InSeSyAes3_Type()
)
inSeSyAes3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyAes3.setStatus("current")


class _InSeSyAoip_Type(Integer32):
    """Custom type inSeSyAoip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InSeSyAoip_Type.__name__ = "Integer32"
_InSeSyAoip_Object = MibScalar
inSeSyAoip = _InSeSyAoip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 4, 8),
    _InSeSyAoip_Type()
)
inSeSyAoip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeSyAoip.setStatus("current")
_InSeSampling_ObjectIdentity = ObjectIdentity
inSeSampling = _InSeSampling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    inSeSampling.setStatus("current")


class _InSeSaLine1_Type(Gauge32):
    """Custom type inSeSaLine1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaLine1_Type.__name__ = "Gauge32"
_InSeSaLine1_Object = MibScalar
inSeSaLine1 = _InSeSaLine1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 1),
    _InSeSaLine1_Type()
)
inSeSaLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaLine1.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaLine1.setUnits("Hz")


class _InSeSaLine2_Type(Gauge32):
    """Custom type inSeSaLine2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaLine2_Type.__name__ = "Gauge32"
_InSeSaLine2_Object = MibScalar
inSeSaLine2 = _InSeSaLine2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 2),
    _InSeSaLine2_Type()
)
inSeSaLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaLine2.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaLine2.setUnits("Hz")


class _InSeSaPlayer_Type(Gauge32):
    """Custom type inSeSaPlayer based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaPlayer_Type.__name__ = "Gauge32"
_InSeSaPlayer_Object = MibScalar
inSeSaPlayer = _InSeSaPlayer_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 3),
    _InSeSaPlayer_Type()
)
inSeSaPlayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaPlayer.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaPlayer.setUnits("Hz")


class _InSeSaMpx1_Type(Gauge32):
    """Custom type inSeSaMpx1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaMpx1_Type.__name__ = "Gauge32"
_InSeSaMpx1_Object = MibScalar
inSeSaMpx1 = _InSeSaMpx1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 4),
    _InSeSaMpx1_Type()
)
inSeSaMpx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaMpx1.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaMpx1.setUnits("Hz")


class _InSeSaMpx2_Type(Gauge32):
    """Custom type inSeSaMpx2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaMpx2_Type.__name__ = "Gauge32"
_InSeSaMpx2_Object = MibScalar
inSeSaMpx2 = _InSeSaMpx2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 5),
    _InSeSaMpx2_Type()
)
inSeSaMpx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaMpx2.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaMpx2.setUnits("Hz")


class _InSeSaMpx3_Type(Gauge32):
    """Custom type inSeSaMpx3 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaMpx3_Type.__name__ = "Gauge32"
_InSeSaMpx3_Object = MibScalar
inSeSaMpx3 = _InSeSaMpx3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 6),
    _InSeSaMpx3_Type()
)
inSeSaMpx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaMpx3.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaMpx3.setUnits("Hz")


class _InSeSaMpx4_Type(Gauge32):
    """Custom type inSeSaMpx4 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_InSeSaMpx4_Type.__name__ = "Gauge32"
_InSeSaMpx4_Object = MibScalar
inSeSaMpx4 = _InSeSaMpx4_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 2, 5, 7),
    _InSeSaMpx4_Type()
)
inSeSaMpx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeSaMpx4.setStatus("current")
if mibBuilder.loadTexts:
    inSeSaMpx4.setUnits("Hz")
_InAlarms_ObjectIdentity = ObjectIdentity
inAlarms = _InAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    inAlarms.setStatus("current")


class _InAlLine1_Type(Integer32):
    """Custom type inAlLine1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlLine1_Type.__name__ = "Integer32"
_InAlLine1_Object = MibScalar
inAlLine1 = _InAlLine1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 1),
    _InAlLine1_Type()
)
inAlLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlLine1.setStatus("current")


class _InAlLine2_Type(Integer32):
    """Custom type inAlLine2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlLine2_Type.__name__ = "Integer32"
_InAlLine2_Object = MibScalar
inAlLine2 = _InAlLine2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 2),
    _InAlLine2_Type()
)
inAlLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlLine2.setStatus("current")


class _InAlMpx1_Type(Integer32):
    """Custom type inAlMpx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlMpx1_Type.__name__ = "Integer32"
_InAlMpx1_Object = MibScalar
inAlMpx1 = _InAlMpx1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 3),
    _InAlMpx1_Type()
)
inAlMpx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlMpx1.setStatus("current")


class _InAlMpx2_Type(Integer32):
    """Custom type inAlMpx2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlMpx2_Type.__name__ = "Integer32"
_InAlMpx2_Object = MibScalar
inAlMpx2 = _InAlMpx2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 4),
    _InAlMpx2_Type()
)
inAlMpx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlMpx2.setStatus("current")


class _InAlPlayer_Type(Integer32):
    """Custom type inAlPlayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlPlayer_Type.__name__ = "Integer32"
_InAlPlayer_Object = MibScalar
inAlPlayer = _InAlPlayer_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 5),
    _InAlPlayer_Type()
)
inAlPlayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlPlayer.setStatus("current")


class _InAlFault_Type(Integer32):
    """Custom type inAlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlFault_Type.__name__ = "Integer32"
_InAlFault_Object = MibScalar
inAlFault = _InAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 6),
    _InAlFault_Type()
)
inAlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlFault.setStatus("current")


class _InAlMpx3_Type(Integer32):
    """Custom type inAlMpx3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlMpx3_Type.__name__ = "Integer32"
_InAlMpx3_Object = MibScalar
inAlMpx3 = _InAlMpx3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 7),
    _InAlMpx3_Type()
)
inAlMpx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlMpx3.setStatus("current")


class _InAlMpx4_Type(Integer32):
    """Custom type inAlMpx4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlMpx4_Type.__name__ = "Integer32"
_InAlMpx4_Object = MibScalar
inAlMpx4 = _InAlMpx4_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 8),
    _InAlMpx4_Type()
)
inAlMpx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlMpx4.setStatus("current")


class _InAlAes1_Type(Integer32):
    """Custom type inAlAes1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlAes1_Type.__name__ = "Integer32"
_InAlAes1_Object = MibScalar
inAlAes1 = _InAlAes1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 9),
    _InAlAes1_Type()
)
inAlAes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlAes1.setStatus("current")


class _InAlAes2_Type(Integer32):
    """Custom type inAlAes2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlAes2_Type.__name__ = "Integer32"
_InAlAes2_Object = MibScalar
inAlAes2 = _InAlAes2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 10),
    _InAlAes2_Type()
)
inAlAes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlAes2.setStatus("current")


class _InAlAes3_Type(Integer32):
    """Custom type inAlAes3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlAes3_Type.__name__ = "Integer32"
_InAlAes3_Object = MibScalar
inAlAes3 = _InAlAes3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 11),
    _InAlAes3_Type()
)
inAlAes3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlAes3.setStatus("current")


class _InAlAna1_Type(Integer32):
    """Custom type inAlAna1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlAna1_Type.__name__ = "Integer32"
_InAlAna1_Object = MibScalar
inAlAna1 = _InAlAna1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 12),
    _InAlAna1_Type()
)
inAlAna1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlAna1.setStatus("current")


class _InAlAoip_Type(Integer32):
    """Custom type inAlAoip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_InAlAoip_Type.__name__ = "Integer32"
_InAlAoip_Object = MibScalar
inAlAoip = _InAlAoip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 4, 3, 13),
    _InAlAoip_Type()
)
inAlAoip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAlAoip.setStatus("current")
_Rds_ObjectIdentity = ObjectIdentity
rds = _Rds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rds.setStatus("current")
_RdSettings_ObjectIdentity = ObjectIdentity
rdSettings = _RdSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rdSettings.setStatus("current")


class _RdSeDsn_Type(Integer32):
    """Custom type rdSeDsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("main", 1),
          ("alt", 2))
    )


_RdSeDsn_Type.__name__ = "Integer32"
_RdSeDsn_Object = MibScalar
rdSeDsn = _RdSeDsn_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 1),
    _RdSeDsn_Type()
)
rdSeDsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdSeDsn.setStatus("current")


class _RdSeMainId_Type(Gauge32):
    """Custom type rdSeMainId based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RdSeMainId_Type.__name__ = "Gauge32"
_RdSeMainId_Object = MibScalar
rdSeMainId = _RdSeMainId_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 2),
    _RdSeMainId_Type()
)
rdSeMainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdSeMainId.setStatus("current")


class _RdSeAltId_Type(Gauge32):
    """Custom type rdSeAltId based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RdSeAltId_Type.__name__ = "Gauge32"
_RdSeAltId_Object = MibScalar
rdSeAltId = _RdSeAltId_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 3),
    _RdSeAltId_Type()
)
rdSeAltId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdSeAltId.setStatus("current")


class _RdSeCtEnable_Type(Integer32):
    """Custom type rdSeCtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdSeCtEnable_Type.__name__ = "Integer32"
_RdSeCtEnable_Object = MibScalar
rdSeCtEnable = _RdSeCtEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 4),
    _RdSeCtEnable_Type()
)
rdSeCtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdSeCtEnable.setStatus("current")


class _RdSeCtOffset_Type(Integer32):
    """Custom type rdSeCtOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_RdSeCtOffset_Type.__name__ = "Integer32"
_RdSeCtOffset_Object = MibScalar
rdSeCtOffset = _RdSeCtOffset_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 5),
    _RdSeCtOffset_Type()
)
rdSeCtOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdSeCtOffset.setStatus("current")
if mibBuilder.loadTexts:
    rdSeCtOffset.setUnits("Hour/2")


class _RdSeCurrentPs_Type(DisplayString):
    """Custom type rdSeCurrentPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RdSeCurrentPs_Type.__name__ = "DisplayString"
_RdSeCurrentPs_Object = MibScalar
rdSeCurrentPs = _RdSeCurrentPs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 6),
    _RdSeCurrentPs_Type()
)
rdSeCurrentPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdSeCurrentPs.setStatus("current")


class _RdSeCurrentRt_Type(DisplayString):
    """Custom type rdSeCurrentRt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RdSeCurrentRt_Type.__name__ = "DisplayString"
_RdSeCurrentRt_Object = MibScalar
rdSeCurrentRt = _RdSeCurrentRt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 1, 7),
    _RdSeCurrentRt_Type()
)
rdSeCurrentRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdSeCurrentRt.setStatus("current")
_RdMain_ObjectIdentity = ObjectIdentity
rdMain = _RdMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    rdMain.setStatus("current")


class _RdMaPi_Type(Integer32):
    """Custom type rdMaPi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdMaPi_Type.__name__ = "Integer32"
_RdMaPi_Object = MibScalar
rdMaPi = _RdMaPi_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 1),
    _RdMaPi_Type()
)
rdMaPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaPi.setStatus("current")


class _RdMaPs_Type(DisplayString):
    """Custom type rdMaPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RdMaPs_Type.__name__ = "DisplayString"
_RdMaPs_Object = MibScalar
rdMaPs = _RdMaPs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 2),
    _RdMaPs_Type()
)
rdMaPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaPs.setStatus("current")


class _RdMaPty_Type(Gauge32):
    """Custom type rdMaPty based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RdMaPty_Type.__name__ = "Gauge32"
_RdMaPty_Object = MibScalar
rdMaPty = _RdMaPty_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 3),
    _RdMaPty_Type()
)
rdMaPty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaPty.setStatus("current")


class _RdMaMs_Type(Integer32):
    """Custom type rdMaMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("speech", 1),
          ("music", 2))
    )


_RdMaMs_Type.__name__ = "Integer32"
_RdMaMs_Object = MibScalar
rdMaMs = _RdMaMs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 4),
    _RdMaMs_Type()
)
rdMaMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaMs.setStatus("current")


class _RdMaDi_Type(Gauge32):
    """Custom type rdMaDi based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdMaDi_Type.__name__ = "Gauge32"
_RdMaDi_Object = MibScalar
rdMaDi = _RdMaDi_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 5),
    _RdMaDi_Type()
)
rdMaDi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaDi.setStatus("current")


class _RdMaAf_Type(DisplayString):
    """Custom type rdMaAf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 182),
    )


_RdMaAf_Type.__name__ = "DisplayString"
_RdMaAf_Object = MibScalar
rdMaAf = _RdMaAf_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 6),
    _RdMaAf_Type()
)
rdMaAf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaAf.setStatus("current")


class _RdMaRt_Type(DisplayString):
    """Custom type rdMaRt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RdMaRt_Type.__name__ = "DisplayString"
_RdMaRt_Object = MibScalar
rdMaRt = _RdMaRt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 7),
    _RdMaRt_Type()
)
rdMaRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaRt.setStatus("current")


class _RdMaPtyn_Type(DisplayString):
    """Custom type rdMaPtyn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RdMaPtyn_Type.__name__ = "DisplayString"
_RdMaPtyn_Object = MibScalar
rdMaPtyn = _RdMaPtyn_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 8),
    _RdMaPtyn_Type()
)
rdMaPtyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaPtyn.setStatus("current")


class _RdMaGs_Type(DisplayString):
    """Custom type rdMaGs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RdMaGs_Type.__name__ = "DisplayString"
_RdMaGs_Object = MibScalar
rdMaGs = _RdMaGs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 9),
    _RdMaGs_Type()
)
rdMaGs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaGs.setStatus("current")


class _RdMaTa_Type(Integer32):
    """Custom type rdMaTa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdMaTa_Type.__name__ = "Integer32"
_RdMaTa_Object = MibScalar
rdMaTa = _RdMaTa_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 10),
    _RdMaTa_Type()
)
rdMaTa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaTa.setStatus("current")


class _RdMaTp_Type(Integer32):
    """Custom type rdMaTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdMaTp_Type.__name__ = "Integer32"
_RdMaTp_Object = MibScalar
rdMaTp = _RdMaTp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 2, 11),
    _RdMaTp_Type()
)
rdMaTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdMaTp.setStatus("current")
_RdAlt_ObjectIdentity = ObjectIdentity
rdAlt = _RdAlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    rdAlt.setStatus("current")


class _RdAtPi_Type(Integer32):
    """Custom type rdAtPi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdAtPi_Type.__name__ = "Integer32"
_RdAtPi_Object = MibScalar
rdAtPi = _RdAtPi_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 1),
    _RdAtPi_Type()
)
rdAtPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtPi.setStatus("current")


class _RdAtPs_Type(DisplayString):
    """Custom type rdAtPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RdAtPs_Type.__name__ = "DisplayString"
_RdAtPs_Object = MibScalar
rdAtPs = _RdAtPs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 2),
    _RdAtPs_Type()
)
rdAtPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtPs.setStatus("current")


class _RdAtPty_Type(Gauge32):
    """Custom type rdAtPty based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RdAtPty_Type.__name__ = "Gauge32"
_RdAtPty_Object = MibScalar
rdAtPty = _RdAtPty_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 3),
    _RdAtPty_Type()
)
rdAtPty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtPty.setStatus("current")


class _RdAtMs_Type(Integer32):
    """Custom type rdAtMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("speech", 1),
          ("music", 2))
    )


_RdAtMs_Type.__name__ = "Integer32"
_RdAtMs_Object = MibScalar
rdAtMs = _RdAtMs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 4),
    _RdAtMs_Type()
)
rdAtMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtMs.setStatus("current")


class _RdAtDi_Type(Gauge32):
    """Custom type rdAtDi based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdAtDi_Type.__name__ = "Gauge32"
_RdAtDi_Object = MibScalar
rdAtDi = _RdAtDi_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 5),
    _RdAtDi_Type()
)
rdAtDi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtDi.setStatus("current")


class _RdAtAf_Type(DisplayString):
    """Custom type rdAtAf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 182),
    )


_RdAtAf_Type.__name__ = "DisplayString"
_RdAtAf_Object = MibScalar
rdAtAf = _RdAtAf_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 6),
    _RdAtAf_Type()
)
rdAtAf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtAf.setStatus("current")


class _RdAtRt_Type(DisplayString):
    """Custom type rdAtRt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RdAtRt_Type.__name__ = "DisplayString"
_RdAtRt_Object = MibScalar
rdAtRt = _RdAtRt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 7),
    _RdAtRt_Type()
)
rdAtRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtRt.setStatus("current")


class _RdAtPtyn_Type(DisplayString):
    """Custom type rdAtPtyn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RdAtPtyn_Type.__name__ = "DisplayString"
_RdAtPtyn_Object = MibScalar
rdAtPtyn = _RdAtPtyn_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 8),
    _RdAtPtyn_Type()
)
rdAtPtyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtPtyn.setStatus("current")


class _RdAtGs_Type(DisplayString):
    """Custom type rdAtGs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RdAtGs_Type.__name__ = "DisplayString"
_RdAtGs_Object = MibScalar
rdAtGs = _RdAtGs_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 9),
    _RdAtGs_Type()
)
rdAtGs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtGs.setStatus("current")


class _RdAtTa_Type(Integer32):
    """Custom type rdAtTa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdAtTa_Type.__name__ = "Integer32"
_RdAtTa_Object = MibScalar
rdAtTa = _RdAtTa_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 10),
    _RdAtTa_Type()
)
rdAtTa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtTa.setStatus("current")


class _RdAtTp_Type(Integer32):
    """Custom type rdAtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdAtTp_Type.__name__ = "Integer32"
_RdAtTp_Object = MibScalar
rdAtTp = _RdAtTp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 3, 11),
    _RdAtTp_Type()
)
rdAtTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdAtTp.setStatus("current")
_RdPsScrollTable_Object = MibTable
rdPsScrollTable = _RdPsScrollTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    rdPsScrollTable.setStatus("current")
_RdPsScrollEntry_Object = MibTableRow
rdPsScrollEntry = _RdPsScrollEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1)
)
rdPsScrollEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "rdPsScrollIndex"),
)
if mibBuilder.loadTexts:
    rdPsScrollEntry.setStatus("current")


class _RdPsScrollIndex_Type(Integer32):
    """Custom type rdPsScrollIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdPsScrollIndex_Type.__name__ = "Integer32"
_RdPsScrollIndex_Object = MibTableColumn
rdPsScrollIndex = _RdPsScrollIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 1),
    _RdPsScrollIndex_Type()
)
rdPsScrollIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdPsScrollIndex.setStatus("current")


class _RdPsScrollText_Type(DisplayString):
    """Custom type rdPsScrollText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_RdPsScrollText_Type.__name__ = "DisplayString"
_RdPsScrollText_Object = MibTableColumn
rdPsScrollText = _RdPsScrollText_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 2),
    _RdPsScrollText_Type()
)
rdPsScrollText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollText.setStatus("current")


class _RdPsScrollRepetition_Type(Gauge32):
    """Custom type rdPsScrollRepetition based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RdPsScrollRepetition_Type.__name__ = "Gauge32"
_RdPsScrollRepetition_Object = MibTableColumn
rdPsScrollRepetition = _RdPsScrollRepetition_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 3),
    _RdPsScrollRepetition_Type()
)
rdPsScrollRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollRepetition.setStatus("current")


class _RdPsScrollEnable_Type(Integer32):
    """Custom type rdPsScrollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdPsScrollEnable_Type.__name__ = "Integer32"
_RdPsScrollEnable_Object = MibTableColumn
rdPsScrollEnable = _RdPsScrollEnable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 4),
    _RdPsScrollEnable_Type()
)
rdPsScrollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollEnable.setStatus("current")


class _RdPsScrollCenter_Type(Integer32):
    """Custom type rdPsScrollCenter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdPsScrollCenter_Type.__name__ = "Integer32"
_RdPsScrollCenter_Object = MibTableColumn
rdPsScrollCenter = _RdPsScrollCenter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 5),
    _RdPsScrollCenter_Type()
)
rdPsScrollCenter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollCenter.setStatus("current")


class _RdPsScrollTrunc_Type(Integer32):
    """Custom type rdPsScrollTrunc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_RdPsScrollTrunc_Type.__name__ = "Integer32"
_RdPsScrollTrunc_Object = MibTableColumn
rdPsScrollTrunc = _RdPsScrollTrunc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 6),
    _RdPsScrollTrunc_Type()
)
rdPsScrollTrunc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollTrunc.setStatus("current")


class _RdPsScrollIncrement_Type(Gauge32):
    """Custom type rdPsScrollIncrement based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RdPsScrollIncrement_Type.__name__ = "Gauge32"
_RdPsScrollIncrement_Object = MibTableColumn
rdPsScrollIncrement = _RdPsScrollIncrement_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 7),
    _RdPsScrollIncrement_Type()
)
rdPsScrollIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollIncrement.setStatus("current")


class _RdPsScrollDelay_Type(Gauge32):
    """Custom type rdPsScrollDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RdPsScrollDelay_Type.__name__ = "Gauge32"
_RdPsScrollDelay_Object = MibTableColumn
rdPsScrollDelay = _RdPsScrollDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 5, 4, 1, 8),
    _RdPsScrollDelay_Type()
)
rdPsScrollDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdPsScrollDelay.setStatus("current")
_Modulator_ObjectIdentity = ObjectIdentity
modulator = _Modulator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    modulator.setStatus("current")
_MoDeviation_ObjectIdentity = ObjectIdentity
moDeviation = _MoDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    moDeviation.setStatus("current")


class _MoDevMpx_Type(Gauge32):
    """Custom type moDevMpx based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MoDevMpx_Type.__name__ = "Gauge32"
_MoDevMpx_Object = MibScalar
moDevMpx = _MoDevMpx_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 1),
    _MoDevMpx_Type()
)
moDevMpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moDevMpx.setStatus("current")
if mibBuilder.loadTexts:
    moDevMpx.setUnits("kHz/100")


class _MoDevAudio_Type(Gauge32):
    """Custom type moDevAudio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MoDevAudio_Type.__name__ = "Gauge32"
_MoDevAudio_Object = MibScalar
moDevAudio = _MoDevAudio_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 2),
    _MoDevAudio_Type()
)
moDevAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moDevAudio.setStatus("current")
if mibBuilder.loadTexts:
    moDevAudio.setUnits("kHz/100")


class _MoDevPilot_Type(Gauge32):
    """Custom type moDevPilot based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoDevPilot_Type.__name__ = "Gauge32"
_MoDevPilot_Object = MibScalar
moDevPilot = _MoDevPilot_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 3),
    _MoDevPilot_Type()
)
moDevPilot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moDevPilot.setStatus("current")
if mibBuilder.loadTexts:
    moDevPilot.setUnits("kHz/10")


class _MoDevRds_Type(Gauge32):
    """Custom type moDevRds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoDevRds_Type.__name__ = "Gauge32"
_MoDevRds_Object = MibScalar
moDevRds = _MoDevRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 4),
    _MoDevRds_Type()
)
moDevRds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moDevRds.setStatus("current")
if mibBuilder.loadTexts:
    moDevRds.setUnits("kHz/10")


class _MoDevSca_Type(Gauge32):
    """Custom type moDevSca based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoDevSca_Type.__name__ = "Gauge32"
_MoDevSca_Object = MibScalar
moDevSca = _MoDevSca_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 5),
    _MoDevSca_Type()
)
moDevSca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moDevSca.setStatus("current")
if mibBuilder.loadTexts:
    moDevSca.setUnits("kHz/10")


class _MoDevRmsMeas_Type(Gauge32):
    """Custom type moDevRmsMeas based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_MoDevRmsMeas_Type.__name__ = "Gauge32"
_MoDevRmsMeas_Object = MibScalar
moDevRmsMeas = _MoDevRmsMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 6),
    _MoDevRmsMeas_Type()
)
moDevRmsMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDevRmsMeas.setStatus("current")
if mibBuilder.loadTexts:
    moDevRmsMeas.setUnits("kHz/100")


class _MoDevPeakMeas_Type(Integer32):
    """Custom type moDevPeakMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15000, 15000),
    )


_MoDevPeakMeas_Type.__name__ = "Integer32"
_MoDevPeakMeas_Object = MibScalar
moDevPeakMeas = _MoDevPeakMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 7),
    _MoDevPeakMeas_Type()
)
moDevPeakMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDevPeakMeas.setStatus("current")
if mibBuilder.loadTexts:
    moDevPeakMeas.setUnits("kHz/100")


class _MoDevPeakMaxMeas_Type(Integer32):
    """Custom type moDevPeakMaxMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15000, 15000),
    )


_MoDevPeakMaxMeas_Type.__name__ = "Integer32"
_MoDevPeakMaxMeas_Object = MibScalar
moDevPeakMaxMeas = _MoDevPeakMaxMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 8),
    _MoDevPeakMaxMeas_Type()
)
moDevPeakMaxMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDevPeakMaxMeas.setStatus("current")
if mibBuilder.loadTexts:
    moDevPeakMaxMeas.setUnits("kHz/100")


class _MoDevMPeakMaxMeas_Type(Integer32):
    """Custom type moDevMPeakMaxMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15000, 15000),
    )


_MoDevMPeakMaxMeas_Type.__name__ = "Integer32"
_MoDevMPeakMaxMeas_Object = MibScalar
moDevMPeakMaxMeas = _MoDevMPeakMaxMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 9),
    _MoDevMPeakMaxMeas_Type()
)
moDevMPeakMaxMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDevMPeakMaxMeas.setStatus("current")
if mibBuilder.loadTexts:
    moDevMPeakMaxMeas.setUnits("kHz/100")


class _MoDevSPeakMaxMeas_Type(Integer32):
    """Custom type moDevSPeakMaxMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15000, 15000),
    )


_MoDevSPeakMaxMeas_Type.__name__ = "Integer32"
_MoDevSPeakMaxMeas_Object = MibScalar
moDevSPeakMaxMeas = _MoDevSPeakMaxMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 1, 10),
    _MoDevSPeakMaxMeas_Type()
)
moDevSPeakMaxMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moDevSPeakMaxMeas.setStatus("current")
if mibBuilder.loadTexts:
    moDevSPeakMaxMeas.setUnits("kHz/100")
_MoSettings_ObjectIdentity = ObjectIdentity
moSettings = _MoSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    moSettings.setStatus("current")


class _MoSeCoder_Type(Integer32):
    """Custom type moSeCoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("stereo", 1),
          ("mono", 2),
          ("monoLeft", 3),
          ("monoRight", 4))
    )


_MoSeCoder_Type.__name__ = "Integer32"
_MoSeCoder_Object = MibScalar
moSeCoder = _MoSeCoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 1),
    _MoSeCoder_Type()
)
moSeCoder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoder.setStatus("current")


class _MoSeCoderRdsSelect_Type(Integer32):
    """Custom type moSeCoderRdsSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mpx1", 1),
          ("mpx2", 2),
          ("aoip1", 3),
          ("aoip2", 4),
          ("tuner1", 5),
          ("tuner2", 6),
          ("internal", 7),
          ("auto", 8),
          ("off", 9),
          ("mpx3", 10),
          ("mpx4", 11),
          ("aes1", 12),
          ("aes2", 13),
          ("aes3", 14))
    )


_MoSeCoderRdsSelect_Type.__name__ = "Integer32"
_MoSeCoderRdsSelect_Object = MibScalar
moSeCoderRdsSelect = _MoSeCoderRdsSelect_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 2),
    _MoSeCoderRdsSelect_Type()
)
moSeCoderRdsSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoderRdsSelect.setStatus("current")


class _MoSeCoderScaSelect_Type(Integer32):
    """Custom type moSeCoderScaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mpx1", 1),
          ("mpx2", 2),
          ("aoip1", 3),
          ("aoip2", 4),
          ("tuner1", 5),
          ("tuner2", 6),
          ("auto", 7),
          ("off", 8),
          ("mpx3", 9),
          ("mpx4", 10),
          ("aes1", 11),
          ("aes2", 12),
          ("aes3", 13))
    )


_MoSeCoderScaSelect_Type.__name__ = "Integer32"
_MoSeCoderScaSelect_Object = MibScalar
moSeCoderScaSelect = _MoSeCoderScaSelect_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 3),
    _MoSeCoderScaSelect_Type()
)
moSeCoderScaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoderScaSelect.setStatus("current")


class _MoSeCoderRdsBackup_Type(Integer32):
    """Custom type moSeCoderRdsBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSeCoderRdsBackup_Type.__name__ = "Integer32"
_MoSeCoderRdsBackup_Object = MibScalar
moSeCoderRdsBackup = _MoSeCoderRdsBackup_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 4),
    _MoSeCoderRdsBackup_Type()
)
moSeCoderRdsBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoderRdsBackup.setStatus("current")


class _MoSeCoderCurrentRds_Type(Integer32):
    """Custom type moSeCoderCurrentRds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("mpx1", 2),
          ("mpx2", 3),
          ("aoip1", 4),
          ("aoip2", 5),
          ("tuner1", 6),
          ("tuner2", 7),
          ("internal", 8),
          ("mpx3", 9),
          ("mpx4", 10),
          ("aes1", 11),
          ("aes2", 12),
          ("aes3", 13),
          ("auto", 14))
    )


_MoSeCoderCurrentRds_Type.__name__ = "Integer32"
_MoSeCoderCurrentRds_Object = MibScalar
moSeCoderCurrentRds = _MoSeCoderCurrentRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 5),
    _MoSeCoderCurrentRds_Type()
)
moSeCoderCurrentRds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSeCoderCurrentRds.setStatus("current")


class _MoSeCoderCurrentSca_Type(Integer32):
    """Custom type moSeCoderCurrentSca based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("mpx1", 2),
          ("mpx2", 3),
          ("aoip1", 4),
          ("aoip2", 5),
          ("tuner1", 6),
          ("tuner2", 7),
          ("mpx3", 8),
          ("mpx4", 9),
          ("aes1", 10),
          ("aes2", 11),
          ("aes3", 12),
          ("auto", 13))
    )


_MoSeCoderCurrentSca_Type.__name__ = "Integer32"
_MoSeCoderCurrentSca_Object = MibScalar
moSeCoderCurrentSca = _MoSeCoderCurrentSca_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 6),
    _MoSeCoderCurrentSca_Type()
)
moSeCoderCurrentSca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSeCoderCurrentSca.setStatus("current")


class _MoSeCoder19kOutLevel_Type(Gauge32):
    """Custom type moSeCoder19kOutLevel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MoSeCoder19kOutLevel_Type.__name__ = "Gauge32"
_MoSeCoder19kOutLevel_Object = MibScalar
moSeCoder19kOutLevel = _MoSeCoder19kOutLevel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 7),
    _MoSeCoder19kOutLevel_Type()
)
moSeCoder19kOutLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoder19kOutLevel.setStatus("current")


class _MoSeCoderAlrRdsSwitch_Type(Integer32):
    """Custom type moSeCoderAlrRdsSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSeCoderAlrRdsSwitch_Type.__name__ = "Integer32"
_MoSeCoderAlrRdsSwitch_Object = MibScalar
moSeCoderAlrRdsSwitch = _MoSeCoderAlrRdsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 8),
    _MoSeCoderAlrRdsSwitch_Type()
)
moSeCoderAlrRdsSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSeCoderAlrRdsSwitch.setStatus("current")


class _MoSeCoderRdsPhase_Type(Integer32):
    """Custom type moSeCoderRdsPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18000, 18000),
    )


_MoSeCoderRdsPhase_Type.__name__ = "Integer32"
_MoSeCoderRdsPhase_Object = MibScalar
moSeCoderRdsPhase = _MoSeCoderRdsPhase_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 9),
    _MoSeCoderRdsPhase_Type()
)
moSeCoderRdsPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoderRdsPhase.setStatus("current")
if mibBuilder.loadTexts:
    moSeCoderRdsPhase.setUnits("deg/100")


class _MoSeCoderRdsSelectBackup_Type(Integer32):
    """Custom type moSeCoderRdsSelectBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("mpx1", 1),
          ("mpx2", 2),
          ("aoip1", 3),
          ("aoip2", 4),
          ("tuner1", 5),
          ("tuner2", 6),
          ("internal", 7),
          ("off", 9),
          ("mpx3", 10),
          ("mpx4", 11),
          ("aes1", 12),
          ("aes2", 13),
          ("aes3", 14))
    )


_MoSeCoderRdsSelectBackup_Type.__name__ = "Integer32"
_MoSeCoderRdsSelectBackup_Object = MibScalar
moSeCoderRdsSelectBackup = _MoSeCoderRdsSelectBackup_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 2, 10),
    _MoSeCoderRdsSelectBackup_Type()
)
moSeCoderRdsSelectBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSeCoderRdsSelectBackup.setStatus("current")
_MoSoundProc_ObjectIdentity = ObjectIdentity
moSoundProc = _MoSoundProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    moSoundProc.setStatus("current")
_MoSpAgc_ObjectIdentity = ObjectIdentity
moSpAgc = _MoSpAgc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    moSpAgc.setStatus("obsolete")


class _MoSpAgState_Type(Integer32):
    """Custom type moSpAgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpAgState_Type.__name__ = "Integer32"
_MoSpAgState_Object = MibScalar
moSpAgState = _MoSpAgState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 1),
    _MoSpAgState_Type()
)
moSpAgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpAgState.setStatus("obsolete")


class _MoSpAgDrive_Type(Integer32):
    """Custom type moSpAgDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_MoSpAgDrive_Type.__name__ = "Integer32"
_MoSpAgDrive_Object = MibScalar
moSpAgDrive = _MoSpAgDrive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 2),
    _MoSpAgDrive_Type()
)
moSpAgDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpAgDrive.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpAgDrive.setUnits("dB/100")


class _MoSpAgAtt_Type(Gauge32):
    """Custom type moSpAgAtt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MoSpAgAtt_Type.__name__ = "Gauge32"
_MoSpAgAtt_Object = MibScalar
moSpAgAtt = _MoSpAgAtt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 3),
    _MoSpAgAtt_Type()
)
moSpAgAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpAgAtt.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpAgAtt.setUnits("dB/s")


class _MoSpAgRel_Type(Gauge32):
    """Custom type moSpAgRel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MoSpAgRel_Type.__name__ = "Gauge32"
_MoSpAgRel_Object = MibScalar
moSpAgRel = _MoSpAgRel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 4),
    _MoSpAgRel_Type()
)
moSpAgRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpAgRel.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpAgRel.setUnits("dB/s/100")


class _MoSpAgThr_Type(Integer32):
    """Custom type moSpAgThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 0),
    )


_MoSpAgThr_Type.__name__ = "Integer32"
_MoSpAgThr_Object = MibScalar
moSpAgThr = _MoSpAgThr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 5),
    _MoSpAgThr_Type()
)
moSpAgThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpAgThr.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpAgThr.setUnits("dB/100")


class _MoSpAgMeas_Type(Integer32):
    """Custom type moSpAgMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_MoSpAgMeas_Type.__name__ = "Integer32"
_MoSpAgMeas_Object = MibScalar
moSpAgMeas = _MoSpAgMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 1, 6),
    _MoSpAgMeas_Type()
)
moSpAgMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpAgMeas.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpAgMeas.setUnits("dB/100")
_MoSpLimiter_ObjectIdentity = ObjectIdentity
moSpLimiter = _MoSpLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    moSpLimiter.setStatus("obsolete")


class _MoSpLimState_Type(Integer32):
    """Custom type moSpLimState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpLimState_Type.__name__ = "Integer32"
_MoSpLimState_Object = MibScalar
moSpLimState = _MoSpLimState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2, 1),
    _MoSpLimState_Type()
)
moSpLimState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpLimState.setStatus("obsolete")


class _MoSpLimVal_Type(Gauge32):
    """Custom type moSpLimVal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MoSpLimVal_Type.__name__ = "Gauge32"
_MoSpLimVal_Object = MibScalar
moSpLimVal = _MoSpLimVal_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2, 2),
    _MoSpLimVal_Type()
)
moSpLimVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpLimVal.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpLimVal.setUnits("kHz")


class _MoSpLimDrive_Type(Gauge32):
    """Custom type moSpLimDrive based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MoSpLimDrive_Type.__name__ = "Gauge32"
_MoSpLimDrive_Object = MibScalar
moSpLimDrive = _MoSpLimDrive_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2, 3),
    _MoSpLimDrive_Type()
)
moSpLimDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpLimDrive.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpLimDrive.setUnits("db/10")


class _MoSpLimMeas_Type(Gauge32):
    """Custom type moSpLimMeas based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoSpLimMeas_Type.__name__ = "Gauge32"
_MoSpLimMeas_Object = MibScalar
moSpLimMeas = _MoSpLimMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2, 4),
    _MoSpLimMeas_Type()
)
moSpLimMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpLimMeas.setStatus("obsolete")
if mibBuilder.loadTexts:
    moSpLimMeas.setUnits("db/10")


class _MoSpLimPreset_Type(Integer32):
    """Custom type moSpLimPreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("custom", 1),
          ("preset1", 2),
          ("preset2", 3),
          ("preset3", 4),
          ("preset4", 5),
          ("preset5", 6),
          ("preset6", 7))
    )


_MoSpLimPreset_Type.__name__ = "Integer32"
_MoSpLimPreset_Object = MibScalar
moSpLimPreset = _MoSpLimPreset_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 2, 5),
    _MoSpLimPreset_Type()
)
moSpLimPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpLimPreset.setStatus("obsolete")
_MoSpClip_ObjectIdentity = ObjectIdentity
moSpClip = _MoSpClip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 3)
)
if mibBuilder.loadTexts:
    moSpClip.setStatus("current")


class _MoSpClState_Type(Integer32):
    """Custom type moSpClState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpClState_Type.__name__ = "Integer32"
_MoSpClState_Object = MibScalar
moSpClState = _MoSpClState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 3, 1),
    _MoSpClState_Type()
)
moSpClState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpClState.setStatus("current")


class _MoSpClVal_Type(Gauge32):
    """Custom type moSpClVal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_MoSpClVal_Type.__name__ = "Gauge32"
_MoSpClVal_Object = MibScalar
moSpClVal = _MoSpClVal_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 3, 2),
    _MoSpClVal_Type()
)
moSpClVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpClVal.setStatus("current")
if mibBuilder.loadTexts:
    moSpClVal.setUnits("kHz")


class _MoSpClMeas_Type(Integer32):
    """Custom type moSpClMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpClMeas_Type.__name__ = "Integer32"
_MoSpClMeas_Object = MibScalar
moSpClMeas = _MoSpClMeas_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 3, 3),
    _MoSpClMeas_Type()
)
moSpClMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpClMeas.setStatus("current")
_MoSpMpxPwr_ObjectIdentity = ObjectIdentity
moSpMpxPwr = _MoSpMpxPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4)
)
if mibBuilder.loadTexts:
    moSpMpxPwr.setStatus("current")


class _MoSpMpState_Type(Integer32):
    """Custom type moSpMpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpMpState_Type.__name__ = "Integer32"
_MoSpMpState_Object = MibScalar
moSpMpState = _MoSpMpState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4, 1),
    _MoSpMpState_Type()
)
moSpMpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpMpState.setStatus("current")


class _MoSpMpTarget_Type(Integer32):
    """Custom type moSpMpTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 120),
    )


_MoSpMpTarget_Type.__name__ = "Integer32"
_MoSpMpTarget_Object = MibScalar
moSpMpTarget = _MoSpMpTarget_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4, 2),
    _MoSpMpTarget_Type()
)
moSpMpTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpMpTarget.setStatus("current")
if mibBuilder.loadTexts:
    moSpMpTarget.setUnits("dB")


class _MoSpMpMeas1m_Type(Integer32):
    """Custom type moSpMpMeas1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_MoSpMpMeas1m_Type.__name__ = "Integer32"
_MoSpMpMeas1m_Object = MibScalar
moSpMpMeas1m = _MoSpMpMeas1m_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4, 3),
    _MoSpMpMeas1m_Type()
)
moSpMpMeas1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpMpMeas1m.setStatus("current")
if mibBuilder.loadTexts:
    moSpMpMeas1m.setUnits("dB/100")


class _MoSpMpMeas10s_Type(Integer32):
    """Custom type moSpMpMeas10s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_MoSpMpMeas10s_Type.__name__ = "Integer32"
_MoSpMpMeas10s_Object = MibScalar
moSpMpMeas10s = _MoSpMpMeas10s_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4, 4),
    _MoSpMpMeas10s_Type()
)
moSpMpMeas10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpMpMeas10s.setStatus("current")
if mibBuilder.loadTexts:
    moSpMpMeas10s.setUnits("dB/100")


class _MoSpMpMeasAtt_Type(Integer32):
    """Custom type moSpMpMeasAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32000, 32000),
    )


_MoSpMpMeasAtt_Type.__name__ = "Integer32"
_MoSpMpMeasAtt_Object = MibScalar
moSpMpMeasAtt = _MoSpMpMeasAtt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 4, 5),
    _MoSpMpMeasAtt_Type()
)
moSpMpMeasAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpMpMeasAtt.setStatus("current")
if mibBuilder.loadTexts:
    moSpMpMeasAtt.setUnits("dB/100")
_MoSpPreset_ObjectIdentity = ObjectIdentity
moSpPreset = _MoSpPreset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5)
)
if mibBuilder.loadTexts:
    moSpPreset.setStatus("current")


class _MoSpPrNum_Type(Gauge32):
    """Custom type moSpPrNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MoSpPrNum_Type.__name__ = "Gauge32"
_MoSpPrNum_Object = MibScalar
moSpPrNum = _MoSpPrNum_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 1),
    _MoSpPrNum_Type()
)
moSpPrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpPrNum.setStatus("current")


class _MoSpPrBypass_Type(Integer32):
    """Custom type moSpPrBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSpPrBypass_Type.__name__ = "Integer32"
_MoSpPrBypass_Object = MibScalar
moSpPrBypass = _MoSpPrBypass_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 2),
    _MoSpPrBypass_Type()
)
moSpPrBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSpPrBypass.setStatus("current")
_MoSpPrPresetsTable_Object = MibTable
moSpPrPresetsTable = _MoSpPrPresetsTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 3)
)
if mibBuilder.loadTexts:
    moSpPrPresetsTable.setStatus("current")
_MoSpPrPresetsEntry_Object = MibTableRow
moSpPrPresetsEntry = _MoSpPrPresetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 3, 1)
)
moSpPrPresetsEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "moSpPrTableIndex"),
)
if mibBuilder.loadTexts:
    moSpPrPresetsEntry.setStatus("current")


class _MoSpPrTableIndex_Type(Integer32):
    """Custom type moSpPrTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MoSpPrTableIndex_Type.__name__ = "Integer32"
_MoSpPrTableIndex_Object = MibTableColumn
moSpPrTableIndex = _MoSpPrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 3, 1, 1),
    _MoSpPrTableIndex_Type()
)
moSpPrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moSpPrTableIndex.setStatus("current")


class _MoSpPrTableName_Type(DisplayString):
    """Custom type moSpPrTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MoSpPrTableName_Type.__name__ = "DisplayString"
_MoSpPrTableName_Object = MibTableColumn
moSpPrTableName = _MoSpPrTableName_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 3, 5, 3, 1, 2),
    _MoSpPrTableName_Type()
)
moSpPrTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSpPrTableName.setStatus("current")
_MoSfn_ObjectIdentity = ObjectIdentity
moSfn = _MoSfn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    moSfn.setStatus("current")


class _MoSfConfDelay_Type(Gauge32):
    """Custom type moSfConfDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000000),
    )


_MoSfConfDelay_Type.__name__ = "Gauge32"
_MoSfConfDelay_Object = MibScalar
moSfConfDelay = _MoSfConfDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 1),
    _MoSfConfDelay_Type()
)
moSfConfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSfConfDelay.setStatus("current")
if mibBuilder.loadTexts:
    moSfConfDelay.setUnits("us/100")


class _MoSfConfState_Type(Integer32):
    """Custom type moSfConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSfConfState_Type.__name__ = "Integer32"
_MoSfConfState_Object = MibScalar
moSfConfState = _MoSfConfState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 2),
    _MoSfConfState_Type()
)
moSfConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSfConfState.setStatus("current")


class _MoSfMeasDelay_Type(Gauge32):
    """Custom type moSfMeasDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000000),
    )


_MoSfMeasDelay_Type.__name__ = "Gauge32"
_MoSfMeasDelay_Object = MibScalar
moSfMeasDelay = _MoSfMeasDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 3),
    _MoSfMeasDelay_Type()
)
moSfMeasDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfMeasDelay.setStatus("current")
if mibBuilder.loadTexts:
    moSfMeasDelay.setUnits("us/100")


class _MoSfAlarm_Type(Integer32):
    """Custom type moSfAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSfAlarm_Type.__name__ = "Integer32"
_MoSfAlarm_Object = MibScalar
moSfAlarm = _MoSfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 4),
    _MoSfAlarm_Type()
)
moSfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfAlarm.setStatus("current")


class _MoSfConfOp10M_Type(Integer32):
    """Custom type moSfConfOp10M based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("manual", 1),
          ("auto", 2))
    )


_MoSfConfOp10M_Type.__name__ = "Integer32"
_MoSfConfOp10M_Object = MibScalar
moSfConfOp10M = _MoSfConfOp10M_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 5),
    _MoSfConfOp10M_Type()
)
moSfConfOp10M.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moSfConfOp10M.setStatus("current")


class _MoSfState10M_Type(Integer32):
    """Custom type moSfState10M based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("present", 1),
          ("notPresent", 2))
    )


_MoSfState10M_Type.__name__ = "Integer32"
_MoSfState10M_Object = MibScalar
moSfState10M = _MoSfState10M_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 6),
    _MoSfState10M_Type()
)
moSfState10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfState10M.setStatus("current")


class _MoSfClockSource_Type(Integer32):
    """Custom type moSfClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("internal", 1),
          ("external", 2))
    )


_MoSfClockSource_Type.__name__ = "Integer32"
_MoSfClockSource_Object = MibScalar
moSfClockSource = _MoSfClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 7),
    _MoSfClockSource_Type()
)
moSfClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfClockSource.setStatus("current")


class _MoSfState1PPS_Type(Integer32):
    """Custom type moSfState1PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("present", 1),
          ("notPresent", 2))
    )


_MoSfState1PPS_Type.__name__ = "Integer32"
_MoSfState1PPS_Object = MibScalar
moSfState1PPS = _MoSfState1PPS_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 8),
    _MoSfState1PPS_Type()
)
moSfState1PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfState1PPS.setStatus("current")


class _MoSfSwitch10MAlarm_Type(Integer32):
    """Custom type moSfSwitch10MAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoSfSwitch10MAlarm_Type.__name__ = "Integer32"
_MoSfSwitch10MAlarm_Object = MibScalar
moSfSwitch10MAlarm = _MoSfSwitch10MAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 6, 4, 9),
    _MoSfSwitch10MAlarm_Type()
)
moSfSwitch10MAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moSfSwitch10MAlarm.setStatus("current")
_Tx_ObjectIdentity = ObjectIdentity
tx = _Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tx.setStatus("current")
_TxGeneral_ObjectIdentity = ObjectIdentity
txGeneral = _TxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    txGeneral.setStatus("current")
_TxGnGlobal_ObjectIdentity = ObjectIdentity
txGnGlobal = _TxGnGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    txGnGlobal.setStatus("current")


class _TxGnGlName_Type(DisplayString):
    """Custom type txGnGlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TxGnGlName_Type.__name__ = "DisplayString"
_TxGnGlName_Object = MibScalar
txGnGlName = _TxGnGlName_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 1),
    _TxGnGlName_Type()
)
txGnGlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnGlName.setStatus("current")


class _TxGnGlType_Type(DisplayString):
    """Custom type txGnGlType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TxGnGlType_Type.__name__ = "DisplayString"
_TxGnGlType_Object = MibScalar
txGnGlType = _TxGnGlType_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 2),
    _TxGnGlType_Type()
)
txGnGlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnGlType.setStatus("current")


class _TxGnGlStandby_Type(Integer32):
    """Custom type txGnGlStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnGlStandby_Type.__name__ = "Integer32"
_TxGnGlStandby_Object = MibScalar
txGnGlStandby = _TxGnGlStandby_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 3),
    _TxGnGlStandby_Type()
)
txGnGlStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnGlStandby.setStatus("current")


class _TxGnGlLocalMode_Type(Integer32):
    """Custom type txGnGlLocalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2))
    )


_TxGnGlLocalMode_Type.__name__ = "Integer32"
_TxGnGlLocalMode_Object = MibScalar
txGnGlLocalMode = _TxGnGlLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 4),
    _TxGnGlLocalMode_Type()
)
txGnGlLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnGlLocalMode.setStatus("current")


class _TxGnGlReserveType_Type(DisplayString):
    """Custom type txGnGlReserveType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TxGnGlReserveType_Type.__name__ = "DisplayString"
_TxGnGlReserveType_Object = MibScalar
txGnGlReserveType = _TxGnGlReserveType_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 5),
    _TxGnGlReserveType_Type()
)
txGnGlReserveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnGlReserveType.setStatus("current")


class _TxGnGlPcap_Type(Gauge32):
    """Custom type txGnGlPcap based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnGlPcap_Type.__name__ = "Gauge32"
_TxGnGlPcap_Object = MibScalar
txGnGlPcap = _TxGnGlPcap_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 1, 6),
    _TxGnGlPcap_Type()
)
txGnGlPcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnGlPcap.setStatus("current")
if mibBuilder.loadTexts:
    txGnGlPcap.setUnits("W")
_TxGnAlarms_ObjectIdentity = ObjectIdentity
txGnAlarms = _TxGnAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    txGnAlarms.setStatus("current")


class _TxGnAl3dB_Type(Integer32):
    """Custom type txGnAl3dB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnAl3dB_Type.__name__ = "Integer32"
_TxGnAl3dB_Object = MibScalar
txGnAl3dB = _TxGnAl3dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 1),
    _TxGnAl3dB_Type()
)
txGnAl3dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAl3dB.setStatus("current")


class _TxGnAlFault_Type(Integer32):
    """Custom type txGnAlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fault", 1),
          ("off", 2))
    )


_TxGnAlFault_Type.__name__ = "Integer32"
_TxGnAlFault_Object = MibScalar
txGnAlFault = _TxGnAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 2),
    _TxGnAlFault_Type()
)
txGnAlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlFault.setStatus("current")


class _TxGnAlWarning_Type(Integer32):
    """Custom type txGnAlWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnAlWarning_Type.__name__ = "Integer32"
_TxGnAlWarning_Object = MibScalar
txGnAlWarning = _TxGnAlWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 3),
    _TxGnAlWarning_Type()
)
txGnAlWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlWarning.setStatus("current")


class _TxGnAlVSWR_Type(Integer32):
    """Custom type txGnAlVSWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnAlVSWR_Type.__name__ = "Integer32"
_TxGnAlVSWR_Object = MibScalar
txGnAlVSWR = _TxGnAlVSWR_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 4),
    _TxGnAlVSWR_Type()
)
txGnAlVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlVSWR.setStatus("current")


class _TxGnAlInterlockAnt_Type(Integer32):
    """Custom type txGnAlInterlockAnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("close", 1),
          ("open", 2))
    )


_TxGnAlInterlockAnt_Type.__name__ = "Integer32"
_TxGnAlInterlockAnt_Object = MibScalar
txGnAlInterlockAnt = _TxGnAlInterlockAnt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 5),
    _TxGnAlInterlockAnt_Type()
)
txGnAlInterlockAnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlInterlockAnt.setStatus("current")


class _TxGnAlInterlockLoad_Type(Integer32):
    """Custom type txGnAlInterlockLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("close", 1),
          ("open", 2))
    )


_TxGnAlInterlockLoad_Type.__name__ = "Integer32"
_TxGnAlInterlockLoad_Object = MibScalar
txGnAlInterlockLoad = _TxGnAlInterlockLoad_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 6),
    _TxGnAlInterlockLoad_Type()
)
txGnAlInterlockLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlInterlockLoad.setStatus("obsolete")


class _TxGnAlLink_Type(Integer32):
    """Custom type txGnAlLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("open", 1),
          ("close", 2))
    )


_TxGnAlLink_Type.__name__ = "Integer32"
_TxGnAlLink_Object = MibScalar
txGnAlLink = _TxGnAlLink_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 7),
    _TxGnAlLink_Type()
)
txGnAlLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlLink.setStatus("current")


class _TxGnAlVswrTrip_Type(Integer32):
    """Custom type txGnAlVswrTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnAlVswrTrip_Type.__name__ = "Integer32"
_TxGnAlVswrTrip_Object = MibScalar
txGnAlVswrTrip = _TxGnAlVswrTrip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 8),
    _TxGnAlVswrTrip_Type()
)
txGnAlVswrTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAlVswrTrip.setStatus("current")


class _TxGnAl1dB_Type(Integer32):
    """Custom type txGnAl1dB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnAl1dB_Type.__name__ = "Integer32"
_TxGnAl1dB_Object = MibScalar
txGnAl1dB = _TxGnAl1dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 2, 9),
    _TxGnAl1dB_Type()
)
txGnAl1dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnAl1dB.setStatus("current")
_TxGnMeasures_ObjectIdentity = ObjectIdentity
txGnMeasures = _TxGnMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    txGnMeasures.setStatus("current")


class _TxGnMsForwardPower_Type(Gauge32):
    """Custom type txGnMsForwardPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnMsForwardPower_Type.__name__ = "Gauge32"
_TxGnMsForwardPower_Object = MibScalar
txGnMsForwardPower = _TxGnMsForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 3, 1),
    _TxGnMsForwardPower_Type()
)
txGnMsForwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnMsForwardPower.setStatus("current")
if mibBuilder.loadTexts:
    txGnMsForwardPower.setUnits("W")


class _TxGnMsReflectedPower_Type(Gauge32):
    """Custom type txGnMsReflectedPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnMsReflectedPower_Type.__name__ = "Gauge32"
_TxGnMsReflectedPower_Object = MibScalar
txGnMsReflectedPower = _TxGnMsReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 3, 2),
    _TxGnMsReflectedPower_Type()
)
txGnMsReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnMsReflectedPower.setStatus("current")
if mibBuilder.loadTexts:
    txGnMsReflectedPower.setUnits("W/10")


class _TxGnMsVSWR_Type(Gauge32):
    """Custom type txGnMsVSWR based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999),
    )


_TxGnMsVSWR_Type.__name__ = "Gauge32"
_TxGnMsVSWR_Object = MibScalar
txGnMsVSWR = _TxGnMsVSWR_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 3, 3),
    _TxGnMsVSWR_Type()
)
txGnMsVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnMsVSWR.setStatus("current")
if mibBuilder.loadTexts:
    txGnMsVSWR.setUnits("/10")


class _TxGnMsVswrTrip_Type(Gauge32):
    """Custom type txGnMsVswrTrip based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TxGnMsVswrTrip_Type.__name__ = "Gauge32"
_TxGnMsVswrTrip_Object = MibScalar
txGnMsVswrTrip = _TxGnMsVswrTrip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 3, 4),
    _TxGnMsVswrTrip_Type()
)
txGnMsVswrTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnMsVswrTrip.setStatus("current")
_TxGnRf_ObjectIdentity = ObjectIdentity
txGnRf = _TxGnRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    txGnRf.setStatus("current")


class _TxGnRfFrequency_Type(Gauge32):
    """Custom type txGnRfFrequency based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8750, 10800),
    )


_TxGnRfFrequency_Type.__name__ = "Gauge32"
_TxGnRfFrequency_Object = MibScalar
txGnRfFrequency = _TxGnRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 1),
    _TxGnRfFrequency_Type()
)
txGnRfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfFrequency.setUnits("MHz/100")


class _TxGnRfThreshold3dB_Type(Gauge32):
    """Custom type txGnRfThreshold3dB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnRfThreshold3dB_Type.__name__ = "Gauge32"
_TxGnRfThreshold3dB_Object = MibScalar
txGnRfThreshold3dB = _TxGnRfThreshold3dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 2),
    _TxGnRfThreshold3dB_Type()
)
txGnRfThreshold3dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfThreshold3dB.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfThreshold3dB.setUnits("W")


class _TxGnRfAutomatic3dBThreshold_Type(Integer32):
    """Custom type txGnRfAutomatic3dBThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("activate", 1),
          ("deactive", 2))
    )


_TxGnRfAutomatic3dBThreshold_Type.__name__ = "Integer32"
_TxGnRfAutomatic3dBThreshold_Object = MibScalar
txGnRfAutomatic3dBThreshold = _TxGnRfAutomatic3dBThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 3),
    _TxGnRfAutomatic3dBThreshold_Type()
)
txGnRfAutomatic3dBThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfAutomatic3dBThreshold.setStatus("current")


class _TxGnRfThresholdVSWR_Type(Gauge32):
    """Custom type txGnRfThresholdVSWR based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999),
    )


_TxGnRfThresholdVSWR_Type.__name__ = "Gauge32"
_TxGnRfThresholdVSWR_Object = MibScalar
txGnRfThresholdVSWR = _TxGnRfThresholdVSWR_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 4),
    _TxGnRfThresholdVSWR_Type()
)
txGnRfThresholdVSWR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfThresholdVSWR.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfThresholdVSWR.setUnits("/10")


class _TxGnRfOpmode_Type(Integer32):
    """Custom type txGnRfOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnRfOpmode_Type.__name__ = "Integer32"
_TxGnRfOpmode_Object = MibScalar
txGnRfOpmode = _TxGnRfOpmode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 5),
    _TxGnRfOpmode_Type()
)
txGnRfOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfOpmode.setStatus("current")


class _TxGnRfPower_Type(Gauge32):
    """Custom type txGnRfPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnRfPower_Type.__name__ = "Gauge32"
_TxGnRfPower_Object = MibScalar
txGnRfPower = _TxGnRfPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 6),
    _TxGnRfPower_Type()
)
txGnRfPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfPower.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfPower.setUnits("W")


class _TxGnRfRFPresent_Type(Integer32):
    """Custom type txGnRfRFPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnRfRFPresent_Type.__name__ = "Integer32"
_TxGnRfRFPresent_Object = MibScalar
txGnRfRFPresent = _TxGnRfRFPresent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 7),
    _TxGnRfRFPresent_Type()
)
txGnRfRFPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGnRfRFPresent.setStatus("current")


class _TxGnRfVswrTrip_Type(Integer32):
    """Custom type txGnRfVswrTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnRfVswrTrip_Type.__name__ = "Integer32"
_TxGnRfVswrTrip_Object = MibScalar
txGnRfVswrTrip = _TxGnRfVswrTrip_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 8),
    _TxGnRfVswrTrip_Type()
)
txGnRfVswrTrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfVswrTrip.setStatus("current")


class _TxGnRfThreshold1dB_Type(Gauge32):
    """Custom type txGnRfThreshold1dB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnRfThreshold1dB_Type.__name__ = "Gauge32"
_TxGnRfThreshold1dB_Object = MibScalar
txGnRfThreshold1dB = _TxGnRfThreshold1dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 9),
    _TxGnRfThreshold1dB_Type()
)
txGnRfThreshold1dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfThreshold1dB.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfThreshold1dB.setUnits("W")


class _TxGnRfMaxPower_Type(Gauge32):
    """Custom type txGnRfMaxPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnRfMaxPower_Type.__name__ = "Gauge32"
_TxGnRfMaxPower_Object = MibScalar
txGnRfMaxPower = _TxGnRfMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 10),
    _TxGnRfMaxPower_Type()
)
txGnRfMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfMaxPower.setUnits("W")


class _TxGnRfRfPresentMin_Type(Gauge32):
    """Custom type txGnRfRfPresentMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnRfRfPresentMin_Type.__name__ = "Gauge32"
_TxGnRfRfPresentMin_Object = MibScalar
txGnRfRfPresentMin = _TxGnRfRfPresentMin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 11),
    _TxGnRfRfPresentMin_Type()
)
txGnRfRfPresentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfRfPresentMin.setStatus("current")
if mibBuilder.loadTexts:
    txGnRfRfPresentMin.setUnits("W")


class _TxGnRfVswrTrig_Type(Integer32):
    """Custom type txGnRfVswrTrig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("warning", 1),
          ("faultWarn", 2),
          ("fault", 3))
    )


_TxGnRfVswrTrig_Type.__name__ = "Integer32"
_TxGnRfVswrTrig_Object = MibScalar
txGnRfVswrTrig = _TxGnRfVswrTrig_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 4, 12),
    _TxGnRfVswrTrig_Type()
)
txGnRfVswrTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnRfVswrTrig.setStatus("current")
_TxGnPresets_ObjectIdentity = ObjectIdentity
txGnPresets = _TxGnPresets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    txGnPresets.setStatus("current")


class _TxGnPrCurrent_Type(Gauge32):
    """Custom type txGnPrCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TxGnPrCurrent_Type.__name__ = "Gauge32"
_TxGnPrCurrent_Object = MibScalar
txGnPrCurrent = _TxGnPrCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 1),
    _TxGnPrCurrent_Type()
)
txGnPrCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrCurrent.setStatus("current")


class _TxGnPrGpioMode_Type(Integer32):
    """Custom type txGnPrGpioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("input4", 1),
          ("input8", 2),
          ("input6", 3))
    )


_TxGnPrGpioMode_Type.__name__ = "Integer32"
_TxGnPrGpioMode_Object = MibScalar
txGnPrGpioMode = _TxGnPrGpioMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 2),
    _TxGnPrGpioMode_Type()
)
txGnPrGpioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrGpioMode.setStatus("current")
_TxGnPrPresetsTable_Object = MibTable
txGnPrPresetsTable = _TxGnPrPresetsTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    txGnPrPresetsTable.setStatus("current")
_TxGnPrPresetsEntry_Object = MibTableRow
txGnPrPresetsEntry = _TxGnPrPresetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1)
)
txGnPrPresetsEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "txGnPrPresetsIndex"),
)
if mibBuilder.loadTexts:
    txGnPrPresetsEntry.setStatus("current")


class _TxGnPrPresetsIndex_Type(Integer32):
    """Custom type txGnPrPresetsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TxGnPrPresetsIndex_Type.__name__ = "Integer32"
_TxGnPrPresetsIndex_Object = MibTableColumn
txGnPrPresetsIndex = _TxGnPrPresetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 1),
    _TxGnPrPresetsIndex_Type()
)
txGnPrPresetsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txGnPrPresetsIndex.setStatus("current")


class _TxGnPrPresetsFreq_Type(Gauge32):
    """Custom type txGnPrPresetsFreq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8750, 10800),
    )


_TxGnPrPresetsFreq_Type.__name__ = "Gauge32"
_TxGnPrPresetsFreq_Object = MibTableColumn
txGnPrPresetsFreq = _TxGnPrPresetsFreq_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 2),
    _TxGnPrPresetsFreq_Type()
)
txGnPrPresetsFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsFreq.setStatus("current")
if mibBuilder.loadTexts:
    txGnPrPresetsFreq.setUnits("MHz/100")


class _TxGnPrPresetsPower_Type(Gauge32):
    """Custom type txGnPrPresetsPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnPrPresetsPower_Type.__name__ = "Gauge32"
_TxGnPrPresetsPower_Object = MibTableColumn
txGnPrPresetsPower = _TxGnPrPresetsPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 3),
    _TxGnPrPresetsPower_Type()
)
txGnPrPresetsPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsPower.setStatus("current")
if mibBuilder.loadTexts:
    txGnPrPresetsPower.setUnits("W")


class _TxGnPrPresetsName_Type(DisplayString):
    """Custom type txGnPrPresetsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TxGnPrPresetsName_Type.__name__ = "DisplayString"
_TxGnPrPresetsName_Object = MibTableColumn
txGnPrPresetsName = _TxGnPrPresetsName_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 4),
    _TxGnPrPresetsName_Type()
)
txGnPrPresetsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsName.setStatus("current")


class _TxGnPrPresetsThreshold3dB_Type(Gauge32):
    """Custom type txGnPrPresetsThreshold3dB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnPrPresetsThreshold3dB_Type.__name__ = "Gauge32"
_TxGnPrPresetsThreshold3dB_Object = MibTableColumn
txGnPrPresetsThreshold3dB = _TxGnPrPresetsThreshold3dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 5),
    _TxGnPrPresetsThreshold3dB_Type()
)
txGnPrPresetsThreshold3dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsThreshold3dB.setStatus("current")
if mibBuilder.loadTexts:
    txGnPrPresetsThreshold3dB.setUnits("W")


class _TxGnPrPresetsThreshold1dB_Type(Gauge32):
    """Custom type txGnPrPresetsThreshold1dB based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnPrPresetsThreshold1dB_Type.__name__ = "Gauge32"
_TxGnPrPresetsThreshold1dB_Object = MibTableColumn
txGnPrPresetsThreshold1dB = _TxGnPrPresetsThreshold1dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 6),
    _TxGnPrPresetsThreshold1dB_Type()
)
txGnPrPresetsThreshold1dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsThreshold1dB.setStatus("current")
if mibBuilder.loadTexts:
    txGnPrPresetsThreshold1dB.setUnits("W")


class _TxGnPrPresetsRfPresentMin_Type(Gauge32):
    """Custom type txGnPrPresetsRfPresentMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxGnPrPresetsRfPresentMin_Type.__name__ = "Gauge32"
_TxGnPrPresetsRfPresentMin_Object = MibTableColumn
txGnPrPresetsRfPresentMin = _TxGnPrPresetsRfPresentMin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 7),
    _TxGnPrPresetsRfPresentMin_Type()
)
txGnPrPresetsRfPresentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsRfPresentMin.setStatus("current")
if mibBuilder.loadTexts:
    txGnPrPresetsRfPresentMin.setUnits("W")


class _TxGnPrPresetsAuto3dB_Type(Integer32):
    """Custom type txGnPrPresetsAuto3dB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxGnPrPresetsAuto3dB_Type.__name__ = "Integer32"
_TxGnPrPresetsAuto3dB_Object = MibTableColumn
txGnPrPresetsAuto3dB = _TxGnPrPresetsAuto3dB_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 1, 5, 3, 1, 8),
    _TxGnPrPresetsAuto3dB_Type()
)
txGnPrPresetsAuto3dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txGnPrPresetsAuto3dB.setStatus("current")
_TxSmartFm_ObjectIdentity = ObjectIdentity
txSmartFm = _TxSmartFm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    txSmartFm.setStatus("current")
_TxSfMeasurements_ObjectIdentity = ObjectIdentity
txSfMeasurements = _TxSfMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    txSfMeasurements.setStatus("current")


class _TxSfMeRangeMin_Type(Gauge32):
    """Custom type txSfMeRangeMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_TxSfMeRangeMin_Type.__name__ = "Gauge32"
_TxSfMeRangeMin_Object = MibScalar
txSfMeRangeMin = _TxSfMeRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 1),
    _TxSfMeRangeMin_Type()
)
txSfMeRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMeRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    txSfMeRangeMin.setUnits("percent")


class _TxSfMeRangeMax_Type(Gauge32):
    """Custom type txSfMeRangeMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_TxSfMeRangeMax_Type.__name__ = "Gauge32"
_TxSfMeRangeMax_Object = MibScalar
txSfMeRangeMax = _TxSfMeRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 2),
    _TxSfMeRangeMax_Type()
)
txSfMeRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMeRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    txSfMeRangeMax.setUnits("percent")


class _TxSfMeCurrentValue_Type(Gauge32):
    """Custom type txSfMeCurrentValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_TxSfMeCurrentValue_Type.__name__ = "Gauge32"
_TxSfMeCurrentValue_Object = MibScalar
txSfMeCurrentValue = _TxSfMeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 3),
    _TxSfMeCurrentValue_Type()
)
txSfMeCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMeCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    txSfMeCurrentValue.setUnits("percent")


class _TxSfMePwr_Type(Gauge32):
    """Custom type txSfMePwr based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxSfMePwr_Type.__name__ = "Gauge32"
_TxSfMePwr_Object = MibScalar
txSfMePwr = _TxSfMePwr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 4),
    _TxSfMePwr_Type()
)
txSfMePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMePwr.setStatus("current")
if mibBuilder.loadTexts:
    txSfMePwr.setUnits("W")


class _TxSfMeCurSavings_Type(Integer32):
    """Custom type txSfMeCurSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999, 99999),
    )


_TxSfMeCurSavings_Type.__name__ = "Integer32"
_TxSfMeCurSavings_Object = MibScalar
txSfMeCurSavings = _TxSfMeCurSavings_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 5),
    _TxSfMeCurSavings_Type()
)
txSfMeCurSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMeCurSavings.setStatus("current")
if mibBuilder.loadTexts:
    txSfMeCurSavings.setUnits("W")


class _TxSfMeCurBoost_Type(Gauge32):
    """Custom type txSfMeCurBoost based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TxSfMeCurBoost_Type.__name__ = "Gauge32"
_TxSfMeCurBoost_Object = MibScalar
txSfMeCurBoost = _TxSfMeCurBoost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 6),
    _TxSfMeCurBoost_Type()
)
txSfMeCurBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMeCurBoost.setStatus("current")
if mibBuilder.loadTexts:
    txSfMeCurBoost.setUnits("W")


class _TxSfMePcons_Type(Gauge32):
    """Custom type txSfMePcons based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxSfMePcons_Type.__name__ = "Gauge32"
_TxSfMePcons_Object = MibScalar
txSfMePcons = _TxSfMePcons_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 7),
    _TxSfMePcons_Type()
)
txSfMePcons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMePcons.setStatus("current")
if mibBuilder.loadTexts:
    txSfMePcons.setUnits("W")


class _TxSfMePconsNoSfm_Type(Gauge32):
    """Custom type txSfMePconsNoSfm based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_TxSfMePconsNoSfm_Type.__name__ = "Gauge32"
_TxSfMePconsNoSfm_Object = MibScalar
txSfMePconsNoSfm = _TxSfMePconsNoSfm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 1, 8),
    _TxSfMePconsNoSfm_Type()
)
txSfMePconsNoSfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfMePconsNoSfm.setStatus("current")
if mibBuilder.loadTexts:
    txSfMePconsNoSfm.setUnits("W")
_TxSfConfiguration_ObjectIdentity = ObjectIdentity
txSfConfiguration = _TxSfConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    txSfConfiguration.setStatus("current")


class _TxSfCoState_Type(Integer32):
    """Custom type txSfCoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxSfCoState_Type.__name__ = "Integer32"
_TxSfCoState_Object = MibScalar
txSfCoState = _TxSfCoState_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 2, 1),
    _TxSfCoState_Type()
)
txSfCoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txSfCoState.setStatus("current")


class _TxSfCoMode_Type(Integer32):
    """Custom type txSfCoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("strategy1", 1),
          ("strategy2", 2),
          ("strategy3", 3),
          ("strategy4", 4),
          ("strategy5", 5))
    )


_TxSfCoMode_Type.__name__ = "Integer32"
_TxSfCoMode_Object = MibScalar
txSfCoMode = _TxSfCoMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 2, 2),
    _TxSfCoMode_Type()
)
txSfCoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txSfCoMode.setStatus("current")


class _TxSfCoRdsCor_Type(Integer32):
    """Custom type txSfCoRdsCor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxSfCoRdsCor_Type.__name__ = "Integer32"
_TxSfCoRdsCor_Object = MibScalar
txSfCoRdsCor = _TxSfCoRdsCor_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 2, 3),
    _TxSfCoRdsCor_Type()
)
txSfCoRdsCor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txSfCoRdsCor.setStatus("current")


class _TxSfCoKwhCost_Type(Gauge32):
    """Custom type txSfCoKwhCost based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_TxSfCoKwhCost_Type.__name__ = "Gauge32"
_TxSfCoKwhCost_Object = MibScalar
txSfCoKwhCost = _TxSfCoKwhCost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 2, 4),
    _TxSfCoKwhCost_Type()
)
txSfCoKwhCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txSfCoKwhCost.setStatus("current")
if mibBuilder.loadTexts:
    txSfCoKwhCost.setUnits("currency*10000")
_TxSfStatus_ObjectIdentity = ObjectIdentity
txSfStatus = _TxSfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    txSfStatus.setStatus("current")


class _TxSfStAct_Type(Integer32):
    """Custom type txSfStAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxSfStAct_Type.__name__ = "Integer32"
_TxSfStAct_Object = MibScalar
txSfStAct = _TxSfStAct_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 3, 1),
    _TxSfStAct_Type()
)
txSfStAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfStAct.setStatus("current")


class _TxSfStAlarm_Type(Integer32):
    """Custom type txSfStAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_TxSfStAlarm_Type.__name__ = "Integer32"
_TxSfStAlarm_Object = MibScalar
txSfStAlarm = _TxSfStAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 3, 2),
    _TxSfStAlarm_Type()
)
txSfStAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfStAlarm.setStatus("current")
_TxSfLifeTime_ObjectIdentity = ObjectIdentity
txSfLifeTime = _TxSfLifeTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 4)
)
if mibBuilder.loadTexts:
    txSfLifeTime.setStatus("current")


class _TxSfLiSavings_Type(Gauge32):
    """Custom type txSfLiSavings based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TxSfLiSavings_Type.__name__ = "Gauge32"
_TxSfLiSavings_Object = MibScalar
txSfLiSavings = _TxSfLiSavings_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 4, 1),
    _TxSfLiSavings_Type()
)
txSfLiSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfLiSavings.setStatus("current")
if mibBuilder.loadTexts:
    txSfLiSavings.setUnits("Wh")


class _TxSfLiBoost_Type(Gauge32):
    """Custom type txSfLiBoost based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TxSfLiBoost_Type.__name__ = "Gauge32"
_TxSfLiBoost_Object = MibScalar
txSfLiBoost = _TxSfLiBoost_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 4, 2),
    _TxSfLiBoost_Type()
)
txSfLiBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfLiBoost.setStatus("current")
if mibBuilder.loadTexts:
    txSfLiBoost.setUnits("Wh")


class _TxSfLiCredits_Type(Gauge32):
    """Custom type txSfLiCredits based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TxSfLiCredits_Type.__name__ = "Gauge32"
_TxSfLiCredits_Object = MibScalar
txSfLiCredits = _TxSfLiCredits_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 7, 2, 4, 3),
    _TxSfLiCredits_Type()
)
txSfLiCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSfLiCredits.setStatus("current")
_Acu_ObjectIdentity = ObjectIdentity
acu = _Acu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    acu.setStatus("current")
_AcGeneral_ObjectIdentity = ObjectIdentity
acGeneral = _AcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    acGeneral.setStatus("current")
_AcGnGlobal_ObjectIdentity = ObjectIdentity
acGnGlobal = _AcGnGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    acGnGlobal.setStatus("current")


class _AcGnGlDelay_Type(Gauge32):
    """Custom type acGnGlDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcGnGlDelay_Type.__name__ = "Gauge32"
_AcGnGlDelay_Object = MibScalar
acGnGlDelay = _AcGnGlDelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 1),
    _AcGnGlDelay_Type()
)
acGnGlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlDelay.setStatus("current")
if mibBuilder.loadTexts:
    acGnGlDelay.setUnits("s")


class _AcGnGlIterConf_Type(Gauge32):
    """Custom type acGnGlIterConf based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcGnGlIterConf_Type.__name__ = "Gauge32"
_AcGnGlIterConf_Object = MibScalar
acGnGlIterConf = _AcGnGlIterConf_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 2),
    _AcGnGlIterConf_Type()
)
acGnGlIterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlIterConf.setStatus("current")


class _AcGnGlOperation_Type(Integer32):
    """Custom type acGnGlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("manu", 1),
          ("auto", 2))
    )


_AcGnGlOperation_Type.__name__ = "Integer32"
_AcGnGlOperation_Object = MibScalar
acGnGlOperation = _AcGnGlOperation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 3),
    _AcGnGlOperation_Type()
)
acGnGlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlOperation.setStatus("current")


class _AcGnGlPreselection_Type(Integer32):
    """Custom type acGnGlPreselection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tx1", 1),
          ("tx2", 2))
    )


_AcGnGlPreselection_Type.__name__ = "Integer32"
_AcGnGlPreselection_Object = MibScalar
acGnGlPreselection = _AcGnGlPreselection_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 4),
    _AcGnGlPreselection_Type()
)
acGnGlPreselection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlPreselection.setStatus("current")


class _AcGnGlVSWRInhibit_Type(Integer32):
    """Custom type acGnGlVSWRInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlVSWRInhibit_Type.__name__ = "Integer32"
_AcGnGlVSWRInhibit_Object = MibScalar
acGnGlVSWRInhibit = _AcGnGlVSWRInhibit_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 5),
    _AcGnGlVSWRInhibit_Type()
)
acGnGlVSWRInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlVSWRInhibit.setStatus("current")


class _AcGnGlReserveControl_Type(Integer32):
    """Custom type acGnGlReserveControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlReserveControl_Type.__name__ = "Integer32"
_AcGnGlReserveControl_Object = MibScalar
acGnGlReserveControl = _AcGnGlReserveControl_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 6),
    _AcGnGlReserveControl_Type()
)
acGnGlReserveControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlReserveControl.setStatus("current")


class _AcGnGlCurrentMain_Type(Integer32):
    """Custom type acGnGlCurrentMain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tx1", 1),
          ("tx2", 2))
    )


_AcGnGlCurrentMain_Type.__name__ = "Integer32"
_AcGnGlCurrentMain_Object = MibScalar
acGnGlCurrentMain = _AcGnGlCurrentMain_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 7),
    _AcGnGlCurrentMain_Type()
)
acGnGlCurrentMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnGlCurrentMain.setStatus("current")


class _AcGnGlLocalMode_Type(Integer32):
    """Custom type acGnGlLocalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2))
    )


_AcGnGlLocalMode_Type.__name__ = "Integer32"
_AcGnGlLocalMode_Object = MibScalar
acGnGlLocalMode = _AcGnGlLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 8),
    _AcGnGlLocalMode_Type()
)
acGnGlLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnGlLocalMode.setStatus("current")


class _AcGnGlMainOpmode_Type(Integer32):
    """Custom type acGnGlMainOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlMainOpmode_Type.__name__ = "Integer32"
_AcGnGlMainOpmode_Object = MibScalar
acGnGlMainOpmode = _AcGnGlMainOpmode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 9),
    _AcGnGlMainOpmode_Type()
)
acGnGlMainOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlMainOpmode.setStatus("current")


class _AcGnGlManSwLoc_Type(Integer32):
    """Custom type acGnGlManSwLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlManSwLoc_Type.__name__ = "Integer32"
_AcGnGlManSwLoc_Object = MibScalar
acGnGlManSwLoc = _AcGnGlManSwLoc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 10),
    _AcGnGlManSwLoc_Type()
)
acGnGlManSwLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlManSwLoc.setStatus("current")


class _AcGnGlDelaySwitch_Type(Gauge32):
    """Custom type acGnGlDelaySwitch based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcGnGlDelaySwitch_Type.__name__ = "Gauge32"
_AcGnGlDelaySwitch_Object = MibScalar
acGnGlDelaySwitch = _AcGnGlDelaySwitch_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 11),
    _AcGnGlDelaySwitch_Type()
)
acGnGlDelaySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlDelaySwitch.setStatus("current")
if mibBuilder.loadTexts:
    acGnGlDelaySwitch.setUnits("s")


class _AcGnGlDelayStart_Type(Gauge32):
    """Custom type acGnGlDelayStart based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcGnGlDelayStart_Type.__name__ = "Gauge32"
_AcGnGlDelayStart_Object = MibScalar
acGnGlDelayStart = _AcGnGlDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 12),
    _AcGnGlDelayStart_Type()
)
acGnGlDelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlDelayStart.setStatus("current")
if mibBuilder.loadTexts:
    acGnGlDelayStart.setUnits("s")


class _AcGnGlSwOnFault_Type(Integer32):
    """Custom type acGnGlSwOnFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlSwOnFault_Type.__name__ = "Integer32"
_AcGnGlSwOnFault_Object = MibScalar
acGnGlSwOnFault = _AcGnGlSwOnFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 13),
    _AcGnGlSwOnFault_Type()
)
acGnGlSwOnFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlSwOnFault.setStatus("current")


class _AcGnGlSwNoComm_Type(Integer32):
    """Custom type acGnGlSwNoComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnGlSwNoComm_Type.__name__ = "Integer32"
_AcGnGlSwNoComm_Object = MibScalar
acGnGlSwNoComm = _AcGnGlSwNoComm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 1, 14),
    _AcGnGlSwNoComm_Type()
)
acGnGlSwNoComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGnGlSwNoComm.setStatus("current")
_AcGnAlarms_ObjectIdentity = ObjectIdentity
acGnAlarms = _AcGnAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    acGnAlarms.setStatus("current")


class _AcGnAlFault_Type(Integer32):
    """Custom type acGnAlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fault", 1),
          ("off", 2))
    )


_AcGnAlFault_Type.__name__ = "Integer32"
_AcGnAlFault_Object = MibScalar
acGnAlFault = _AcGnAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 2, 1),
    _AcGnAlFault_Type()
)
acGnAlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnAlFault.setStatus("current")


class _AcGnAlSwitchOver_Type(Integer32):
    """Custom type acGnAlSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcGnAlSwitchOver_Type.__name__ = "Integer32"
_AcGnAlSwitchOver_Object = MibScalar
acGnAlSwitchOver = _AcGnAlSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 2, 2),
    _AcGnAlSwitchOver_Type()
)
acGnAlSwitchOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnAlSwitchOver.setStatus("current")


class _AcGnAlInterlockAnt_Type(Integer32):
    """Custom type acGnAlInterlockAnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("close", 1),
          ("open", 2))
    )


_AcGnAlInterlockAnt_Type.__name__ = "Integer32"
_AcGnAlInterlockAnt_Object = MibScalar
acGnAlInterlockAnt = _AcGnAlInterlockAnt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 2, 3),
    _AcGnAlInterlockAnt_Type()
)
acGnAlInterlockAnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnAlInterlockAnt.setStatus("current")


class _AcGnAlInterlockLoad_Type(Integer32):
    """Custom type acGnAlInterlockLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("close", 1),
          ("open", 2))
    )


_AcGnAlInterlockLoad_Type.__name__ = "Integer32"
_AcGnAlInterlockLoad_Object = MibScalar
acGnAlInterlockLoad = _AcGnAlInterlockLoad_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 2, 4),
    _AcGnAlInterlockLoad_Type()
)
acGnAlInterlockLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnAlInterlockLoad.setStatus("current")
_AcGnMeasures_ObjectIdentity = ObjectIdentity
acGnMeasures = _AcGnMeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    acGnMeasures.setStatus("current")


class _AcGnMsIter_Type(Gauge32):
    """Custom type acGnMsIter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcGnMsIter_Type.__name__ = "Gauge32"
_AcGnMsIter_Object = MibScalar
acGnMsIter = _AcGnMsIter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 3, 1),
    _AcGnMsIter_Type()
)
acGnMsIter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnMsIter.setStatus("current")


class _AcGnMsPos_Type(Integer32):
    """Custom type acGnMsPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("pos1", 1),
          ("pos2", 2),
          ("invalid", 3))
    )


_AcGnMsPos_Type.__name__ = "Integer32"
_AcGnMsPos_Object = MibScalar
acGnMsPos = _AcGnMsPos_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 3, 2),
    _AcGnMsPos_Type()
)
acGnMsPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnMsPos.setStatus("current")


class _AcGnMsSwitchLast_Type(DisplayString):
    """Custom type acGnMsSwitchLast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcGnMsSwitchLast_Type.__name__ = "DisplayString"
_AcGnMsSwitchLast_Object = MibScalar
acGnMsSwitchLast = _AcGnMsSwitchLast_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 1, 3, 3),
    _AcGnMsSwitchLast_Type()
)
acGnMsSwitchLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acGnMsSwitchLast.setStatus("current")
_AcTx1_ObjectIdentity = ObjectIdentity
acTx1 = _AcTx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    acTx1.setStatus("current")
_AcTx1Global_ObjectIdentity = ObjectIdentity
acTx1Global = _AcTx1Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    acTx1Global.setStatus("current")


class _AcTx1GlLocalMode_Type(Integer32):
    """Custom type acTx1GlLocalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2))
    )


_AcTx1GlLocalMode_Type.__name__ = "Integer32"
_AcTx1GlLocalMode_Object = MibScalar
acTx1GlLocalMode = _AcTx1GlLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 1, 1),
    _AcTx1GlLocalMode_Type()
)
acTx1GlLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx1GlLocalMode.setStatus("current")
_AcTx1Alarms_ObjectIdentity = ObjectIdentity
acTx1Alarms = _AcTx1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 2)
)
if mibBuilder.loadTexts:
    acTx1Alarms.setStatus("current")


class _AcTx1AlFault_Type(Integer32):
    """Custom type acTx1AlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fault", 1),
          ("off", 2))
    )


_AcTx1AlFault_Type.__name__ = "Integer32"
_AcTx1AlFault_Object = MibScalar
acTx1AlFault = _AcTx1AlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 2, 1),
    _AcTx1AlFault_Type()
)
acTx1AlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx1AlFault.setStatus("current")


class _AcTx1AlWarning_Type(Integer32):
    """Custom type acTx1AlWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcTx1AlWarning_Type.__name__ = "Integer32"
_AcTx1AlWarning_Object = MibScalar
acTx1AlWarning = _AcTx1AlWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 2, 2),
    _AcTx1AlWarning_Type()
)
acTx1AlWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx1AlWarning.setStatus("current")


class _AcTx1AlCom_Type(Integer32):
    """Custom type acTx1AlCom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("failed", 1),
          ("ok", 2))
    )


_AcTx1AlCom_Type.__name__ = "Integer32"
_AcTx1AlCom_Object = MibScalar
acTx1AlCom = _AcTx1AlCom_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 2, 3),
    _AcTx1AlCom_Type()
)
acTx1AlCom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx1AlCom.setStatus("current")
_AcTx1Measures_ObjectIdentity = ObjectIdentity
acTx1Measures = _AcTx1Measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 3)
)
if mibBuilder.loadTexts:
    acTx1Measures.setStatus("current")
_AcTx1Rf_ObjectIdentity = ObjectIdentity
acTx1Rf = _AcTx1Rf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 4)
)
if mibBuilder.loadTexts:
    acTx1Rf.setStatus("current")


class _AcTx1RfRFPresent_Type(Integer32):
    """Custom type acTx1RfRFPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcTx1RfRFPresent_Type.__name__ = "Integer32"
_AcTx1RfRFPresent_Object = MibScalar
acTx1RfRFPresent = _AcTx1RfRFPresent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 2, 4, 1),
    _AcTx1RfRFPresent_Type()
)
acTx1RfRFPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx1RfRFPresent.setStatus("current")
_AcTx2_ObjectIdentity = ObjectIdentity
acTx2 = _AcTx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    acTx2.setStatus("current")
_AcTx2Global_ObjectIdentity = ObjectIdentity
acTx2Global = _AcTx2Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    acTx2Global.setStatus("current")


class _AcTx2GlLocalMode_Type(Integer32):
    """Custom type acTx2GlLocalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2))
    )


_AcTx2GlLocalMode_Type.__name__ = "Integer32"
_AcTx2GlLocalMode_Object = MibScalar
acTx2GlLocalMode = _AcTx2GlLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 1, 1),
    _AcTx2GlLocalMode_Type()
)
acTx2GlLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx2GlLocalMode.setStatus("current")
_AcTx2Alarms_ObjectIdentity = ObjectIdentity
acTx2Alarms = _AcTx2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    acTx2Alarms.setStatus("current")


class _AcTx2AlFault_Type(Integer32):
    """Custom type acTx2AlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fault", 1),
          ("off", 2))
    )


_AcTx2AlFault_Type.__name__ = "Integer32"
_AcTx2AlFault_Object = MibScalar
acTx2AlFault = _AcTx2AlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 2, 1),
    _AcTx2AlFault_Type()
)
acTx2AlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx2AlFault.setStatus("current")


class _AcTx2AlWarning_Type(Integer32):
    """Custom type acTx2AlWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcTx2AlWarning_Type.__name__ = "Integer32"
_AcTx2AlWarning_Object = MibScalar
acTx2AlWarning = _AcTx2AlWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 2, 2),
    _AcTx2AlWarning_Type()
)
acTx2AlWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx2AlWarning.setStatus("current")


class _AcTx2AlCom_Type(Integer32):
    """Custom type acTx2AlCom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("failed", 1),
          ("ok", 2))
    )


_AcTx2AlCom_Type.__name__ = "Integer32"
_AcTx2AlCom_Object = MibScalar
acTx2AlCom = _AcTx2AlCom_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 2, 3),
    _AcTx2AlCom_Type()
)
acTx2AlCom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx2AlCom.setStatus("current")
_AcTx2Measures_ObjectIdentity = ObjectIdentity
acTx2Measures = _AcTx2Measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    acTx2Measures.setStatus("current")
_AcTx2Rf_ObjectIdentity = ObjectIdentity
acTx2Rf = _AcTx2Rf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    acTx2Rf.setStatus("current")


class _AcTx2RfRFPresent_Type(Integer32):
    """Custom type acTx2RfRFPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_AcTx2RfRFPresent_Type.__name__ = "Integer32"
_AcTx2RfRFPresent_Object = MibScalar
acTx2RfRFPresent = _AcTx2RfRFPresent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 8, 3, 4, 1),
    _AcTx2RfRFPresent_Type()
)
acTx2RfRFPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTx2RfRFPresent.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    sys.setStatus("current")
_SyGeneral_ObjectIdentity = ObjectIdentity
syGeneral = _SyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    syGeneral.setStatus("current")


class _SyGeType_Type(DisplayString):
    """Custom type syGeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeType_Type.__name__ = "DisplayString"
_SyGeType_Object = MibScalar
syGeType = _SyGeType_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 1),
    _SyGeType_Type()
)
syGeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeType.setStatus("current")


class _SyGeDate_Type(DisplayString):
    """Custom type syGeDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SyGeDate_Type.__name__ = "DisplayString"
_SyGeDate_Object = MibScalar
syGeDate = _SyGeDate_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 2),
    _SyGeDate_Type()
)
syGeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeDate.setStatus("current")


class _SyGeTime_Type(DisplayString):
    """Custom type syGeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeTime_Type.__name__ = "DisplayString"
_SyGeTime_Object = MibScalar
syGeTime = _SyGeTime_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 3),
    _SyGeTime_Type()
)
syGeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeTime.setStatus("current")


class _SyGeName_Type(DisplayString):
    """Custom type syGeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SyGeName_Type.__name__ = "DisplayString"
_SyGeName_Object = MibScalar
syGeName = _SyGeName_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 4),
    _SyGeName_Type()
)
syGeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeName.setStatus("current")


class _SyGeHardRel_Type(DisplayString):
    """Custom type syGeHardRel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeHardRel_Type.__name__ = "DisplayString"
_SyGeHardRel_Object = MibScalar
syGeHardRel = _SyGeHardRel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 5),
    _SyGeHardRel_Type()
)
syGeHardRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeHardRel.setStatus("current")


class _SyGeSoftRel_Type(DisplayString):
    """Custom type syGeSoftRel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeSoftRel_Type.__name__ = "DisplayString"
_SyGeSoftRel_Object = MibScalar
syGeSoftRel = _SyGeSoftRel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 6),
    _SyGeSoftRel_Type()
)
syGeSoftRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeSoftRel.setStatus("current")


class _SyGeDateCode_Type(DisplayString):
    """Custom type syGeDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeDateCode_Type.__name__ = "DisplayString"
_SyGeDateCode_Object = MibScalar
syGeDateCode = _SyGeDateCode_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 7),
    _SyGeDateCode_Type()
)
syGeDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeDateCode.setStatus("current")


class _SyGeSerial_Type(DisplayString):
    """Custom type syGeSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SyGeSerial_Type.__name__ = "DisplayString"
_SyGeSerial_Object = MibScalar
syGeSerial = _SyGeSerial_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 8),
    _SyGeSerial_Type()
)
syGeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeSerial.setStatus("current")


class _SyGeUptime_Type(Gauge32):
    """Custom type syGeUptime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyGeUptime_Type.__name__ = "Gauge32"
_SyGeUptime_Object = MibScalar
syGeUptime = _SyGeUptime_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 9),
    _SyGeUptime_Type()
)
syGeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeUptime.setStatus("current")


class _SyGeOptList_Type(DisplayString):
    """Custom type syGeOptList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SyGeOptList_Type.__name__ = "DisplayString"
_SyGeOptList_Object = MibScalar
syGeOptList = _SyGeOptList_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 10),
    _SyGeOptList_Type()
)
syGeOptList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeOptList.setStatus("current")


class _SyGeLocation_Type(DisplayString):
    """Custom type syGeLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SyGeLocation_Type.__name__ = "DisplayString"
_SyGeLocation_Object = MibScalar
syGeLocation = _SyGeLocation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 11),
    _SyGeLocation_Type()
)
syGeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeLocation.setStatus("current")


class _SyGeContact_Type(DisplayString):
    """Custom type syGeContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SyGeContact_Type.__name__ = "DisplayString"
_SyGeContact_Object = MibScalar
syGeContact = _SyGeContact_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 12),
    _SyGeContact_Type()
)
syGeContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeContact.setStatus("current")


class _SyGeUnit_Type(Integer32):
    """Custom type syGeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("absolute", 1),
          ("relative", 2))
    )


_SyGeUnit_Type.__name__ = "Integer32"
_SyGeUnit_Object = MibScalar
syGeUnit = _SyGeUnit_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 13),
    _SyGeUnit_Type()
)
syGeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeUnit.setStatus("current")
_SyGeTrapCounter_Type = Gauge32
_SyGeTrapCounter_Object = MibScalar
syGeTrapCounter = _SyGeTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 14),
    _SyGeTrapCounter_Type()
)
syGeTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeTrapCounter.setStatus("current")


class _SyGeDigMPX_Type(Integer32):
    """Custom type syGeDigMPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_SyGeDigMPX_Type.__name__ = "Integer32"
_SyGeDigMPX_Object = MibScalar
syGeDigMPX = _SyGeDigMPX_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 15),
    _SyGeDigMPX_Type()
)
syGeDigMPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeDigMPX.setStatus("current")


class _SyGeDigMPX2_Type(Integer32):
    """Custom type syGeDigMPX2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_SyGeDigMPX2_Type.__name__ = "Integer32"
_SyGeDigMPX2_Object = MibScalar
syGeDigMPX2 = _SyGeDigMPX2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 16),
    _SyGeDigMPX2_Type()
)
syGeDigMPX2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeDigMPX2.setStatus("current")


class _SyGeDigMPX3_Type(Integer32):
    """Custom type syGeDigMPX3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_SyGeDigMPX3_Type.__name__ = "Integer32"
_SyGeDigMPX3_Object = MibScalar
syGeDigMPX3 = _SyGeDigMPX3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 17),
    _SyGeDigMPX3_Type()
)
syGeDigMPX3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syGeDigMPX3.setStatus("current")


class _SyGeAOIPMpx_Type(Integer32):
    """Custom type syGeAOIPMpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )


_SyGeAOIPMpx_Type.__name__ = "Integer32"
_SyGeAOIPMpx_Object = MibScalar
syGeAOIPMpx = _SyGeAOIPMpx_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 1, 18),
    _SyGeAOIPMpx_Type()
)
syGeAOIPMpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syGeAOIPMpx.setStatus("current")
_SyAlarms_ObjectIdentity = ObjectIdentity
syAlarms = _SyAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    syAlarms.setStatus("current")


class _SyAlWarning_Type(Integer32):
    """Custom type syAlWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlWarning_Type.__name__ = "Integer32"
_SyAlWarning_Object = MibScalar
syAlWarning = _SyAlWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 1),
    _SyAlWarning_Type()
)
syAlWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlWarning.setStatus("current")


class _SyAlFault_Type(Integer32):
    """Custom type syAlFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlFault_Type.__name__ = "Integer32"
_SyAlFault_Object = MibScalar
syAlFault = _SyAlFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 2),
    _SyAlFault_Type()
)
syAlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlFault.setStatus("current")


class _SyAlAmb_Type(Integer32):
    """Custom type syAlAmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlAmb_Type.__name__ = "Integer32"
_SyAlAmb_Object = MibScalar
syAlAmb = _SyAlAmb_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 3),
    _SyAlAmb_Type()
)
syAlAmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlAmb.setStatus("current")


class _SyAlVoltAux_Type(Integer32):
    """Custom type syAlVoltAux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlVoltAux_Type.__name__ = "Integer32"
_SyAlVoltAux_Object = MibScalar
syAlVoltAux = _SyAlVoltAux_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 4),
    _SyAlVoltAux_Type()
)
syAlVoltAux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlVoltAux.setStatus("current")


class _SyAlRelay_Type(Integer32):
    """Custom type syAlRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlRelay_Type.__name__ = "Integer32"
_SyAlRelay_Object = MibScalar
syAlRelay = _SyAlRelay_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 5),
    _SyAlRelay_Type()
)
syAlRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlRelay.setStatus("current")


class _SyAlReserve_Type(Integer32):
    """Custom type syAlReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlReserve_Type.__name__ = "Integer32"
_SyAlReserve_Object = MibScalar
syAlReserve = _SyAlReserve_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 6),
    _SyAlReserve_Type()
)
syAlReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlReserve.setStatus("current")


class _SyAlInvalidData_Type(Integer32):
    """Custom type syAlInvalidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlInvalidData_Type.__name__ = "Integer32"
_SyAlInvalidData_Object = MibScalar
syAlInvalidData = _SyAlInvalidData_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 7),
    _SyAlInvalidData_Type()
)
syAlInvalidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlInvalidData.setStatus("current")


class _SyAl24v_Type(Integer32):
    """Custom type syAl24v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAl24v_Type.__name__ = "Integer32"
_SyAl24v_Object = MibScalar
syAl24v = _SyAl24v_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 8),
    _SyAl24v_Type()
)
syAl24v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAl24v.setStatus("current")


class _SyAlComm_Type(Integer32):
    """Custom type syAlComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlComm_Type.__name__ = "Integer32"
_SyAlComm_Object = MibScalar
syAlComm = _SyAlComm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 9),
    _SyAlComm_Type()
)
syAlComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlComm.setStatus("current")


class _SyAlLogging_Type(Integer32):
    """Custom type syAlLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyAlLogging_Type.__name__ = "Integer32"
_SyAlLogging_Object = MibScalar
syAlLogging = _SyAlLogging_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 10),
    _SyAlLogging_Type()
)
syAlLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syAlLogging.setStatus("current")


class _SyLossOfEth0_Type(Integer32):
    """Custom type syLossOfEth0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLossOfEth0_Type.__name__ = "Integer32"
_SyLossOfEth0_Object = MibScalar
syLossOfEth0 = _SyLossOfEth0_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 11),
    _SyLossOfEth0_Type()
)
syLossOfEth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLossOfEth0.setStatus("current")


class _SyLossOfEth1_Type(Integer32):
    """Custom type syLossOfEth1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLossOfEth1_Type.__name__ = "Integer32"
_SyLossOfEth1_Object = MibScalar
syLossOfEth1 = _SyLossOfEth1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 2, 12),
    _SyLossOfEth1_Type()
)
syLossOfEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLossOfEth1.setStatus("current")
_SyNetwork_ObjectIdentity = ObjectIdentity
syNetwork = _SyNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    syNetwork.setStatus("current")
_SyPorts_ObjectIdentity = ObjectIdentity
syPorts = _SyPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    syPorts.setStatus("current")
_SyLicenses_ObjectIdentity = ObjectIdentity
syLicenses = _SyLicenses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    syLicenses.setStatus("current")
_SyLiPresence_ObjectIdentity = ObjectIdentity
syLiPresence = _SyLiPresence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    syLiPresence.setStatus("current")


class _SyLiPrRds_Type(Integer32):
    """Custom type syLiPrRds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrRds_Type.__name__ = "Integer32"
_SyLiPrRds_Object = MibScalar
syLiPrRds = _SyLiPrRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 1),
    _SyLiPrRds_Type()
)
syLiPrRds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrRds.setStatus("current")


class _SyLiPrSoundProc_Type(Integer32):
    """Custom type syLiPrSoundProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrSoundProc_Type.__name__ = "Integer32"
_SyLiPrSoundProc_Object = MibScalar
syLiPrSoundProc = _SyLiPrSoundProc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 2),
    _SyLiPrSoundProc_Type()
)
syLiPrSoundProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrSoundProc.setStatus("current")


class _SyLiPrSfm_Type(Integer32):
    """Custom type syLiPrSfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrSfm_Type.__name__ = "Integer32"
_SyLiPrSfm_Object = MibScalar
syLiPrSfm = _SyLiPrSfm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 3),
    _SyLiPrSfm_Type()
)
syLiPrSfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrSfm.setStatus("current")


class _SyLiPrActivation_Type(Integer32):
    """Custom type syLiPrActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrActivation_Type.__name__ = "Integer32"
_SyLiPrActivation_Object = MibScalar
syLiPrActivation = _SyLiPrActivation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 4),
    _SyLiPrActivation_Type()
)
syLiPrActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrActivation.setStatus("current")


class _SyLiPrAoipdecoder_Type(Integer32):
    """Custom type syLiPrAoipdecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrAoipdecoder_Type.__name__ = "Integer32"
_SyLiPrAoipdecoder_Object = MibScalar
syLiPrAoipdecoder = _SyLiPrAoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 5),
    _SyLiPrAoipdecoder_Type()
)
syLiPrAoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrAoipdecoder.setStatus("current")


class _SyLiPrMpxoipdecoder_Type(Integer32):
    """Custom type syLiPrMpxoipdecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrMpxoipdecoder_Type.__name__ = "Integer32"
_SyLiPrMpxoipdecoder_Object = MibScalar
syLiPrMpxoipdecoder = _SyLiPrMpxoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 6),
    _SyLiPrMpxoipdecoder_Type()
)
syLiPrMpxoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrMpxoipdecoder.setStatus("current")


class _SyLiPrSurestream_Type(Integer32):
    """Custom type syLiPrSurestream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrSurestream_Type.__name__ = "Integer32"
_SyLiPrSurestream_Object = MibScalar
syLiPrSurestream = _SyLiPrSurestream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 7),
    _SyLiPrSurestream_Type()
)
syLiPrSurestream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrSurestream.setStatus("current")


class _SyLiPrSynchrostream_Type(Integer32):
    """Custom type syLiPrSynchrostream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notPresent", 1),
          ("temporary", 2),
          ("definitive", 3))
    )


_SyLiPrSynchrostream_Type.__name__ = "Integer32"
_SyLiPrSynchrostream_Object = MibScalar
syLiPrSynchrostream = _SyLiPrSynchrostream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 1, 8),
    _SyLiPrSynchrostream_Type()
)
syLiPrSynchrostream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiPrSynchrostream.setStatus("current")
_SyLiRemaining_ObjectIdentity = ObjectIdentity
syLiRemaining = _SyLiRemaining_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    syLiRemaining.setStatus("current")


class _SyLiReRds_Type(Gauge32):
    """Custom type syLiReRds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReRds_Type.__name__ = "Gauge32"
_SyLiReRds_Object = MibScalar
syLiReRds = _SyLiReRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 1),
    _SyLiReRds_Type()
)
syLiReRds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReRds.setStatus("current")


class _SyLiReSoundProc_Type(Gauge32):
    """Custom type syLiReSoundProc based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReSoundProc_Type.__name__ = "Gauge32"
_SyLiReSoundProc_Object = MibScalar
syLiReSoundProc = _SyLiReSoundProc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 2),
    _SyLiReSoundProc_Type()
)
syLiReSoundProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReSoundProc.setStatus("current")


class _SyLiReSfm_Type(Gauge32):
    """Custom type syLiReSfm based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReSfm_Type.__name__ = "Gauge32"
_SyLiReSfm_Object = MibScalar
syLiReSfm = _SyLiReSfm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 3),
    _SyLiReSfm_Type()
)
syLiReSfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReSfm.setStatus("current")


class _SyLiReActivation_Type(Gauge32):
    """Custom type syLiReActivation based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReActivation_Type.__name__ = "Gauge32"
_SyLiReActivation_Object = MibScalar
syLiReActivation = _SyLiReActivation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 4),
    _SyLiReActivation_Type()
)
syLiReActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReActivation.setStatus("current")


class _SyLiReAoipdecoder_Type(Gauge32):
    """Custom type syLiReAoipdecoder based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReAoipdecoder_Type.__name__ = "Gauge32"
_SyLiReAoipdecoder_Object = MibScalar
syLiReAoipdecoder = _SyLiReAoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 5),
    _SyLiReAoipdecoder_Type()
)
syLiReAoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReAoipdecoder.setStatus("current")


class _SyLiReMpxoipdecoder_Type(Gauge32):
    """Custom type syLiReMpxoipdecoder based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReMpxoipdecoder_Type.__name__ = "Gauge32"
_SyLiReMpxoipdecoder_Object = MibScalar
syLiReMpxoipdecoder = _SyLiReMpxoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 6),
    _SyLiReMpxoipdecoder_Type()
)
syLiReMpxoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReMpxoipdecoder.setStatus("current")


class _SyLiReSurestream_Type(Gauge32):
    """Custom type syLiReSurestream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReSurestream_Type.__name__ = "Gauge32"
_SyLiReSurestream_Object = MibScalar
syLiReSurestream = _SyLiReSurestream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 7),
    _SyLiReSurestream_Type()
)
syLiReSurestream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReSurestream.setStatus("current")


class _SyLiReSynchrostream_Type(Gauge32):
    """Custom type syLiReSynchrostream based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SyLiReSynchrostream_Type.__name__ = "Gauge32"
_SyLiReSynchrostream_Object = MibScalar
syLiReSynchrostream = _SyLiReSynchrostream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 2, 8),
    _SyLiReSynchrostream_Type()
)
syLiReSynchrostream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiReSynchrostream.setStatus("current")
_SyLiAlarms_ObjectIdentity = ObjectIdentity
syLiAlarms = _SyLiAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3)
)
if mibBuilder.loadTexts:
    syLiAlarms.setStatus("current")


class _SyLiAlRds_Type(Integer32):
    """Custom type syLiAlRds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlRds_Type.__name__ = "Integer32"
_SyLiAlRds_Object = MibScalar
syLiAlRds = _SyLiAlRds_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 1),
    _SyLiAlRds_Type()
)
syLiAlRds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlRds.setStatus("current")


class _SyLiAlSoundProc_Type(Integer32):
    """Custom type syLiAlSoundProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlSoundProc_Type.__name__ = "Integer32"
_SyLiAlSoundProc_Object = MibScalar
syLiAlSoundProc = _SyLiAlSoundProc_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 2),
    _SyLiAlSoundProc_Type()
)
syLiAlSoundProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlSoundProc.setStatus("current")


class _SyLiAlSfm_Type(Integer32):
    """Custom type syLiAlSfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlSfm_Type.__name__ = "Integer32"
_SyLiAlSfm_Object = MibScalar
syLiAlSfm = _SyLiAlSfm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 3),
    _SyLiAlSfm_Type()
)
syLiAlSfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlSfm.setStatus("current")


class _SyLiAlActivation_Type(Integer32):
    """Custom type syLiAlActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlActivation_Type.__name__ = "Integer32"
_SyLiAlActivation_Object = MibScalar
syLiAlActivation = _SyLiAlActivation_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 4),
    _SyLiAlActivation_Type()
)
syLiAlActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlActivation.setStatus("current")


class _SyLiAlAoipdecoder_Type(Integer32):
    """Custom type syLiAlAoipdecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlAoipdecoder_Type.__name__ = "Integer32"
_SyLiAlAoipdecoder_Object = MibScalar
syLiAlAoipdecoder = _SyLiAlAoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 5),
    _SyLiAlAoipdecoder_Type()
)
syLiAlAoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlAoipdecoder.setStatus("current")


class _SyLiAlMpxoipdecoder_Type(Integer32):
    """Custom type syLiAlMpxoipdecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlMpxoipdecoder_Type.__name__ = "Integer32"
_SyLiAlMpxoipdecoder_Object = MibScalar
syLiAlMpxoipdecoder = _SyLiAlMpxoipdecoder_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 6),
    _SyLiAlMpxoipdecoder_Type()
)
syLiAlMpxoipdecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlMpxoipdecoder.setStatus("current")


class _SyLiAlSurestream_Type(Integer32):
    """Custom type syLiAlSurestream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlSurestream_Type.__name__ = "Integer32"
_SyLiAlSurestream_Object = MibScalar
syLiAlSurestream = _SyLiAlSurestream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 7),
    _SyLiAlSurestream_Type()
)
syLiAlSurestream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlSurestream.setStatus("current")


class _SyLiAlSynchrostream_Type(Integer32):
    """Custom type syLiAlSynchrostream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_SyLiAlSynchrostream_Type.__name__ = "Integer32"
_SyLiAlSynchrostream_Object = MibScalar
syLiAlSynchrostream = _SyLiAlSynchrostream_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 9, 5, 3, 8),
    _SyLiAlSynchrostream_Type()
)
syLiAlSynchrostream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syLiAlSynchrostream.setStatus("current")
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10)
)
if mibBuilder.loadTexts:
    monitoring.setStatus("obsolete")
_MoMain_ObjectIdentity = ObjectIdentity
moMain = _MoMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    moMain.setStatus("obsolete")
_MoMaMeas_ObjectIdentity = ObjectIdentity
moMaMeas = _MoMaMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    moMaMeas.setStatus("obsolete")


class _MoMaMeVolt1_Type(Gauge32):
    """Custom type moMaMeVolt1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoMaMeVolt1_Type.__name__ = "Gauge32"
_MoMaMeVolt1_Object = MibScalar
moMaMeVolt1 = _MoMaMeVolt1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 1),
    _MoMaMeVolt1_Type()
)
moMaMeVolt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeVolt1.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeVolt1.setUnits("V/10")


class _MoMaMeVolt2_Type(Gauge32):
    """Custom type moMaMeVolt2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoMaMeVolt2_Type.__name__ = "Gauge32"
_MoMaMeVolt2_Object = MibScalar
moMaMeVolt2 = _MoMaMeVolt2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 2),
    _MoMaMeVolt2_Type()
)
moMaMeVolt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeVolt2.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeVolt2.setUnits("V/10")


class _MoMaMeCur1_Type(Gauge32):
    """Custom type moMaMeCur1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoMaMeCur1_Type.__name__ = "Gauge32"
_MoMaMeCur1_Object = MibScalar
moMaMeCur1 = _MoMaMeCur1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 3),
    _MoMaMeCur1_Type()
)
moMaMeCur1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeCur1.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeCur1.setUnits("A/10")


class _MoMaMeCur2_Type(Gauge32):
    """Custom type moMaMeCur2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoMaMeCur2_Type.__name__ = "Gauge32"
_MoMaMeCur2_Object = MibScalar
moMaMeCur2 = _MoMaMeCur2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 4),
    _MoMaMeCur2_Type()
)
moMaMeCur2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeCur2.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeCur2.setUnits("A/10")


class _MoMaMeEffSys_Type(Gauge32):
    """Custom type moMaMeEffSys based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MoMaMeEffSys_Type.__name__ = "Gauge32"
_MoMaMeEffSys_Object = MibScalar
moMaMeEffSys = _MoMaMeEffSys_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 5),
    _MoMaMeEffSys_Type()
)
moMaMeEffSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeEffSys.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeEffSys.setUnits("percent")


class _MoMaMeEffTrans_Type(Gauge32):
    """Custom type moMaMeEffTrans based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MoMaMeEffTrans_Type.__name__ = "Gauge32"
_MoMaMeEffTrans_Object = MibScalar
moMaMeEffTrans = _MoMaMeEffTrans_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 6),
    _MoMaMeEffTrans_Type()
)
moMaMeEffTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMeEffTrans.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMeEffTrans.setUnits("percent")


class _MoMaMePin_Type(Gauge32):
    """Custom type moMaMePin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoMaMePin_Type.__name__ = "Gauge32"
_MoMaMePin_Object = MibScalar
moMaMePin = _MoMaMePin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 1, 7),
    _MoMaMePin_Type()
)
moMaMePin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMaMePin.setStatus("obsolete")
if mibBuilder.loadTexts:
    moMaMePin.setUnits("W/10")
_MoMaAlarms_ObjectIdentity = ObjectIdentity
moMaAlarms = _MoMaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    moMaAlarms.setStatus("obsolete")


class _MoMainAlVolt1_Type(Integer32):
    """Custom type moMainAlVolt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoMainAlVolt1_Type.__name__ = "Integer32"
_MoMainAlVolt1_Object = MibScalar
moMainAlVolt1 = _MoMainAlVolt1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2, 1),
    _MoMainAlVolt1_Type()
)
moMainAlVolt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMainAlVolt1.setStatus("obsolete")


class _MoMainAlVolt2_Type(Integer32):
    """Custom type moMainAlVolt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoMainAlVolt2_Type.__name__ = "Integer32"
_MoMainAlVolt2_Object = MibScalar
moMainAlVolt2 = _MoMainAlVolt2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2, 2),
    _MoMainAlVolt2_Type()
)
moMainAlVolt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMainAlVolt2.setStatus("obsolete")


class _MoMainAlCur1_Type(Integer32):
    """Custom type moMainAlCur1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoMainAlCur1_Type.__name__ = "Integer32"
_MoMainAlCur1_Object = MibScalar
moMainAlCur1 = _MoMainAlCur1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2, 3),
    _MoMainAlCur1_Type()
)
moMainAlCur1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMainAlCur1.setStatus("obsolete")


class _MoMainAlCur2_Type(Integer32):
    """Custom type moMainAlCur2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoMainAlCur2_Type.__name__ = "Integer32"
_MoMainAlCur2_Object = MibScalar
moMainAlCur2 = _MoMainAlCur2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2, 4),
    _MoMainAlCur2_Type()
)
moMainAlCur2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMainAlCur2.setStatus("obsolete")


class _MoMainAlPin_Type(Integer32):
    """Custom type moMainAlPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoMainAlPin_Type.__name__ = "Integer32"
_MoMainAlPin_Object = MibScalar
moMainAlPin = _MoMainAlPin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 1, 2, 5),
    _MoMainAlPin_Type()
)
moMainAlPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moMainAlPin.setStatus("obsolete")
_MoConditions_ObjectIdentity = ObjectIdentity
moConditions = _MoConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    moConditions.setStatus("obsolete")
_MoCoMeas_ObjectIdentity = ObjectIdentity
moCoMeas = _MoCoMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    moCoMeas.setStatus("obsolete")


class _MoCoMeAmb_Type(Integer32):
    """Custom type moCoMeAmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MoCoMeAmb_Type.__name__ = "Integer32"
_MoCoMeAmb_Object = MibScalar
moCoMeAmb = _MoCoMeAmb_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 1),
    _MoCoMeAmb_Type()
)
moCoMeAmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMeAmb.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMeAmb.setUnits("Celsius Degrees")


class _MoCoMeHeat1_Type(Integer32):
    """Custom type moCoMeHeat1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MoCoMeHeat1_Type.__name__ = "Integer32"
_MoCoMeHeat1_Object = MibScalar
moCoMeHeat1 = _MoCoMeHeat1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 2),
    _MoCoMeHeat1_Type()
)
moCoMeHeat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMeHeat1.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMeHeat1.setUnits("Celsius Degrees")


class _MoCoMeHeat2_Type(Integer32):
    """Custom type moCoMeHeat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MoCoMeHeat2_Type.__name__ = "Integer32"
_MoCoMeHeat2_Object = MibScalar
moCoMeHeat2 = _MoCoMeHeat2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 3),
    _MoCoMeHeat2_Type()
)
moCoMeHeat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMeHeat2.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMeHeat2.setUnits("Celsius Degrees")


class _MoCoMePsuTemp_Type(Integer32):
    """Custom type moCoMePsuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MoCoMePsuTemp_Type.__name__ = "Integer32"
_MoCoMePsuTemp_Object = MibScalar
moCoMePsuTemp = _MoCoMePsuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 4),
    _MoCoMePsuTemp_Type()
)
moCoMePsuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMePsuTemp.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMePsuTemp.setUnits("Celsius Degrees")


class _MoCoMeIntTemp_Type(Gauge32):
    """Custom type moCoMeIntTemp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MoCoMeIntTemp_Type.__name__ = "Gauge32"
_MoCoMeIntTemp_Object = MibScalar
moCoMeIntTemp = _MoCoMeIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 5),
    _MoCoMeIntTemp_Type()
)
moCoMeIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMeIntTemp.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMeIntTemp.setUnits("Celsius Degrees")


class _MoCoMePressure_Type(Gauge32):
    """Custom type moCoMePressure based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_MoCoMePressure_Type.__name__ = "Gauge32"
_MoCoMePressure_Object = MibScalar
moCoMePressure = _MoCoMePressure_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 6),
    _MoCoMePressure_Type()
)
moCoMePressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMePressure.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMePressure.setUnits("hPa")


class _MoCoMeExcTemp_Type(Integer32):
    """Custom type moCoMeExcTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MoCoMeExcTemp_Type.__name__ = "Integer32"
_MoCoMeExcTemp_Object = MibScalar
moCoMeExcTemp = _MoCoMeExcTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 1, 7),
    _MoCoMeExcTemp_Type()
)
moCoMeExcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoMeExcTemp.setStatus("obsolete")
if mibBuilder.loadTexts:
    moCoMeExcTemp.setUnits("Celsius Degrees")
_MoCoAlarms_ObjectIdentity = ObjectIdentity
moCoAlarms = _MoCoAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2)
)
if mibBuilder.loadTexts:
    moCoAlarms.setStatus("obsolete")


class _MoCoAlHeat1_Type(Integer32):
    """Custom type moCoAlHeat1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlHeat1_Type.__name__ = "Integer32"
_MoCoAlHeat1_Object = MibScalar
moCoAlHeat1 = _MoCoAlHeat1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 1),
    _MoCoAlHeat1_Type()
)
moCoAlHeat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlHeat1.setStatus("obsolete")


class _MoCoAlHeat2_Type(Integer32):
    """Custom type moCoAlHeat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlHeat2_Type.__name__ = "Integer32"
_MoCoAlHeat2_Object = MibScalar
moCoAlHeat2 = _MoCoAlHeat2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 2),
    _MoCoAlHeat2_Type()
)
moCoAlHeat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlHeat2.setStatus("obsolete")


class _MoCoAlTemp1_Type(Integer32):
    """Custom type moCoAlTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlTemp1_Type.__name__ = "Integer32"
_MoCoAlTemp1_Object = MibScalar
moCoAlTemp1 = _MoCoAlTemp1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 3),
    _MoCoAlTemp1_Type()
)
moCoAlTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlTemp1.setStatus("obsolete")


class _MoCoAlTemp2_Type(Integer32):
    """Custom type moCoAlTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlTemp2_Type.__name__ = "Integer32"
_MoCoAlTemp2_Object = MibScalar
moCoAlTemp2 = _MoCoAlTemp2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 4),
    _MoCoAlTemp2_Type()
)
moCoAlTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlTemp2.setStatus("obsolete")


class _MoCoAlPsuTemp_Type(Integer32):
    """Custom type moCoAlPsuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlPsuTemp_Type.__name__ = "Integer32"
_MoCoAlPsuTemp_Object = MibScalar
moCoAlPsuTemp = _MoCoAlPsuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 5),
    _MoCoAlPsuTemp_Type()
)
moCoAlPsuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlPsuTemp.setStatus("obsolete")


class _MoCoAlIntTemp_Type(Integer32):
    """Custom type moCoAlIntTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlIntTemp_Type.__name__ = "Integer32"
_MoCoAlIntTemp_Object = MibScalar
moCoAlIntTemp = _MoCoAlIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 6),
    _MoCoAlIntTemp_Type()
)
moCoAlIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlIntTemp.setStatus("obsolete")


class _MoCoAlExcTemp_Type(Integer32):
    """Custom type moCoAlExcTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlExcTemp_Type.__name__ = "Integer32"
_MoCoAlExcTemp_Object = MibScalar
moCoAlExcTemp = _MoCoAlExcTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 7),
    _MoCoAlExcTemp_Type()
)
moCoAlExcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlExcTemp.setStatus("obsolete")


class _MoCoAlPressure_Type(Integer32):
    """Custom type moCoAlPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoCoAlPressure_Type.__name__ = "Integer32"
_MoCoAlPressure_Object = MibScalar
moCoAlPressure = _MoCoAlPressure_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 2, 2, 8),
    _MoCoAlPressure_Type()
)
moCoAlPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moCoAlPressure.setStatus("obsolete")
_MoAuxVolt_ObjectIdentity = ObjectIdentity
moAuxVolt = _MoAuxVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    moAuxVolt.setStatus("obsolete")
_MoAuMeas_ObjectIdentity = ObjectIdentity
moAuMeas = _MoAuMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    moAuMeas.setStatus("obsolete")


class _MoAuMe5V_Type(Gauge32):
    """Custom type moAuMe5V based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MoAuMe5V_Type.__name__ = "Gauge32"
_MoAuMe5V_Object = MibScalar
moAuMe5V = _MoAuMe5V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3, 1, 1),
    _MoAuMe5V_Type()
)
moAuMe5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moAuMe5V.setStatus("obsolete")
if mibBuilder.loadTexts:
    moAuMe5V.setUnits("Volt/100")


class _MoAuMe12V_Type(Gauge32):
    """Custom type moAuMe12V based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MoAuMe12V_Type.__name__ = "Gauge32"
_MoAuMe12V_Object = MibScalar
moAuMe12V = _MoAuMe12V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3, 1, 2),
    _MoAuMe12V_Type()
)
moAuMe12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moAuMe12V.setStatus("obsolete")
if mibBuilder.loadTexts:
    moAuMe12V.setUnits("Volt/100")


class _MoAuMeN12V_Type(Integer32):
    """Custom type moAuMeN12V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 0),
    )


_MoAuMeN12V_Type.__name__ = "Integer32"
_MoAuMeN12V_Object = MibScalar
moAuMeN12V = _MoAuMeN12V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3, 1, 3),
    _MoAuMeN12V_Type()
)
moAuMeN12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moAuMeN12V.setStatus("obsolete")
if mibBuilder.loadTexts:
    moAuMeN12V.setUnits("Volt/100")
_MoAuAlarms_ObjectIdentity = ObjectIdentity
moAuAlarms = _MoAuAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 3, 2)
)
if mibBuilder.loadTexts:
    moAuAlarms.setStatus("obsolete")
_MoFan_ObjectIdentity = ObjectIdentity
moFan = _MoFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    moFan.setStatus("obsolete")
_MoFanMes_ObjectIdentity = ObjectIdentity
moFanMes = _MoFanMes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    moFanMes.setStatus("obsolete")


class _MoFanMeFan1Speed_Type(Gauge32):
    """Custom type moFanMeFan1Speed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MoFanMeFan1Speed_Type.__name__ = "Gauge32"
_MoFanMeFan1Speed_Object = MibScalar
moFanMeFan1Speed = _MoFanMeFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 1, 1),
    _MoFanMeFan1Speed_Type()
)
moFanMeFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFanMeFan1Speed.setStatus("obsolete")
if mibBuilder.loadTexts:
    moFanMeFan1Speed.setUnits("rpm")


class _MoFanMeFan2Speed_Type(Gauge32):
    """Custom type moFanMeFan2Speed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MoFanMeFan2Speed_Type.__name__ = "Gauge32"
_MoFanMeFan2Speed_Object = MibScalar
moFanMeFan2Speed = _MoFanMeFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 1, 2),
    _MoFanMeFan2Speed_Type()
)
moFanMeFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFanMeFan2Speed.setStatus("obsolete")
if mibBuilder.loadTexts:
    moFanMeFan2Speed.setUnits("rpm")
_MoFanAlarms_ObjectIdentity = ObjectIdentity
moFanAlarms = _MoFanAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 2)
)
if mibBuilder.loadTexts:
    moFanAlarms.setStatus("obsolete")


class _MoFanAlFan1Alarm_Type(Integer32):
    """Custom type moFanAlFan1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoFanAlFan1Alarm_Type.__name__ = "Integer32"
_MoFanAlFan1Alarm_Object = MibScalar
moFanAlFan1Alarm = _MoFanAlFan1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 2, 1),
    _MoFanAlFan1Alarm_Type()
)
moFanAlFan1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFanAlFan1Alarm.setStatus("obsolete")


class _MoFanAlFan2Alarm_Type(Integer32):
    """Custom type moFanAlFan2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MoFanAlFan2Alarm_Type.__name__ = "Integer32"
_MoFanAlFan2Alarm_Object = MibScalar
moFanAlFan2Alarm = _MoFanAlFan2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 10, 4, 2, 2),
    _MoFanAlFan2Alarm_Type()
)
moFanAlFan2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moFanAlFan2Alarm.setStatus("obsolete")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11)
)
if mibBuilder.loadTexts:
    maintenance.setStatus("current")
_MaMonitoring_ObjectIdentity = ObjectIdentity
maMonitoring = _MaMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    maMonitoring.setStatus("current")
_MaMoMain_ObjectIdentity = ObjectIdentity
maMoMain = _MaMoMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    maMoMain.setStatus("current")


class _MaMoMaEffTrans_Type(Gauge32):
    """Custom type maMoMaEffTrans based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaMoMaEffTrans_Type.__name__ = "Gauge32"
_MaMoMaEffTrans_Object = MibScalar
maMoMaEffTrans = _MaMoMaEffTrans_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 1, 1),
    _MaMoMaEffTrans_Type()
)
maMoMaEffTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMaEffTrans.setStatus("current")
if mibBuilder.loadTexts:
    maMoMaEffTrans.setUnits("percent")


class _MaMoMaEffPa_Type(Gauge32):
    """Custom type maMoMaEffPa based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaMoMaEffPa_Type.__name__ = "Gauge32"
_MaMoMaEffPa_Object = MibScalar
maMoMaEffPa = _MaMoMaEffPa_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 1, 2),
    _MaMoMaEffPa_Type()
)
maMoMaEffPa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMaEffPa.setStatus("current")
if mibBuilder.loadTexts:
    maMoMaEffPa.setUnits("percent")


class _MaMoMaEffPsu_Type(Gauge32):
    """Custom type maMoMaEffPsu based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaMoMaEffPsu_Type.__name__ = "Gauge32"
_MaMoMaEffPsu_Object = MibScalar
maMoMaEffPsu = _MaMoMaEffPsu_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 1, 3),
    _MaMoMaEffPsu_Type()
)
maMoMaEffPsu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMaEffPsu.setStatus("current")
if mibBuilder.loadTexts:
    maMoMaEffPsu.setUnits("percent")


class _MaMoMaEffSys_Type(Gauge32):
    """Custom type maMoMaEffSys based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaMoMaEffSys_Type.__name__ = "Gauge32"
_MaMoMaEffSys_Object = MibScalar
maMoMaEffSys = _MaMoMaEffSys_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 1, 4),
    _MaMoMaEffSys_Type()
)
maMoMaEffSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMaEffSys.setStatus("current")
if mibBuilder.loadTexts:
    maMoMaEffSys.setUnits("percent")
_MaMoCcu_ObjectIdentity = ObjectIdentity
maMoCcu = _MaMoCcu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 2)
)
if mibBuilder.loadTexts:
    maMoCcu.setStatus("current")


class _MaMoCcFault_Type(Integer32):
    """Custom type maMoCcFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCcFault_Type.__name__ = "Integer32"
_MaMoCcFault_Object = MibScalar
maMoCcFault = _MaMoCcFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 2, 1),
    _MaMoCcFault_Type()
)
maMoCcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCcFault.setStatus("current")


class _MaMoCcWarn_Type(Integer32):
    """Custom type maMoCcWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCcWarn_Type.__name__ = "Integer32"
_MaMoCcWarn_Object = MibScalar
maMoCcWarn = _MaMoCcWarn_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 2, 2),
    _MaMoCcWarn_Type()
)
maMoCcWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCcWarn.setStatus("current")
_MaMoConditions_ObjectIdentity = ObjectIdentity
maMoConditions = _MaMoConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3)
)
if mibBuilder.loadTexts:
    maMoConditions.setStatus("current")
_MaMoCoMeas_ObjectIdentity = ObjectIdentity
maMoCoMeas = _MaMoCoMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    maMoCoMeas.setStatus("current")


class _MaMoCoMeAmb_Type(Integer32):
    """Custom type maMoCoMeAmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaMoCoMeAmb_Type.__name__ = "Integer32"
_MaMoCoMeAmb_Object = MibScalar
maMoCoMeAmb = _MaMoCoMeAmb_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 1),
    _MaMoCoMeAmb_Type()
)
maMoCoMeAmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeAmb.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeAmb.setUnits("Celsius Degrees")


class _MaMoCoMeLoad1InputTemp_Type(Integer32):
    """Custom type maMoCoMeLoad1InputTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_MaMoCoMeLoad1InputTemp_Type.__name__ = "Integer32"
_MaMoCoMeLoad1InputTemp_Object = MibScalar
maMoCoMeLoad1InputTemp = _MaMoCoMeLoad1InputTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 2),
    _MaMoCoMeLoad1InputTemp_Type()
)
maMoCoMeLoad1InputTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeLoad1InputTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeLoad1InputTemp.setUnits("Celsius Degrees")


class _MaMoCoMeLoad1HeatsinkTemp_Type(Integer32):
    """Custom type maMoCoMeLoad1HeatsinkTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_MaMoCoMeLoad1HeatsinkTemp_Type.__name__ = "Integer32"
_MaMoCoMeLoad1HeatsinkTemp_Object = MibScalar
maMoCoMeLoad1HeatsinkTemp = _MaMoCoMeLoad1HeatsinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 3),
    _MaMoCoMeLoad1HeatsinkTemp_Type()
)
maMoCoMeLoad1HeatsinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeLoad1HeatsinkTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeLoad1HeatsinkTemp.setUnits("Celsius Degrees")


class _MaMoCoMeLoad2InputTemp_Type(Integer32):
    """Custom type maMoCoMeLoad2InputTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_MaMoCoMeLoad2InputTemp_Type.__name__ = "Integer32"
_MaMoCoMeLoad2InputTemp_Object = MibScalar
maMoCoMeLoad2InputTemp = _MaMoCoMeLoad2InputTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 4),
    _MaMoCoMeLoad2InputTemp_Type()
)
maMoCoMeLoad2InputTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeLoad2InputTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeLoad2InputTemp.setUnits("Celsius Degrees")


class _MaMoCoMeLoad2HeatsinkTemp_Type(Integer32):
    """Custom type maMoCoMeLoad2HeatsinkTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_MaMoCoMeLoad2HeatsinkTemp_Type.__name__ = "Integer32"
_MaMoCoMeLoad2HeatsinkTemp_Object = MibScalar
maMoCoMeLoad2HeatsinkTemp = _MaMoCoMeLoad2HeatsinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 5),
    _MaMoCoMeLoad2HeatsinkTemp_Type()
)
maMoCoMeLoad2HeatsinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeLoad2HeatsinkTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeLoad2HeatsinkTemp.setUnits("Celsius Degrees")


class _MaMoCoMePressure_Type(Gauge32):
    """Custom type maMoCoMePressure based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_MaMoCoMePressure_Type.__name__ = "Gauge32"
_MaMoCoMePressure_Object = MibScalar
maMoCoMePressure = _MaMoCoMePressure_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 6),
    _MaMoCoMePressure_Type()
)
maMoCoMePressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMePressure.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMePressure.setUnits("Celsius Degrees")


class _MaMoCoMeHeat1_Type(Integer32):
    """Custom type maMoCoMeHeat1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaMoCoMeHeat1_Type.__name__ = "Integer32"
_MaMoCoMeHeat1_Object = MibScalar
maMoCoMeHeat1 = _MaMoCoMeHeat1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 7),
    _MaMoCoMeHeat1_Type()
)
maMoCoMeHeat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeHeat1.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeHeat1.setUnits("Celsius Degrees")


class _MaMoCoMeHeat2_Type(Integer32):
    """Custom type maMoCoMeHeat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaMoCoMeHeat2_Type.__name__ = "Integer32"
_MaMoCoMeHeat2_Object = MibScalar
maMoCoMeHeat2 = _MaMoCoMeHeat2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 8),
    _MaMoCoMeHeat2_Type()
)
maMoCoMeHeat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeHeat2.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeHeat2.setUnits("Celsius Degrees")


class _MaMoCoMePsuTemp_Type(Integer32):
    """Custom type maMoCoMePsuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaMoCoMePsuTemp_Type.__name__ = "Integer32"
_MaMoCoMePsuTemp_Object = MibScalar
maMoCoMePsuTemp = _MaMoCoMePsuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 9),
    _MaMoCoMePsuTemp_Type()
)
maMoCoMePsuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMePsuTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMePsuTemp.setUnits("Celsius Degrees")


class _MaMoCoMeIntTemp_Type(Gauge32):
    """Custom type maMoCoMeIntTemp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoCoMeIntTemp_Type.__name__ = "Gauge32"
_MaMoCoMeIntTemp_Object = MibScalar
maMoCoMeIntTemp = _MaMoCoMeIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 10),
    _MaMoCoMeIntTemp_Type()
)
maMoCoMeIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeIntTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeIntTemp.setUnits("Celsius Degrees")


class _MaMoCoMeExcTemp_Type(Integer32):
    """Custom type maMoCoMeExcTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaMoCoMeExcTemp_Type.__name__ = "Integer32"
_MaMoCoMeExcTemp_Object = MibScalar
maMoCoMeExcTemp = _MaMoCoMeExcTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 1, 11),
    _MaMoCoMeExcTemp_Type()
)
maMoCoMeExcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoMeExcTemp.setStatus("current")
if mibBuilder.loadTexts:
    maMoCoMeExcTemp.setUnits("Celsius Degrees")
_MaMoCoAlarms_ObjectIdentity = ObjectIdentity
maMoCoAlarms = _MaMoCoAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    maMoCoAlarms.setStatus("current")


class _MaMoCoAlAmb_Type(Integer32):
    """Custom type maMoCoAlAmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlAmb_Type.__name__ = "Integer32"
_MaMoCoAlAmb_Object = MibScalar
maMoCoAlAmb = _MaMoCoAlAmb_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 1),
    _MaMoCoAlAmb_Type()
)
maMoCoAlAmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlAmb.setStatus("current")


class _MaMoCoAlLoad1Heatsink_Type(Integer32):
    """Custom type maMoCoAlLoad1Heatsink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlLoad1Heatsink_Type.__name__ = "Integer32"
_MaMoCoAlLoad1Heatsink_Object = MibScalar
maMoCoAlLoad1Heatsink = _MaMoCoAlLoad1Heatsink_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 2),
    _MaMoCoAlLoad1Heatsink_Type()
)
maMoCoAlLoad1Heatsink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlLoad1Heatsink.setStatus("current")


class _MaMoCoAlLoad2Heatsink_Type(Integer32):
    """Custom type maMoCoAlLoad2Heatsink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlLoad2Heatsink_Type.__name__ = "Integer32"
_MaMoCoAlLoad2Heatsink_Object = MibScalar
maMoCoAlLoad2Heatsink = _MaMoCoAlLoad2Heatsink_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 3),
    _MaMoCoAlLoad2Heatsink_Type()
)
maMoCoAlLoad2Heatsink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlLoad2Heatsink.setStatus("current")


class _MaMoCoAlPressure_Type(Integer32):
    """Custom type maMoCoAlPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlPressure_Type.__name__ = "Integer32"
_MaMoCoAlPressure_Object = MibScalar
maMoCoAlPressure = _MaMoCoAlPressure_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 4),
    _MaMoCoAlPressure_Type()
)
maMoCoAlPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlPressure.setStatus("current")


class _MaMoCoAlHeat1_Type(Integer32):
    """Custom type maMoCoAlHeat1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlHeat1_Type.__name__ = "Integer32"
_MaMoCoAlHeat1_Object = MibScalar
maMoCoAlHeat1 = _MaMoCoAlHeat1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 5),
    _MaMoCoAlHeat1_Type()
)
maMoCoAlHeat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlHeat1.setStatus("current")


class _MaMoCoAlHeat2_Type(Integer32):
    """Custom type maMoCoAlHeat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlHeat2_Type.__name__ = "Integer32"
_MaMoCoAlHeat2_Object = MibScalar
maMoCoAlHeat2 = _MaMoCoAlHeat2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 6),
    _MaMoCoAlHeat2_Type()
)
maMoCoAlHeat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlHeat2.setStatus("current")


class _MaMoCoAlTemp1_Type(Integer32):
    """Custom type maMoCoAlTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlTemp1_Type.__name__ = "Integer32"
_MaMoCoAlTemp1_Object = MibScalar
maMoCoAlTemp1 = _MaMoCoAlTemp1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 7),
    _MaMoCoAlTemp1_Type()
)
maMoCoAlTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlTemp1.setStatus("current")


class _MaMoCoAlTemp2_Type(Integer32):
    """Custom type maMoCoAlTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlTemp2_Type.__name__ = "Integer32"
_MaMoCoAlTemp2_Object = MibScalar
maMoCoAlTemp2 = _MaMoCoAlTemp2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 8),
    _MaMoCoAlTemp2_Type()
)
maMoCoAlTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlTemp2.setStatus("current")


class _MaMoCoAlPsuTemp_Type(Integer32):
    """Custom type maMoCoAlPsuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlPsuTemp_Type.__name__ = "Integer32"
_MaMoCoAlPsuTemp_Object = MibScalar
maMoCoAlPsuTemp = _MaMoCoAlPsuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 9),
    _MaMoCoAlPsuTemp_Type()
)
maMoCoAlPsuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlPsuTemp.setStatus("current")


class _MaMoCoAlIntTemp_Type(Integer32):
    """Custom type maMoCoAlIntTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlIntTemp_Type.__name__ = "Integer32"
_MaMoCoAlIntTemp_Object = MibScalar
maMoCoAlIntTemp = _MaMoCoAlIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 10),
    _MaMoCoAlIntTemp_Type()
)
maMoCoAlIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlIntTemp.setStatus("current")


class _MaMoCoAlExcTemp_Type(Integer32):
    """Custom type maMoCoAlExcTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoCoAlExcTemp_Type.__name__ = "Integer32"
_MaMoCoAlExcTemp_Object = MibScalar
maMoCoAlExcTemp = _MaMoCoAlExcTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 3, 2, 11),
    _MaMoCoAlExcTemp_Type()
)
maMoCoAlExcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoCoAlExcTemp.setStatus("current")
_MaMoAuxVolt_ObjectIdentity = ObjectIdentity
maMoAuxVolt = _MaMoAuxVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    maMoAuxVolt.setStatus("current")
_MaMoAuMeas_ObjectIdentity = ObjectIdentity
maMoAuMeas = _MaMoAuMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    maMoAuMeas.setStatus("current")


class _MaMoAuMe5V_Type(Gauge32):
    """Custom type maMoAuMe5V based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MaMoAuMe5V_Type.__name__ = "Gauge32"
_MaMoAuMe5V_Object = MibScalar
maMoAuMe5V = _MaMoAuMe5V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 1, 1),
    _MaMoAuMe5V_Type()
)
maMoAuMe5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuMe5V.setStatus("current")
if mibBuilder.loadTexts:
    maMoAuMe5V.setUnits("Volt/100")


class _MaMoAuMe12V_Type(Gauge32):
    """Custom type maMoAuMe12V based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MaMoAuMe12V_Type.__name__ = "Gauge32"
_MaMoAuMe12V_Object = MibScalar
maMoAuMe12V = _MaMoAuMe12V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 1, 2),
    _MaMoAuMe12V_Type()
)
maMoAuMe12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuMe12V.setStatus("current")
if mibBuilder.loadTexts:
    maMoAuMe12V.setUnits("Volt/100")


class _MaMoAuMeN12V_Type(Integer32):
    """Custom type maMoAuMeN12V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 0),
    )


_MaMoAuMeN12V_Type.__name__ = "Integer32"
_MaMoAuMeN12V_Object = MibScalar
maMoAuMeN12V = _MaMoAuMeN12V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 1, 3),
    _MaMoAuMeN12V_Type()
)
maMoAuMeN12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuMeN12V.setStatus("current")
if mibBuilder.loadTexts:
    maMoAuMeN12V.setUnits("Volt/100")


class _MaMoAuMe24V_Type(Gauge32):
    """Custom type maMoAuMe24V based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MaMoAuMe24V_Type.__name__ = "Gauge32"
_MaMoAuMe24V_Object = MibScalar
maMoAuMe24V = _MaMoAuMe24V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 1, 4),
    _MaMoAuMe24V_Type()
)
maMoAuMe24V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuMe24V.setStatus("current")
if mibBuilder.loadTexts:
    maMoAuMe24V.setUnits("Volt/100")
_MaMoAuAlarms_ObjectIdentity = ObjectIdentity
maMoAuAlarms = _MaMoAuAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 2)
)
if mibBuilder.loadTexts:
    maMoAuAlarms.setStatus("current")


class _MaMoAuAlVoltAux_Type(Integer32):
    """Custom type maMoAuAlVoltAux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAuAlVoltAux_Type.__name__ = "Integer32"
_MaMoAuAlVoltAux_Object = MibScalar
maMoAuAlVoltAux = _MaMoAuAlVoltAux_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 2, 1),
    _MaMoAuAlVoltAux_Type()
)
maMoAuAlVoltAux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuAlVoltAux.setStatus("current")


class _MaMoAuAl24V_Type(Integer32):
    """Custom type maMoAuAl24V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAuAl24V_Type.__name__ = "Integer32"
_MaMoAuAl24V_Object = MibScalar
maMoAuAl24V = _MaMoAuAl24V_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 4, 2, 2),
    _MaMoAuAl24V_Type()
)
maMoAuAl24V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAuAl24V.setStatus("current")
_MaMoFanTable_Object = MibTable
maMoFanTable = _MaMoFanTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 5)
)
if mibBuilder.loadTexts:
    maMoFanTable.setStatus("current")
_MaMoFanEntry_Object = MibTableRow
maMoFanEntry = _MaMoFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 5, 1)
)
maMoFanEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "maMoFanIndex"),
)
if mibBuilder.loadTexts:
    maMoFanEntry.setStatus("current")


class _MaMoFanIndex_Type(Integer32):
    """Custom type maMoFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaMoFanIndex_Type.__name__ = "Integer32"
_MaMoFanIndex_Object = MibTableColumn
maMoFanIndex = _MaMoFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 5, 1, 1),
    _MaMoFanIndex_Type()
)
maMoFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maMoFanIndex.setStatus("current")


class _MaMoFanSpeed_Type(Gauge32):
    """Custom type maMoFanSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaMoFanSpeed_Type.__name__ = "Gauge32"
_MaMoFanSpeed_Object = MibTableColumn
maMoFanSpeed = _MaMoFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 5, 1, 2),
    _MaMoFanSpeed_Type()
)
maMoFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    maMoFanSpeed.setUnits("Rpm")


class _MaMoFanAlarms_Type(Integer32):
    """Custom type maMoFanAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoFanAlarms_Type.__name__ = "Integer32"
_MaMoFanAlarms_Object = MibTableColumn
maMoFanAlarms = _MaMoFanAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 5, 1, 3),
    _MaMoFanAlarms_Type()
)
maMoFanAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoFanAlarms.setStatus("current")
_MaMoMeas_ObjectIdentity = ObjectIdentity
maMoMeas = _MaMoMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6)
)
if mibBuilder.loadTexts:
    maMoMeas.setStatus("current")


class _MaMoMeVolt1_Type(Gauge32):
    """Custom type maMoMeVolt1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMeVolt1_Type.__name__ = "Gauge32"
_MaMoMeVolt1_Object = MibScalar
maMoMeVolt1 = _MaMoMeVolt1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 1),
    _MaMoMeVolt1_Type()
)
maMoMeVolt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeVolt1.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeVolt1.setUnits("V/10")


class _MaMoMeVolt2_Type(Gauge32):
    """Custom type maMoMeVolt2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMeVolt2_Type.__name__ = "Gauge32"
_MaMoMeVolt2_Object = MibScalar
maMoMeVolt2 = _MaMoMeVolt2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 2),
    _MaMoMeVolt2_Type()
)
maMoMeVolt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeVolt2.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeVolt2.setUnits("V/10")


class _MaMoMeCur1_Type(Gauge32):
    """Custom type maMoMeCur1 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMeCur1_Type.__name__ = "Gauge32"
_MaMoMeCur1_Object = MibScalar
maMoMeCur1 = _MaMoMeCur1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 3),
    _MaMoMeCur1_Type()
)
maMoMeCur1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeCur1.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeCur1.setUnits("A/10")


class _MaMoMeCur2_Type(Gauge32):
    """Custom type maMoMeCur2 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMeCur2_Type.__name__ = "Gauge32"
_MaMoMeCur2_Object = MibScalar
maMoMeCur2 = _MaMoMeCur2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 4),
    _MaMoMeCur2_Type()
)
maMoMeCur2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeCur2.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeCur2.setUnits("A/10")


class _MaMoMePin_Type(Gauge32):
    """Custom type maMoMePin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMePin_Type.__name__ = "Gauge32"
_MaMoMePin_Object = MibScalar
maMoMePin = _MaMoMePin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 5),
    _MaMoMePin_Type()
)
maMoMePin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMePin.setStatus("current")
if mibBuilder.loadTexts:
    maMoMePin.setUnits("W/10")


class _MaMoMeVolt3_Type(Gauge32):
    """Custom type maMoMeVolt3 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MaMoMeVolt3_Type.__name__ = "Gauge32"
_MaMoMeVolt3_Object = MibScalar
maMoMeVolt3 = _MaMoMeVolt3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 6),
    _MaMoMeVolt3_Type()
)
maMoMeVolt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeVolt3.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeVolt3.setUnits("mV")


class _MaMoMeCur3_Type(Gauge32):
    """Custom type maMoMeCur3 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaMoMeCur3_Type.__name__ = "Gauge32"
_MaMoMeCur3_Object = MibScalar
maMoMeCur3 = _MaMoMeCur3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 6, 7),
    _MaMoMeCur3_Type()
)
maMoMeCur3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoMeCur3.setStatus("current")
if mibBuilder.loadTexts:
    maMoMeCur3.setUnits("mA")
_MaMoAlarm_ObjectIdentity = ObjectIdentity
maMoAlarm = _MaMoAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7)
)
if mibBuilder.loadTexts:
    maMoAlarm.setStatus("current")


class _MaMoAlVolt1_Type(Integer32):
    """Custom type maMoAlVolt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlVolt1_Type.__name__ = "Integer32"
_MaMoAlVolt1_Object = MibScalar
maMoAlVolt1 = _MaMoAlVolt1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 1),
    _MaMoAlVolt1_Type()
)
maMoAlVolt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlVolt1.setStatus("current")


class _MaMoAlVolt2_Type(Integer32):
    """Custom type maMoAlVolt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlVolt2_Type.__name__ = "Integer32"
_MaMoAlVolt2_Object = MibScalar
maMoAlVolt2 = _MaMoAlVolt2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 2),
    _MaMoAlVolt2_Type()
)
maMoAlVolt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlVolt2.setStatus("current")


class _MaMoAlCur1_Type(Integer32):
    """Custom type maMoAlCur1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlCur1_Type.__name__ = "Integer32"
_MaMoAlCur1_Object = MibScalar
maMoAlCur1 = _MaMoAlCur1_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 3),
    _MaMoAlCur1_Type()
)
maMoAlCur1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlCur1.setStatus("current")


class _MaMoAlCur2_Type(Integer32):
    """Custom type maMoAlCur2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlCur2_Type.__name__ = "Integer32"
_MaMoAlCur2_Object = MibScalar
maMoAlCur2 = _MaMoAlCur2_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 4),
    _MaMoAlCur2_Type()
)
maMoAlCur2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlCur2.setStatus("current")


class _MaMoAlPin_Type(Integer32):
    """Custom type maMoAlPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlPin_Type.__name__ = "Integer32"
_MaMoAlPin_Object = MibScalar
maMoAlPin = _MaMoAlPin_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 5),
    _MaMoAlPin_Type()
)
maMoAlPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlPin.setStatus("current")


class _MaMoAlSecPref_Type(Integer32):
    """Custom type maMoAlSecPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlSecPref_Type.__name__ = "Integer32"
_MaMoAlSecPref_Object = MibScalar
maMoAlSecPref = _MaMoAlSecPref_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 6),
    _MaMoAlSecPref_Type()
)
maMoAlSecPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlSecPref.setStatus("current")


class _MaMoAlCur3_Type(Integer32):
    """Custom type maMoAlCur3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaMoAlCur3_Type.__name__ = "Integer32"
_MaMoAlCur3_Object = MibScalar
maMoAlCur3 = _MaMoAlCur3_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 1, 7, 7),
    _MaMoAlCur3_Type()
)
maMoAlCur3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maMoAlCur3.setStatus("current")
_MaDrive_ObjectIdentity = ObjectIdentity
maDrive = _MaDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    maDrive.setStatus("current")
_MaDrTable_Object = MibTable
maDrTable = _MaDrTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    maDrTable.setStatus("current")
_MaDrEntry_Object = MibTableRow
maDrEntry = _MaDrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1)
)
maDrEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "maDrIndex"),
)
if mibBuilder.loadTexts:
    maDrEntry.setStatus("current")


class _MaDrIndex_Type(Integer32):
    """Custom type maDrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaDrIndex_Type.__name__ = "Integer32"
_MaDrIndex_Object = MibTableColumn
maDrIndex = _MaDrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 1),
    _MaDrIndex_Type()
)
maDrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maDrIndex.setStatus("current")


class _MaDrCommunication_Type(Integer32):
    """Custom type maDrCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaDrCommunication_Type.__name__ = "Integer32"
_MaDrCommunication_Object = MibTableColumn
maDrCommunication = _MaDrCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 2),
    _MaDrCommunication_Type()
)
maDrCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrCommunication.setStatus("current")


class _MaDrFault_Type(Integer32):
    """Custom type maDrFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaDrFault_Type.__name__ = "Integer32"
_MaDrFault_Object = MibTableColumn
maDrFault = _MaDrFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 3),
    _MaDrFault_Type()
)
maDrFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrFault.setStatus("current")


class _MaDrWarning_Type(Integer32):
    """Custom type maDrWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaDrWarning_Type.__name__ = "Integer32"
_MaDrWarning_Object = MibTableColumn
maDrWarning = _MaDrWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 4),
    _MaDrWarning_Type()
)
maDrWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrWarning.setStatus("current")


class _MaDrForwardPower_Type(Gauge32):
    """Custom type maDrForwardPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaDrForwardPower_Type.__name__ = "Gauge32"
_MaDrForwardPower_Object = MibTableColumn
maDrForwardPower = _MaDrForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 5),
    _MaDrForwardPower_Type()
)
maDrForwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrForwardPower.setStatus("current")
if mibBuilder.loadTexts:
    maDrForwardPower.setUnits("W")


class _MaDrReflectedPower_Type(Gauge32):
    """Custom type maDrReflectedPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaDrReflectedPower_Type.__name__ = "Gauge32"
_MaDrReflectedPower_Object = MibTableColumn
maDrReflectedPower = _MaDrReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 6),
    _MaDrReflectedPower_Type()
)
maDrReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrReflectedPower.setStatus("current")
if mibBuilder.loadTexts:
    maDrReflectedPower.setUnits("W")


class _MaDrHeatsink_Type(Integer32):
    """Custom type maDrHeatsink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaDrHeatsink_Type.__name__ = "Integer32"
_MaDrHeatsink_Object = MibTableColumn
maDrHeatsink = _MaDrHeatsink_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 7),
    _MaDrHeatsink_Type()
)
maDrHeatsink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrHeatsink.setStatus("current")
if mibBuilder.loadTexts:
    maDrHeatsink.setUnits("Celsius Degrees")


class _MaDrFanSpeed_Type(Gauge32):
    """Custom type maDrFanSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaDrFanSpeed_Type.__name__ = "Gauge32"
_MaDrFanSpeed_Object = MibTableColumn
maDrFanSpeed = _MaDrFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 2, 1, 1, 8),
    _MaDrFanSpeed_Type()
)
maDrFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maDrFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    maDrFanSpeed.setUnits("Rpm")
_MaPa_ObjectIdentity = ObjectIdentity
maPa = _MaPa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    maPa.setStatus("current")
_MaPaTable_Object = MibTable
maPaTable = _MaPaTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    maPaTable.setStatus("current")
_MaPaEntry_Object = MibTableRow
maPaEntry = _MaPaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1)
)
maPaEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "maPaIndex"),
)
if mibBuilder.loadTexts:
    maPaEntry.setStatus("current")


class _MaPaIndex_Type(Integer32):
    """Custom type maPaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaPaIndex_Type.__name__ = "Integer32"
_MaPaIndex_Object = MibTableColumn
maPaIndex = _MaPaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 1),
    _MaPaIndex_Type()
)
maPaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maPaIndex.setStatus("current")


class _MaPaCommunication_Type(Integer32):
    """Custom type maPaCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaCommunication_Type.__name__ = "Integer32"
_MaPaCommunication_Object = MibTableColumn
maPaCommunication = _MaPaCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 2),
    _MaPaCommunication_Type()
)
maPaCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaCommunication.setStatus("current")


class _MaPaFault_Type(Integer32):
    """Custom type maPaFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaFault_Type.__name__ = "Integer32"
_MaPaFault_Object = MibTableColumn
maPaFault = _MaPaFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 3),
    _MaPaFault_Type()
)
maPaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaFault.setStatus("current")


class _MaPaWarning_Type(Integer32):
    """Custom type maPaWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaWarning_Type.__name__ = "Integer32"
_MaPaWarning_Object = MibTableColumn
maPaWarning = _MaPaWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 4),
    _MaPaWarning_Type()
)
maPaWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaWarning.setStatus("current")


class _MaPaForwardPower_Type(Gauge32):
    """Custom type maPaForwardPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPaForwardPower_Type.__name__ = "Gauge32"
_MaPaForwardPower_Object = MibTableColumn
maPaForwardPower = _MaPaForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 5),
    _MaPaForwardPower_Type()
)
maPaForwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaForwardPower.setStatus("current")
if mibBuilder.loadTexts:
    maPaForwardPower.setUnits("W")


class _MaPaReflectedPower_Type(Gauge32):
    """Custom type maPaReflectedPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPaReflectedPower_Type.__name__ = "Gauge32"
_MaPaReflectedPower_Object = MibTableColumn
maPaReflectedPower = _MaPaReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 6),
    _MaPaReflectedPower_Type()
)
maPaReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaReflectedPower.setStatus("current")
if mibBuilder.loadTexts:
    maPaReflectedPower.setUnits("W")


class _MaPaEfficiency_Type(Gauge32):
    """Custom type maPaEfficiency based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaPaEfficiency_Type.__name__ = "Gauge32"
_MaPaEfficiency_Object = MibTableColumn
maPaEfficiency = _MaPaEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 7),
    _MaPaEfficiency_Type()
)
maPaEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    maPaEfficiency.setUnits("percent")


class _MaPaCurrent_Type(Gauge32):
    """Custom type maPaCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPaCurrent_Type.__name__ = "Gauge32"
_MaPaCurrent_Object = MibTableColumn
maPaCurrent = _MaPaCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 8),
    _MaPaCurrent_Type()
)
maPaCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaCurrent.setStatus("current")
if mibBuilder.loadTexts:
    maPaCurrent.setUnits("Ampere/100")


class _MaPaHeatMax_Type(Integer32):
    """Custom type maPaHeatMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaPaHeatMax_Type.__name__ = "Integer32"
_MaPaHeatMax_Object = MibTableColumn
maPaHeatMax = _MaPaHeatMax_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 9),
    _MaPaHeatMax_Type()
)
maPaHeatMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaHeatMax.setStatus("current")
if mibBuilder.loadTexts:
    maPaHeatMax.setUnits("Celsius Degrees")


class _MaPaAlrCur_Type(Integer32):
    """Custom type maPaAlrCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaAlrCur_Type.__name__ = "Integer32"
_MaPaAlrCur_Object = MibTableColumn
maPaAlrCur = _MaPaAlrCur_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 10),
    _MaPaAlrCur_Type()
)
maPaAlrCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaAlrCur.setStatus("current")


class _MaPaVoltage_Type(Gauge32):
    """Custom type maPaVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPaVoltage_Type.__name__ = "Gauge32"
_MaPaVoltage_Object = MibTableColumn
maPaVoltage = _MaPaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 11),
    _MaPaVoltage_Type()
)
maPaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    maPaVoltage.setUnits("mV")


class _MaPaAlrVolt_Type(Integer32):
    """Custom type maPaAlrVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaAlrVolt_Type.__name__ = "Integer32"
_MaPaAlrVolt_Object = MibTableColumn
maPaAlrVolt = _MaPaAlrVolt_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 12),
    _MaPaAlrVolt_Type()
)
maPaAlrVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaAlrVolt.setStatus("current")


class _MaPaAmbTemp_Type(Integer32):
    """Custom type maPaAmbTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaPaAmbTemp_Type.__name__ = "Integer32"
_MaPaAmbTemp_Object = MibTableColumn
maPaAmbTemp = _MaPaAmbTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 13),
    _MaPaAmbTemp_Type()
)
maPaAmbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaAmbTemp.setStatus("current")
if mibBuilder.loadTexts:
    maPaAmbTemp.setUnits("Celsius Degrees")


class _MaPaAlrHeat_Type(Integer32):
    """Custom type maPaAlrHeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaAlrHeat_Type.__name__ = "Integer32"
_MaPaAlrHeat_Object = MibTableColumn
maPaAlrHeat = _MaPaAlrHeat_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 14),
    _MaPaAlrHeat_Type()
)
maPaAlrHeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaAlrHeat.setStatus("current")


class _MaPaAlrTemp_Type(Integer32):
    """Custom type maPaAlrTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPaAlrTemp_Type.__name__ = "Integer32"
_MaPaAlrTemp_Object = MibTableColumn
maPaAlrTemp = _MaPaAlrTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 3, 1, 1, 15),
    _MaPaAlrTemp_Type()
)
maPaAlrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPaAlrTemp.setStatus("current")
_MaPsu_ObjectIdentity = ObjectIdentity
maPsu = _MaPsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    maPsu.setStatus("current")


class _MaPsVoltageInput_Type(Gauge32):
    """Custom type maPsVoltageInput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsVoltageInput_Type.__name__ = "Gauge32"
_MaPsVoltageInput_Object = MibScalar
maPsVoltageInput = _MaPsVoltageInput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 1),
    _MaPsVoltageInput_Type()
)
maPsVoltageInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsVoltageInput.setStatus("current")
if mibBuilder.loadTexts:
    maPsVoltageInput.setUnits("Volt/100")


class _MaPsCurrentInput_Type(Gauge32):
    """Custom type maPsCurrentInput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsCurrentInput_Type.__name__ = "Gauge32"
_MaPsCurrentInput_Object = MibScalar
maPsCurrentInput = _MaPsCurrentInput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 2),
    _MaPsCurrentInput_Type()
)
maPsCurrentInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsCurrentInput.setStatus("current")
if mibBuilder.loadTexts:
    maPsCurrentInput.setUnits("Ampere/100")


class _MaPsPowerInput_Type(Gauge32):
    """Custom type maPsPowerInput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsPowerInput_Type.__name__ = "Gauge32"
_MaPsPowerInput_Object = MibScalar
maPsPowerInput = _MaPsPowerInput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 3),
    _MaPsPowerInput_Type()
)
maPsPowerInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsPowerInput.setStatus("current")
if mibBuilder.loadTexts:
    maPsPowerInput.setUnits("W")


class _MaPsVoltageOutput_Type(Gauge32):
    """Custom type maPsVoltageOutput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsVoltageOutput_Type.__name__ = "Gauge32"
_MaPsVoltageOutput_Object = MibScalar
maPsVoltageOutput = _MaPsVoltageOutput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 4),
    _MaPsVoltageOutput_Type()
)
maPsVoltageOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsVoltageOutput.setStatus("current")
if mibBuilder.loadTexts:
    maPsVoltageOutput.setUnits("Volt/100")


class _MaPsCurrentOutput_Type(Gauge32):
    """Custom type maPsCurrentOutput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsCurrentOutput_Type.__name__ = "Gauge32"
_MaPsCurrentOutput_Object = MibScalar
maPsCurrentOutput = _MaPsCurrentOutput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 5),
    _MaPsCurrentOutput_Type()
)
maPsCurrentOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsCurrentOutput.setStatus("current")
if mibBuilder.loadTexts:
    maPsCurrentOutput.setUnits("Ampere/100")


class _MaPsPowerOutput_Type(Gauge32):
    """Custom type maPsPowerOutput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsPowerOutput_Type.__name__ = "Gauge32"
_MaPsPowerOutput_Object = MibScalar
maPsPowerOutput = _MaPsPowerOutput_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 6),
    _MaPsPowerOutput_Type()
)
maPsPowerOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsPowerOutput.setStatus("current")
if mibBuilder.loadTexts:
    maPsPowerOutput.setUnits("W")
_MaPsTable_Object = MibTable
maPsTable = _MaPsTable_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7)
)
if mibBuilder.loadTexts:
    maPsTable.setStatus("current")
_MaPsEntry_Object = MibTableRow
maPsEntry = _MaPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1)
)
maPsEntry.setIndexNames(
    (0, "ECRESO-FM-TRANS-MIB", "maPsIndex"),
)
if mibBuilder.loadTexts:
    maPsEntry.setStatus("current")


class _MaPsIndex_Type(Integer32):
    """Custom type maPsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MaPsIndex_Type.__name__ = "Integer32"
_MaPsIndex_Object = MibTableColumn
maPsIndex = _MaPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 1),
    _MaPsIndex_Type()
)
maPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maPsIndex.setStatus("current")


class _MaPsCommunication_Type(Integer32):
    """Custom type maPsCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsCommunication_Type.__name__ = "Integer32"
_MaPsCommunication_Object = MibTableColumn
maPsCommunication = _MaPsCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 2),
    _MaPsCommunication_Type()
)
maPsCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsCommunication.setStatus("current")


class _MaPsFault_Type(Integer32):
    """Custom type maPsFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsFault_Type.__name__ = "Integer32"
_MaPsFault_Object = MibTableColumn
maPsFault = _MaPsFault_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 3),
    _MaPsFault_Type()
)
maPsFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsFault.setStatus("current")


class _MaPsWarning_Type(Integer32):
    """Custom type maPsWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsWarning_Type.__name__ = "Integer32"
_MaPsWarning_Object = MibTableColumn
maPsWarning = _MaPsWarning_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 4),
    _MaPsWarning_Type()
)
maPsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsWarning.setStatus("current")


class _MaPsEfficiency_Type(Gauge32):
    """Custom type maPsEfficiency based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaPsEfficiency_Type.__name__ = "Gauge32"
_MaPsEfficiency_Object = MibTableColumn
maPsEfficiency = _MaPsEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 5),
    _MaPsEfficiency_Type()
)
maPsEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    maPsEfficiency.setUnits("percent")


class _MaPsOutputPower_Type(Gauge32):
    """Custom type maPsOutputPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsOutputPower_Type.__name__ = "Gauge32"
_MaPsOutputPower_Object = MibTableColumn
maPsOutputPower = _MaPsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 6),
    _MaPsOutputPower_Type()
)
maPsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    maPsOutputPower.setUnits("W")


class _MaPsInputPower_Type(Gauge32):
    """Custom type maPsInputPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsInputPower_Type.__name__ = "Gauge32"
_MaPsInputPower_Object = MibTableColumn
maPsInputPower = _MaPsInputPower_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 7),
    _MaPsInputPower_Type()
)
maPsInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsInputPower.setStatus("current")
if mibBuilder.loadTexts:
    maPsInputPower.setUnits("W")


class _MaPsMissing_Type(Integer32):
    """Custom type maPsMissing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsMissing_Type.__name__ = "Integer32"
_MaPsMissing_Object = MibTableColumn
maPsMissing = _MaPsMissing_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 8),
    _MaPsMissing_Type()
)
maPsMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsMissing.setStatus("current")


class _MaPsInputCurrent_Type(Gauge32):
    """Custom type maPsInputCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsInputCurrent_Type.__name__ = "Gauge32"
_MaPsInputCurrent_Object = MibTableColumn
maPsInputCurrent = _MaPsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 9),
    _MaPsInputCurrent_Type()
)
maPsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    maPsInputCurrent.setUnits("mA")


class _MaPsInputCurAlr_Type(Integer32):
    """Custom type maPsInputCurAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsInputCurAlr_Type.__name__ = "Integer32"
_MaPsInputCurAlr_Object = MibTableColumn
maPsInputCurAlr = _MaPsInputCurAlr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 10),
    _MaPsInputCurAlr_Type()
)
maPsInputCurAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsInputCurAlr.setStatus("current")


class _MaPsInputVoltage_Type(Gauge32):
    """Custom type maPsInputVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_MaPsInputVoltage_Type.__name__ = "Gauge32"
_MaPsInputVoltage_Object = MibTableColumn
maPsInputVoltage = _MaPsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 11),
    _MaPsInputVoltage_Type()
)
maPsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    maPsInputVoltage.setUnits("mV")


class _MaPsInputVoltAlr_Type(Integer32):
    """Custom type maPsInputVoltAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsInputVoltAlr_Type.__name__ = "Integer32"
_MaPsInputVoltAlr_Object = MibTableColumn
maPsInputVoltAlr = _MaPsInputVoltAlr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 12),
    _MaPsInputVoltAlr_Type()
)
maPsInputVoltAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsInputVoltAlr.setStatus("current")


class _MaPsOutputCurrent_Type(Gauge32):
    """Custom type maPsOutputCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsOutputCurrent_Type.__name__ = "Gauge32"
_MaPsOutputCurrent_Object = MibTableColumn
maPsOutputCurrent = _MaPsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 13),
    _MaPsOutputCurrent_Type()
)
maPsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    maPsOutputCurrent.setUnits("mA")


class _MaPsOutputCurAlr_Type(Integer32):
    """Custom type maPsOutputCurAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsOutputCurAlr_Type.__name__ = "Integer32"
_MaPsOutputCurAlr_Object = MibTableColumn
maPsOutputCurAlr = _MaPsOutputCurAlr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 14),
    _MaPsOutputCurAlr_Type()
)
maPsOutputCurAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsOutputCurAlr.setStatus("current")


class _MaPsOutputVoltage_Type(Gauge32):
    """Custom type maPsOutputVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsOutputVoltage_Type.__name__ = "Gauge32"
_MaPsOutputVoltage_Object = MibTableColumn
maPsOutputVoltage = _MaPsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 15),
    _MaPsOutputVoltage_Type()
)
maPsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    maPsOutputVoltage.setUnits("mV")


class _MaPsOutputVoltAlr_Type(Integer32):
    """Custom type maPsOutputVoltAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsOutputVoltAlr_Type.__name__ = "Integer32"
_MaPsOutputVoltAlr_Object = MibTableColumn
maPsOutputVoltAlr = _MaPsOutputVoltAlr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 16),
    _MaPsOutputVoltAlr_Type()
)
maPsOutputVoltAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsOutputVoltAlr.setStatus("current")


class _MaPsAmbTemp_Type(Integer32):
    """Custom type maPsAmbTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaPsAmbTemp_Type.__name__ = "Integer32"
_MaPsAmbTemp_Object = MibTableColumn
maPsAmbTemp = _MaPsAmbTemp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 17),
    _MaPsAmbTemp_Type()
)
maPsAmbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsAmbTemp.setStatus("current")
if mibBuilder.loadTexts:
    maPsAmbTemp.setUnits("Celsius Degrees")


class _MaPsAmbAlr_Type(Integer32):
    """Custom type maPsAmbAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsAmbAlr_Type.__name__ = "Integer32"
_MaPsAmbAlr_Object = MibTableColumn
maPsAmbAlr = _MaPsAmbAlr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 18),
    _MaPsAmbAlr_Type()
)
maPsAmbAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsAmbAlr.setStatus("current")


class _MaPsHeat1Temp_Type(Integer32):
    """Custom type maPsHeat1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_MaPsHeat1Temp_Type.__name__ = "Integer32"
_MaPsHeat1Temp_Object = MibTableColumn
maPsHeat1Temp = _MaPsHeat1Temp_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 19),
    _MaPsHeat1Temp_Type()
)
maPsHeat1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsHeat1Temp.setStatus("current")
if mibBuilder.loadTexts:
    maPsHeat1Temp.setUnits("Celsius Degrees")


class _MaPsHeat1Alr_Type(Integer32):
    """Custom type maPsHeat1Alr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsHeat1Alr_Type.__name__ = "Integer32"
_MaPsHeat1Alr_Object = MibTableColumn
maPsHeat1Alr = _MaPsHeat1Alr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 20),
    _MaPsHeat1Alr_Type()
)
maPsHeat1Alr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsHeat1Alr.setStatus("current")


class _MaPsFan1Speed_Type(Gauge32):
    """Custom type maPsFan1Speed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaPsFan1Speed_Type.__name__ = "Gauge32"
_MaPsFan1Speed_Object = MibTableColumn
maPsFan1Speed = _MaPsFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 21),
    _MaPsFan1Speed_Type()
)
maPsFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    maPsFan1Speed.setUnits("rpm")


class _MaPsFan1Alr_Type(Integer32):
    """Custom type maPsFan1Alr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )


_MaPsFan1Alr_Type.__name__ = "Integer32"
_MaPsFan1Alr_Object = MibTableColumn
maPsFan1Alr = _MaPsFan1Alr_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 22),
    _MaPsFan1Alr_Type()
)
maPsFan1Alr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsFan1Alr.setStatus("current")


class _MaPsSerial_Type(DisplayString):
    """Custom type maPsSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_MaPsSerial_Type.__name__ = "DisplayString"
_MaPsSerial_Object = MibTableColumn
maPsSerial = _MaPsSerial_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 23),
    _MaPsSerial_Type()
)
maPsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsSerial.setStatus("current")


class _MaPsSoftRel_Type(DisplayString):
    """Custom type maPsSoftRel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MaPsSoftRel_Type.__name__ = "DisplayString"
_MaPsSoftRel_Object = MibTableColumn
maPsSoftRel = _MaPsSoftRel_Object(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 11, 4, 7, 1, 24),
    _MaPsSoftRel_Type()
)
maPsSoftRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maPsSoftRel.setStatus("current")

# Managed Objects groups

objectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 2, 1)
)
objectGroup.setObjects(
      *(("ECRESO-FM-TRANS-MIB", "eventTxLocalModePriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxLocalModeEnable"),
        ("ECRESO-FM-TRANS-MIB", "txLocalModeSignalSuppression"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl3dBPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl3dBEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlFaultEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlWarningPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlWarningEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlVSWRPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlVSWREnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockAntPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockAntEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfOpmodePriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfOpmodeEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfRFPresentPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfRFPresentEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcReserveControlPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine1Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine1Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine2Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine2Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx1Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx1Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx2Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx2Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlPlayerPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlPlayerEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcReserveControlEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcLocalModePriority"),
        ("ECRESO-FM-TRANS-MIB", "eventAcLocalModeEnable"),
        ("ECRESO-FM-TRANS-MIB", "acLocalModeSignalSuppression"),
        ("ECRESO-FM-TRANS-MIB", "eventAcFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventAcFaultEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcSwitchOverPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventAcSwitchOverEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysWarningPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysWarningEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysFaultEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlAmbPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlAmbEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlVoltAuxPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlVoltAuxEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlRelayPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlRelayEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlReservePriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlReserveEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventInSeAlrInputSwitchPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventInSeAlrInputSwitchEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl1dBPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl1dBEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxGnGlStandbyPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxGnGlStandbyEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlInvalidDataPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlInvalidDataEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockAntPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockAntEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockLoadPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockLoadEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAl24vPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAl24vEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlCommPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlCommEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOnPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOnEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventHeartBeatPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventHeartBeatEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventConfigChangedPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventConfigChangedEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlFaultEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfAlarmEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfSwitch10MAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfSwitch10MAlarmEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyAlLoggingPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyAlLoggingEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx3Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx3Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx4Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx4Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAoipPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAoipEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStActPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStActEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStAlarmEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlRdsPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlRdsEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSoundProcPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSoundProcEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSfmPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSfmEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlActivationPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlActivationEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes1Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes1Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes2Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes2Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes3Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes3Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAna1Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAna1Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth0Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth0Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth1Priority"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth1Enable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlAoipdecoderPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlAoipdecoderEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlMpxoipdecoderPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlMpxoipdecoderEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSurestreamPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSurestreamEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSynchrostreamPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSynchrostreamEnable"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Type"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoL1AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Type"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoL2AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes1AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes2AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoAes3AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1LeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1RightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1LeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1RightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Trim"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Filter"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Preacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoAna1AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoTySlot1"),
        ("ECRESO-FM-TRANS-MIB", "inSoTySlot2"),
        ("ECRESO-FM-TRANS-MIB", "inSoTySlot3"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipPresence"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipLeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipRightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipLeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipRightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipLevel"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipDrive"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipTrim"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipFilter"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipPreacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipLost"),
        ("ECRESO-FM-TRANS-MIB", "inSoAoipAlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoM1AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "moSfSwitch10MAlarm"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoM2AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlPresence"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlLeftPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlRightPeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlLeftPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlRightPeak"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlLevel"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlDrive"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlTrim"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlFilter"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlPreacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlSampling"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlLost"),
        ("ECRESO-FM-TRANS-MIB", "inSoPlAlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoGeState"),
        ("ECRESO-FM-TRANS-MIB", "inSoGeLevel1"),
        ("ECRESO-FM-TRANS-MIB", "inSoGeLevel2"),
        ("ECRESO-FM-TRANS-MIB", "inSoGeFreq1"),
        ("ECRESO-FM-TRANS-MIB", "inSoGeFreq2"),
        ("ECRESO-FM-TRANS-MIB", "inSoGePreacc"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoM3AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4Presence"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4PeakMax"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4Peak"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4Level"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4Drive"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4Lost"),
        ("ECRESO-FM-TRANS-MIB", "inSoM4AlarmTrig"),
        ("ECRESO-FM-TRANS-MIB", "inSeLine1Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSeLine2Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSeMpx1Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSeMpx2Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSePlayerPrio"),
        ("ECRESO-FM-TRANS-MIB", "inSeMpx3Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSeMpx4Prio"),
        ("ECRESO-FM-TRANS-MIB", "inSeCrossfade"),
        ("ECRESO-FM-TRANS-MIB", "inSeSelectAudio"),
        ("ECRESO-FM-TRANS-MIB", "inSeCurrentAudio"),
        ("ECRESO-FM-TRANS-MIB", "inSeAuBackupMode"),
        ("ECRESO-FM-TRANS-MIB", "inSeAlrInputSwitch"),
        ("ECRESO-FM-TRANS-MIB", "inSeFadein"),
        ("ECRESO-FM-TRANS-MIB", "inSeThLine1Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThLine1Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThLine2Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThLine2Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThPlayerTh"),
        ("ECRESO-FM-TRANS-MIB", "inSeThPlayerSil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThMpx1Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThMpx2Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThMpx3Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThMpx4Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes1Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes1Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes2Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes2Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes3Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAes3Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAna1Th"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAna1Sil"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAoipTh"),
        ("ECRESO-FM-TRANS-MIB", "inSeThAoipSil"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeLine1BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeLine1Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeLine2BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeLine2Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDePlayerBackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDePlayerDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpxBackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpxDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx34BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx34Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes1BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes1Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes2BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes2Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes3BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAes3Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAna1BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAna1Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx1BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx1Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx2BackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeMpx2Delay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAoipBackDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeDeAoipDelay"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyLine1"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyLine2"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyPlayer"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyMpx34"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyAes1"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyAes2"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyAes3"),
        ("ECRESO-FM-TRANS-MIB", "inSeSyAoip"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaLine1"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaLine2"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaPlayer"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaMpx1"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaMpx2"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaMpx3"),
        ("ECRESO-FM-TRANS-MIB", "inSeSaMpx4"),
        ("ECRESO-FM-TRANS-MIB", "inSeBackupsSource"),
        ("ECRESO-FM-TRANS-MIB", "inAlLine1"),
        ("ECRESO-FM-TRANS-MIB", "inAlLine2"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx1"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx2"),
        ("ECRESO-FM-TRANS-MIB", "inAlPlayer"),
        ("ECRESO-FM-TRANS-MIB", "inAlFault"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx3"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx4"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes1"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes2"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes3"),
        ("ECRESO-FM-TRANS-MIB", "inAlAna1"),
        ("ECRESO-FM-TRANS-MIB", "inAlAoip"),
        ("ECRESO-FM-TRANS-MIB", "rdSeDsn"),
        ("ECRESO-FM-TRANS-MIB", "rdSeMainId"),
        ("ECRESO-FM-TRANS-MIB", "rdSeAltId"),
        ("ECRESO-FM-TRANS-MIB", "rdSeCtEnable"),
        ("ECRESO-FM-TRANS-MIB", "rdSeCtOffset"),
        ("ECRESO-FM-TRANS-MIB", "rdMaPi"),
        ("ECRESO-FM-TRANS-MIB", "rdMaPs"),
        ("ECRESO-FM-TRANS-MIB", "rdMaPty"),
        ("ECRESO-FM-TRANS-MIB", "rdMaMs"),
        ("ECRESO-FM-TRANS-MIB", "rdMaDi"),
        ("ECRESO-FM-TRANS-MIB", "rdMaAf"),
        ("ECRESO-FM-TRANS-MIB", "rdMaRt"),
        ("ECRESO-FM-TRANS-MIB", "rdMaPtyn"),
        ("ECRESO-FM-TRANS-MIB", "rdMaGs"),
        ("ECRESO-FM-TRANS-MIB", "rdMaTa"),
        ("ECRESO-FM-TRANS-MIB", "rdMaTp"),
        ("ECRESO-FM-TRANS-MIB", "rdAtPi"),
        ("ECRESO-FM-TRANS-MIB", "rdAtPs"),
        ("ECRESO-FM-TRANS-MIB", "rdAtPty"),
        ("ECRESO-FM-TRANS-MIB", "rdAtMs"),
        ("ECRESO-FM-TRANS-MIB", "rdAtDi"),
        ("ECRESO-FM-TRANS-MIB", "rdAtAf"),
        ("ECRESO-FM-TRANS-MIB", "rdAtRt"),
        ("ECRESO-FM-TRANS-MIB", "rdAtPtyn"),
        ("ECRESO-FM-TRANS-MIB", "rdAtGs"),
        ("ECRESO-FM-TRANS-MIB", "rdAtTa"),
        ("ECRESO-FM-TRANS-MIB", "rdAtTp"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollText"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollRepetition"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollEnable"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollCenter"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollTrunc"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollIncrement"),
        ("ECRESO-FM-TRANS-MIB", "rdPsScrollDelay"),
        ("ECRESO-FM-TRANS-MIB", "rdSeCurrentPs"),
        ("ECRESO-FM-TRANS-MIB", "rdSeCurrentRt"),
        ("ECRESO-FM-TRANS-MIB", "moDevMpx"),
        ("ECRESO-FM-TRANS-MIB", "moDevAudio"),
        ("ECRESO-FM-TRANS-MIB", "moDevPilot"),
        ("ECRESO-FM-TRANS-MIB", "moDevRds"),
        ("ECRESO-FM-TRANS-MIB", "moDevSca"),
        ("ECRESO-FM-TRANS-MIB", "moDevRmsMeas"),
        ("ECRESO-FM-TRANS-MIB", "moDevPeakMeas"),
        ("ECRESO-FM-TRANS-MIB", "moDevPeakMaxMeas"),
        ("ECRESO-FM-TRANS-MIB", "moDevMPeakMaxMeas"),
        ("ECRESO-FM-TRANS-MIB", "moDevSPeakMaxMeas"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoder"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderRdsSelect"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderScaSelect"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderRdsBackup"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderCurrentRds"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderCurrentSca"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoder19kOutLevel"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderAlrRdsSwitch"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderRdsPhase"),
        ("ECRESO-FM-TRANS-MIB", "moSeCoderRdsSelectBackup"),
        ("ECRESO-FM-TRANS-MIB", "moSpClState"),
        ("ECRESO-FM-TRANS-MIB", "moSpClVal"),
        ("ECRESO-FM-TRANS-MIB", "moSpClMeas"),
        ("ECRESO-FM-TRANS-MIB", "moSpMpState"),
        ("ECRESO-FM-TRANS-MIB", "moSpMpTarget"),
        ("ECRESO-FM-TRANS-MIB", "moSpMpMeas1m"),
        ("ECRESO-FM-TRANS-MIB", "moSpMpMeas10s"),
        ("ECRESO-FM-TRANS-MIB", "moSpMpMeasAtt"),
        ("ECRESO-FM-TRANS-MIB", "moSpPrNum"),
        ("ECRESO-FM-TRANS-MIB", "moSpPrBypass"),
        ("ECRESO-FM-TRANS-MIB", "moSpPrTableName"),
        ("ECRESO-FM-TRANS-MIB", "moSfConfDelay"),
        ("ECRESO-FM-TRANS-MIB", "moSfConfState"),
        ("ECRESO-FM-TRANS-MIB", "moSfMeasDelay"),
        ("ECRESO-FM-TRANS-MIB", "moSfAlarm"),
        ("ECRESO-FM-TRANS-MIB", "moSfConfOp10M"),
        ("ECRESO-FM-TRANS-MIB", "moSfState10M"),
        ("ECRESO-FM-TRANS-MIB", "moSfClockSource"),
        ("ECRESO-FM-TRANS-MIB", "moSfState1PPS"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlName"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlPcap"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlType"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlStandby"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlReserveType"),
        ("ECRESO-FM-TRANS-MIB", "txGnAl3dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlFault"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlWarning"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlVSWR"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlLink"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlVswrTrip"),
        ("ECRESO-FM-TRANS-MIB", "txGnAl1dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnMsForwardPower"),
        ("ECRESO-FM-TRANS-MIB", "txGnMsReflectedPower"),
        ("ECRESO-FM-TRANS-MIB", "txGnMsVSWR"),
        ("ECRESO-FM-TRANS-MIB", "txGnMsVswrTrip"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfFrequency"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfThreshold3dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfAutomatic3dBThreshold"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfThresholdVSWR"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfOpmode"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfPower"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfVswrTrip"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfThreshold1dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfMaxPower"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfRfPresentMin"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfVswrTrig"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrCurrent"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrGpioMode"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsFreq"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsPower"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsName"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsThreshold3dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsThreshold1dB"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsRfPresentMin"),
        ("ECRESO-FM-TRANS-MIB", "txGnPrPresetsAuto3dB"),
        ("ECRESO-FM-TRANS-MIB", "txSfMeRangeMin"),
        ("ECRESO-FM-TRANS-MIB", "txSfMeRangeMax"),
        ("ECRESO-FM-TRANS-MIB", "txSfMeCurrentValue"),
        ("ECRESO-FM-TRANS-MIB", "txSfMePwr"),
        ("ECRESO-FM-TRANS-MIB", "txSfMeCurSavings"),
        ("ECRESO-FM-TRANS-MIB", "txSfMeCurBoost"),
        ("ECRESO-FM-TRANS-MIB", "txSfMePcons"),
        ("ECRESO-FM-TRANS-MIB", "txSfMePconsNoSfm"),
        ("ECRESO-FM-TRANS-MIB", "txSfCoState"),
        ("ECRESO-FM-TRANS-MIB", "txSfCoMode"),
        ("ECRESO-FM-TRANS-MIB", "txSfCoRdsCor"),
        ("ECRESO-FM-TRANS-MIB", "txSfCoKwhCost"),
        ("ECRESO-FM-TRANS-MIB", "txSfStAct"),
        ("ECRESO-FM-TRANS-MIB", "txSfStAlarm"),
        ("ECRESO-FM-TRANS-MIB", "txSfLiSavings"),
        ("ECRESO-FM-TRANS-MIB", "txSfLiBoost"),
        ("ECRESO-FM-TRANS-MIB", "txSfLiCredits"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlDelay"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlIterConf"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlOperation"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlPreselection"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlVSWRInhibit"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlReserveControl"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlCurrentMain"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlMainOpmode"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlManSwLoc"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlDelaySwitch"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlDelayStart"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlSwOnFault"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlSwNoComm"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlFault"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlSwitchOver"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "acGnMsIter"),
        ("ECRESO-FM-TRANS-MIB", "acGnMsPos"),
        ("ECRESO-FM-TRANS-MIB", "acGnMsSwitchLast"),
        ("ECRESO-FM-TRANS-MIB", "acTx1GlLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "acTx1AlFault"),
        ("ECRESO-FM-TRANS-MIB", "acTx1AlWarning"),
        ("ECRESO-FM-TRANS-MIB", "acTx1AlCom"),
        ("ECRESO-FM-TRANS-MIB", "acTx1RfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "acTx2GlLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "acTx2AlFault"),
        ("ECRESO-FM-TRANS-MIB", "acTx2AlWarning"),
        ("ECRESO-FM-TRANS-MIB", "acTx2AlCom"),
        ("ECRESO-FM-TRANS-MIB", "acTx2RfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "syGeType"),
        ("ECRESO-FM-TRANS-MIB", "syGeDate"),
        ("ECRESO-FM-TRANS-MIB", "syGeTime"),
        ("ECRESO-FM-TRANS-MIB", "syGeName"),
        ("ECRESO-FM-TRANS-MIB", "syGeHardRel"),
        ("ECRESO-FM-TRANS-MIB", "syGeSoftRel"),
        ("ECRESO-FM-TRANS-MIB", "syGeDateCode"),
        ("ECRESO-FM-TRANS-MIB", "syGeContact"),
        ("ECRESO-FM-TRANS-MIB", "syGeUnit"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "syGeUptime"),
        ("ECRESO-FM-TRANS-MIB", "syGeOptList"),
        ("ECRESO-FM-TRANS-MIB", "syGeLocation"),
        ("ECRESO-FM-TRANS-MIB", "syGeDigMPX"),
        ("ECRESO-FM-TRANS-MIB", "syGeDigMPX2"),
        ("ECRESO-FM-TRANS-MIB", "syGeDigMPX3"),
        ("ECRESO-FM-TRANS-MIB", "syGeAOIPMpx"),
        ("ECRESO-FM-TRANS-MIB", "syAlWarning"),
        ("ECRESO-FM-TRANS-MIB", "syAlFault"),
        ("ECRESO-FM-TRANS-MIB", "syAlAmb"),
        ("ECRESO-FM-TRANS-MIB", "syAlVoltAux"),
        ("ECRESO-FM-TRANS-MIB", "syAlRelay"),
        ("ECRESO-FM-TRANS-MIB", "syAlReserve"),
        ("ECRESO-FM-TRANS-MIB", "syAlInvalidData"),
        ("ECRESO-FM-TRANS-MIB", "syAl24v"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "syAlComm"),
        ("ECRESO-FM-TRANS-MIB", "syAlLogging"),
        ("ECRESO-FM-TRANS-MIB", "syLossOfEth0"),
        ("ECRESO-FM-TRANS-MIB", "syLossOfEth1"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "maMoMaEffTrans"),
        ("ECRESO-FM-TRANS-MIB", "maMoMaEffPa"),
        ("ECRESO-FM-TRANS-MIB", "maMoMaEffPsu"),
        ("ECRESO-FM-TRANS-MIB", "maMoMaEffSys"),
        ("ECRESO-FM-TRANS-MIB", "maMoCcFault"),
        ("ECRESO-FM-TRANS-MIB", "maMoCcWarn"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeAmb"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeLoad1InputTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeLoad1HeatsinkTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeLoad2InputTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeLoad2HeatsinkTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMePressure"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeHeat1"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeHeat2"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMePsuTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeIntTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoMeExcTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlAmb"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlLoad1Heatsink"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlLoad2Heatsink"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlPressure"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlHeat1"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlHeat2"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlTemp1"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlTemp2"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlPsuTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlIntTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoCoAlExcTemp"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlSecPref"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuMe5V"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuMe12V"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuMeN12V"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuMe24V"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuAlVoltAux"),
        ("ECRESO-FM-TRANS-MIB", "maMoAuAl24V"),
        ("ECRESO-FM-TRANS-MIB", "maMoFanSpeed"),
        ("ECRESO-FM-TRANS-MIB", "maMoFanAlarms"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeVolt1"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeVolt2"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeCur1"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeCur2"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeCur3"),
        ("ECRESO-FM-TRANS-MIB", "maMoMeVolt3"),
        ("ECRESO-FM-TRANS-MIB", "maMoMePin"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlVolt1"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlVolt2"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlCur1"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlCur2"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlCur3"),
        ("ECRESO-FM-TRANS-MIB", "maMoAlPin"),
        ("ECRESO-FM-TRANS-MIB", "maDrCommunication"),
        ("ECRESO-FM-TRANS-MIB", "maDrFault"),
        ("ECRESO-FM-TRANS-MIB", "maDrWarning"),
        ("ECRESO-FM-TRANS-MIB", "maDrForwardPower"),
        ("ECRESO-FM-TRANS-MIB", "maDrReflectedPower"),
        ("ECRESO-FM-TRANS-MIB", "maDrHeatsink"),
        ("ECRESO-FM-TRANS-MIB", "maDrFanSpeed"),
        ("ECRESO-FM-TRANS-MIB", "maPaCommunication"),
        ("ECRESO-FM-TRANS-MIB", "maPaFault"),
        ("ECRESO-FM-TRANS-MIB", "maPaWarning"),
        ("ECRESO-FM-TRANS-MIB", "maPaForwardPower"),
        ("ECRESO-FM-TRANS-MIB", "maPaReflectedPower"),
        ("ECRESO-FM-TRANS-MIB", "maPaEfficiency"),
        ("ECRESO-FM-TRANS-MIB", "maPaCurrent"),
        ("ECRESO-FM-TRANS-MIB", "maPaHeatMax"),
        ("ECRESO-FM-TRANS-MIB", "maPaAlrCur"),
        ("ECRESO-FM-TRANS-MIB", "maPaVoltage"),
        ("ECRESO-FM-TRANS-MIB", "maPaAlrVolt"),
        ("ECRESO-FM-TRANS-MIB", "maPaAmbTemp"),
        ("ECRESO-FM-TRANS-MIB", "maPaAlrHeat"),
        ("ECRESO-FM-TRANS-MIB", "maPaAlrTemp"),
        ("ECRESO-FM-TRANS-MIB", "maPsVoltageInput"),
        ("ECRESO-FM-TRANS-MIB", "maPsCurrentInput"),
        ("ECRESO-FM-TRANS-MIB", "maPsPowerInput"),
        ("ECRESO-FM-TRANS-MIB", "maPsVoltageOutput"),
        ("ECRESO-FM-TRANS-MIB", "maPsCurrentOutput"),
        ("ECRESO-FM-TRANS-MIB", "maPsPowerOutput"),
        ("ECRESO-FM-TRANS-MIB", "maPsCommunication"),
        ("ECRESO-FM-TRANS-MIB", "maPsFault"),
        ("ECRESO-FM-TRANS-MIB", "maPsWarning"),
        ("ECRESO-FM-TRANS-MIB", "maPsEfficiency"),
        ("ECRESO-FM-TRANS-MIB", "maPsOutputPower"),
        ("ECRESO-FM-TRANS-MIB", "maPsInputPower"),
        ("ECRESO-FM-TRANS-MIB", "maPsMissing"),
        ("ECRESO-FM-TRANS-MIB", "maPsInputCurrent"),
        ("ECRESO-FM-TRANS-MIB", "maPsInputCurAlr"),
        ("ECRESO-FM-TRANS-MIB", "maPsInputVoltage"),
        ("ECRESO-FM-TRANS-MIB", "maPsInputVoltAlr"),
        ("ECRESO-FM-TRANS-MIB", "maPsOutputCurrent"),
        ("ECRESO-FM-TRANS-MIB", "maPsOutputCurAlr"),
        ("ECRESO-FM-TRANS-MIB", "maPsOutputVoltage"),
        ("ECRESO-FM-TRANS-MIB", "maPsOutputVoltAlr"),
        ("ECRESO-FM-TRANS-MIB", "maPsAmbTemp"),
        ("ECRESO-FM-TRANS-MIB", "maPsAmbAlr"),
        ("ECRESO-FM-TRANS-MIB", "maPsHeat1Temp"),
        ("ECRESO-FM-TRANS-MIB", "maPsHeat1Alr"),
        ("ECRESO-FM-TRANS-MIB", "maPsFan1Speed"),
        ("ECRESO-FM-TRANS-MIB", "maPsFan1Alr"),
        ("ECRESO-FM-TRANS-MIB", "maPsSerial"),
        ("ECRESO-FM-TRANS-MIB", "maPsSoftRel"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrRds"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrSfm"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrActivation"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrSurestream"),
        ("ECRESO-FM-TRANS-MIB", "syLiPrSynchrostream"),
        ("ECRESO-FM-TRANS-MIB", "syLiReRds"),
        ("ECRESO-FM-TRANS-MIB", "syLiReSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "syLiReSfm"),
        ("ECRESO-FM-TRANS-MIB", "syLiReActivation"),
        ("ECRESO-FM-TRANS-MIB", "syLiReAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiReMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiReSurestream"),
        ("ECRESO-FM-TRANS-MIB", "syLiReSynchrostream"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlRds"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSfm"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlActivation"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSurestream"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSynchrostream"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAl3dB"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlFault"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlWarning"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlVSWR"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxRfOpmode"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxRfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcReserveControl"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcFault"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcSwitchOver"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysWarning"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysFault"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlAmb"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlVoltAux"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlRelay"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlReserve"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInSeAlrInputSwitch"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAl1dB"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxGnGlStandby"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlLine1"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlLine2"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx1"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx2"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlPlayer"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlInvalidData"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcGnAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcGnAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAl24v"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlComm"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampEquipmentOn"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOnDownTime"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampHeartBeat"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampConfigChanged"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlFault"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampMoSfAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampMoSfSwitch10MAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyAlLogging"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx3"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx4"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes1"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes2"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes3"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAna1"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxSfStAct"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxSfStAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlRds"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSfm"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlActivation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAoip"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampLossOfEth0"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampLossOfEth1"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSurestream"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSynchrostream"))
)
if mibBuilder.loadTexts:
    objectGroup.setStatus("current")

objectObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 2, 2)
)
objectObsoleteGroup.setObjects(
      *(("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockLoadPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockLoadEnable"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "inSeThMpxTh"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFaultEnable"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampEquipmentFault"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFaultError"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgState"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgDrive"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgAtt"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgRel"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgThr"),
        ("ECRESO-FM-TRANS-MIB", "moSpAgMeas"),
        ("ECRESO-FM-TRANS-MIB", "moSpLimState"),
        ("ECRESO-FM-TRANS-MIB", "moSpLimVal"),
        ("ECRESO-FM-TRANS-MIB", "moSpLimDrive"),
        ("ECRESO-FM-TRANS-MIB", "moSpLimMeas"),
        ("ECRESO-FM-TRANS-MIB", "moSpLimPreset"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeVolt1"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeVolt2"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeCur1"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeCur2"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeEffSys"),
        ("ECRESO-FM-TRANS-MIB", "moMaMeEffTrans"),
        ("ECRESO-FM-TRANS-MIB", "moMaMePin"),
        ("ECRESO-FM-TRANS-MIB", "moMainAlVolt1"),
        ("ECRESO-FM-TRANS-MIB", "moMainAlVolt2"),
        ("ECRESO-FM-TRANS-MIB", "moMainAlCur1"),
        ("ECRESO-FM-TRANS-MIB", "moMainAlCur2"),
        ("ECRESO-FM-TRANS-MIB", "moMainAlPin"),
        ("ECRESO-FM-TRANS-MIB", "moCoMeAmb"),
        ("ECRESO-FM-TRANS-MIB", "moCoMeHeat1"),
        ("ECRESO-FM-TRANS-MIB", "moCoMeHeat2"),
        ("ECRESO-FM-TRANS-MIB", "moCoMePsuTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoMeIntTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoMePressure"),
        ("ECRESO-FM-TRANS-MIB", "moCoMeExcTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlHeat1"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlHeat2"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlTemp1"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlTemp2"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlPsuTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlIntTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlExcTemp"),
        ("ECRESO-FM-TRANS-MIB", "moCoAlPressure"),
        ("ECRESO-FM-TRANS-MIB", "moAuMe5V"),
        ("ECRESO-FM-TRANS-MIB", "moAuMe12V"),
        ("ECRESO-FM-TRANS-MIB", "moAuMeN12V"),
        ("ECRESO-FM-TRANS-MIB", "moFanMeFan1Speed"),
        ("ECRESO-FM-TRANS-MIB", "moFanMeFan2Speed"),
        ("ECRESO-FM-TRANS-MIB", "moFanAlFan1Alarm"),
        ("ECRESO-FM-TRANS-MIB", "moFanAlFan2Alarm"))
)
if mibBuilder.loadTexts:
    objectObsoleteGroup.setStatus("obsolete")


# Notification objects

eventTxLocalMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 1)
)
eventTxLocalMode.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxLocalModePriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlLocalMode"))
)
if mibBuilder.loadTexts:
    eventTxLocalMode.setStatus(
        "current"
    )

eventTxAl3dB = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 2)
)
eventTxAl3dB.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAl3dB"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl3dBPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAl3dB"))
)
if mibBuilder.loadTexts:
    eventTxAl3dB.setStatus(
        "current"
    )

eventTxAlFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 3)
)
eventTxAlFault.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlFault"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlFault"))
)
if mibBuilder.loadTexts:
    eventTxAlFault.setStatus(
        "current"
    )

eventTxAlWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 4)
)
eventTxAlWarning.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlWarning"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlWarningPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlWarning"))
)
if mibBuilder.loadTexts:
    eventTxAlWarning.setStatus(
        "current"
    )

eventTxAlVSWR = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 5)
)
eventTxAlVSWR.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlVSWR"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlVSWRPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlVSWR"))
)
if mibBuilder.loadTexts:
    eventTxAlVSWR.setStatus(
        "current"
    )

eventTxAlInterlockAnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 6)
)
eventTxAlInterlockAnt.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockAntPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlInterlockAnt"))
)
if mibBuilder.loadTexts:
    eventTxAlInterlockAnt.setStatus(
        "current"
    )

eventTxAlInterlockLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 7)
)
eventTxAlInterlockLoad.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockLoadPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAlInterlockLoad"))
)
if mibBuilder.loadTexts:
    eventTxAlInterlockLoad.setStatus(
        "obsolete"
    )

eventTxRfOpmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 8)
)
eventTxRfOpmode.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxRfOpmode"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfOpmodePriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfOpmode"))
)
if mibBuilder.loadTexts:
    eventTxRfOpmode.setStatus(
        "current"
    )

eventTxRfRFPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 9)
)
eventTxRfRFPresent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxRfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfRFPresentPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnRfRFPresent"))
)
if mibBuilder.loadTexts:
    eventTxRfRFPresent.setStatus(
        "current"
    )

eventAcReserveControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 10)
)
eventAcReserveControl.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcReserveControl"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcReserveControlPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlReserveControl"))
)
if mibBuilder.loadTexts:
    eventAcReserveControl.setStatus(
        "current"
    )

eventAcLocalMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 11)
)
eventAcLocalMode.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcLocalModePriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnGlLocalMode"))
)
if mibBuilder.loadTexts:
    eventAcLocalMode.setStatus(
        "current"
    )

eventAcFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 12)
)
eventAcFault.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcFault"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlFault"))
)
if mibBuilder.loadTexts:
    eventAcFault.setStatus(
        "current"
    )

eventAcSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 13)
)
eventAcSwitchOver.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcSwitchOver"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcSwitchOverPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlSwitchOver"))
)
if mibBuilder.loadTexts:
    eventAcSwitchOver.setStatus(
        "current"
    )

eventSysWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 14)
)
eventSysWarning.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysWarning"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysWarningPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlWarning"))
)
if mibBuilder.loadTexts:
    eventSysWarning.setStatus(
        "current"
    )

eventSysFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 15)
)
eventSysFault.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysFault"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlFault"))
)
if mibBuilder.loadTexts:
    eventSysFault.setStatus(
        "current"
    )

eventSysAlAmb = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 16)
)
eventSysAlAmb.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlAmb"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlAmbPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlAmb"))
)
if mibBuilder.loadTexts:
    eventSysAlAmb.setStatus(
        "current"
    )

eventSysAlVoltAux = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 17)
)
eventSysAlVoltAux.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlVoltAux"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlVoltAuxPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlVoltAux"))
)
if mibBuilder.loadTexts:
    eventSysAlVoltAux.setStatus(
        "current"
    )

eventSysAlRelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 18)
)
eventSysAlRelay.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlRelay"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlRelayPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlRelay"))
)
if mibBuilder.loadTexts:
    eventSysAlRelay.setStatus(
        "current"
    )

eventSysAlReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 19)
)
eventSysAlReserve.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlReserve"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlReservePriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlReserve"))
)
if mibBuilder.loadTexts:
    eventSysAlReserve.setStatus(
        "current"
    )

eventInSeAlrInputSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 20)
)
eventInSeAlrInputSwitch.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInSeAlrInputSwitch"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInSeAlrInputSwitchPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inSeAlrInputSwitch"))
)
if mibBuilder.loadTexts:
    eventInSeAlrInputSwitch.setStatus(
        "current"
    )

eventTxAl1dB = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 21)
)
eventTxAl1dB.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxAl1dB"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl1dBPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnAl1dB"))
)
if mibBuilder.loadTexts:
    eventTxAl1dB.setStatus(
        "current"
    )

eventTxGnGlStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 22)
)
eventTxGnGlStandby.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxGnGlStandby"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxGnGlStandbyPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txGnGlStandby"))
)
if mibBuilder.loadTexts:
    eventTxGnGlStandby.setStatus(
        "current"
    )

eventInAlLine1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 23)
)
eventInAlLine1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlLine1"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine1Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlLine1"))
)
if mibBuilder.loadTexts:
    eventInAlLine1.setStatus(
        "current"
    )

eventInAlLine2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 24)
)
eventInAlLine2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlLine2"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine2Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlLine2"))
)
if mibBuilder.loadTexts:
    eventInAlLine2.setStatus(
        "current"
    )

eventInAlMpx1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 25)
)
eventInAlMpx1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx1"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx1Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx1"))
)
if mibBuilder.loadTexts:
    eventInAlMpx1.setStatus(
        "current"
    )

eventInAlMpx2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 26)
)
eventInAlMpx2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx2"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx2Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx2"))
)
if mibBuilder.loadTexts:
    eventInAlMpx2.setStatus(
        "current"
    )

eventInAlPlayer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 27)
)
eventInAlPlayer.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlPlayer"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlPlayerPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlPlayer"))
)
if mibBuilder.loadTexts:
    eventInAlPlayer.setStatus(
        "current"
    )

eventSysAlInvalidData = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 28)
)
eventSysAlInvalidData.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlInvalidData"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlInvalidDataPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlInvalidData"))
)
if mibBuilder.loadTexts:
    eventSysAlInvalidData.setStatus(
        "current"
    )

eventAcGnAlInterlockAnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 29)
)
eventAcGnAlInterlockAnt.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcGnAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockAntPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlInterlockAnt"))
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockAnt.setStatus(
        "current"
    )

eventAcGnAlInterlockLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 30)
)
eventAcGnAlInterlockLoad.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampAcGnAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockLoadPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "acGnAlInterlockLoad"))
)
if mibBuilder.loadTexts:
    eventAcGnAlInterlockLoad.setStatus(
        "current"
    )

eventSysAl24v = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 31)
)
eventSysAl24v.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAl24v"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAl24vPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAl24v"))
)
if mibBuilder.loadTexts:
    eventSysAl24v.setStatus(
        "current"
    )

eventSysAlComm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 32)
)
eventSysAlComm.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSysAlComm"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlCommPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlComm"))
)
if mibBuilder.loadTexts:
    eventSysAlComm.setStatus(
        "current"
    )

eventEquipmentOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 33)
)
eventEquipmentOn.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampEquipmentOn"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOnPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOnDownTime"))
)
if mibBuilder.loadTexts:
    eventEquipmentOn.setStatus(
        "current"
    )

eventHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 34)
)
eventHeartBeat.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampHeartBeat"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventHeartBeatPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"))
)
if mibBuilder.loadTexts:
    eventHeartBeat.setStatus(
        "current"
    )

eventConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 35)
)
eventConfigChanged.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampConfigChanged"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventConfigChangedPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"))
)
if mibBuilder.loadTexts:
    eventConfigChanged.setStatus(
        "current"
    )

eventEquipmentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 36)
)
eventEquipmentFault.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampEquipmentFault"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFaultError"))
)
if mibBuilder.loadTexts:
    eventEquipmentFault.setStatus(
        "obsolete"
    )

eventInAlFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 37)
)
eventInAlFault.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlFault"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlFaultPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlFault"))
)
if mibBuilder.loadTexts:
    eventInAlFault.setStatus(
        "current"
    )

eventMoSfAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 38)
)
eventMoSfAlarm.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampMoSfAlarm"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "moSfAlarm"))
)
if mibBuilder.loadTexts:
    eventMoSfAlarm.setStatus(
        "current"
    )

eventMoSfSwitch10MAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 39)
)
eventMoSfSwitch10MAlarm.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampMoSfSwitch10MAlarm"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "moSfSwitch10MAlarm"))
)
if mibBuilder.loadTexts:
    eventMoSfSwitch10MAlarm.setStatus(
        "current"
    )

eventSyAlLogging = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 40)
)
eventSyAlLogging.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyAlLogging"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyAlLoggingPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syAlLogging"))
)
if mibBuilder.loadTexts:
    eventSyAlLogging.setStatus(
        "current"
    )

eventInAlMpx3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 41)
)
eventInAlMpx3.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx3"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx3Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx3"))
)
if mibBuilder.loadTexts:
    eventInAlMpx3.setStatus(
        "current"
    )

eventInAlMpx4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 42)
)
eventInAlMpx4.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlMpx4"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx4Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlMpx4"))
)
if mibBuilder.loadTexts:
    eventInAlMpx4.setStatus(
        "current"
    )

eventTxSfStAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 43)
)
eventTxSfStAct.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxSfStAct"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStActPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txSfStAct"))
)
if mibBuilder.loadTexts:
    eventTxSfStAct.setStatus(
        "current"
    )

eventTxSfStAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 44)
)
eventTxSfStAlarm.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampTxSfStAlarm"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStAlarmPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "txSfStAlarm"))
)
if mibBuilder.loadTexts:
    eventTxSfStAlarm.setStatus(
        "current"
    )

eventSyLiAlRds = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 45)
)
eventSyLiAlRds.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlRds"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlRdsPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlRds"))
)
if mibBuilder.loadTexts:
    eventSyLiAlRds.setStatus(
        "current"
    )

eventSyLiAlSoundProc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 46)
)
eventSyLiAlSoundProc.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSoundProcPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSoundProc"))
)
if mibBuilder.loadTexts:
    eventSyLiAlSoundProc.setStatus(
        "current"
    )

eventSyLiAlSfm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 47)
)
eventSyLiAlSfm.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSfm"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSfmPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSfm"))
)
if mibBuilder.loadTexts:
    eventSyLiAlSfm.setStatus(
        "current"
    )

eventSyLiAlActivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 48)
)
eventSyLiAlActivation.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlActivation"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlActivationPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlActivation"))
)
if mibBuilder.loadTexts:
    eventSyLiAlActivation.setStatus(
        "current"
    )

eventInAlAes1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 49)
)
eventInAlAes1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes1"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes1Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes1"))
)
if mibBuilder.loadTexts:
    eventInAlAes1.setStatus(
        "current"
    )

eventInAlAes2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 50)
)
eventInAlAes2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes2"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes2Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes2"))
)
if mibBuilder.loadTexts:
    eventInAlAes2.setStatus(
        "current"
    )

eventInAlAes3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 51)
)
eventInAlAes3.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAes3"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes3Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlAes3"))
)
if mibBuilder.loadTexts:
    eventInAlAes3.setStatus(
        "current"
    )

eventInAlAna1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 52)
)
eventInAlAna1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAna1"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAna1Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlAna1"))
)
if mibBuilder.loadTexts:
    eventInAlAna1.setStatus(
        "current"
    )

eventInAlAoip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 53)
)
eventInAlAoip.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampInAlAoip"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAoipPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "inAlAoip"))
)
if mibBuilder.loadTexts:
    eventInAlAoip.setStatus(
        "current"
    )

eventLossOfEth0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 54)
)
eventLossOfEth0.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampLossOfEth0"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth0Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLossOfEth0"))
)
if mibBuilder.loadTexts:
    eventLossOfEth0.setStatus(
        "current"
    )

eventLossOfEth1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 55)
)
eventLossOfEth1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampLossOfEth1"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth1Priority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLossOfEth1"))
)
if mibBuilder.loadTexts:
    eventLossOfEth1.setStatus(
        "current"
    )

eventSyLiAlAoipdecoder = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 56)
)
eventSyLiAlAoipdecoder.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlAoipdecoderPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlAoipdecoder"))
)
if mibBuilder.loadTexts:
    eventSyLiAlAoipdecoder.setStatus(
        "current"
    )

eventSyLiAlMpxoipdecoder = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 57)
)
eventSyLiAlMpxoipdecoder.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlMpxoipdecoderPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlMpxoipdecoder"))
)
if mibBuilder.loadTexts:
    eventSyLiAlMpxoipdecoder.setStatus(
        "current"
    )

eventSyLiAlSurestream = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 58)
)
eventSyLiAlSurestream.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSurestream"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSurestreamPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSurestream"))
)
if mibBuilder.loadTexts:
    eventSyLiAlSurestream.setStatus(
        "current"
    )

eventSyLiAlSynchrostream = NotificationType(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 0, 59)
)
eventSyLiAlSynchrostream.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ECRESO-FM-TRANS-MIB", "eventTimeStampSyLiAlSynchrostream"),
        ("ECRESO-FM-TRANS-MIB", "syGeSerial"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSynchrostreamPriority"),
        ("ECRESO-FM-TRANS-MIB", "syGeTrapCounter"),
        ("ECRESO-FM-TRANS-MIB", "syLiAlSynchrostream"))
)
if mibBuilder.loadTexts:
    eventSyLiAlSynchrostream.setStatus(
        "current"
    )


# Notifications groups

eventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 2, 3)
)
eventGroup.setObjects(
      *(("ECRESO-FM-TRANS-MIB", "eventTxLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl3dB"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlFault"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlWarning"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlVSWR"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfOpmode"),
        ("ECRESO-FM-TRANS-MIB", "eventTxRfRFPresent"),
        ("ECRESO-FM-TRANS-MIB", "eventAcReserveControl"),
        ("ECRESO-FM-TRANS-MIB", "eventAcLocalMode"),
        ("ECRESO-FM-TRANS-MIB", "eventAcFault"),
        ("ECRESO-FM-TRANS-MIB", "eventAcSwitchOver"),
        ("ECRESO-FM-TRANS-MIB", "eventSysWarning"),
        ("ECRESO-FM-TRANS-MIB", "eventSysFault"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlAmb"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlVoltAux"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlRelay"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlReserve"),
        ("ECRESO-FM-TRANS-MIB", "eventInSeAlrInputSwitch"),
        ("ECRESO-FM-TRANS-MIB", "eventTxAl1dB"),
        ("ECRESO-FM-TRANS-MIB", "eventTxGnGlStandby"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine1"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlLine2"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx1"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx2"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlPlayer"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes1"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes2"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAes3"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAna1"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlInvalidData"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockAnt"),
        ("ECRESO-FM-TRANS-MIB", "eventAcGnAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAl24v"),
        ("ECRESO-FM-TRANS-MIB", "eventSysAlComm"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentOn"),
        ("ECRESO-FM-TRANS-MIB", "eventHeartBeat"),
        ("ECRESO-FM-TRANS-MIB", "eventConfigChanged"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlFault"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventMoSfSwitch10MAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventSyAlLogging"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth0"),
        ("ECRESO-FM-TRANS-MIB", "eventLossOfEth1"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx3"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlMpx4"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStAct"),
        ("ECRESO-FM-TRANS-MIB", "eventTxSfStAlarm"),
        ("ECRESO-FM-TRANS-MIB", "eventInAlAoip"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlRds"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSoundProc"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSfm"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlActivation"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlAoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlMpxoipdecoder"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSurestream"),
        ("ECRESO-FM-TRANS-MIB", "eventSyLiAlSynchrostream"))
)
if mibBuilder.loadTexts:
    eventGroup.setStatus(
        "current"
    )

eventObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6404, 3, 1, 2, 2, 4)
)
eventObsoleteGroup.setObjects(
      *(("ECRESO-FM-TRANS-MIB", "eventTxAlInterlockLoad"),
        ("ECRESO-FM-TRANS-MIB", "eventEquipmentFault"))
)
if mibBuilder.loadTexts:
    eventObsoleteGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECRESO-FM-TRANS-MIB",
    **{"ecreso": ecreso,
       "transv3": transv3,
       "fm": fm,
       "transmitter": transmitter,
       "events": events,
       "eventTxLocalMode": eventTxLocalMode,
       "eventTxAl3dB": eventTxAl3dB,
       "eventTxAlFault": eventTxAlFault,
       "eventTxAlWarning": eventTxAlWarning,
       "eventTxAlVSWR": eventTxAlVSWR,
       "eventTxAlInterlockAnt": eventTxAlInterlockAnt,
       "eventTxAlInterlockLoad": eventTxAlInterlockLoad,
       "eventTxRfOpmode": eventTxRfOpmode,
       "eventTxRfRFPresent": eventTxRfRFPresent,
       "eventAcReserveControl": eventAcReserveControl,
       "eventAcLocalMode": eventAcLocalMode,
       "eventAcFault": eventAcFault,
       "eventAcSwitchOver": eventAcSwitchOver,
       "eventSysWarning": eventSysWarning,
       "eventSysFault": eventSysFault,
       "eventSysAlAmb": eventSysAlAmb,
       "eventSysAlVoltAux": eventSysAlVoltAux,
       "eventSysAlRelay": eventSysAlRelay,
       "eventSysAlReserve": eventSysAlReserve,
       "eventInSeAlrInputSwitch": eventInSeAlrInputSwitch,
       "eventTxAl1dB": eventTxAl1dB,
       "eventTxGnGlStandby": eventTxGnGlStandby,
       "eventInAlLine1": eventInAlLine1,
       "eventInAlLine2": eventInAlLine2,
       "eventInAlMpx1": eventInAlMpx1,
       "eventInAlMpx2": eventInAlMpx2,
       "eventInAlPlayer": eventInAlPlayer,
       "eventSysAlInvalidData": eventSysAlInvalidData,
       "eventAcGnAlInterlockAnt": eventAcGnAlInterlockAnt,
       "eventAcGnAlInterlockLoad": eventAcGnAlInterlockLoad,
       "eventSysAl24v": eventSysAl24v,
       "eventSysAlComm": eventSysAlComm,
       "eventEquipmentOn": eventEquipmentOn,
       "eventHeartBeat": eventHeartBeat,
       "eventConfigChanged": eventConfigChanged,
       "eventEquipmentFault": eventEquipmentFault,
       "eventInAlFault": eventInAlFault,
       "eventMoSfAlarm": eventMoSfAlarm,
       "eventMoSfSwitch10MAlarm": eventMoSfSwitch10MAlarm,
       "eventSyAlLogging": eventSyAlLogging,
       "eventInAlMpx3": eventInAlMpx3,
       "eventInAlMpx4": eventInAlMpx4,
       "eventTxSfStAct": eventTxSfStAct,
       "eventTxSfStAlarm": eventTxSfStAlarm,
       "eventSyLiAlRds": eventSyLiAlRds,
       "eventSyLiAlSoundProc": eventSyLiAlSoundProc,
       "eventSyLiAlSfm": eventSyLiAlSfm,
       "eventSyLiAlActivation": eventSyLiAlActivation,
       "eventInAlAes1": eventInAlAes1,
       "eventInAlAes2": eventInAlAes2,
       "eventInAlAes3": eventInAlAes3,
       "eventInAlAna1": eventInAlAna1,
       "eventInAlAoip": eventInAlAoip,
       "eventLossOfEth0": eventLossOfEth0,
       "eventLossOfEth1": eventLossOfEth1,
       "eventSyLiAlAoipdecoder": eventSyLiAlAoipdecoder,
       "eventSyLiAlMpxoipdecoder": eventSyLiAlMpxoipdecoder,
       "eventSyLiAlSurestream": eventSyLiAlSurestream,
       "eventSyLiAlSynchrostream": eventSyLiAlSynchrostream,
       "eventBindings": eventBindings,
       "eventTxLocalModeBindings": eventTxLocalModeBindings,
       "eventTimeStampTxLocalMode": eventTimeStampTxLocalMode,
       "eventTxAl3dBBindings": eventTxAl3dBBindings,
       "eventTimeStampTxAl3dB": eventTimeStampTxAl3dB,
       "eventTxAlFaultBindings": eventTxAlFaultBindings,
       "eventTimeStampTxAlFault": eventTimeStampTxAlFault,
       "eventTxAlWarningBindings": eventTxAlWarningBindings,
       "eventTimeStampTxAlWarning": eventTimeStampTxAlWarning,
       "eventTxAlVSWRBindings": eventTxAlVSWRBindings,
       "eventTimeStampTxAlVSWR": eventTimeStampTxAlVSWR,
       "eventTxAlInterlockAntBindings": eventTxAlInterlockAntBindings,
       "eventTimeStampTxAlInterlockAnt": eventTimeStampTxAlInterlockAnt,
       "eventTxAlInterlockLoadBindings": eventTxAlInterlockLoadBindings,
       "eventTimeStampTxAlInterlockLoad": eventTimeStampTxAlInterlockLoad,
       "eventTxRfOpmodeBindings": eventTxRfOpmodeBindings,
       "eventTimeStampTxRfOpmode": eventTimeStampTxRfOpmode,
       "eventTxRfRFPresentBindings": eventTxRfRFPresentBindings,
       "eventTimeStampTxRfRFPresent": eventTimeStampTxRfRFPresent,
       "eventAcReserveControlBindings": eventAcReserveControlBindings,
       "eventTimeStampAcReserveControl": eventTimeStampAcReserveControl,
       "eventAcLocalModeBindings": eventAcLocalModeBindings,
       "eventTimeStampAcLocalMode": eventTimeStampAcLocalMode,
       "eventAcFaultBindings": eventAcFaultBindings,
       "eventTimeStampAcFault": eventTimeStampAcFault,
       "eventAcSwitchOverBindings": eventAcSwitchOverBindings,
       "eventTimeStampAcSwitchOver": eventTimeStampAcSwitchOver,
       "eventSysWarningBindings": eventSysWarningBindings,
       "eventTimeStampSysWarning": eventTimeStampSysWarning,
       "eventSysFaultBindings": eventSysFaultBindings,
       "eventTimeStampSysFault": eventTimeStampSysFault,
       "eventSysAlAmbBindings": eventSysAlAmbBindings,
       "eventTimeStampSysAlAmb": eventTimeStampSysAlAmb,
       "eventSysAlVoltAuxBindings": eventSysAlVoltAuxBindings,
       "eventTimeStampSysAlVoltAux": eventTimeStampSysAlVoltAux,
       "eventSysAlRelayBindings": eventSysAlRelayBindings,
       "eventTimeStampSysAlRelay": eventTimeStampSysAlRelay,
       "eventSysAlReserveBindings": eventSysAlReserveBindings,
       "eventTimeStampSysAlReserve": eventTimeStampSysAlReserve,
       "eventInSeAlrInputSwitchBindings": eventInSeAlrInputSwitchBindings,
       "eventTimeStampInSeAlrInputSwitch": eventTimeStampInSeAlrInputSwitch,
       "eventTxAl1dBBindings": eventTxAl1dBBindings,
       "eventTimeStampTxAl1dB": eventTimeStampTxAl1dB,
       "eventTxGnGlStandbyBindings": eventTxGnGlStandbyBindings,
       "eventTimeStampTxGnGlStandby": eventTimeStampTxGnGlStandby,
       "eventInAlLine1Bindings": eventInAlLine1Bindings,
       "eventTimeStampInAlLine1": eventTimeStampInAlLine1,
       "eventInAlLine2Bindings": eventInAlLine2Bindings,
       "eventTimeStampInAlLine2": eventTimeStampInAlLine2,
       "eventInAlMpx1Bindings": eventInAlMpx1Bindings,
       "eventTimeStampInAlMpx1": eventTimeStampInAlMpx1,
       "eventInAlMpx2Bindings": eventInAlMpx2Bindings,
       "eventTimeStampInAlMpx2": eventTimeStampInAlMpx2,
       "eventInAlPlayerBindings": eventInAlPlayerBindings,
       "eventTimeStampInAlPlayer": eventTimeStampInAlPlayer,
       "eventSysAlInvalidDataBindings": eventSysAlInvalidDataBindings,
       "eventTimeStampSysAlInvalidData": eventTimeStampSysAlInvalidData,
       "eventAcGnAlInterlockAntBindings": eventAcGnAlInterlockAntBindings,
       "eventTimeStampAcGnAlInterlockAnt": eventTimeStampAcGnAlInterlockAnt,
       "eventAcGnAlInterlockLoadBindings": eventAcGnAlInterlockLoadBindings,
       "eventTimeStampAcGnAlInterlockLoad": eventTimeStampAcGnAlInterlockLoad,
       "eventSysAl24vBindings": eventSysAl24vBindings,
       "eventTimeStampSysAl24v": eventTimeStampSysAl24v,
       "eventSysAlCommBindings": eventSysAlCommBindings,
       "eventTimeStampSysAlComm": eventTimeStampSysAlComm,
       "eventEquipmentOnBindings": eventEquipmentOnBindings,
       "eventTimeStampEquipmentOn": eventTimeStampEquipmentOn,
       "eventEquipmentOnDownTime": eventEquipmentOnDownTime,
       "eventHeartBeatBindings": eventHeartBeatBindings,
       "eventTimeStampHeartBeat": eventTimeStampHeartBeat,
       "eventConfigChangedBindings": eventConfigChangedBindings,
       "eventTimeStampConfigChanged": eventTimeStampConfigChanged,
       "eventEquipmentFaultBindings": eventEquipmentFaultBindings,
       "eventTimeStampEquipmentFault": eventTimeStampEquipmentFault,
       "eventEquipmentFaultError": eventEquipmentFaultError,
       "eventInAlFaultBindings": eventInAlFaultBindings,
       "eventTimeStampInAlFault": eventTimeStampInAlFault,
       "eventMoSfAlarmBindings": eventMoSfAlarmBindings,
       "eventTimeStampMoSfAlarm": eventTimeStampMoSfAlarm,
       "eventMoSfSwitch10MAlarmBindings": eventMoSfSwitch10MAlarmBindings,
       "eventTimeStampMoSfSwitch10MAlarm": eventTimeStampMoSfSwitch10MAlarm,
       "eventSyAlLoggingBindings": eventSyAlLoggingBindings,
       "eventTimeStampSyAlLogging": eventTimeStampSyAlLogging,
       "eventInAlMpx3Bindings": eventInAlMpx3Bindings,
       "eventTimeStampInAlMpx3": eventTimeStampInAlMpx3,
       "eventInAlMpx4Bindings": eventInAlMpx4Bindings,
       "eventTimeStampInAlMpx4": eventTimeStampInAlMpx4,
       "eventTxSfStActBindings": eventTxSfStActBindings,
       "eventTimeStampTxSfStAct": eventTimeStampTxSfStAct,
       "eventTxSfStAlarmBindings": eventTxSfStAlarmBindings,
       "eventTimeStampTxSfStAlarm": eventTimeStampTxSfStAlarm,
       "eventSyLiAlRdsBindings": eventSyLiAlRdsBindings,
       "eventTimeStampSyLiAlRds": eventTimeStampSyLiAlRds,
       "eventSyLiAlSoundProcBindings": eventSyLiAlSoundProcBindings,
       "eventTimeStampSyLiAlSoundProc": eventTimeStampSyLiAlSoundProc,
       "eventSyLiAlSfmBindings": eventSyLiAlSfmBindings,
       "eventTimeStampSyLiAlSfm": eventTimeStampSyLiAlSfm,
       "eventSyLiAlActivationBindings": eventSyLiAlActivationBindings,
       "eventTimeStampSyLiAlActivation": eventTimeStampSyLiAlActivation,
       "eventInAlAes1Bindings": eventInAlAes1Bindings,
       "eventTimeStampInAlAes1": eventTimeStampInAlAes1,
       "eventInAlAes2Bindings": eventInAlAes2Bindings,
       "eventTimeStampInAlAes2": eventTimeStampInAlAes2,
       "eventInAlAes3Bindings": eventInAlAes3Bindings,
       "eventTimeStampInAlAes3": eventTimeStampInAlAes3,
       "eventInAlAna1Bindings": eventInAlAna1Bindings,
       "eventTimeStampInAlAna1": eventTimeStampInAlAna1,
       "eventInAlAoipBindings": eventInAlAoipBindings,
       "eventTimeStampInAlAoip": eventTimeStampInAlAoip,
       "eventLossOfEth0Bindings": eventLossOfEth0Bindings,
       "eventTimeStampLossOfEth0": eventTimeStampLossOfEth0,
       "eventLossOfEth1Bindings": eventLossOfEth1Bindings,
       "eventTimeStampLossOfEth1": eventTimeStampLossOfEth1,
       "eventSyLiAlAoipdecoderBindings": eventSyLiAlAoipdecoderBindings,
       "eventTimeStampSyLiAlAoipdecoder": eventTimeStampSyLiAlAoipdecoder,
       "eventSyLiAlMpxoipdecoderBindings": eventSyLiAlMpxoipdecoderBindings,
       "eventTimeStampSyLiAlMpxoipdecoder": eventTimeStampSyLiAlMpxoipdecoder,
       "eventSyLiAlSurestreamBindings": eventSyLiAlSurestreamBindings,
       "eventTimeStampSyLiAlSurestream": eventTimeStampSyLiAlSurestream,
       "eventSyLiAlSynchrostreamBindings": eventSyLiAlSynchrostreamBindings,
       "eventTimeStampSyLiAlSynchrostream": eventTimeStampSyLiAlSynchrostream,
       "groups": groups,
       "objectGroup": objectGroup,
       "objectObsoleteGroup": objectObsoleteGroup,
       "eventGroup": eventGroup,
       "eventObsoleteGroup": eventObsoleteGroup,
       "eventsParams": eventsParams,
       "eventTxLocalModeParams": eventTxLocalModeParams,
       "eventTxLocalModePriority": eventTxLocalModePriority,
       "eventTxLocalModeEnable": eventTxLocalModeEnable,
       "txLocalModeSignalSuppression": txLocalModeSignalSuppression,
       "eventTxAl3dBParams": eventTxAl3dBParams,
       "eventTxAl3dBPriority": eventTxAl3dBPriority,
       "eventTxAl3dBEnable": eventTxAl3dBEnable,
       "eventTxAlFaultParams": eventTxAlFaultParams,
       "eventTxAlFaultPriority": eventTxAlFaultPriority,
       "eventTxAlFaultEnable": eventTxAlFaultEnable,
       "eventTxAlWarningParams": eventTxAlWarningParams,
       "eventTxAlWarningPriority": eventTxAlWarningPriority,
       "eventTxAlWarningEnable": eventTxAlWarningEnable,
       "eventTxAlVSWRParams": eventTxAlVSWRParams,
       "eventTxAlVSWRPriority": eventTxAlVSWRPriority,
       "eventTxAlVSWREnable": eventTxAlVSWREnable,
       "eventTxAlInterlockAntParams": eventTxAlInterlockAntParams,
       "eventTxAlInterlockAntPriority": eventTxAlInterlockAntPriority,
       "eventTxAlInterlockAntEnable": eventTxAlInterlockAntEnable,
       "eventTxAlInterlockLoadParams": eventTxAlInterlockLoadParams,
       "eventTxAlInterlockLoadPriority": eventTxAlInterlockLoadPriority,
       "eventTxAlInterlockLoadEnable": eventTxAlInterlockLoadEnable,
       "eventTxRfOpmodeParams": eventTxRfOpmodeParams,
       "eventTxRfOpmodePriority": eventTxRfOpmodePriority,
       "eventTxRfOpmodeEnable": eventTxRfOpmodeEnable,
       "eventTxRfRFPresentParams": eventTxRfRFPresentParams,
       "eventTxRfRFPresentPriority": eventTxRfRFPresentPriority,
       "eventTxRfRFPresentEnable": eventTxRfRFPresentEnable,
       "eventAcReserveControlParams": eventAcReserveControlParams,
       "eventAcReserveControlPriority": eventAcReserveControlPriority,
       "eventAcReserveControlEnable": eventAcReserveControlEnable,
       "eventAcLocalModeParams": eventAcLocalModeParams,
       "eventAcLocalModePriority": eventAcLocalModePriority,
       "eventAcLocalModeEnable": eventAcLocalModeEnable,
       "acLocalModeSignalSuppression": acLocalModeSignalSuppression,
       "eventAcFaultParams": eventAcFaultParams,
       "eventAcFaultPriority": eventAcFaultPriority,
       "eventAcFaultEnable": eventAcFaultEnable,
       "eventAcSwitchOverParams": eventAcSwitchOverParams,
       "eventAcSwitchOverPriority": eventAcSwitchOverPriority,
       "eventAcSwitchOverEnable": eventAcSwitchOverEnable,
       "eventSysWarningParams": eventSysWarningParams,
       "eventSysWarningPriority": eventSysWarningPriority,
       "eventSysWarningEnable": eventSysWarningEnable,
       "eventSysFaultParams": eventSysFaultParams,
       "eventSysFaultPriority": eventSysFaultPriority,
       "eventSysFaultEnable": eventSysFaultEnable,
       "eventSysAlAmbParams": eventSysAlAmbParams,
       "eventSysAlAmbPriority": eventSysAlAmbPriority,
       "eventSysAlAmbEnable": eventSysAlAmbEnable,
       "eventSysAlVoltAuxParams": eventSysAlVoltAuxParams,
       "eventSysAlVoltAuxPriority": eventSysAlVoltAuxPriority,
       "eventSysAlVoltAuxEnable": eventSysAlVoltAuxEnable,
       "eventSysAlRelayParams": eventSysAlRelayParams,
       "eventSysAlRelayPriority": eventSysAlRelayPriority,
       "eventSysAlRelayEnable": eventSysAlRelayEnable,
       "eventSysAlReserveParams": eventSysAlReserveParams,
       "eventSysAlReservePriority": eventSysAlReservePriority,
       "eventSysAlReserveEnable": eventSysAlReserveEnable,
       "eventInSeAlrInputSwitchParams": eventInSeAlrInputSwitchParams,
       "eventInSeAlrInputSwitchPriority": eventInSeAlrInputSwitchPriority,
       "eventInSeAlrInputSwitchEnable": eventInSeAlrInputSwitchEnable,
       "eventTxAl1dBParams": eventTxAl1dBParams,
       "eventTxAl1dBPriority": eventTxAl1dBPriority,
       "eventTxAl1dBEnable": eventTxAl1dBEnable,
       "eventTxGnGlStandbyParams": eventTxGnGlStandbyParams,
       "eventTxGnGlStandbyPriority": eventTxGnGlStandbyPriority,
       "eventTxGnGlStandbyEnable": eventTxGnGlStandbyEnable,
       "eventInAlLine1Params": eventInAlLine1Params,
       "eventInAlLine1Priority": eventInAlLine1Priority,
       "eventInAlLine1Enable": eventInAlLine1Enable,
       "eventInAlLine2Params": eventInAlLine2Params,
       "eventInAlLine2Priority": eventInAlLine2Priority,
       "eventInAlLine2Enable": eventInAlLine2Enable,
       "eventInAlMpx1Params": eventInAlMpx1Params,
       "eventInAlMpx1Priority": eventInAlMpx1Priority,
       "eventInAlMpx1Enable": eventInAlMpx1Enable,
       "eventInAlMpx2Params": eventInAlMpx2Params,
       "eventInAlMpx2Priority": eventInAlMpx2Priority,
       "eventInAlMpx2Enable": eventInAlMpx2Enable,
       "eventInAlPlayerParams": eventInAlPlayerParams,
       "eventInAlPlayerPriority": eventInAlPlayerPriority,
       "eventInAlPlayerEnable": eventInAlPlayerEnable,
       "eventSysAlInvalidDataParams": eventSysAlInvalidDataParams,
       "eventSysAlInvalidDataPriority": eventSysAlInvalidDataPriority,
       "eventSysAlInvalidDataEnable": eventSysAlInvalidDataEnable,
       "eventAcGnAlInterlockAntParams": eventAcGnAlInterlockAntParams,
       "eventAcGnAlInterlockAntPriority": eventAcGnAlInterlockAntPriority,
       "eventAcGnAlInterlockAntEnable": eventAcGnAlInterlockAntEnable,
       "eventAcGnAlInterlockLoadParams": eventAcGnAlInterlockLoadParams,
       "eventAcGnAlInterlockLoadPriority": eventAcGnAlInterlockLoadPriority,
       "eventAcGnAlInterlockLoadEnable": eventAcGnAlInterlockLoadEnable,
       "eventSysAl24vParams": eventSysAl24vParams,
       "eventSysAl24vPriority": eventSysAl24vPriority,
       "eventSysAl24vEnable": eventSysAl24vEnable,
       "eventSysAlCommParams": eventSysAlCommParams,
       "eventSysAlCommPriority": eventSysAlCommPriority,
       "eventSysAlCommEnable": eventSysAlCommEnable,
       "eventEquipmentOnParams": eventEquipmentOnParams,
       "eventEquipmentOnPriority": eventEquipmentOnPriority,
       "eventEquipmentOnEnable": eventEquipmentOnEnable,
       "eventHeartBeatParams": eventHeartBeatParams,
       "eventHeartBeatPriority": eventHeartBeatPriority,
       "eventHeartBeatEnable": eventHeartBeatEnable,
       "eventConfigChangedParams": eventConfigChangedParams,
       "eventConfigChangedPriority": eventConfigChangedPriority,
       "eventConfigChangedEnable": eventConfigChangedEnable,
       "eventEquipmentFaultParams": eventEquipmentFaultParams,
       "eventEquipmentFaultPriority": eventEquipmentFaultPriority,
       "eventEquipmentFaultEnable": eventEquipmentFaultEnable,
       "eventInAlFaultParams": eventInAlFaultParams,
       "eventInAlFaultPriority": eventInAlFaultPriority,
       "eventInAlFaultEnable": eventInAlFaultEnable,
       "eventMoSfAlarmParams": eventMoSfAlarmParams,
       "eventMoSfAlarmPriority": eventMoSfAlarmPriority,
       "eventMoSfAlarmEnable": eventMoSfAlarmEnable,
       "eventMoSfSwitch10MAlarmParams": eventMoSfSwitch10MAlarmParams,
       "eventMoSfSwitch10MAlarmPriority": eventMoSfSwitch10MAlarmPriority,
       "eventMoSfSwitch10MAlarmEnable": eventMoSfSwitch10MAlarmEnable,
       "eventSyAlLoggingParams": eventSyAlLoggingParams,
       "eventSyAlLoggingPriority": eventSyAlLoggingPriority,
       "eventSyAlLoggingEnable": eventSyAlLoggingEnable,
       "eventInAlMpx3Params": eventInAlMpx3Params,
       "eventInAlMpx3Priority": eventInAlMpx3Priority,
       "eventInAlMpx3Enable": eventInAlMpx3Enable,
       "eventInAlMpx4Params": eventInAlMpx4Params,
       "eventInAlMpx4Priority": eventInAlMpx4Priority,
       "eventInAlMpx4Enable": eventInAlMpx4Enable,
       "eventTxSfStActParams": eventTxSfStActParams,
       "eventTxSfStActPriority": eventTxSfStActPriority,
       "eventTxSfStActEnable": eventTxSfStActEnable,
       "eventTxSfStAlarmParams": eventTxSfStAlarmParams,
       "eventTxSfStAlarmPriority": eventTxSfStAlarmPriority,
       "eventTxSfStAlarmEnable": eventTxSfStAlarmEnable,
       "eventSyLiAlRdsParams": eventSyLiAlRdsParams,
       "eventSyLiAlRdsPriority": eventSyLiAlRdsPriority,
       "eventSyLiAlRdsEnable": eventSyLiAlRdsEnable,
       "eventSyLiAlSoundProcParams": eventSyLiAlSoundProcParams,
       "eventSyLiAlSoundProcPriority": eventSyLiAlSoundProcPriority,
       "eventSyLiAlSoundProcEnable": eventSyLiAlSoundProcEnable,
       "eventSyLiAlSfmParams": eventSyLiAlSfmParams,
       "eventSyLiAlSfmPriority": eventSyLiAlSfmPriority,
       "eventSyLiAlSfmEnable": eventSyLiAlSfmEnable,
       "eventSyLiAlActivationParams": eventSyLiAlActivationParams,
       "eventSyLiAlActivationPriority": eventSyLiAlActivationPriority,
       "eventSyLiAlActivationEnable": eventSyLiAlActivationEnable,
       "eventInAlAes1Params": eventInAlAes1Params,
       "eventInAlAes1Priority": eventInAlAes1Priority,
       "eventInAlAes1Enable": eventInAlAes1Enable,
       "eventInAlAes2Params": eventInAlAes2Params,
       "eventInAlAes2Priority": eventInAlAes2Priority,
       "eventInAlAes2Enable": eventInAlAes2Enable,
       "eventInAlAes3Params": eventInAlAes3Params,
       "eventInAlAes3Priority": eventInAlAes3Priority,
       "eventInAlAes3Enable": eventInAlAes3Enable,
       "eventInAlAna1Params": eventInAlAna1Params,
       "eventInAlAna1Priority": eventInAlAna1Priority,
       "eventInAlAna1Enable": eventInAlAna1Enable,
       "eventInAlAoipParams": eventInAlAoipParams,
       "eventInAlAoipPriority": eventInAlAoipPriority,
       "eventInAlAoipEnable": eventInAlAoipEnable,
       "eventLossOfEth0Params": eventLossOfEth0Params,
       "eventLossOfEth0Priority": eventLossOfEth0Priority,
       "eventLossOfEth0Enable": eventLossOfEth0Enable,
       "eventLossOfEth1Params": eventLossOfEth1Params,
       "eventLossOfEth1Priority": eventLossOfEth1Priority,
       "eventLossOfEth1Enable": eventLossOfEth1Enable,
       "eventSyLiAlAoipdecoderParams": eventSyLiAlAoipdecoderParams,
       "eventSyLiAlAoipdecoderPriority": eventSyLiAlAoipdecoderPriority,
       "eventSyLiAlAoipdecoderEnable": eventSyLiAlAoipdecoderEnable,
       "eventSyLiAlMpxoipdecoderParams": eventSyLiAlMpxoipdecoderParams,
       "eventSyLiAlMpxoipdecoderPriority": eventSyLiAlMpxoipdecoderPriority,
       "eventSyLiAlMpxoipdecoderEnable": eventSyLiAlMpxoipdecoderEnable,
       "eventSyLiAlSurestreamParams": eventSyLiAlSurestreamParams,
       "eventSyLiAlSurestreamPriority": eventSyLiAlSurestreamPriority,
       "eventSyLiAlSurestreamEnable": eventSyLiAlSurestreamEnable,
       "eventSyLiAlSynchrostreamParams": eventSyLiAlSynchrostreamParams,
       "eventSyLiAlSynchrostreamPriority": eventSyLiAlSynchrostreamPriority,
       "eventSyLiAlSynchrostreamEnable": eventSyLiAlSynchrostreamEnable,
       "inputs": inputs,
       "inSource": inSource,
       "inSoLine1": inSoLine1,
       "inSoL1Presence": inSoL1Presence,
       "inSoL1Type": inSoL1Type,
       "inSoL1LeftPeakMax": inSoL1LeftPeakMax,
       "inSoL1RightPeakMax": inSoL1RightPeakMax,
       "inSoL1LeftPeak": inSoL1LeftPeak,
       "inSoL1RightPeak": inSoL1RightPeak,
       "inSoL1Level": inSoL1Level,
       "inSoL1Drive": inSoL1Drive,
       "inSoL1Trim": inSoL1Trim,
       "inSoL1Filter": inSoL1Filter,
       "inSoL1Preacc": inSoL1Preacc,
       "inSoL1Lost": inSoL1Lost,
       "inSoL1AlarmTrig": inSoL1AlarmTrig,
       "inSoLine2": inSoLine2,
       "inSoL2Presence": inSoL2Presence,
       "inSoL2Type": inSoL2Type,
       "inSoL2LeftPeakMax": inSoL2LeftPeakMax,
       "inSoL2RightPeakMax": inSoL2RightPeakMax,
       "inSoL2LeftPeak": inSoL2LeftPeak,
       "inSoL2RightPeak": inSoL2RightPeak,
       "inSoL2Level": inSoL2Level,
       "inSoL2Drive": inSoL2Drive,
       "inSoL2Trim": inSoL2Trim,
       "inSoL2Filter": inSoL2Filter,
       "inSoL2Preacc": inSoL2Preacc,
       "inSoL2Lost": inSoL2Lost,
       "inSoL2AlarmTrig": inSoL2AlarmTrig,
       "inSoMpx1": inSoMpx1,
       "inSoM1Presence": inSoM1Presence,
       "inSoM1PeakMax": inSoM1PeakMax,
       "inSoM1Peak": inSoM1Peak,
       "inSoM1Level": inSoM1Level,
       "inSoM1Drive": inSoM1Drive,
       "inSoM1Lost": inSoM1Lost,
       "inSoM1AlarmTrig": inSoM1AlarmTrig,
       "inSoMpx2": inSoMpx2,
       "inSoM2Presence": inSoM2Presence,
       "inSoM2PeakMax": inSoM2PeakMax,
       "inSoM2Peak": inSoM2Peak,
       "inSoM2Level": inSoM2Level,
       "inSoM2Drive": inSoM2Drive,
       "inSoM2Lost": inSoM2Lost,
       "inSoM2AlarmTrig": inSoM2AlarmTrig,
       "inSoPlayer": inSoPlayer,
       "inSoPlPresence": inSoPlPresence,
       "inSoPlLeftPeakMax": inSoPlLeftPeakMax,
       "inSoPlRightPeakMax": inSoPlRightPeakMax,
       "inSoPlLeftPeak": inSoPlLeftPeak,
       "inSoPlRightPeak": inSoPlRightPeak,
       "inSoPlLevel": inSoPlLevel,
       "inSoPlDrive": inSoPlDrive,
       "inSoPlTrim": inSoPlTrim,
       "inSoPlFilter": inSoPlFilter,
       "inSoPlPreacc": inSoPlPreacc,
       "inSoPlSampling": inSoPlSampling,
       "inSoPlLost": inSoPlLost,
       "inSoPlAlarmTrig": inSoPlAlarmTrig,
       "inSoGenerator": inSoGenerator,
       "inSoGeState": inSoGeState,
       "inSoGeLevel1": inSoGeLevel1,
       "inSoGeLevel2": inSoGeLevel2,
       "inSoGeFreq1": inSoGeFreq1,
       "inSoGeFreq2": inSoGeFreq2,
       "inSoGePreacc": inSoGePreacc,
       "inSoMpx3": inSoMpx3,
       "inSoM3Presence": inSoM3Presence,
       "inSoM3PeakMax": inSoM3PeakMax,
       "inSoM3Peak": inSoM3Peak,
       "inSoM3Level": inSoM3Level,
       "inSoM3Drive": inSoM3Drive,
       "inSoM3Lost": inSoM3Lost,
       "inSoM3AlarmTrig": inSoM3AlarmTrig,
       "inSoMpx4": inSoMpx4,
       "inSoM4Presence": inSoM4Presence,
       "inSoM4PeakMax": inSoM4PeakMax,
       "inSoM4Peak": inSoM4Peak,
       "inSoM4Level": inSoM4Level,
       "inSoM4Drive": inSoM4Drive,
       "inSoM4Lost": inSoM4Lost,
       "inSoM4AlarmTrig": inSoM4AlarmTrig,
       "inSoAes1": inSoAes1,
       "inSoAes1Presence": inSoAes1Presence,
       "inSoAes1LeftPeakMax": inSoAes1LeftPeakMax,
       "inSoAes1RightPeakMax": inSoAes1RightPeakMax,
       "inSoAes1LeftPeak": inSoAes1LeftPeak,
       "inSoAes1RightPeak": inSoAes1RightPeak,
       "inSoAes1PeakMax": inSoAes1PeakMax,
       "inSoAes1Peak": inSoAes1Peak,
       "inSoAes1Level": inSoAes1Level,
       "inSoAes1Drive": inSoAes1Drive,
       "inSoAes1Trim": inSoAes1Trim,
       "inSoAes1Filter": inSoAes1Filter,
       "inSoAes1Preacc": inSoAes1Preacc,
       "inSoAes1Lost": inSoAes1Lost,
       "inSoAes1AlarmTrig": inSoAes1AlarmTrig,
       "inSoAes2": inSoAes2,
       "inSoAes2Presence": inSoAes2Presence,
       "inSoAes2LeftPeakMax": inSoAes2LeftPeakMax,
       "inSoAes2RightPeakMax": inSoAes2RightPeakMax,
       "inSoAes2LeftPeak": inSoAes2LeftPeak,
       "inSoAes2RightPeak": inSoAes2RightPeak,
       "inSoAes2PeakMax": inSoAes2PeakMax,
       "inSoAes2Peak": inSoAes2Peak,
       "inSoAes2Level": inSoAes2Level,
       "inSoAes2Drive": inSoAes2Drive,
       "inSoAes2Trim": inSoAes2Trim,
       "inSoAes2Filter": inSoAes2Filter,
       "inSoAes2Preacc": inSoAes2Preacc,
       "inSoAes2Lost": inSoAes2Lost,
       "inSoAes2AlarmTrig": inSoAes2AlarmTrig,
       "inSoAes3": inSoAes3,
       "inSoAes3Presence": inSoAes3Presence,
       "inSoAes3LeftPeakMax": inSoAes3LeftPeakMax,
       "inSoAes3RightPeakMax": inSoAes3RightPeakMax,
       "inSoAes3LeftPeak": inSoAes3LeftPeak,
       "inSoAes3RightPeak": inSoAes3RightPeak,
       "inSoAes3PeakMax": inSoAes3PeakMax,
       "inSoAes3Peak": inSoAes3Peak,
       "inSoAes3Level": inSoAes3Level,
       "inSoAes3Drive": inSoAes3Drive,
       "inSoAes3Trim": inSoAes3Trim,
       "inSoAes3Filter": inSoAes3Filter,
       "inSoAes3Preacc": inSoAes3Preacc,
       "inSoAes3Lost": inSoAes3Lost,
       "inSoAes3AlarmTrig": inSoAes3AlarmTrig,
       "inSoAna1": inSoAna1,
       "inSoAna1Presence": inSoAna1Presence,
       "inSoAna1LeftPeakMax": inSoAna1LeftPeakMax,
       "inSoAna1RightPeakMax": inSoAna1RightPeakMax,
       "inSoAna1LeftPeak": inSoAna1LeftPeak,
       "inSoAna1RightPeak": inSoAna1RightPeak,
       "inSoAna1Level": inSoAna1Level,
       "inSoAna1Drive": inSoAna1Drive,
       "inSoAna1Trim": inSoAna1Trim,
       "inSoAna1Filter": inSoAna1Filter,
       "inSoAna1Preacc": inSoAna1Preacc,
       "inSoAna1Lost": inSoAna1Lost,
       "inSoAna1AlarmTrig": inSoAna1AlarmTrig,
       "inSoType": inSoType,
       "inSoTySlot1": inSoTySlot1,
       "inSoTySlot2": inSoTySlot2,
       "inSoTySlot3": inSoTySlot3,
       "inSoAoip": inSoAoip,
       "inSoAoipPresence": inSoAoipPresence,
       "inSoAoipLeftPeakMax": inSoAoipLeftPeakMax,
       "inSoAoipRightPeakMax": inSoAoipRightPeakMax,
       "inSoAoipLeftPeak": inSoAoipLeftPeak,
       "inSoAoipRightPeak": inSoAoipRightPeak,
       "inSoAoipPeakMax": inSoAoipPeakMax,
       "inSoAoipPeak": inSoAoipPeak,
       "inSoAoipLevel": inSoAoipLevel,
       "inSoAoipDrive": inSoAoipDrive,
       "inSoAoipTrim": inSoAoipTrim,
       "inSoAoipFilter": inSoAoipFilter,
       "inSoAoipPreacc": inSoAoipPreacc,
       "inSoAoipLost": inSoAoipLost,
       "inSoAoipAlarmTrig": inSoAoipAlarmTrig,
       "inSelect": inSelect,
       "inSeAudio": inSeAudio,
       "inSeLine1Prio": inSeLine1Prio,
       "inSeLine2Prio": inSeLine2Prio,
       "inSeMpx1Prio": inSeMpx1Prio,
       "inSeMpx2Prio": inSeMpx2Prio,
       "inSePlayerPrio": inSePlayerPrio,
       "inSeCrossfade": inSeCrossfade,
       "inSeSelectAudio": inSeSelectAudio,
       "inSeCurrentAudio": inSeCurrentAudio,
       "inSeAlrInputSwitch": inSeAlrInputSwitch,
       "inSeFadein": inSeFadein,
       "inSeMpx3Prio": inSeMpx3Prio,
       "inSeMpx4Prio": inSeMpx4Prio,
       "inSeBackupsTable": inSeBackupsTable,
       "inSeBackupsEntry": inSeBackupsEntry,
       "inSeBackupsIndex": inSeBackupsIndex,
       "inSeBackupsSource": inSeBackupsSource,
       "inSeAuBackupMode": inSeAuBackupMode,
       "inSeThresholds": inSeThresholds,
       "inSeThLine1Th": inSeThLine1Th,
       "inSeThLine1Sil": inSeThLine1Sil,
       "inSeThLine2Th": inSeThLine2Th,
       "inSeThLine2Sil": inSeThLine2Sil,
       "inSeThPlayerTh": inSeThPlayerTh,
       "inSeThPlayerSil": inSeThPlayerSil,
       "inSeThMpxTh": inSeThMpxTh,
       "inSeThMpx1Th": inSeThMpx1Th,
       "inSeThMpx2Th": inSeThMpx2Th,
       "inSeThMpx3Th": inSeThMpx3Th,
       "inSeThMpx4Th": inSeThMpx4Th,
       "inSeThAes1Th": inSeThAes1Th,
       "inSeThAes1Sil": inSeThAes1Sil,
       "inSeThAes2Th": inSeThAes2Th,
       "inSeThAes2Sil": inSeThAes2Sil,
       "inSeThAes3Th": inSeThAes3Th,
       "inSeThAes3Sil": inSeThAes3Sil,
       "inSeThAna1Th": inSeThAna1Th,
       "inSeThAna1Sil": inSeThAna1Sil,
       "inSeThAoipTh": inSeThAoipTh,
       "inSeThAoipSil": inSeThAoipSil,
       "inSeDelays": inSeDelays,
       "inSeDeLine1BackDelay": inSeDeLine1BackDelay,
       "inSeDeLine1Delay": inSeDeLine1Delay,
       "inSeDeLine2BackDelay": inSeDeLine2BackDelay,
       "inSeDeLine2Delay": inSeDeLine2Delay,
       "inSeDePlayerBackDelay": inSeDePlayerBackDelay,
       "inSeDePlayerDelay": inSeDePlayerDelay,
       "inSeDeMpxBackDelay": inSeDeMpxBackDelay,
       "inSeDeMpxDelay": inSeDeMpxDelay,
       "inSeDeMpx34BackDelay": inSeDeMpx34BackDelay,
       "inSeDeMpx34Delay": inSeDeMpx34Delay,
       "inSeDeAes1BackDelay": inSeDeAes1BackDelay,
       "inSeDeAes1Delay": inSeDeAes1Delay,
       "inSeDeAes2BackDelay": inSeDeAes2BackDelay,
       "inSeDeAes2Delay": inSeDeAes2Delay,
       "inSeDeAes3BackDelay": inSeDeAes3BackDelay,
       "inSeDeAes3Delay": inSeDeAes3Delay,
       "inSeDeAna1BackDelay": inSeDeAna1BackDelay,
       "inSeDeAna1Delay": inSeDeAna1Delay,
       "inSeDeMpx1BackDelay": inSeDeMpx1BackDelay,
       "inSeDeMpx1Delay": inSeDeMpx1Delay,
       "inSeDeMpx2BackDelay": inSeDeMpx2BackDelay,
       "inSeDeMpx2Delay": inSeDeMpx2Delay,
       "inSeDeAoipBackDelay": inSeDeAoipBackDelay,
       "inSeDeAoipDelay": inSeDeAoipDelay,
       "inSeSync": inSeSync,
       "inSeSyLine1": inSeSyLine1,
       "inSeSyLine2": inSeSyLine2,
       "inSeSyPlayer": inSeSyPlayer,
       "inSeSyMpx34": inSeSyMpx34,
       "inSeSyAes1": inSeSyAes1,
       "inSeSyAes2": inSeSyAes2,
       "inSeSyAes3": inSeSyAes3,
       "inSeSyAoip": inSeSyAoip,
       "inSeSampling": inSeSampling,
       "inSeSaLine1": inSeSaLine1,
       "inSeSaLine2": inSeSaLine2,
       "inSeSaPlayer": inSeSaPlayer,
       "inSeSaMpx1": inSeSaMpx1,
       "inSeSaMpx2": inSeSaMpx2,
       "inSeSaMpx3": inSeSaMpx3,
       "inSeSaMpx4": inSeSaMpx4,
       "inAlarms": inAlarms,
       "inAlLine1": inAlLine1,
       "inAlLine2": inAlLine2,
       "inAlMpx1": inAlMpx1,
       "inAlMpx2": inAlMpx2,
       "inAlPlayer": inAlPlayer,
       "inAlFault": inAlFault,
       "inAlMpx3": inAlMpx3,
       "inAlMpx4": inAlMpx4,
       "inAlAes1": inAlAes1,
       "inAlAes2": inAlAes2,
       "inAlAes3": inAlAes3,
       "inAlAna1": inAlAna1,
       "inAlAoip": inAlAoip,
       "rds": rds,
       "rdSettings": rdSettings,
       "rdSeDsn": rdSeDsn,
       "rdSeMainId": rdSeMainId,
       "rdSeAltId": rdSeAltId,
       "rdSeCtEnable": rdSeCtEnable,
       "rdSeCtOffset": rdSeCtOffset,
       "rdSeCurrentPs": rdSeCurrentPs,
       "rdSeCurrentRt": rdSeCurrentRt,
       "rdMain": rdMain,
       "rdMaPi": rdMaPi,
       "rdMaPs": rdMaPs,
       "rdMaPty": rdMaPty,
       "rdMaMs": rdMaMs,
       "rdMaDi": rdMaDi,
       "rdMaAf": rdMaAf,
       "rdMaRt": rdMaRt,
       "rdMaPtyn": rdMaPtyn,
       "rdMaGs": rdMaGs,
       "rdMaTa": rdMaTa,
       "rdMaTp": rdMaTp,
       "rdAlt": rdAlt,
       "rdAtPi": rdAtPi,
       "rdAtPs": rdAtPs,
       "rdAtPty": rdAtPty,
       "rdAtMs": rdAtMs,
       "rdAtDi": rdAtDi,
       "rdAtAf": rdAtAf,
       "rdAtRt": rdAtRt,
       "rdAtPtyn": rdAtPtyn,
       "rdAtGs": rdAtGs,
       "rdAtTa": rdAtTa,
       "rdAtTp": rdAtTp,
       "rdPsScrollTable": rdPsScrollTable,
       "rdPsScrollEntry": rdPsScrollEntry,
       "rdPsScrollIndex": rdPsScrollIndex,
       "rdPsScrollText": rdPsScrollText,
       "rdPsScrollRepetition": rdPsScrollRepetition,
       "rdPsScrollEnable": rdPsScrollEnable,
       "rdPsScrollCenter": rdPsScrollCenter,
       "rdPsScrollTrunc": rdPsScrollTrunc,
       "rdPsScrollIncrement": rdPsScrollIncrement,
       "rdPsScrollDelay": rdPsScrollDelay,
       "modulator": modulator,
       "moDeviation": moDeviation,
       "moDevMpx": moDevMpx,
       "moDevAudio": moDevAudio,
       "moDevPilot": moDevPilot,
       "moDevRds": moDevRds,
       "moDevSca": moDevSca,
       "moDevRmsMeas": moDevRmsMeas,
       "moDevPeakMeas": moDevPeakMeas,
       "moDevPeakMaxMeas": moDevPeakMaxMeas,
       "moDevMPeakMaxMeas": moDevMPeakMaxMeas,
       "moDevSPeakMaxMeas": moDevSPeakMaxMeas,
       "moSettings": moSettings,
       "moSeCoder": moSeCoder,
       "moSeCoderRdsSelect": moSeCoderRdsSelect,
       "moSeCoderScaSelect": moSeCoderScaSelect,
       "moSeCoderRdsBackup": moSeCoderRdsBackup,
       "moSeCoderCurrentRds": moSeCoderCurrentRds,
       "moSeCoderCurrentSca": moSeCoderCurrentSca,
       "moSeCoder19kOutLevel": moSeCoder19kOutLevel,
       "moSeCoderAlrRdsSwitch": moSeCoderAlrRdsSwitch,
       "moSeCoderRdsPhase": moSeCoderRdsPhase,
       "moSeCoderRdsSelectBackup": moSeCoderRdsSelectBackup,
       "moSoundProc": moSoundProc,
       "moSpAgc": moSpAgc,
       "moSpAgState": moSpAgState,
       "moSpAgDrive": moSpAgDrive,
       "moSpAgAtt": moSpAgAtt,
       "moSpAgRel": moSpAgRel,
       "moSpAgThr": moSpAgThr,
       "moSpAgMeas": moSpAgMeas,
       "moSpLimiter": moSpLimiter,
       "moSpLimState": moSpLimState,
       "moSpLimVal": moSpLimVal,
       "moSpLimDrive": moSpLimDrive,
       "moSpLimMeas": moSpLimMeas,
       "moSpLimPreset": moSpLimPreset,
       "moSpClip": moSpClip,
       "moSpClState": moSpClState,
       "moSpClVal": moSpClVal,
       "moSpClMeas": moSpClMeas,
       "moSpMpxPwr": moSpMpxPwr,
       "moSpMpState": moSpMpState,
       "moSpMpTarget": moSpMpTarget,
       "moSpMpMeas1m": moSpMpMeas1m,
       "moSpMpMeas10s": moSpMpMeas10s,
       "moSpMpMeasAtt": moSpMpMeasAtt,
       "moSpPreset": moSpPreset,
       "moSpPrNum": moSpPrNum,
       "moSpPrBypass": moSpPrBypass,
       "moSpPrPresetsTable": moSpPrPresetsTable,
       "moSpPrPresetsEntry": moSpPrPresetsEntry,
       "moSpPrTableIndex": moSpPrTableIndex,
       "moSpPrTableName": moSpPrTableName,
       "moSfn": moSfn,
       "moSfConfDelay": moSfConfDelay,
       "moSfConfState": moSfConfState,
       "moSfMeasDelay": moSfMeasDelay,
       "moSfAlarm": moSfAlarm,
       "moSfConfOp10M": moSfConfOp10M,
       "moSfState10M": moSfState10M,
       "moSfClockSource": moSfClockSource,
       "moSfState1PPS": moSfState1PPS,
       "moSfSwitch10MAlarm": moSfSwitch10MAlarm,
       "tx": tx,
       "txGeneral": txGeneral,
       "txGnGlobal": txGnGlobal,
       "txGnGlName": txGnGlName,
       "txGnGlType": txGnGlType,
       "txGnGlStandby": txGnGlStandby,
       "txGnGlLocalMode": txGnGlLocalMode,
       "txGnGlReserveType": txGnGlReserveType,
       "txGnGlPcap": txGnGlPcap,
       "txGnAlarms": txGnAlarms,
       "txGnAl3dB": txGnAl3dB,
       "txGnAlFault": txGnAlFault,
       "txGnAlWarning": txGnAlWarning,
       "txGnAlVSWR": txGnAlVSWR,
       "txGnAlInterlockAnt": txGnAlInterlockAnt,
       "txGnAlInterlockLoad": txGnAlInterlockLoad,
       "txGnAlLink": txGnAlLink,
       "txGnAlVswrTrip": txGnAlVswrTrip,
       "txGnAl1dB": txGnAl1dB,
       "txGnMeasures": txGnMeasures,
       "txGnMsForwardPower": txGnMsForwardPower,
       "txGnMsReflectedPower": txGnMsReflectedPower,
       "txGnMsVSWR": txGnMsVSWR,
       "txGnMsVswrTrip": txGnMsVswrTrip,
       "txGnRf": txGnRf,
       "txGnRfFrequency": txGnRfFrequency,
       "txGnRfThreshold3dB": txGnRfThreshold3dB,
       "txGnRfAutomatic3dBThreshold": txGnRfAutomatic3dBThreshold,
       "txGnRfThresholdVSWR": txGnRfThresholdVSWR,
       "txGnRfOpmode": txGnRfOpmode,
       "txGnRfPower": txGnRfPower,
       "txGnRfRFPresent": txGnRfRFPresent,
       "txGnRfVswrTrip": txGnRfVswrTrip,
       "txGnRfThreshold1dB": txGnRfThreshold1dB,
       "txGnRfMaxPower": txGnRfMaxPower,
       "txGnRfRfPresentMin": txGnRfRfPresentMin,
       "txGnRfVswrTrig": txGnRfVswrTrig,
       "txGnPresets": txGnPresets,
       "txGnPrCurrent": txGnPrCurrent,
       "txGnPrGpioMode": txGnPrGpioMode,
       "txGnPrPresetsTable": txGnPrPresetsTable,
       "txGnPrPresetsEntry": txGnPrPresetsEntry,
       "txGnPrPresetsIndex": txGnPrPresetsIndex,
       "txGnPrPresetsFreq": txGnPrPresetsFreq,
       "txGnPrPresetsPower": txGnPrPresetsPower,
       "txGnPrPresetsName": txGnPrPresetsName,
       "txGnPrPresetsThreshold3dB": txGnPrPresetsThreshold3dB,
       "txGnPrPresetsThreshold1dB": txGnPrPresetsThreshold1dB,
       "txGnPrPresetsRfPresentMin": txGnPrPresetsRfPresentMin,
       "txGnPrPresetsAuto3dB": txGnPrPresetsAuto3dB,
       "txSmartFm": txSmartFm,
       "txSfMeasurements": txSfMeasurements,
       "txSfMeRangeMin": txSfMeRangeMin,
       "txSfMeRangeMax": txSfMeRangeMax,
       "txSfMeCurrentValue": txSfMeCurrentValue,
       "txSfMePwr": txSfMePwr,
       "txSfMeCurSavings": txSfMeCurSavings,
       "txSfMeCurBoost": txSfMeCurBoost,
       "txSfMePcons": txSfMePcons,
       "txSfMePconsNoSfm": txSfMePconsNoSfm,
       "txSfConfiguration": txSfConfiguration,
       "txSfCoState": txSfCoState,
       "txSfCoMode": txSfCoMode,
       "txSfCoRdsCor": txSfCoRdsCor,
       "txSfCoKwhCost": txSfCoKwhCost,
       "txSfStatus": txSfStatus,
       "txSfStAct": txSfStAct,
       "txSfStAlarm": txSfStAlarm,
       "txSfLifeTime": txSfLifeTime,
       "txSfLiSavings": txSfLiSavings,
       "txSfLiBoost": txSfLiBoost,
       "txSfLiCredits": txSfLiCredits,
       "acu": acu,
       "acGeneral": acGeneral,
       "acGnGlobal": acGnGlobal,
       "acGnGlDelay": acGnGlDelay,
       "acGnGlIterConf": acGnGlIterConf,
       "acGnGlOperation": acGnGlOperation,
       "acGnGlPreselection": acGnGlPreselection,
       "acGnGlVSWRInhibit": acGnGlVSWRInhibit,
       "acGnGlReserveControl": acGnGlReserveControl,
       "acGnGlCurrentMain": acGnGlCurrentMain,
       "acGnGlLocalMode": acGnGlLocalMode,
       "acGnGlMainOpmode": acGnGlMainOpmode,
       "acGnGlManSwLoc": acGnGlManSwLoc,
       "acGnGlDelaySwitch": acGnGlDelaySwitch,
       "acGnGlDelayStart": acGnGlDelayStart,
       "acGnGlSwOnFault": acGnGlSwOnFault,
       "acGnGlSwNoComm": acGnGlSwNoComm,
       "acGnAlarms": acGnAlarms,
       "acGnAlFault": acGnAlFault,
       "acGnAlSwitchOver": acGnAlSwitchOver,
       "acGnAlInterlockAnt": acGnAlInterlockAnt,
       "acGnAlInterlockLoad": acGnAlInterlockLoad,
       "acGnMeasures": acGnMeasures,
       "acGnMsIter": acGnMsIter,
       "acGnMsPos": acGnMsPos,
       "acGnMsSwitchLast": acGnMsSwitchLast,
       "acTx1": acTx1,
       "acTx1Global": acTx1Global,
       "acTx1GlLocalMode": acTx1GlLocalMode,
       "acTx1Alarms": acTx1Alarms,
       "acTx1AlFault": acTx1AlFault,
       "acTx1AlWarning": acTx1AlWarning,
       "acTx1AlCom": acTx1AlCom,
       "acTx1Measures": acTx1Measures,
       "acTx1Rf": acTx1Rf,
       "acTx1RfRFPresent": acTx1RfRFPresent,
       "acTx2": acTx2,
       "acTx2Global": acTx2Global,
       "acTx2GlLocalMode": acTx2GlLocalMode,
       "acTx2Alarms": acTx2Alarms,
       "acTx2AlFault": acTx2AlFault,
       "acTx2AlWarning": acTx2AlWarning,
       "acTx2AlCom": acTx2AlCom,
       "acTx2Measures": acTx2Measures,
       "acTx2Rf": acTx2Rf,
       "acTx2RfRFPresent": acTx2RfRFPresent,
       "sys": sys,
       "syGeneral": syGeneral,
       "syGeType": syGeType,
       "syGeDate": syGeDate,
       "syGeTime": syGeTime,
       "syGeName": syGeName,
       "syGeHardRel": syGeHardRel,
       "syGeSoftRel": syGeSoftRel,
       "syGeDateCode": syGeDateCode,
       "syGeSerial": syGeSerial,
       "syGeUptime": syGeUptime,
       "syGeOptList": syGeOptList,
       "syGeLocation": syGeLocation,
       "syGeContact": syGeContact,
       "syGeUnit": syGeUnit,
       "syGeTrapCounter": syGeTrapCounter,
       "syGeDigMPX": syGeDigMPX,
       "syGeDigMPX2": syGeDigMPX2,
       "syGeDigMPX3": syGeDigMPX3,
       "syGeAOIPMpx": syGeAOIPMpx,
       "syAlarms": syAlarms,
       "syAlWarning": syAlWarning,
       "syAlFault": syAlFault,
       "syAlAmb": syAlAmb,
       "syAlVoltAux": syAlVoltAux,
       "syAlRelay": syAlRelay,
       "syAlReserve": syAlReserve,
       "syAlInvalidData": syAlInvalidData,
       "syAl24v": syAl24v,
       "syAlComm": syAlComm,
       "syAlLogging": syAlLogging,
       "syLossOfEth0": syLossOfEth0,
       "syLossOfEth1": syLossOfEth1,
       "syNetwork": syNetwork,
       "syPorts": syPorts,
       "syLicenses": syLicenses,
       "syLiPresence": syLiPresence,
       "syLiPrRds": syLiPrRds,
       "syLiPrSoundProc": syLiPrSoundProc,
       "syLiPrSfm": syLiPrSfm,
       "syLiPrActivation": syLiPrActivation,
       "syLiPrAoipdecoder": syLiPrAoipdecoder,
       "syLiPrMpxoipdecoder": syLiPrMpxoipdecoder,
       "syLiPrSurestream": syLiPrSurestream,
       "syLiPrSynchrostream": syLiPrSynchrostream,
       "syLiRemaining": syLiRemaining,
       "syLiReRds": syLiReRds,
       "syLiReSoundProc": syLiReSoundProc,
       "syLiReSfm": syLiReSfm,
       "syLiReActivation": syLiReActivation,
       "syLiReAoipdecoder": syLiReAoipdecoder,
       "syLiReMpxoipdecoder": syLiReMpxoipdecoder,
       "syLiReSurestream": syLiReSurestream,
       "syLiReSynchrostream": syLiReSynchrostream,
       "syLiAlarms": syLiAlarms,
       "syLiAlRds": syLiAlRds,
       "syLiAlSoundProc": syLiAlSoundProc,
       "syLiAlSfm": syLiAlSfm,
       "syLiAlActivation": syLiAlActivation,
       "syLiAlAoipdecoder": syLiAlAoipdecoder,
       "syLiAlMpxoipdecoder": syLiAlMpxoipdecoder,
       "syLiAlSurestream": syLiAlSurestream,
       "syLiAlSynchrostream": syLiAlSynchrostream,
       "monitoring": monitoring,
       "moMain": moMain,
       "moMaMeas": moMaMeas,
       "moMaMeVolt1": moMaMeVolt1,
       "moMaMeVolt2": moMaMeVolt2,
       "moMaMeCur1": moMaMeCur1,
       "moMaMeCur2": moMaMeCur2,
       "moMaMeEffSys": moMaMeEffSys,
       "moMaMeEffTrans": moMaMeEffTrans,
       "moMaMePin": moMaMePin,
       "moMaAlarms": moMaAlarms,
       "moMainAlVolt1": moMainAlVolt1,
       "moMainAlVolt2": moMainAlVolt2,
       "moMainAlCur1": moMainAlCur1,
       "moMainAlCur2": moMainAlCur2,
       "moMainAlPin": moMainAlPin,
       "moConditions": moConditions,
       "moCoMeas": moCoMeas,
       "moCoMeAmb": moCoMeAmb,
       "moCoMeHeat1": moCoMeHeat1,
       "moCoMeHeat2": moCoMeHeat2,
       "moCoMePsuTemp": moCoMePsuTemp,
       "moCoMeIntTemp": moCoMeIntTemp,
       "moCoMePressure": moCoMePressure,
       "moCoMeExcTemp": moCoMeExcTemp,
       "moCoAlarms": moCoAlarms,
       "moCoAlHeat1": moCoAlHeat1,
       "moCoAlHeat2": moCoAlHeat2,
       "moCoAlTemp1": moCoAlTemp1,
       "moCoAlTemp2": moCoAlTemp2,
       "moCoAlPsuTemp": moCoAlPsuTemp,
       "moCoAlIntTemp": moCoAlIntTemp,
       "moCoAlExcTemp": moCoAlExcTemp,
       "moCoAlPressure": moCoAlPressure,
       "moAuxVolt": moAuxVolt,
       "moAuMeas": moAuMeas,
       "moAuMe5V": moAuMe5V,
       "moAuMe12V": moAuMe12V,
       "moAuMeN12V": moAuMeN12V,
       "moAuAlarms": moAuAlarms,
       "moFan": moFan,
       "moFanMes": moFanMes,
       "moFanMeFan1Speed": moFanMeFan1Speed,
       "moFanMeFan2Speed": moFanMeFan2Speed,
       "moFanAlarms": moFanAlarms,
       "moFanAlFan1Alarm": moFanAlFan1Alarm,
       "moFanAlFan2Alarm": moFanAlFan2Alarm,
       "maintenance": maintenance,
       "maMonitoring": maMonitoring,
       "maMoMain": maMoMain,
       "maMoMaEffTrans": maMoMaEffTrans,
       "maMoMaEffPa": maMoMaEffPa,
       "maMoMaEffPsu": maMoMaEffPsu,
       "maMoMaEffSys": maMoMaEffSys,
       "maMoCcu": maMoCcu,
       "maMoCcFault": maMoCcFault,
       "maMoCcWarn": maMoCcWarn,
       "maMoConditions": maMoConditions,
       "maMoCoMeas": maMoCoMeas,
       "maMoCoMeAmb": maMoCoMeAmb,
       "maMoCoMeLoad1InputTemp": maMoCoMeLoad1InputTemp,
       "maMoCoMeLoad1HeatsinkTemp": maMoCoMeLoad1HeatsinkTemp,
       "maMoCoMeLoad2InputTemp": maMoCoMeLoad2InputTemp,
       "maMoCoMeLoad2HeatsinkTemp": maMoCoMeLoad2HeatsinkTemp,
       "maMoCoMePressure": maMoCoMePressure,
       "maMoCoMeHeat1": maMoCoMeHeat1,
       "maMoCoMeHeat2": maMoCoMeHeat2,
       "maMoCoMePsuTemp": maMoCoMePsuTemp,
       "maMoCoMeIntTemp": maMoCoMeIntTemp,
       "maMoCoMeExcTemp": maMoCoMeExcTemp,
       "maMoCoAlarms": maMoCoAlarms,
       "maMoCoAlAmb": maMoCoAlAmb,
       "maMoCoAlLoad1Heatsink": maMoCoAlLoad1Heatsink,
       "maMoCoAlLoad2Heatsink": maMoCoAlLoad2Heatsink,
       "maMoCoAlPressure": maMoCoAlPressure,
       "maMoCoAlHeat1": maMoCoAlHeat1,
       "maMoCoAlHeat2": maMoCoAlHeat2,
       "maMoCoAlTemp1": maMoCoAlTemp1,
       "maMoCoAlTemp2": maMoCoAlTemp2,
       "maMoCoAlPsuTemp": maMoCoAlPsuTemp,
       "maMoCoAlIntTemp": maMoCoAlIntTemp,
       "maMoCoAlExcTemp": maMoCoAlExcTemp,
       "maMoAuxVolt": maMoAuxVolt,
       "maMoAuMeas": maMoAuMeas,
       "maMoAuMe5V": maMoAuMe5V,
       "maMoAuMe12V": maMoAuMe12V,
       "maMoAuMeN12V": maMoAuMeN12V,
       "maMoAuMe24V": maMoAuMe24V,
       "maMoAuAlarms": maMoAuAlarms,
       "maMoAuAlVoltAux": maMoAuAlVoltAux,
       "maMoAuAl24V": maMoAuAl24V,
       "maMoFanTable": maMoFanTable,
       "maMoFanEntry": maMoFanEntry,
       "maMoFanIndex": maMoFanIndex,
       "maMoFanSpeed": maMoFanSpeed,
       "maMoFanAlarms": maMoFanAlarms,
       "maMoMeas": maMoMeas,
       "maMoMeVolt1": maMoMeVolt1,
       "maMoMeVolt2": maMoMeVolt2,
       "maMoMeCur1": maMoMeCur1,
       "maMoMeCur2": maMoMeCur2,
       "maMoMePin": maMoMePin,
       "maMoMeVolt3": maMoMeVolt3,
       "maMoMeCur3": maMoMeCur3,
       "maMoAlarm": maMoAlarm,
       "maMoAlVolt1": maMoAlVolt1,
       "maMoAlVolt2": maMoAlVolt2,
       "maMoAlCur1": maMoAlCur1,
       "maMoAlCur2": maMoAlCur2,
       "maMoAlPin": maMoAlPin,
       "maMoAlSecPref": maMoAlSecPref,
       "maMoAlCur3": maMoAlCur3,
       "maDrive": maDrive,
       "maDrTable": maDrTable,
       "maDrEntry": maDrEntry,
       "maDrIndex": maDrIndex,
       "maDrCommunication": maDrCommunication,
       "maDrFault": maDrFault,
       "maDrWarning": maDrWarning,
       "maDrForwardPower": maDrForwardPower,
       "maDrReflectedPower": maDrReflectedPower,
       "maDrHeatsink": maDrHeatsink,
       "maDrFanSpeed": maDrFanSpeed,
       "maPa": maPa,
       "maPaTable": maPaTable,
       "maPaEntry": maPaEntry,
       "maPaIndex": maPaIndex,
       "maPaCommunication": maPaCommunication,
       "maPaFault": maPaFault,
       "maPaWarning": maPaWarning,
       "maPaForwardPower": maPaForwardPower,
       "maPaReflectedPower": maPaReflectedPower,
       "maPaEfficiency": maPaEfficiency,
       "maPaCurrent": maPaCurrent,
       "maPaHeatMax": maPaHeatMax,
       "maPaAlrCur": maPaAlrCur,
       "maPaVoltage": maPaVoltage,
       "maPaAlrVolt": maPaAlrVolt,
       "maPaAmbTemp": maPaAmbTemp,
       "maPaAlrHeat": maPaAlrHeat,
       "maPaAlrTemp": maPaAlrTemp,
       "maPsu": maPsu,
       "maPsVoltageInput": maPsVoltageInput,
       "maPsCurrentInput": maPsCurrentInput,
       "maPsPowerInput": maPsPowerInput,
       "maPsVoltageOutput": maPsVoltageOutput,
       "maPsCurrentOutput": maPsCurrentOutput,
       "maPsPowerOutput": maPsPowerOutput,
       "maPsTable": maPsTable,
       "maPsEntry": maPsEntry,
       "maPsIndex": maPsIndex,
       "maPsCommunication": maPsCommunication,
       "maPsFault": maPsFault,
       "maPsWarning": maPsWarning,
       "maPsEfficiency": maPsEfficiency,
       "maPsOutputPower": maPsOutputPower,
       "maPsInputPower": maPsInputPower,
       "maPsMissing": maPsMissing,
       "maPsInputCurrent": maPsInputCurrent,
       "maPsInputCurAlr": maPsInputCurAlr,
       "maPsInputVoltage": maPsInputVoltage,
       "maPsInputVoltAlr": maPsInputVoltAlr,
       "maPsOutputCurrent": maPsOutputCurrent,
       "maPsOutputCurAlr": maPsOutputCurAlr,
       "maPsOutputVoltage": maPsOutputVoltage,
       "maPsOutputVoltAlr": maPsOutputVoltAlr,
       "maPsAmbTemp": maPsAmbTemp,
       "maPsAmbAlr": maPsAmbAlr,
       "maPsHeat1Temp": maPsHeat1Temp,
       "maPsHeat1Alr": maPsHeat1Alr,
       "maPsFan1Speed": maPsFan1Speed,
       "maPsFan1Alr": maPsFan1Alr,
       "maPsSerial": maPsSerial,
       "maPsSoftRel": maPsSoftRel}
)
