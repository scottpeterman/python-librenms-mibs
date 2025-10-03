# SNMP MIB module (PEGASUS-LEAN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pegasus\PEGASUS-LEAN-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:37 2025
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

(pegasusMibModule,) = mibBuilder.importSymbols(
    "PEGASUS-MIB",
    "pegasusMibModule")

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
 TimeTicks,
 Unsigned32,
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pegasusLeanTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5)
)
if mibBuilder.loadTexts:
    pegasusLeanTrapModule.setRevisions(
        ("2005-02-02 00:00",
         "2004-12-17 00:00",
         "2004-03-18 00:00",
         "2004-01-15 00:00",
         "2003-11-11 00:00",
         "2003-03-21 00:00",
         "2002-09-19 00:00",
         "2002-04-25 00:00",
         "2002-04-02 00:00",
         "2002-03-14 00:00",
         "2002-02-18 00:00",
         "2002-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LeanTrapObjects_ObjectIdentity = ObjectIdentity
leanTrapObjects = _LeanTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1)
)
_Sender_Type = ObjectIdentifier
_Sender_Object = MibScalar
sender = _Sender_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 1),
    _Sender_Type()
)
sender.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sender.setStatus("current")
_SenderObjectName_Type = DisplayString
_SenderObjectName_Object = MibScalar
senderObjectName = _SenderObjectName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 2),
    _SenderObjectName_Type()
)
senderObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    senderObjectName.setStatus("current")
_SenderDescription_Type = DisplayString
_SenderDescription_Object = MibScalar
senderDescription = _SenderDescription_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 3),
    _SenderDescription_Type()
)
senderDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    senderDescription.setStatus("current")


class _ProbableCause_Type(Integer32):
    """Custom type probableCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96)
        )
    )
    namedValues = NamedValues(
        *(("disconnectionError", 1),
          ("communicationError", 2),
          ("outOfMemory", 3),
          ("cfgUploadProblem", 4),
          ("cfgDownloadProblem", 5),
          ("statusSyncProblem", 6),
          ("operStateDisabled", 7),
          ("activeMaintenanceLoop", 8),
          ("deviceFailure", 9),
          ("lossOfSignal", 10),
          ("lossOfFrameAlignement", 11),
          ("alarmIndicationSignal", 12),
          ("bitErrorRateToHigh", 13),
          ("lossOfExternalClock", 14),
          ("remoteAlarmIndication", 15),
          ("deviceInactive", 16),
          ("wrongProgram", 17),
          ("inTest", 18),
          ("failed", 19),
          ("powerOff", 20),
          ("offLine", 21),
          ("offDuty", 22),
          ("dependency", 23),
          ("degraded", 24),
          ("notInstalled", 25),
          ("logFull", 26),
          ("blocked", 27),
          ("l1Activation", 28),
          ("hasLosAtTrefPoint", 29),
          ("hasL1ActivationFault", 30),
          ("hasLosAtDigSection", 31),
          ("iadPowerLoss", 32),
          ("iadLifeline", 33),
          ("iadDCContinuity", 34),
          ("dslConfig", 35),
          ("dslUserService", 36),
          ("dslLoopAtt", 37),
          ("dslLoswFailure", 38),
          ("dataswitchPsu1Fail", 39),
          ("dataswitchPsu2Fail", 40),
          ("dataswitchFanFail", 41),
          ("dataswitchUrgentExt", 42),
          ("dataswitchNonurgentExt", 43),
          ("v5InterfaceIDFailure", 44),
          ("v5InterfaceProvisMismatch", 45),
          ("v5LinkIdFailure", 46),
          ("unsupported2ndV5Card", 47),
          ("currentLimit", 48),
          ("watsonDTRFailed", 49),
          ("softwareMismatch", 50),
          ("hardwareProblem", 51),
          ("ethernetIfLinkIntegrityFailed", 52),
          ("ethernetIfFifoError", 53),
          ("unknownProbableCause", 54),
          ("lossOfFrame", 55),
          ("traceIdMissmatch", 56),
          ("lossOfMultiframe", 57),
          ("multiplexSectionRemoteDefectIndication", 58),
          ("multiplexSectionAlarmIndicationSignal", 59),
          ("regeneratorSectionTraceIdMismatch", 60),
          ("outOfLock", 61),
          ("lossOfPointer", 62),
          ("remoteDefectIndication", 63),
          ("payloadLabelMismatch", 64),
          ("unequipped", 65),
          ("initFailed", 66),
          ("watsonRegW2-AlarmA", 67),
          ("watsonRegW2-AlarmB", 68),
          ("watsonRegR-LoswFailure", 69),
          ("watsonRegC-LoswFailure", 70),
          ("watsonRegR-BerToHigh", 71),
          ("watsonRegC-BerToHigh", 72),
          ("watsonTrapPortBindFailed", 73),
          ("watsonHPOVConnectFailed", 74),
          ("dslCurrentLimit", 75),
          ("m16ProgramTransfer", 76),
          ("writeError", 77),
          ("maintenance", 78),
          ("remoteFailureIndication", 79),
          ("lcasCrcError", 80),
          ("nonLcasSequenceError", 81),
          ("rxLowOrderGroupIdMismatch", 82),
          ("rxHighOrderGroupIdMismatch", 83),
          ("rxLowOrderDifferentialDelay", 84),
          ("rxHighOrderDifferentialDelay", 85),
          ("rxLowOrderDifferentialDelayAllVT", 86),
          ("rxHighOrderDifferentialDelayAllVT", 87),
          ("txFifoOverflow", 88),
          ("rxFifoOverflow", 89),
          ("emailServiceAlarm", 90),
          ("licenseMissing", 91),
          ("licenseInvalid", 92),
          ("licenseWrongHostId", 93),
          ("licenseMaxNetworkNodesExceeded", 94),
          ("alarmFilteringParseError", 95),
          ("iadNoCOS", 96))
    )


_ProbableCause_Type.__name__ = "Integer32"
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 4),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    probableCause.setStatus("current")
_ProbableCauseText_Type = DisplayString
_ProbableCauseText_Object = MibScalar
probableCauseText = _ProbableCauseText_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 5),
    _ProbableCauseText_Type()
)
probableCauseText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    probableCauseText.setStatus("current")


class _PerceivedSeverity_Type(Integer32):
    """Custom type perceivedSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("cleared", 5),
          ("indeterminate", 6))
    )


_PerceivedSeverity_Type.__name__ = "Integer32"
_PerceivedSeverity_Object = MibScalar
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 6),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("current")
_PerceivedSeverityText_Type = DisplayString
_PerceivedSeverityText_Object = MibScalar
perceivedSeverityText = _PerceivedSeverityText_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 7),
    _PerceivedSeverityText_Type()
)
perceivedSeverityText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    perceivedSeverityText.setStatus("current")
_LeanNotifications_ObjectIdentity = ObjectIdentity
leanNotifications = _LeanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 2)
)
_LeanTraps_ObjectIdentity = ObjectIdentity
leanTraps = _LeanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

pegasusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0, 1)
)
pegasusAlarm.setObjects(
      *(("PEGASUS-LEAN-TRAP-MIB", "sender"),
        ("PEGASUS-LEAN-TRAP-MIB", "senderObjectName"),
        ("PEGASUS-LEAN-TRAP-MIB", "senderDescription"),
        ("PEGASUS-LEAN-TRAP-MIB", "probableCause"),
        ("PEGASUS-LEAN-TRAP-MIB", "probableCauseText"),
        ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverity"),
        ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverityText"))
)
if mibBuilder.loadTexts:
    pegasusAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEGASUS-LEAN-TRAP-MIB",
    **{"pegasusLeanTrapModule": pegasusLeanTrapModule,
       "leanTrapObjects": leanTrapObjects,
       "sender": sender,
       "senderObjectName": senderObjectName,
       "senderDescription": senderDescription,
       "probableCause": probableCause,
       "probableCauseText": probableCauseText,
       "perceivedSeverity": perceivedSeverity,
       "perceivedSeverityText": perceivedSeverityText,
       "leanNotifications": leanNotifications,
       "leanTraps": leanTraps,
       "pegasusAlarm": pegasusAlarm}
)
