# SNMP MIB module (ALCATEL-NMC-PROXY-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alcatel\ALCATEL-NMC-PROXY-AGENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:11 2025
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

(openViewSeverity,) = mibBuilder.importSymbols(
    "HPOV-NNM-MIB",
    "openViewSeverity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alcatel_ObjectIdentity = ObjectIdentity
alcatel = _Alcatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637)
)
_Abs_ObjectIdentity = ObjectIdentity
abs = _Abs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64)
)
_Nmc4755_ObjectIdentity = ObjectIdentity
nmc4755 = _Nmc4755_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0)
)
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10)
)
_NmcProxyAgent_ObjectIdentity = ObjectIdentity
nmcProxyAgent = _NmcProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1)
)
_CmipEventArg_ObjectIdentity = ObjectIdentity
cmipEventArg = _CmipEventArg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1)
)
_ObjectClass_ObjectIdentity = ObjectIdentity
objectClass = _ObjectClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1)
)
_TopClass_Type = Integer32
_TopClass_Object = MibScalar
topClass = _TopClass_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1, 1),
    _TopClass_Type()
)
topClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topClass.setStatus("mandatory")
_BaseClass_Type = Integer32
_BaseClass_Object = MibScalar
baseClass = _BaseClass_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 1, 2),
    _BaseClass_Type()
)
baseClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseClass.setStatus("mandatory")
_ObjectInstance_ObjectIdentity = ObjectIdentity
objectInstance = _ObjectInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2)
)
_ContainmentTree_ObjectIdentity = ObjectIdentity
containmentTree = _ContainmentTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1)
)
_A4400_ObjectIdentity = ObjectIdentity
a4400 = _A4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89)
)
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29)
)
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23)
)
_ActOrSuEvents_ObjectIdentity = ObjectIdentity
actOrSuEvents = _ActOrSuEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23, 175)
)
_Terminal_ObjectIdentity = ObjectIdentity
terminal = _Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 29, 23, 175, 82)
)
_LogicalLinks_ObjectIdentity = ObjectIdentity
logicalLinks = _LogicalLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 101)
)
_Dect_ObjectIdentity = ObjectIdentity
dect = _Dect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 1, 89, 201)
)
_RdnDepth_Type = Integer32
_RdnDepth_Object = MibScalar
rdnDepth = _RdnDepth_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 2),
    _RdnDepth_Type()
)
rdnDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnDepth.setStatus("mandatory")
_RdnValues_ObjectIdentity = ObjectIdentity
rdnValues = _RdnValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3)
)
_Rdn1_ObjectIdentity = ObjectIdentity
rdn1 = _Rdn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1)
)
_ClassId1_Type = Integer32
_ClassId1_Object = MibScalar
classId1 = _ClassId1_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 1),
    _ClassId1_Type()
)
classId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classId1.setStatus("mandatory")
_RdnValue1_Type = OctetString
_RdnValue1_Object = MibScalar
rdnValue1 = _RdnValue1_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 1, 2),
    _RdnValue1_Type()
)
rdnValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnValue1.setStatus("mandatory")
_Rdn2_ObjectIdentity = ObjectIdentity
rdn2 = _Rdn2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2)
)
_ClassId2_Type = Integer32
_ClassId2_Object = MibScalar
classId2 = _ClassId2_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 1),
    _ClassId2_Type()
)
classId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classId2.setStatus("mandatory")
_RdnValue2_Type = OctetString
_RdnValue2_Object = MibScalar
rdnValue2 = _RdnValue2_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 2, 2),
    _RdnValue2_Type()
)
rdnValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnValue2.setStatus("mandatory")
_Rdn3_ObjectIdentity = ObjectIdentity
rdn3 = _Rdn3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3)
)
_ClassId3_Type = Integer32
_ClassId3_Object = MibScalar
classId3 = _ClassId3_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 1),
    _ClassId3_Type()
)
classId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classId3.setStatus("mandatory")
_RdnValue3_Type = OctetString
_RdnValue3_Object = MibScalar
rdnValue3 = _RdnValue3_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 3, 2),
    _RdnValue3_Type()
)
rdnValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnValue3.setStatus("mandatory")
_Rdn4_ObjectIdentity = ObjectIdentity
rdn4 = _Rdn4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4)
)
_ClassId4_Type = Integer32
_ClassId4_Object = MibScalar
classId4 = _ClassId4_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 1),
    _ClassId4_Type()
)
classId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classId4.setStatus("mandatory")
_RdnValue4_Type = OctetString
_RdnValue4_Object = MibScalar
rdnValue4 = _RdnValue4_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 4, 2),
    _RdnValue4_Type()
)
rdnValue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnValue4.setStatus("mandatory")
_Rdn5_ObjectIdentity = ObjectIdentity
rdn5 = _Rdn5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5)
)
_ClassId5_Type = Integer32
_ClassId5_Object = MibScalar
classId5 = _ClassId5_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 1),
    _ClassId5_Type()
)
classId5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classId5.setStatus("mandatory")
_RdnValue5_Type = OctetString
_RdnValue5_Object = MibScalar
rdnValue5 = _RdnValue5_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 3, 5, 2),
    _RdnValue5_Type()
)
rdnValue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnValue5.setStatus("mandatory")
_VoiceIds_ObjectIdentity = ObjectIdentity
voiceIds = _VoiceIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4)
)
_ObjectNumber_Type = Integer32
_ObjectNumber_Object = MibScalar
objectNumber = _ObjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 1),
    _ObjectNumber_Type()
)
objectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectNumber.setStatus("optional")
_ParentNumber_Type = Integer32
_ParentNumber_Object = MibScalar
parentNumber = _ParentNumber_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 2, 4, 2),
    _ParentNumber_Type()
)
parentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentNumber.setStatus("optional")
_EventTime_Type = OctetString
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 3),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("mandatory")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("communicationAlarm", 2),
          ("environmentalAlarm", 3),
          ("equipmentAlarm", 4),
          ("processingErrorAlarm", 10),
          ("qualityOfServiceAlarm", 11))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 4),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("mandatory")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("clear", 6))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 5),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("mandatory")


class _ProbableCause_Type(Integer32):
    """Custom type probableCause based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("AdapterError", 1),
          ("ApplicationSubsystemFailure", 2),
          ("BandWidthReduced", 3),
          ("CallEstablishmentError", 4),
          ("CommunicationsProtocolError", 5),
          ("CommunicationsSubsystemFailure", 6),
          ("ConfigurationOrCustomizationError", 7),
          ("Congestion", 8),
          ("CorruptData", 9),
          ("CpuCyclesLimitExceeded", 10),
          ("DataSetOrModemError", 11),
          ("DegradedSignal", 12),
          ("DteDceInterfaceError", 13),
          ("EnclosureDoorOpen", 14),
          ("EquipmentMalFunction", 15),
          ("ExcessiveVibration", 16),
          ("FileError", 17),
          ("FireDetected", 18),
          ("FloodDetected", 19),
          ("FramingError", 20),
          ("HeatingVentilationCoolingSystemProblem", 21),
          ("HumidityUnacceptable", 22),
          ("InputOutputDeviceError", 23),
          ("InputDeviceError", 24),
          ("LANError", 25),
          ("LeakDetected", 26),
          ("LocalNodeTransmissionError", 27),
          ("LossOfFrame", 28),
          ("LossOfSignal", 29),
          ("MaterialSupplyExhausted", 30),
          ("MultiplexerProblem", 31),
          ("OutOfMemory", 32),
          ("OutputDeviceError", 33),
          ("PerformanceDegraded", 34),
          ("PowerProblem", 35),
          ("PressureUnacceptable", 36),
          ("ProcessorProblem", 37),
          ("PumpFailure", 38),
          ("QueueSizeExceeded", 39),
          ("ReceiveFailure", 40),
          ("ReceiverFailure", 41),
          ("RemoteNodeTransmissionFailure", 42),
          ("ResourceAtOrNearingCapacity", 43),
          ("ResponseTimeExcessive", 44),
          ("RetransmissionRateExcessive", 45),
          ("SoftwareError", 46),
          ("SoftwareProgramAbnormallyTerminated", 47),
          ("SoftwareProgramError", 48),
          ("StorageCapacityProblem", 49),
          ("TemperatureUnacceptable", 50),
          ("ThresholdCrossed", 51),
          ("TimingProblem", 52),
          ("ToxicLeakDetected", 53),
          ("TransmitFailure", 54),
          ("TransmitterFailure", 55),
          ("UnderlyingResourceUnavailable", 56),
          ("VersionMismatch", 57))
    )


_ProbableCause_Type.__name__ = "Integer32"
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 6),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCause.setStatus("mandatory")
_PackedForm_Type = OctetString
_PackedForm_Object = MibScalar
packedForm = _PackedForm_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 7),
    _PackedForm_Type()
)
packedForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packedForm.setStatus("mandatory")
_NotificationId_Type = Integer32
_NotificationId_Object = MibScalar
notificationId = _NotificationId_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 8),
    _NotificationId_Type()
)
notificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationId.setStatus("mandatory")
_AddText_Type = OctetString
_AddText_Object = MibScalar
addText = _AddText_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 1, 9),
    _AddText_Type()
)
addText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addText.setStatus("optional")
_NmcProxyTraps_ObjectIdentity = ObjectIdentity
nmcProxyTraps = _NmcProxyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2)
)

# Managed Objects groups


# Notification objects

packedCmipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 1)
)
packedCmipTrap.setObjects(
      *(("HPOV-NNM-MIB", "openViewSeverity"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "packedForm"))
)
if mibBuilder.loadTexts:
    packedCmipTrap.setStatus(
        ""
    )

startOfResyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    startOfResyncTrap.setStatus(
        ""
    )

cmipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 3)
)
cmipTrap.setObjects(
      *(("ALCATEL-NMC-PROXY-AGENT-MIB", "topClass"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "baseClass"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnDepth"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId2"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue2"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId3"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue3"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId4"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue4"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "classId5"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue5"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventTime"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "eventType"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "probableCause"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "notificationId"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "addText"))
)
if mibBuilder.loadTexts:
    cmipTrap.setStatus(
        ""
    )

startProxyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    startProxyTrap.setStatus(
        ""
    )

stopProxyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    stopProxyTrap.setStatus(
        ""
    )

eventLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    eventLostTrap.setStatus(
        ""
    )

topClassStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 64, 0, 10, 1, 2, 0, 7)
)
topClassStateTrap.setObjects(
      *(("ALCATEL-NMC-PROXY-AGENT-MIB", "classId1"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "rdnValue1"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "severity"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "objectNumber"),
        ("ALCATEL-NMC-PROXY-AGENT-MIB", "parentNumber"))
)
if mibBuilder.loadTexts:
    topClassStateTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-NMC-PROXY-AGENT-MIB",
    **{"alcatel": alcatel,
       "abs": abs,
       "nmc4755": nmc4755,
       "notification": notification,
       "nmcProxyAgent": nmcProxyAgent,
       "cmipEventArg": cmipEventArg,
       "objectClass": objectClass,
       "topClass": topClass,
       "baseClass": baseClass,
       "objectInstance": objectInstance,
       "containmentTree": containmentTree,
       "a4400": a4400,
       "shelf": shelf,
       "board": board,
       "actOrSuEvents": actOrSuEvents,
       "terminal": terminal,
       "logicalLinks": logicalLinks,
       "dect": dect,
       "rdnDepth": rdnDepth,
       "rdnValues": rdnValues,
       "rdn1": rdn1,
       "classId1": classId1,
       "rdnValue1": rdnValue1,
       "rdn2": rdn2,
       "classId2": classId2,
       "rdnValue2": rdnValue2,
       "rdn3": rdn3,
       "classId3": classId3,
       "rdnValue3": rdnValue3,
       "rdn4": rdn4,
       "classId4": classId4,
       "rdnValue4": rdnValue4,
       "rdn5": rdn5,
       "classId5": classId5,
       "rdnValue5": rdnValue5,
       "voiceIds": voiceIds,
       "objectNumber": objectNumber,
       "parentNumber": parentNumber,
       "eventTime": eventTime,
       "eventType": eventType,
       "severity": severity,
       "probableCause": probableCause,
       "packedForm": packedForm,
       "notificationId": notificationId,
       "addText": addText,
       "nmcProxyTraps": nmcProxyTraps,
       "packedCmipTrap": packedCmipTrap,
       "startOfResyncTrap": startOfResyncTrap,
       "cmipTrap": cmipTrap,
       "startProxyTrap": startProxyTrap,
       "stopProxyTrap": stopProxyTrap,
       "eventLostTrap": eventLostTrap,
       "topClassStateTrap": topClassStateTrap}
)
