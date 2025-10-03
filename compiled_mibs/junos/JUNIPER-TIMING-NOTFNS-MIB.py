# SNMP MIB module (JUNIPER-TIMING-NOTFNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-TIMING-NOTFNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:55 2025
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

(InterfaceIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifOperStatus")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(jnxTimingNotfnsMIBRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxTimingNotfnsMIBRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxTimingNotfnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1)
)
if mibBuilder.loadTexts:
    jnxTimingNotfnsMIB.setRevisions(
        ("2019-09-02 04:08",
         "2015-11-14 04:08",
         "2015-10-14 00:00",
         "2013-03-15 15:41")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPtpClockIdTC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class JnxPtpPhaseOffsetTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_JnxTimingFaults_ObjectIdentity = ObjectIdentity
jnxTimingFaults = _JnxTimingFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1)
)
_JnxTimingEvents_ObjectIdentity = ObjectIdentity
jnxTimingEvents = _JnxTimingEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2)
)
_JnxTimingNotfObjects_ObjectIdentity = ObjectIdentity
jnxTimingNotfObjects = _JnxTimingNotfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3)
)


class _JnxClksyncState_Type(Integer32):
    """Custom type jnxClksyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_JnxClksyncState_Type.__name__ = "Integer32"
_JnxClksyncState_Object = MibScalar
jnxClksyncState = _JnxClksyncState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 1),
    _JnxClksyncState_Type()
)
jnxClksyncState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncState.setStatus("current")
_JnxClksyncIfIndex_Type = InterfaceIndex
_JnxClksyncIfIndex_Object = MibScalar
jnxClksyncIfIndex = _JnxClksyncIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 2),
    _JnxClksyncIfIndex_Type()
)
jnxClksyncIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncIfIndex.setStatus("current")
_JnxClksyncIntfName_Type = DisplayString
_JnxClksyncIntfName_Object = MibScalar
jnxClksyncIntfName = _JnxClksyncIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 3),
    _JnxClksyncIntfName_Type()
)
jnxClksyncIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncIntfName.setStatus("current")
_JnxAcbFpgaRevMajor_Type = Integer32
_JnxAcbFpgaRevMajor_Object = MibScalar
jnxAcbFpgaRevMajor = _JnxAcbFpgaRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 4),
    _JnxAcbFpgaRevMajor_Type()
)
jnxAcbFpgaRevMajor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAcbFpgaRevMajor.setStatus("current")
_JnxAcbFpgaRevMinor_Type = Integer32
_JnxAcbFpgaRevMinor_Object = MibScalar
jnxAcbFpgaRevMinor = _JnxAcbFpgaRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 5),
    _JnxAcbFpgaRevMinor_Type()
)
jnxAcbFpgaRevMinor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAcbFpgaRevMinor.setStatus("current")
_JnxBootCpldFpgaRevMajor_Type = Integer32
_JnxBootCpldFpgaRevMajor_Object = MibScalar
jnxBootCpldFpgaRevMajor = _JnxBootCpldFpgaRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 6),
    _JnxBootCpldFpgaRevMajor_Type()
)
jnxBootCpldFpgaRevMajor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBootCpldFpgaRevMajor.setStatus("current")
_JnxBootCpldFpgaRevMinor_Type = Integer32
_JnxBootCpldFpgaRevMinor_Object = MibScalar
jnxBootCpldFpgaRevMinor = _JnxBootCpldFpgaRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 7),
    _JnxBootCpldFpgaRevMinor_Type()
)
jnxBootCpldFpgaRevMinor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBootCpldFpgaRevMinor.setStatus("current")


class _JnxClksyncQualityCode_Type(Integer32):
    """Custom type jnxClksyncQualityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("stu", 0),
          ("prs", 1),
          ("prc", 2),
          ("ssu-a", 4),
          ("st2", 7),
          ("ssu-b", 8),
          ("st3", 10),
          ("sec", 11),
          ("smc", 12),
          ("st3e", 13),
          ("st4", 14),
          ("dnu", 15),
          ("tnc", 16),
          ("dus", 17))
    )


_JnxClksyncQualityCode_Type.__name__ = "Integer32"
_JnxClksyncQualityCode_Object = MibScalar
jnxClksyncQualityCode = _JnxClksyncQualityCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 8),
    _JnxClksyncQualityCode_Type()
)
jnxClksyncQualityCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncQualityCode.setStatus("current")


class _JnxClksyncDpllState_Type(Integer32):
    """Custom type jnxClksyncDpllState based on Integer32"""
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
        *(("init-phase", 0),
          ("acquiring-lock", 1),
          ("locked", 2),
          ("holdover", 3),
          ("free-run", 4),
          ("unknown", 5))
    )


_JnxClksyncDpllState_Type.__name__ = "Integer32"
_JnxClksyncDpllState_Object = MibScalar
jnxClksyncDpllState = _JnxClksyncDpllState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 9),
    _JnxClksyncDpllState_Type()
)
jnxClksyncDpllState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncDpllState.setStatus("current")


class _JnxPtpServoState_Type(Integer32):
    """Custom type jnxPtpServoState based on Integer32"""
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
        *(("init", 0),
          ("free-run", 1),
          ("holdover", 2),
          ("acquiring", 3),
          ("freq-locked", 4),
          ("phase-aligned", 5))
    )


_JnxPtpServoState_Type.__name__ = "Integer32"
_JnxPtpServoState_Object = MibScalar
jnxPtpServoState = _JnxPtpServoState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 10),
    _JnxPtpServoState_Type()
)
jnxPtpServoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpServoState.setStatus("current")
_JnxPtpClass_Type = Integer32
_JnxPtpClass_Object = MibScalar
jnxPtpClass = _JnxPtpClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 11),
    _JnxPtpClass_Type()
)
jnxPtpClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpClass.setStatus("current")
_JnxPtpAccuracy_Type = Integer32
_JnxPtpAccuracy_Object = MibScalar
jnxPtpAccuracy = _JnxPtpAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 12),
    _JnxPtpAccuracy_Type()
)
jnxPtpAccuracy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpAccuracy.setStatus("current")
_JnxPtpGmId_Type = JnxPtpClockIdTC
_JnxPtpGmId_Object = MibScalar
jnxPtpGmId = _JnxPtpGmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 13),
    _JnxPtpGmId_Type()
)
jnxPtpGmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpGmId.setStatus("current")
_JnxPtpGmIpAddr_Type = InetAddress
_JnxPtpGmIpAddr_Object = MibScalar
jnxPtpGmIpAddr = _JnxPtpGmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 14),
    _JnxPtpGmIpAddr_Type()
)
jnxPtpGmIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpGmIpAddr.setStatus("current")
_JnxClkStreamHandle_Type = Integer32
_JnxClkStreamHandle_Object = MibScalar
jnxClkStreamHandle = _JnxClkStreamHandle_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 15),
    _JnxClkStreamHandle_Type()
)
jnxClkStreamHandle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClkStreamHandle.setStatus("current")
_JnxRemoteIpAddr_Type = InetAddress
_JnxRemoteIpAddr_Object = MibScalar
jnxRemoteIpAddr = _JnxRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 16),
    _JnxRemoteIpAddr_Type()
)
jnxRemoteIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxRemoteIpAddr.setStatus("current")


class _JnxClksyncHybridState_Type(Integer32):
    """Custom type jnxClksyncHybridState based on Integer32"""
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
        *(("init", 0),
          ("freq-acq", 1),
          ("freqLck-phaseAcq1", 2),
          ("freqLck-phaseAcq2", 3),
          ("freqLck-phaseAcq3", 4),
          ("freq-phase-lck", 5))
    )


_JnxClksyncHybridState_Type.__name__ = "Integer32"
_JnxClksyncHybridState_Object = MibScalar
jnxClksyncHybridState = _JnxClksyncHybridState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 17),
    _JnxClksyncHybridState_Type()
)
jnxClksyncHybridState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncHybridState.setStatus("current")
_JnxPtpPhaseOffset_Type = DisplayString
_JnxPtpPhaseOffset_Object = MibScalar
jnxPtpPhaseOffset = _JnxPtpPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 18),
    _JnxPtpPhaseOffset_Type()
)
jnxPtpPhaseOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpPhaseOffset.setStatus("current")
_JnxClksyncQualityCodeStr_Type = DisplayString
_JnxClksyncQualityCodeStr_Object = MibScalar
jnxClksyncQualityCodeStr = _JnxClksyncQualityCodeStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 19),
    _JnxClksyncQualityCodeStr_Type()
)
jnxClksyncQualityCodeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncQualityCodeStr.setStatus("current")
_JnxClksyncDpllStateStr_Type = DisplayString
_JnxClksyncDpllStateStr_Object = MibScalar
jnxClksyncDpllStateStr = _JnxClksyncDpllStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 20),
    _JnxClksyncDpllStateStr_Type()
)
jnxClksyncDpllStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncDpllStateStr.setStatus("current")
_JnxPtpServoStateStr_Type = DisplayString
_JnxPtpServoStateStr_Object = MibScalar
jnxPtpServoStateStr = _JnxPtpServoStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 21),
    _JnxPtpServoStateStr_Type()
)
jnxPtpServoStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpServoStateStr.setStatus("current")
_JnxClksyncHybridStateStr_Type = DisplayString
_JnxClksyncHybridStateStr_Object = MibScalar
jnxClksyncHybridStateStr = _JnxClksyncHybridStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 22),
    _JnxClksyncHybridStateStr_Type()
)
jnxClksyncHybridStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncHybridStateStr.setStatus("current")
_JnxClksyncColorStr_Type = DisplayString
_JnxClksyncColorStr_Object = MibScalar
jnxClksyncColorStr = _JnxClksyncColorStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 23),
    _JnxClksyncColorStr_Type()
)
jnxClksyncColorStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncColorStr.setStatus("current")
_JnxPtpUtcOffset_Type = JnxPtpPhaseOffsetTC
_JnxPtpUtcOffset_Object = MibScalar
jnxPtpUtcOffset = _JnxPtpUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 24),
    _JnxPtpUtcOffset_Type()
)
jnxPtpUtcOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpUtcOffset.setStatus("current")
_JnxGpsRecvStatus_Type = DisplayString
_JnxGpsRecvStatus_Object = MibScalar
jnxGpsRecvStatus = _JnxGpsRecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 25),
    _JnxGpsRecvStatus_Type()
)
jnxGpsRecvStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxGpsRecvStatus.setStatus("current")
_JnxPtpAdvClockClass_Type = Integer32
_JnxPtpAdvClockClass_Object = MibScalar
jnxPtpAdvClockClass = _JnxPtpAdvClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 26),
    _JnxPtpAdvClockClass_Type()
)
jnxPtpAdvClockClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpAdvClockClass.setStatus("current")
_JnxClksyncSynceLockedIfIndex_Type = InterfaceIndex
_JnxClksyncSynceLockedIfIndex_Object = MibScalar
jnxClksyncSynceLockedIfIndex = _JnxClksyncSynceLockedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 27),
    _JnxClksyncSynceLockedIfIndex_Type()
)
jnxClksyncSynceLockedIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncSynceLockedIfIndex.setStatus("current")
_JnxClksyncSynceLockedIntfName_Type = DisplayString
_JnxClksyncSynceLockedIntfName_Object = MibScalar
jnxClksyncSynceLockedIntfName = _JnxClksyncSynceLockedIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 28),
    _JnxClksyncSynceLockedIntfName_Type()
)
jnxClksyncSynceLockedIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncSynceLockedIntfName.setStatus("current")
_JnxClksyncSynceQualityTable_Object = MibTable
jnxClksyncSynceQualityTable = _JnxClksyncSynceQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 29)
)
if mibBuilder.loadTexts:
    jnxClksyncSynceQualityTable.setStatus("current")
_JnxClksyncSynceQualityEntry_Object = MibTableRow
jnxClksyncSynceQualityEntry = _JnxClksyncSynceQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 29, 1)
)
jnxClksyncSynceQualityEntry.setIndexNames(
    (0, "JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncSynceQualityTableIndex"),
)
if mibBuilder.loadTexts:
    jnxClksyncSynceQualityEntry.setStatus("current")
_JnxClksyncSynceQualityTableIndex_Type = Integer32
_JnxClksyncSynceQualityTableIndex_Object = MibTableColumn
jnxClksyncSynceQualityTableIndex = _JnxClksyncSynceQualityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 29, 1, 1),
    _JnxClksyncSynceQualityTableIndex_Type()
)
jnxClksyncSynceQualityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClksyncSynceQualityTableIndex.setStatus("current")
_JnxClksyncSynceQualityIntfName_Type = DisplayString
_JnxClksyncSynceQualityIntfName_Object = MibTableColumn
jnxClksyncSynceQualityIntfName = _JnxClksyncSynceQualityIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 29, 1, 2),
    _JnxClksyncSynceQualityIntfName_Type()
)
jnxClksyncSynceQualityIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxClksyncSynceQualityIntfName.setStatus("current")
_JnxClksyncSynceQualityValue_Type = DisplayString
_JnxClksyncSynceQualityValue_Object = MibTableColumn
jnxClksyncSynceQualityValue = _JnxClksyncSynceQualityValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 29, 1, 3),
    _JnxClksyncSynceQualityValue_Type()
)
jnxClksyncSynceQualityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxClksyncSynceQualityValue.setStatus("current")


class _JnxPtpUtcValid_Type(Integer32):
    """Custom type jnxPtpUtcValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_JnxPtpUtcValid_Type.__name__ = "Integer32"
_JnxPtpUtcValid_Object = MibScalar
jnxPtpUtcValid = _JnxPtpUtcValid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 30),
    _JnxPtpUtcValid_Type()
)
jnxPtpUtcValid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpUtcValid.setStatus("current")


class _JnxTimingFrequencyTraceability_Type(Integer32):
    """Custom type jnxTimingFrequencyTraceability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_JnxTimingFrequencyTraceability_Type.__name__ = "Integer32"
_JnxTimingFrequencyTraceability_Object = MibScalar
jnxTimingFrequencyTraceability = _JnxTimingFrequencyTraceability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 33),
    _JnxTimingFrequencyTraceability_Type()
)
jnxTimingFrequencyTraceability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxTimingFrequencyTraceability.setStatus("current")


class _JnxTimingTimeTraceability_Type(Integer32):
    """Custom type jnxTimingTimeTraceability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_JnxTimingTimeTraceability_Type.__name__ = "Integer32"
_JnxTimingTimeTraceability_Object = MibScalar
jnxTimingTimeTraceability = _JnxTimingTimeTraceability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 34),
    _JnxTimingTimeTraceability_Type()
)
jnxTimingTimeTraceability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxTimingTimeTraceability.setStatus("current")
_JnxClksyncPtpOperationalMasterTable_Object = MibTable
jnxClksyncPtpOperationalMasterTable = _JnxClksyncPtpOperationalMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 35)
)
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalMasterTable.setStatus("current")
_JnxClksyncPtpOperationalMasterEntry_Object = MibTableRow
jnxClksyncPtpOperationalMasterEntry = _JnxClksyncPtpOperationalMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 35, 1)
)
jnxClksyncPtpOperationalMasterEntry.setIndexNames(
    (0, "JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncPtpOperationalMasterIndex"),
    (0, "JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncPtpOperationalMasterAttrIndex"),
)
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalMasterEntry.setStatus("current")


class _JnxClksyncPtpOperationalMasterIndex_Type(Integer32):
    """Custom type jnxClksyncPtpOperationalMasterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_JnxClksyncPtpOperationalMasterIndex_Type.__name__ = "Integer32"
_JnxClksyncPtpOperationalMasterIndex_Object = MibTableColumn
jnxClksyncPtpOperationalMasterIndex = _JnxClksyncPtpOperationalMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 35, 1, 1),
    _JnxClksyncPtpOperationalMasterIndex_Type()
)
jnxClksyncPtpOperationalMasterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalMasterIndex.setStatus("current")


class _JnxClksyncPtpOperationalMasterAttrIndex_Type(Integer32):
    """Custom type jnxClksyncPtpOperationalMasterAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_JnxClksyncPtpOperationalMasterAttrIndex_Type.__name__ = "Integer32"
_JnxClksyncPtpOperationalMasterAttrIndex_Object = MibTableColumn
jnxClksyncPtpOperationalMasterAttrIndex = _JnxClksyncPtpOperationalMasterAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 35, 1, 2),
    _JnxClksyncPtpOperationalMasterAttrIndex_Type()
)
jnxClksyncPtpOperationalMasterAttrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalMasterAttrIndex.setStatus("current")
_JnxClksyncPtpOperationalMasters_Type = DisplayString
_JnxClksyncPtpOperationalMasters_Object = MibTableColumn
jnxClksyncPtpOperationalMasters = _JnxClksyncPtpOperationalMasters_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 35, 1, 3),
    _JnxClksyncPtpOperationalMasters_Type()
)
jnxClksyncPtpOperationalMasters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalMasters.setStatus("current")
_JnxClksyncPtpOperationalSlaveTable_Object = MibTable
jnxClksyncPtpOperationalSlaveTable = _JnxClksyncPtpOperationalSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 36)
)
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalSlaveTable.setStatus("current")
_JnxClksyncPtpOperationalSlaveEntry_Object = MibTableRow
jnxClksyncPtpOperationalSlaveEntry = _JnxClksyncPtpOperationalSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 36, 1)
)
jnxClksyncPtpOperationalSlaveEntry.setIndexNames(
    (0, "JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncPtpOperationalSlaveIndex"),
    (0, "JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncPtpOperationalSlaveAttrIndex"),
)
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalSlaveEntry.setStatus("current")


class _JnxClksyncPtpOperationalSlaveIndex_Type(Integer32):
    """Custom type jnxClksyncPtpOperationalSlaveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_JnxClksyncPtpOperationalSlaveIndex_Type.__name__ = "Integer32"
_JnxClksyncPtpOperationalSlaveIndex_Object = MibTableColumn
jnxClksyncPtpOperationalSlaveIndex = _JnxClksyncPtpOperationalSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 36, 1, 1),
    _JnxClksyncPtpOperationalSlaveIndex_Type()
)
jnxClksyncPtpOperationalSlaveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalSlaveIndex.setStatus("current")


class _JnxClksyncPtpOperationalSlaveAttrIndex_Type(Integer32):
    """Custom type jnxClksyncPtpOperationalSlaveAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_JnxClksyncPtpOperationalSlaveAttrIndex_Type.__name__ = "Integer32"
_JnxClksyncPtpOperationalSlaveAttrIndex_Object = MibTableColumn
jnxClksyncPtpOperationalSlaveAttrIndex = _JnxClksyncPtpOperationalSlaveAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 36, 1, 2),
    _JnxClksyncPtpOperationalSlaveAttrIndex_Type()
)
jnxClksyncPtpOperationalSlaveAttrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalSlaveAttrIndex.setStatus("current")
_JnxClksyncPtpOperationalSlaves_Type = DisplayString
_JnxClksyncPtpOperationalSlaves_Object = MibTableColumn
jnxClksyncPtpOperationalSlaves = _JnxClksyncPtpOperationalSlaves_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 36, 1, 3),
    _JnxClksyncPtpOperationalSlaves_Type()
)
jnxClksyncPtpOperationalSlaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxClksyncPtpOperationalSlaves.setStatus("current")
_JnxClksyncAdditionalInformationStr_Type = DisplayString
_JnxClksyncAdditionalInformationStr_Object = MibScalar
jnxClksyncAdditionalInformationStr = _JnxClksyncAdditionalInformationStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 37),
    _JnxClksyncAdditionalInformationStr_Type()
)
jnxClksyncAdditionalInformationStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncAdditionalInformationStr.setStatus("current")
_JnxTimingConformance_ObjectIdentity = ObjectIdentity
jnxTimingConformance = _JnxTimingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4)
)
_JnxTimingCompliances_ObjectIdentity = ObjectIdentity
jnxTimingCompliances = _JnxTimingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 1)
)
_JnxTimingGroups_ObjectIdentity = ObjectIdentity
jnxTimingGroups = _JnxTimingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2)
)

# Managed Objects groups

jnxTimingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 1)
)
jnxTimingObjectsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMinor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMinor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpClass"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpAccuracy"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmIpAddr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpPhaseOffset"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncColorStr"))
)
if mibBuilder.loadTexts:
    jnxTimingObjectsGroup.setStatus("current")


# Notification objects

jnxTimingFaultLOSSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 1)
)
jnxTimingFaultLOSSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOSSet.setStatus(
        "current"
    )

jnxTimingFaultLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 2)
)
jnxTimingFaultLOSClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOSClear.setStatus(
        "current"
    )

jnxTimingFaultEFDSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 3)
)
jnxTimingFaultEFDSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultEFDSet.setStatus(
        "current"
    )

jnxTimingFaultEFDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 4)
)
jnxTimingFaultEFDClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultEFDClear.setStatus(
        "current"
    )

jnxTimingFaultLOESMCSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 5)
)
jnxTimingFaultLOESMCSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOESMCSet.setStatus(
        "current"
    )

jnxTimingFaultLOESMCClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 6)
)
jnxTimingFaultLOESMCClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOESMCClear.setStatus(
        "current"
    )

jnxTimingFaultQLFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 7)
)
jnxTimingFaultQLFailSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultQLFailSet.setStatus(
        "current"
    )

jnxTimingFaultQLFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 8)
)
jnxTimingFaultQLFailClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultQLFailClear.setStatus(
        "current"
    )

jnxTimingFaultLTISet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 9)
)
jnxTimingFaultLTISet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLTISet.setStatus(
        "current"
    )

jnxTimingFaultLTIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 10)
)
jnxTimingFaultLTIClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLTIClear.setStatus(
        "current"
    )

jnxTimingFaultAcbcFpgaVerNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 11)
)
jnxTimingFaultAcbcFpgaVerNotCompatible.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMinor"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultAcbcFpgaVerNotCompatible.setStatus(
        "current"
    )

jnxTimingFaultBootCpldVerNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 12)
)
jnxTimingFaultBootCpldVerNotCompatible.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMinor"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultBootCpldVerNotCompatible.setStatus(
        "current"
    )

jnxTimingFaultPriSrcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 13)
)
jnxTimingFaultPriSrcFailed.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPriSrcFailed.setStatus(
        "current"
    )

jnxTimingFaultSecSrcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 14)
)
jnxTimingFaultSecSrcFailed.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultSecSrcFailed.setStatus(
        "current"
    )

jnxTimingFaultPtpUniNegRateRejectSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 15)
)
jnxTimingFaultPtpUniNegRateRejectSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPtpUniNegRateRejectSet.setStatus(
        "current"
    )

jnxTimingFaultPtpUniNegRateRejectClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 16)
)
jnxTimingFaultPtpUniNegRateRejectClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPtpUniNegRateRejectClear.setStatus(
        "current"
    )

jnxTimingEventSquelchSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 17)
)
jnxTimingEventSquelchSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSquelchSet.setStatus(
        "current"
    )

jnxTimingEventSquelchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 18)
)
jnxTimingEventSquelchClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSquelchClear.setStatus(
        "current"
    )

jnxTimingAlarmNoAnnounceMessageSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 19)
)
jnxTimingAlarmNoAnnounceMessageSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoAnnounceMessageSet.setStatus(
        "current"
    )

jnxTimingAlarmNoAnnounceMessageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 20)
)
jnxTimingAlarmNoAnnounceMessageClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoAnnounceMessageClear.setStatus(
        "current"
    )

jnxTimingAlarmNoSyncMessageSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 21)
)
jnxTimingAlarmNoSyncMessageSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoSyncMessageSet.setStatus(
        "current"
    )

jnxTimingAlarmNoSyncMessageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 22)
)
jnxTimingAlarmNoSyncMessageClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoSyncMessageClear.setStatus(
        "current"
    )

jnxTimingAlarmNoDelayResponseMessageSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 23)
)
jnxTimingAlarmNoDelayResponseMessageSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoDelayResponseMessageSet.setStatus(
        "current"
    )

jnxTimingAlarmNoDelayResponseMessageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 24)
)
jnxTimingAlarmNoDelayResponseMessageClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoDelayResponseMessageClear.setStatus(
        "current"
    )

jnxTimingAlarmHighPDVDetectedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 25)
)
jnxTimingAlarmHighPDVDetectedSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmHighPDVDetectedSet.setStatus(
        "current"
    )

jnxTimingAlarmHighPDVDetectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 26)
)
jnxTimingAlarmHighPDVDetectedClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmHighPDVDetectedClear.setStatus(
        "current"
    )

jnxTimingAlarmSlaveCandidateStateLoseLockSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 27)
)
jnxTimingAlarmSlaveCandidateStateLoseLockSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmSlaveCandidateStateLoseLockSet.setStatus(
        "current"
    )

jnxTimingAlarmSlaveCandidateStateLoseLockClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 28)
)
jnxTimingAlarmSlaveCandidateStateLoseLockClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmSlaveCandidateStateLoseLockClear.setStatus(
        "current"
    )

jnxTimingAlarmNoForeignMasterSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 29)
)
jnxTimingAlarmNoForeignMasterSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoForeignMasterSet.setStatus(
        "current"
    )

jnxTimingAlarmNoForeignMasterClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 30)
)
jnxTimingAlarmNoForeignMasterClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoForeignMasterClear.setStatus(
        "current"
    )

jnxTimingAlarmPtpSyncFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 31)
)
jnxTimingAlarmPtpSyncFailSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmPtpSyncFailSet.setStatus(
        "current"
    )

jnxTimingAlarmPtpSyncFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 32)
)
jnxTimingAlarmPtpSyncFailClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmPtpSyncFailClear.setStatus(
        "current"
    )

jnxTimingAlarmPtpLocalClockOutOfSyncSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 33)
)
jnxTimingAlarmPtpLocalClockOutOfSyncSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmPtpLocalClockOutOfSyncSet.setStatus(
        "current"
    )

jnxTimingAlarmPtpLocalClockOutOfSyncClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 34)
)
jnxTimingAlarmPtpLocalClockOutOfSyncClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmPtpLocalClockOutOfSyncClear.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference1Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 35)
)
jnxTimingAlarmLossOfReference1Set.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference1Set.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference1Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 36)
)
jnxTimingAlarmLossOfReference1Clear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference1Clear.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference2Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 37)
)
jnxTimingAlarmLossOfReference2Set.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference2Set.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference2Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 38)
)
jnxTimingAlarmLossOfReference2Clear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference2Clear.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference3Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 39)
)
jnxTimingAlarmLossOfReference3Set.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference3Set.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference3Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 40)
)
jnxTimingAlarmLossOfReference3Clear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference3Clear.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference4Set = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 41)
)
jnxTimingAlarmLossOfReference4Set.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference4Set.setStatus(
        "current"
    )

jnxTimingAlarmLossOfReference4Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 42)
)
jnxTimingAlarmLossOfReference4Clear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmLossOfReference4Clear.setStatus(
        "current"
    )

jnxTimingAlarmNoMoreReferenceSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 43)
)
jnxTimingAlarmNoMoreReferenceSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoMoreReferenceSet.setStatus(
        "current"
    )

jnxTimingAlarmNoMoreReferenceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 44)
)
jnxTimingAlarmNoMoreReferenceClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmNoMoreReferenceClear.setStatus(
        "current"
    )

jnxTimingAlarmQlBelowThresholdSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 45)
)
jnxTimingAlarmQlBelowThresholdSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmQlBelowThresholdSet.setStatus(
        "current"
    )

jnxTimingAlarmQlBelowThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 46)
)
jnxTimingAlarmQlBelowThresholdClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmQlBelowThresholdClear.setStatus(
        "current"
    )

jnxTimingAlarmDPLLNotLockedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 47)
)
jnxTimingAlarmDPLLNotLockedSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmDPLLNotLockedSet.setStatus(
        "current"
    )

jnxTimingAlarmDPLLNotLockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 48)
)
jnxTimingAlarmDPLLNotLockedClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmDPLLNotLockedClear.setStatus(
        "current"
    )

jnxTimingAlarmTodInSignalFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 49)
)
jnxTimingAlarmTodInSignalFailSet.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmTodInSignalFailSet.setStatus(
        "current"
    )

jnxTimingAlarmTodInSignalFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 50)
)
jnxTimingAlarmTodInSignalFailClear.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingAlarmTodInSignalFailClear.setStatus(
        "current"
    )

jnxTimingEventDelayAsymmetryExceedMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 51)
)
jnxTimingEventDelayAsymmetryExceedMinor.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingEventDelayAsymmetryExceedMinor.setStatus(
        "current"
    )

jnxTimingEventDelayAsymmetryExceedCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 52)
)
jnxTimingEventDelayAsymmetryExceedCritical.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncAdditionalInformationStr")
)
if mibBuilder.loadTexts:
    jnxTimingEventDelayAsymmetryExceedCritical.setStatus(
        "current"
    )

jnxTimingEventPriSrcRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 1)
)
jnxTimingEventPriSrcRecovered.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPriSrcRecovered.setStatus(
        "current"
    )

jnxTimingEventSecSrcRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 2)
)
jnxTimingEventSecSrcRecovered.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSecSrcRecovered.setStatus(
        "current"
    )

jnxTimingEventPriRefChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 3)
)
jnxTimingEventPriRefChanged.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPriRefChanged.setStatus(
        "current"
    )

jnxTimingEventSecRefChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 4)
)
jnxTimingEventSecRefChanged.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSecRefChanged.setStatus(
        "current"
    )

jnxTimingEventQLChangedRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 5)
)
jnxTimingEventQLChangedRx.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventQLChangedRx.setStatus(
        "current"
    )

jnxTimingEventQLChangedTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 6)
)
jnxTimingEventQLChangedTx.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventQLChangedTx.setStatus(
        "current"
    )

jnxTimingEventSynceHldovrToLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 7)
)
jnxTimingEventSynceHldovrToLck.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceHldovrToLck.setStatus(
        "current"
    )

jnxTimingEventSynceLckToHldovr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 8)
)
jnxTimingEventSynceLckToHldovr.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceLckToHldovr.setStatus(
        "current"
    )

jnxTimingEventDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 9)
)
jnxTimingEventDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventDpllStatus.setStatus(
        "current"
    )

jnxTimingEventSynceDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 10)
)
jnxTimingEventSynceDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceDpllStatus.setStatus(
        "current"
    )

jnxTimingEventBitsDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 11)
)
jnxTimingEventBitsDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventBitsDpllStatus.setStatus(
        "current"
    )

jnxTimingEventPtpServoStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 12)
)
jnxTimingEventPtpServoStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpServoStatus.setStatus(
        "current"
    )

jnxTimingEventPtpGMClockClassChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 13)
)
jnxTimingEventPtpGMClockClassChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpClass"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMClockClassChange.setStatus(
        "current"
    )

jnxTimingEventPtpGMClockAccuracyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 14)
)
jnxTimingEventPtpGMClockAccuracyChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpAccuracy"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMClockAccuracyChange.setStatus(
        "current"
    )

jnxTimingEventPtpGMChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 15)
)
jnxTimingEventPtpGMChange.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId")
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMChange.setStatus(
        "current"
    )

jnxTimingEventHybridStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 16)
)
jnxTimingEventHybridStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventHybridStatus.setStatus(
        "current"
    )

jnxTimingEventLedColorChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 19)
)
jnxTimingEventLedColorChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncColorStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventLedColorChange.setStatus(
        "current"
    )


# Notifications groups

jnxTimingNotfnFaultsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 2)
)
jnxTimingNotfnFaultsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOSSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOSClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultEFDSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultEFDClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOESMCSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOESMCClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultQLFailSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultQLFailClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLTISet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLTIClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultAcbcFpgaVerNotCompatible"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultBootCpldVerNotCompatible"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPriSrcFailed"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultSecSrcFailed"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPtpUniNegRateRejectSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPtpUniNegRateRejectClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoAnnounceMessageSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoAnnounceMessageClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoSyncMessageSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoSyncMessageClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoDelayResponseMessageSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoDelayResponseMessageClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmHighPDVDetectedSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmHighPDVDetectedClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmSlaveCandidateStateLoseLockSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmSlaveCandidateStateLoseLockClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoForeignMasterSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoForeignMasterClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmPtpSyncFailSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmPtpSyncFailClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmPtpLocalClockOutOfSyncSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmPtpLocalClockOutOfSyncClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference1Set"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference1Clear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference2Set"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference2Clear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference3Set"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference3Clear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference4Set"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmLossOfReference4Clear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoMoreReferenceSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmNoMoreReferenceClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmQlBelowThresholdSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmQlBelowThresholdClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmDPLLNotLockedSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmDPLLNotLockedClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmTodInSignalFailSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingAlarmTodInSignalFailClear"))
)
if mibBuilder.loadTexts:
    jnxTimingNotfnFaultsGroup.setStatus(
        "current"
    )

jnxTimingNotfnEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 3)
)
jnxTimingNotfnEventsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPriSrcRecovered"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSecSrcRecovered"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPriRefChanged"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSecRefChanged"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventQLChangedRx"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventQLChangedTx"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceHldovrToLck"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceLckToHldovr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventBitsDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpServoStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMClockClassChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMClockAccuracyChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventHybridStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSquelchSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSquelchClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventLedColorChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventDelayAsymmetryExceedMinor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventDelayAsymmetryExceedCritical"))
)
if mibBuilder.loadTexts:
    jnxTimingNotfnEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jnxTimingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 1, 1)
)
jnxTimingCompliance.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingObjectsGroup"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingNotfnFaultsGroup"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingNotfnEventsGroup"))
)
if mibBuilder.loadTexts:
    jnxTimingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TIMING-NOTFNS-MIB",
    **{"JnxPtpClockIdTC": JnxPtpClockIdTC,
       "JnxPtpPhaseOffsetTC": JnxPtpPhaseOffsetTC,
       "jnxTimingNotfnsMIB": jnxTimingNotfnsMIB,
       "jnxTimingFaults": jnxTimingFaults,
       "jnxTimingFaultLOSSet": jnxTimingFaultLOSSet,
       "jnxTimingFaultLOSClear": jnxTimingFaultLOSClear,
       "jnxTimingFaultEFDSet": jnxTimingFaultEFDSet,
       "jnxTimingFaultEFDClear": jnxTimingFaultEFDClear,
       "jnxTimingFaultLOESMCSet": jnxTimingFaultLOESMCSet,
       "jnxTimingFaultLOESMCClear": jnxTimingFaultLOESMCClear,
       "jnxTimingFaultQLFailSet": jnxTimingFaultQLFailSet,
       "jnxTimingFaultQLFailClear": jnxTimingFaultQLFailClear,
       "jnxTimingFaultLTISet": jnxTimingFaultLTISet,
       "jnxTimingFaultLTIClear": jnxTimingFaultLTIClear,
       "jnxTimingFaultAcbcFpgaVerNotCompatible": jnxTimingFaultAcbcFpgaVerNotCompatible,
       "jnxTimingFaultBootCpldVerNotCompatible": jnxTimingFaultBootCpldVerNotCompatible,
       "jnxTimingFaultPriSrcFailed": jnxTimingFaultPriSrcFailed,
       "jnxTimingFaultSecSrcFailed": jnxTimingFaultSecSrcFailed,
       "jnxTimingFaultPtpUniNegRateRejectSet": jnxTimingFaultPtpUniNegRateRejectSet,
       "jnxTimingFaultPtpUniNegRateRejectClear": jnxTimingFaultPtpUniNegRateRejectClear,
       "jnxTimingEventSquelchSet": jnxTimingEventSquelchSet,
       "jnxTimingEventSquelchClear": jnxTimingEventSquelchClear,
       "jnxTimingAlarmNoAnnounceMessageSet": jnxTimingAlarmNoAnnounceMessageSet,
       "jnxTimingAlarmNoAnnounceMessageClear": jnxTimingAlarmNoAnnounceMessageClear,
       "jnxTimingAlarmNoSyncMessageSet": jnxTimingAlarmNoSyncMessageSet,
       "jnxTimingAlarmNoSyncMessageClear": jnxTimingAlarmNoSyncMessageClear,
       "jnxTimingAlarmNoDelayResponseMessageSet": jnxTimingAlarmNoDelayResponseMessageSet,
       "jnxTimingAlarmNoDelayResponseMessageClear": jnxTimingAlarmNoDelayResponseMessageClear,
       "jnxTimingAlarmHighPDVDetectedSet": jnxTimingAlarmHighPDVDetectedSet,
       "jnxTimingAlarmHighPDVDetectedClear": jnxTimingAlarmHighPDVDetectedClear,
       "jnxTimingAlarmSlaveCandidateStateLoseLockSet": jnxTimingAlarmSlaveCandidateStateLoseLockSet,
       "jnxTimingAlarmSlaveCandidateStateLoseLockClear": jnxTimingAlarmSlaveCandidateStateLoseLockClear,
       "jnxTimingAlarmNoForeignMasterSet": jnxTimingAlarmNoForeignMasterSet,
       "jnxTimingAlarmNoForeignMasterClear": jnxTimingAlarmNoForeignMasterClear,
       "jnxTimingAlarmPtpSyncFailSet": jnxTimingAlarmPtpSyncFailSet,
       "jnxTimingAlarmPtpSyncFailClear": jnxTimingAlarmPtpSyncFailClear,
       "jnxTimingAlarmPtpLocalClockOutOfSyncSet": jnxTimingAlarmPtpLocalClockOutOfSyncSet,
       "jnxTimingAlarmPtpLocalClockOutOfSyncClear": jnxTimingAlarmPtpLocalClockOutOfSyncClear,
       "jnxTimingAlarmLossOfReference1Set": jnxTimingAlarmLossOfReference1Set,
       "jnxTimingAlarmLossOfReference1Clear": jnxTimingAlarmLossOfReference1Clear,
       "jnxTimingAlarmLossOfReference2Set": jnxTimingAlarmLossOfReference2Set,
       "jnxTimingAlarmLossOfReference2Clear": jnxTimingAlarmLossOfReference2Clear,
       "jnxTimingAlarmLossOfReference3Set": jnxTimingAlarmLossOfReference3Set,
       "jnxTimingAlarmLossOfReference3Clear": jnxTimingAlarmLossOfReference3Clear,
       "jnxTimingAlarmLossOfReference4Set": jnxTimingAlarmLossOfReference4Set,
       "jnxTimingAlarmLossOfReference4Clear": jnxTimingAlarmLossOfReference4Clear,
       "jnxTimingAlarmNoMoreReferenceSet": jnxTimingAlarmNoMoreReferenceSet,
       "jnxTimingAlarmNoMoreReferenceClear": jnxTimingAlarmNoMoreReferenceClear,
       "jnxTimingAlarmQlBelowThresholdSet": jnxTimingAlarmQlBelowThresholdSet,
       "jnxTimingAlarmQlBelowThresholdClear": jnxTimingAlarmQlBelowThresholdClear,
       "jnxTimingAlarmDPLLNotLockedSet": jnxTimingAlarmDPLLNotLockedSet,
       "jnxTimingAlarmDPLLNotLockedClear": jnxTimingAlarmDPLLNotLockedClear,
       "jnxTimingAlarmTodInSignalFailSet": jnxTimingAlarmTodInSignalFailSet,
       "jnxTimingAlarmTodInSignalFailClear": jnxTimingAlarmTodInSignalFailClear,
       "jnxTimingEventDelayAsymmetryExceedMinor": jnxTimingEventDelayAsymmetryExceedMinor,
       "jnxTimingEventDelayAsymmetryExceedCritical": jnxTimingEventDelayAsymmetryExceedCritical,
       "jnxTimingEvents": jnxTimingEvents,
       "jnxTimingEventPriSrcRecovered": jnxTimingEventPriSrcRecovered,
       "jnxTimingEventSecSrcRecovered": jnxTimingEventSecSrcRecovered,
       "jnxTimingEventPriRefChanged": jnxTimingEventPriRefChanged,
       "jnxTimingEventSecRefChanged": jnxTimingEventSecRefChanged,
       "jnxTimingEventQLChangedRx": jnxTimingEventQLChangedRx,
       "jnxTimingEventQLChangedTx": jnxTimingEventQLChangedTx,
       "jnxTimingEventSynceHldovrToLck": jnxTimingEventSynceHldovrToLck,
       "jnxTimingEventSynceLckToHldovr": jnxTimingEventSynceLckToHldovr,
       "jnxTimingEventDpllStatus": jnxTimingEventDpllStatus,
       "jnxTimingEventSynceDpllStatus": jnxTimingEventSynceDpllStatus,
       "jnxTimingEventBitsDpllStatus": jnxTimingEventBitsDpllStatus,
       "jnxTimingEventPtpServoStatus": jnxTimingEventPtpServoStatus,
       "jnxTimingEventPtpGMClockClassChange": jnxTimingEventPtpGMClockClassChange,
       "jnxTimingEventPtpGMClockAccuracyChange": jnxTimingEventPtpGMClockAccuracyChange,
       "jnxTimingEventPtpGMChange": jnxTimingEventPtpGMChange,
       "jnxTimingEventHybridStatus": jnxTimingEventHybridStatus,
       "jnxTimingEventLedColorChange": jnxTimingEventLedColorChange,
       "jnxTimingNotfObjects": jnxTimingNotfObjects,
       "jnxClksyncState": jnxClksyncState,
       "jnxClksyncIfIndex": jnxClksyncIfIndex,
       "jnxClksyncIntfName": jnxClksyncIntfName,
       "jnxAcbFpgaRevMajor": jnxAcbFpgaRevMajor,
       "jnxAcbFpgaRevMinor": jnxAcbFpgaRevMinor,
       "jnxBootCpldFpgaRevMajor": jnxBootCpldFpgaRevMajor,
       "jnxBootCpldFpgaRevMinor": jnxBootCpldFpgaRevMinor,
       "jnxClksyncQualityCode": jnxClksyncQualityCode,
       "jnxClksyncDpllState": jnxClksyncDpllState,
       "jnxPtpServoState": jnxPtpServoState,
       "jnxPtpClass": jnxPtpClass,
       "jnxPtpAccuracy": jnxPtpAccuracy,
       "jnxPtpGmId": jnxPtpGmId,
       "jnxPtpGmIpAddr": jnxPtpGmIpAddr,
       "jnxClkStreamHandle": jnxClkStreamHandle,
       "jnxRemoteIpAddr": jnxRemoteIpAddr,
       "jnxClksyncHybridState": jnxClksyncHybridState,
       "jnxPtpPhaseOffset": jnxPtpPhaseOffset,
       "jnxClksyncQualityCodeStr": jnxClksyncQualityCodeStr,
       "jnxClksyncDpllStateStr": jnxClksyncDpllStateStr,
       "jnxPtpServoStateStr": jnxPtpServoStateStr,
       "jnxClksyncHybridStateStr": jnxClksyncHybridStateStr,
       "jnxClksyncColorStr": jnxClksyncColorStr,
       "jnxPtpUtcOffset": jnxPtpUtcOffset,
       "jnxGpsRecvStatus": jnxGpsRecvStatus,
       "jnxPtpAdvClockClass": jnxPtpAdvClockClass,
       "jnxClksyncSynceLockedIfIndex": jnxClksyncSynceLockedIfIndex,
       "jnxClksyncSynceLockedIntfName": jnxClksyncSynceLockedIntfName,
       "jnxClksyncSynceQualityTable": jnxClksyncSynceQualityTable,
       "jnxClksyncSynceQualityEntry": jnxClksyncSynceQualityEntry,
       "jnxClksyncSynceQualityTableIndex": jnxClksyncSynceQualityTableIndex,
       "jnxClksyncSynceQualityIntfName": jnxClksyncSynceQualityIntfName,
       "jnxClksyncSynceQualityValue": jnxClksyncSynceQualityValue,
       "jnxPtpUtcValid": jnxPtpUtcValid,
       "jnxTimingFrequencyTraceability": jnxTimingFrequencyTraceability,
       "jnxTimingTimeTraceability": jnxTimingTimeTraceability,
       "jnxClksyncPtpOperationalMasterTable": jnxClksyncPtpOperationalMasterTable,
       "jnxClksyncPtpOperationalMasterEntry": jnxClksyncPtpOperationalMasterEntry,
       "jnxClksyncPtpOperationalMasterIndex": jnxClksyncPtpOperationalMasterIndex,
       "jnxClksyncPtpOperationalMasterAttrIndex": jnxClksyncPtpOperationalMasterAttrIndex,
       "jnxClksyncPtpOperationalMasters": jnxClksyncPtpOperationalMasters,
       "jnxClksyncPtpOperationalSlaveTable": jnxClksyncPtpOperationalSlaveTable,
       "jnxClksyncPtpOperationalSlaveEntry": jnxClksyncPtpOperationalSlaveEntry,
       "jnxClksyncPtpOperationalSlaveIndex": jnxClksyncPtpOperationalSlaveIndex,
       "jnxClksyncPtpOperationalSlaveAttrIndex": jnxClksyncPtpOperationalSlaveAttrIndex,
       "jnxClksyncPtpOperationalSlaves": jnxClksyncPtpOperationalSlaves,
       "jnxClksyncAdditionalInformationStr": jnxClksyncAdditionalInformationStr,
       "jnxTimingConformance": jnxTimingConformance,
       "jnxTimingCompliances": jnxTimingCompliances,
       "jnxTimingCompliance": jnxTimingCompliance,
       "jnxTimingGroups": jnxTimingGroups,
       "jnxTimingObjectsGroup": jnxTimingObjectsGroup,
       "jnxTimingNotfnFaultsGroup": jnxTimingNotfnFaultsGroup,
       "jnxTimingNotfnEventsGroup": jnxTimingNotfnEventsGroup}
)
