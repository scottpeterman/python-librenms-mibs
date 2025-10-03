# SNMP MIB module (SL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:42 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slAlarmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlAlarmType(TextualConvention, Integer32):
    status = "current"
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              151,
              152,
              201,
              202,
              203,
              204,
              301,
              302,
              303,
              304,
              306,
              307,
              311,
              312,
              313,
              314,
              315,
              351,
              352,
              353,
              354,
              401,
              403,
              404,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              451,
              452,
              453,
              454,
              455,
              456,
              470,
              471,
              472,
              501,
              502,
              503,
              602,
              603,
              604,
              606,
              608,
              621,
              622,
              623,
              624,
              625,
              701,
              702,
              703,
              704,
              705,
              706,
              707,
              708,
              709,
              710,
              711,
              712,
              713,
              720,
              721,
              726,
              727,
              728,
              729,
              730,
              731,
              732,
              733,
              734,
              735,
              736,
              737,
              750,
              751,
              752,
              753,
              754,
              755,
              756,
              757,
              758,
              759,
              780,
              781,
              782,
              783,
              784,
              785,
              801,
              803,
              804,
              806,
              807,
              808,
              820,
              821,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              909,
              910,
              1001,
              1002,
              1003,
              1004)
        )
    )
    namedValues = NamedValues(
        *(("losSonetAlarm", 1),
          ("lofSonetAlarm", 2),
          ("lopSonetAlarm", 3),
          ("aisLineSonetAlarm", 4),
          ("rfiLineSonetAlarm", 5),
          ("uneqSonetAlarm", 6),
          ("timLine", 7),
          ("slm", 8),
          ("sd", 9),
          ("sf", 10),
          ("hwfail", 11),
          ("aisPathSonetAlarm", 12),
          ("rfiPathSonetAlarm", 13),
          ("timPath", 14),
          ("uplinkTransmitMismatch", 15),
          ("uplinkClockSourceLol", 16),
          ("aisVtSonetAlarm", 21),
          ("lopVtSonetAlarm", 22),
          ("rfiVtSonetAlarm", 23),
          ("timVt", 24),
          ("slmVt", 25),
          ("uneqVtSonetAlarm", 26),
          ("lomVt", 27),
          ("vcgFarLossClientSignal", 101),
          ("vcgFarLossClientSync", 102),
          ("vcgLossAlignment", 103),
          ("vcgLossMultiframe", 104),
          ("vcgLossSequence", 105),
          ("vcgGfpLossSync", 106),
          ("vcgFarGfpLossSync", 107),
          ("vcgBadGidMember", 108),
          ("provUnequipped", 151),
          ("provMismatch", 152),
          ("ethConfigTransmitFault", 201),
          ("ethConfigLossOfSignal", 202),
          ("ethConfigLinkFail", 203),
          ("ethConfigPcsLossSync", 204),
          ("fcBxPortTransmitFault", 301),
          ("fcBxPortLossOfSignal", 302),
          ("fcBxPortNoLink", 303),
          ("fcBxPortLossOfSync", 304),
          ("fcBxPortTransmitMismatch", 306),
          ("fcBxPortPcsLossSync", 307),
          ("fcipLinkNoLink", 311),
          ("fcipLinkLossOfSync", 312),
          ("fcipSntpFailure", 313),
          ("fcipIpsecFailure", 314),
          ("fcipFarLossOfClient", 315),
          ("esconPortTransmitFault", 351),
          ("esconPortLossOfSignal", 352),
          ("esconPortNoLink", 353),
          ("esconPortLossOfSync", 354),
          ("edfaPumpTemperuture", 401),
          ("edfaHwFail", 403),
          ("edfaRvcSignalDetect", 404),
          ("edfaRcvPower", 406),
          ("edfaTemprature", 407),
          ("edfaEyeSafty", 408),
          ("edafGainFlatness", 409),
          ("edfaXmtPower", 410),
          ("edfaGain", 411),
          ("edfaEol", 412),
          ("muxAisPath", 451),
          ("muxLof", 452),
          ("muxRdi", 453),
          ("muxInbandFail", 454),
          ("muxTempLicense", 455),
          ("muxNoLicense", 456),
          ("oswHwFail", 470),
          ("oswLossOfSignal", 471),
          ("oswEdfaLossProp", 472),
          ("loopback", 501),
          ("apsForceActive", 502),
          ("apsManualActive", 503),
          ("cluHoldoverState", 602),
          ("cluFreerunState", 603),
          ("cluBelowLevel", 604),
          ("cluFail", 606),
          ("cluJittered", 608),
          ("channelLowDegrade", 621),
          ("channelHighDegrade", 622),
          ("channelLowFail", 623),
          ("channelHighFail", 624),
          ("unequalizedOuputPower", 625),
          ("sfpTransmitFault", 701),
          ("sfpRemoved", 702),
          ("sfpMuxWlMismatch", 703),
          ("sfpBitRateMismatch", 704),
          ("sfpLossOfLock", 705),
          ("sfpSfpWlMismatch", 706),
          ("sfpLossOfLight", 707),
          ("sfpLaserEndOfLife", 708),
          ("sfpMuxSpacingMismatch", 709),
          ("sfpHardwareFault", 710),
          ("sfpBlocked", 711),
          ("sfpLossPropagation", 712),
          ("sfpUnknownType", 713),
          ("sfpHighTemp", 720),
          ("sfpLowTemp", 721),
          ("sfpHighTxPower", 726),
          ("sfpLowTxPower", 727),
          ("sfpHighRxPower", 728),
          ("sfpLowRxPower", 729),
          ("sfpHighLaserTemp", 730),
          ("sfpLowLaserTemp", 731),
          ("sfpHighLaserWl", 732),
          ("sfpLowLaserWl", 733),
          ("xfpTxNR", 734),
          ("xfpTxCdrNotLocked", 735),
          ("xfpRxNR", 736),
          ("xfpRxCdrNotLocked", 737),
          ("otnFecExc", 750),
          ("otnFecDeg", 751),
          ("otnOtuDeg", 752),
          ("otnOduDeg", 753),
          ("otnLos", 754),
          ("otnLof", 755),
          ("otnLom", 756),
          ("otuAis", 757),
          ("otuBdi", 758),
          ("otuTtim", 759),
          ("oduAis", 780),
          ("oduOci", 781),
          ("oduLck", 782),
          ("oduBdi", 783),
          ("oduTtim", 784),
          ("oduPtm", 785),
          ("entityRemoved", 801),
          ("entityClockFail", 803),
          ("entityHwTxFail", 804),
          ("entitySwMismatch", 806),
          ("entitySwUpgrade", 807),
          ("entitySwInvalidBank", 808),
          ("entityIpLanPending", 820),
          ("entityIpOscPending", 821),
          ("nePowerFault", 902),
          ("neFanFault", 903),
          ("neLowVoltagePower", 904),
          ("entitySwUpgradeFail", 905),
          ("entityRadiusPrimFail", 906),
          ("entityRadiusSecFail", 907),
          ("entityDbRestoreFail", 908),
          ("entityDbRestoreInProgress", 909),
          ("entitySntpFail", 910),
          ("dcActive", 1001),
          ("lcpDown", 1002),
          ("ncpDown", 1003),
          ("rtcFailure", 1004))
    )



# MIB Managed Objects in the order of their OIDs

_SlAlarmConfig_ObjectIdentity = ObjectIdentity
slAlarmConfig = _SlAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1)
)
_SlAlarmConfigTable_Object = MibTable
slAlarmConfigTable = _SlAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1)
)
if mibBuilder.loadTexts:
    slAlarmConfigTable.setStatus("current")
_SlAlarmConfigEntry_Object = MibTableRow
slAlarmConfigEntry = _SlAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1)
)
slAlarmConfigEntry.setIndexNames(
    (0, "SL-ALARM-MIB", "slAlarmIfIndex"),
    (0, "SL-ALARM-MIB", "slAlarmType"),
)
if mibBuilder.loadTexts:
    slAlarmConfigEntry.setStatus("current")
_SlAlarmIfIndex_Type = InterfaceIndex
_SlAlarmIfIndex_Object = MibTableColumn
slAlarmIfIndex = _SlAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 1),
    _SlAlarmIfIndex_Type()
)
slAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmIfIndex.setStatus("current")
_SlAlarmType_Type = SlAlarmType
_SlAlarmType_Object = MibTableColumn
slAlarmType = _SlAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 2),
    _SlAlarmType_Type()
)
slAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmType.setStatus("current")


class _SlAlarmSeverity_Type(Integer32):
    """Custom type slAlarmSeverity based on Integer32"""
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
        *(("noAlarm", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("cleared", 4),
          ("notification", 5))
    )


_SlAlarmSeverity_Type.__name__ = "Integer32"
_SlAlarmSeverity_Object = MibTableColumn
slAlarmSeverity = _SlAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 3),
    _SlAlarmSeverity_Type()
)
slAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmSeverity.setStatus("current")
_SlAlarmServiceAffect_Type = TruthValue
_SlAlarmServiceAffect_Object = MibTableColumn
slAlarmServiceAffect = _SlAlarmServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 4),
    _SlAlarmServiceAffect_Type()
)
slAlarmServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmServiceAffect.setStatus("current")
_SlAlarmTimeStamp_Type = TimeStamp
_SlAlarmTimeStamp_Object = MibTableColumn
slAlarmTimeStamp = _SlAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 5),
    _SlAlarmTimeStamp_Type()
)
slAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmTimeStamp.setStatus("current")
_SlAlarmAcknowledged_Type = TruthValue
_SlAlarmAcknowledged_Object = MibTableColumn
slAlarmAcknowledged = _SlAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 6),
    _SlAlarmAcknowledged_Type()
)
slAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlarmAcknowledged.setStatus("current")
_SlAlarmAckUser_Type = DisplayString
_SlAlarmAckUser_Object = MibTableColumn
slAlarmAckUser = _SlAlarmAckUser_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 7),
    _SlAlarmAckUser_Type()
)
slAlarmAckUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slAlarmAckUser.setStatus("current")
_SlAlarmText_Type = DisplayString
_SlAlarmText_Object = MibTableColumn
slAlarmText = _SlAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 8),
    _SlAlarmText_Type()
)
slAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmText.setStatus("current")
_SlAlarmTraps_ObjectIdentity = ObjectIdentity
slAlarmTraps = _SlAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2)
)
_SlAlarmTraps0_ObjectIdentity = ObjectIdentity
slAlarmTraps0 = _SlAlarmTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 0)
)
_SlAlarmActive_Type = TruthValue
_SlAlarmActive_Object = MibScalar
slAlarmActive = _SlAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 1),
    _SlAlarmActive_Type()
)
slAlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slAlarmActive.setStatus("current")

# Managed Objects groups


# Notification objects

slAlarmTrap0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 0, 2)
)
slAlarmTrap0.setObjects(
      *(("SL-ALARM-MIB", "slAlarmIfIndex"),
        ("SL-ALARM-MIB", "slAlarmType"),
        ("SL-ALARM-MIB", "slAlarmSeverity"),
        ("SL-ALARM-MIB", "slAlarmServiceAffect"),
        ("SL-ALARM-MIB", "slAlarmActive"),
        ("SL-ALARM-MIB", "slAlarmText"))
)
if mibBuilder.loadTexts:
    slAlarmTrap0.setStatus(
        "current"
    )

slAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 2)
)
slAlarmTrap.setObjects(
      *(("SL-ALARM-MIB", "slAlarmIfIndex"),
        ("SL-ALARM-MIB", "slAlarmType"),
        ("SL-ALARM-MIB", "slAlarmSeverity"),
        ("SL-ALARM-MIB", "slAlarmServiceAffect"),
        ("SL-ALARM-MIB", "slAlarmActive"),
        ("SL-ALARM-MIB", "slAlarmText"))
)
if mibBuilder.loadTexts:
    slAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ALARM-MIB",
    **{"SlAlarmType": SlAlarmType,
       "slAlarmMib": slAlarmMib,
       "slAlarmConfig": slAlarmConfig,
       "slAlarmConfigTable": slAlarmConfigTable,
       "slAlarmConfigEntry": slAlarmConfigEntry,
       "slAlarmIfIndex": slAlarmIfIndex,
       "slAlarmType": slAlarmType,
       "slAlarmSeverity": slAlarmSeverity,
       "slAlarmServiceAffect": slAlarmServiceAffect,
       "slAlarmTimeStamp": slAlarmTimeStamp,
       "slAlarmAcknowledged": slAlarmAcknowledged,
       "slAlarmAckUser": slAlarmAckUser,
       "slAlarmText": slAlarmText,
       "slAlarmTraps": slAlarmTraps,
       "slAlarmTraps0": slAlarmTraps0,
       "slAlarmTrap0": slAlarmTrap0,
       "slAlarmActive": slAlarmActive,
       "slAlarmTrap": slAlarmTrap}
)
