# SNMP MIB module (MEINBERG-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\meinberg\MEINBERG-OS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:30 2025
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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

meinbergOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7)
)
if mibBuilder.loadTexts:
    meinbergOS.setRevisions(
        ("2020-03-10 11:00",
         "2019-08-13 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtpTimestamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 27),
    )
    fixed_length = 27



class YesNo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class NtpReach(TextualConvention, Integer32):
    status = "current"
    displayHint = "o"


class Nanoseconds32(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class PtpClockAccuracy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
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
              49)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -2),
          ("accurateTo25ns", 32),
          ("accurateTo100ns", 33),
          ("accurateTo250ns", 34),
          ("accurateTo1us", 35),
          ("accurateTo2Point5us", 36),
          ("accurateTo10us", 37),
          ("accurateTo25us", 38),
          ("accurateTo100us", 39),
          ("accurateTo250us", 40),
          ("accurateTo1ms", 41),
          ("accurateTo2to5ms", 42),
          ("accurateTo10ms", 43),
          ("accurateTo25ms", 44),
          ("accurateTo100ms", 45),
          ("accurateTo250ms", 46),
          ("accurateTo1s", 47),
          ("accurateTo10s", 48),
          ("accurateToGT10s", 49))
    )



# MIB Managed Objects in the order of their OIDs

_MbgOsHelper_ObjectIdentity = ObjectIdentity
mbgOsHelper = _MbgOsHelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1)
)
_MbgOsPayload_Type = DisplayString
_MbgOsPayload_Object = MibScalar
mbgOsPayload = _MbgOsPayload_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1),
    _MbgOsPayload_Type()
)
mbgOsPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPayload.setStatus("current")
_MbgOsObjects_ObjectIdentity = ObjectIdentity
mbgOsObjects = _MbgOsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2)
)
_MbgOsNtp_ObjectIdentity = ObjectIdentity
mbgOsNtp = _MbgOsNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1)
)
_MbgOsNtpConfig_ObjectIdentity = ObjectIdentity
mbgOsNtpConfig = _MbgOsNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 1)
)
_MbgOsNtpState_ObjectIdentity = ObjectIdentity
mbgOsNtpState = _MbgOsNtpState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2)
)
_MbgOsNtpSysState_ObjectIdentity = ObjectIdentity
mbgOsNtpSysState = _MbgOsNtpSysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1)
)


class _MbgOsNtpSysStateMain_Type(Integer32):
    """Custom type mbgOsNtpSysStateMain based on Integer32"""
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
        *(("init", 0),
          ("sync", 1),
          ("notSync", 2),
          ("stopped", 3))
    )


_MbgOsNtpSysStateMain_Type.__name__ = "Integer32"
_MbgOsNtpSysStateMain_Object = MibScalar
mbgOsNtpSysStateMain = _MbgOsNtpSysStateMain_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 1),
    _MbgOsNtpSysStateMain_Type()
)
mbgOsNtpSysStateMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateMain.setStatus("current")
_MbgOsNtpSysStateRefId_Type = DisplayString
_MbgOsNtpSysStateRefId_Object = MibScalar
mbgOsNtpSysStateRefId = _MbgOsNtpSysStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 2),
    _MbgOsNtpSysStateRefId_Type()
)
mbgOsNtpSysStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateRefId.setStatus("current")


class _MbgOsNtpSysStateStratum_Type(Integer32):
    """Custom type mbgOsNtpSysStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MbgOsNtpSysStateStratum_Type.__name__ = "Integer32"
_MbgOsNtpSysStateStratum_Object = MibScalar
mbgOsNtpSysStateStratum = _MbgOsNtpSysStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 3),
    _MbgOsNtpSysStateStratum_Type()
)
mbgOsNtpSysStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateStratum.setStatus("current")


class _MbgOsNtpSysStateLeapIndicator_Type(Integer32):
    """Custom type mbgOsNtpSysStateLeapIndicator based on Integer32"""
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
        *(("none", 0),
          ("addSecond", 1),
          ("deleteSecond", 2),
          ("alarm", 3))
    )


_MbgOsNtpSysStateLeapIndicator_Type.__name__ = "Integer32"
_MbgOsNtpSysStateLeapIndicator_Object = MibScalar
mbgOsNtpSysStateLeapIndicator = _MbgOsNtpSysStateLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 4),
    _MbgOsNtpSysStateLeapIndicator_Type()
)
mbgOsNtpSysStateLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateLeapIndicator.setStatus("current")
_MbgOsNtpSysStateAssocId_Type = Unsigned32
_MbgOsNtpSysStateAssocId_Object = MibScalar
mbgOsNtpSysStateAssocId = _MbgOsNtpSysStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 5),
    _MbgOsNtpSysStateAssocId_Type()
)
mbgOsNtpSysStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateAssocId.setStatus("current")
_MbgOsNtpSysStateTime_Type = NtpTimestamp
_MbgOsNtpSysStateTime_Object = MibScalar
mbgOsNtpSysStateTime = _MbgOsNtpSysStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 6),
    _MbgOsNtpSysStateTime_Type()
)
mbgOsNtpSysStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateTime.setStatus("current")
_MbgOsNtpSysStateRootDelay_Type = Integer32
_MbgOsNtpSysStateRootDelay_Object = MibScalar
mbgOsNtpSysStateRootDelay = _MbgOsNtpSysStateRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 7),
    _MbgOsNtpSysStateRootDelay_Type()
)
mbgOsNtpSysStateRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateRootDelay.setUnits("us")
_MbgOsNtpSysStateRootDispersion_Type = Integer32
_MbgOsNtpSysStateRootDispersion_Object = MibScalar
mbgOsNtpSysStateRootDispersion = _MbgOsNtpSysStateRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 1, 8),
    _MbgOsNtpSysStateRootDispersion_Type()
)
mbgOsNtpSysStateRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpSysStateRootDispersion.setUnits("us")
_MbgOsNtpRefclkStates_ObjectIdentity = ObjectIdentity
mbgOsNtpRefclkStates = _MbgOsNtpRefclkStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2)
)
_MbgOsNtpRefclkStateTable_Object = MibTable
mbgOsNtpRefclkStateTable = _MbgOsNtpRefclkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateTable.setStatus("current")
_MbgOsNtpRefclkStateTableEntry_Object = MibTableRow
mbgOsNtpRefclkStateTableEntry = _MbgOsNtpRefclkStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1)
)
mbgOsNtpRefclkStateTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsNtpRefclkStateIndex"),
)
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateTableEntry.setStatus("current")
_MbgOsNtpRefclkStateIndex_Type = Unsigned32
_MbgOsNtpRefclkStateIndex_Object = MibTableColumn
mbgOsNtpRefclkStateIndex = _MbgOsNtpRefclkStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 1),
    _MbgOsNtpRefclkStateIndex_Type()
)
mbgOsNtpRefclkStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateIndex.setStatus("current")
_MbgOsNtpRefclkStateValid_Type = YesNo
_MbgOsNtpRefclkStateValid_Object = MibTableColumn
mbgOsNtpRefclkStateValid = _MbgOsNtpRefclkStateValid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 2),
    _MbgOsNtpRefclkStateValid_Type()
)
mbgOsNtpRefclkStateValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateValid.setStatus("current")
_MbgOsNtpRefclkStateRefId_Type = DisplayString
_MbgOsNtpRefclkStateRefId_Object = MibTableColumn
mbgOsNtpRefclkStateRefId = _MbgOsNtpRefclkStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 3),
    _MbgOsNtpRefclkStateRefId_Type()
)
mbgOsNtpRefclkStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateRefId.setStatus("current")


class _MbgOsNtpRefclkStateStratum_Type(Integer32):
    """Custom type mbgOsNtpRefclkStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgOsNtpRefclkStateStratum_Type.__name__ = "Integer32"
_MbgOsNtpRefclkStateStratum_Object = MibTableColumn
mbgOsNtpRefclkStateStratum = _MbgOsNtpRefclkStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 4),
    _MbgOsNtpRefclkStateStratum_Type()
)
mbgOsNtpRefclkStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateStratum.setStatus("current")
_MbgOsNtpRefclkStateReach_Type = NtpReach
_MbgOsNtpRefclkStateReach_Object = MibTableColumn
mbgOsNtpRefclkStateReach = _MbgOsNtpRefclkStateReach_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 5),
    _MbgOsNtpRefclkStateReach_Type()
)
mbgOsNtpRefclkStateReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateReach.setStatus("current")
_MbgOsNtpRefclkStateAssocId_Type = Integer32
_MbgOsNtpRefclkStateAssocId_Object = MibTableColumn
mbgOsNtpRefclkStateAssocId = _MbgOsNtpRefclkStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 6),
    _MbgOsNtpRefclkStateAssocId_Type()
)
mbgOsNtpRefclkStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateAssocId.setStatus("current")
_MbgOsNtpRefclkStateTime_Type = NtpTimestamp
_MbgOsNtpRefclkStateTime_Object = MibTableColumn
mbgOsNtpRefclkStateTime = _MbgOsNtpRefclkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 7),
    _MbgOsNtpRefclkStateTime_Type()
)
mbgOsNtpRefclkStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkStateTime.setStatus("current")
_MbgOsNtpRefclkOffset_Type = Integer32
_MbgOsNtpRefclkOffset_Object = MibTableColumn
mbgOsNtpRefclkOffset = _MbgOsNtpRefclkOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 8),
    _MbgOsNtpRefclkOffset_Type()
)
mbgOsNtpRefclkOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkOffset.setUnits("ns")
_MbgOsNtpRefclkDelay_Type = Integer32
_MbgOsNtpRefclkDelay_Object = MibTableColumn
mbgOsNtpRefclkDelay = _MbgOsNtpRefclkDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 9),
    _MbgOsNtpRefclkDelay_Type()
)
mbgOsNtpRefclkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkDelay.setUnits("ns")
_MbgOsNtpRefclkDispersion_Type = Integer32
_MbgOsNtpRefclkDispersion_Object = MibTableColumn
mbgOsNtpRefclkDispersion = _MbgOsNtpRefclkDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 10),
    _MbgOsNtpRefclkDispersion_Type()
)
mbgOsNtpRefclkDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkDispersion.setUnits("us")
_MbgOsNtpRefclkJitter_Type = Integer32
_MbgOsNtpRefclkJitter_Object = MibTableColumn
mbgOsNtpRefclkJitter = _MbgOsNtpRefclkJitter_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 2, 1, 1, 11),
    _MbgOsNtpRefclkJitter_Type()
)
mbgOsNtpRefclkJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkJitter.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpRefclkJitter.setUnits("us")
_MbgOsNtpPeerStates_ObjectIdentity = ObjectIdentity
mbgOsNtpPeerStates = _MbgOsNtpPeerStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3)
)
_MbgOsNtpPeerStateTable_Object = MibTable
mbgOsNtpPeerStateTable = _MbgOsNtpPeerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateTable.setStatus("current")
_MbgOsNtpPeerStateTableEntry_Object = MibTableRow
mbgOsNtpPeerStateTableEntry = _MbgOsNtpPeerStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1)
)
mbgOsNtpPeerStateTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsNtpPeerStateIndex"),
)
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateTableEntry.setStatus("current")
_MbgOsNtpPeerStateIndex_Type = Unsigned32
_MbgOsNtpPeerStateIndex_Object = MibTableColumn
mbgOsNtpPeerStateIndex = _MbgOsNtpPeerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 1),
    _MbgOsNtpPeerStateIndex_Type()
)
mbgOsNtpPeerStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateIndex.setStatus("current")
_MbgOsNtpPeerStateValid_Type = YesNo
_MbgOsNtpPeerStateValid_Object = MibTableColumn
mbgOsNtpPeerStateValid = _MbgOsNtpPeerStateValid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 2),
    _MbgOsNtpPeerStateValid_Type()
)
mbgOsNtpPeerStateValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateValid.setStatus("current")
_MbgOsNtpPeerStateRefId_Type = DisplayString
_MbgOsNtpPeerStateRefId_Object = MibTableColumn
mbgOsNtpPeerStateRefId = _MbgOsNtpPeerStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 3),
    _MbgOsNtpPeerStateRefId_Type()
)
mbgOsNtpPeerStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateRefId.setStatus("current")


class _MbgOsNtpPeerStateStratum_Type(Integer32):
    """Custom type mbgOsNtpPeerStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgOsNtpPeerStateStratum_Type.__name__ = "Integer32"
_MbgOsNtpPeerStateStratum_Object = MibTableColumn
mbgOsNtpPeerStateStratum = _MbgOsNtpPeerStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 4),
    _MbgOsNtpPeerStateStratum_Type()
)
mbgOsNtpPeerStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateStratum.setStatus("current")
_MbgOsNtpPeerStateReach_Type = NtpReach
_MbgOsNtpPeerStateReach_Object = MibTableColumn
mbgOsNtpPeerStateReach = _MbgOsNtpPeerStateReach_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 5),
    _MbgOsNtpPeerStateReach_Type()
)
mbgOsNtpPeerStateReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateReach.setStatus("current")
_MbgOsNtpPeerStateAssocId_Type = Integer32
_MbgOsNtpPeerStateAssocId_Object = MibTableColumn
mbgOsNtpPeerStateAssocId = _MbgOsNtpPeerStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 6),
    _MbgOsNtpPeerStateAssocId_Type()
)
mbgOsNtpPeerStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateAssocId.setStatus("current")
_MbgOsNtpPeerStateTime_Type = NtpTimestamp
_MbgOsNtpPeerStateTime_Object = MibTableColumn
mbgOsNtpPeerStateTime = _MbgOsNtpPeerStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 7),
    _MbgOsNtpPeerStateTime_Type()
)
mbgOsNtpPeerStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerStateTime.setStatus("current")
_MbgOsNtpPeerOffset_Type = Integer32
_MbgOsNtpPeerOffset_Object = MibTableColumn
mbgOsNtpPeerOffset = _MbgOsNtpPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 8),
    _MbgOsNtpPeerOffset_Type()
)
mbgOsNtpPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpPeerOffset.setUnits("ns")
_MbgOsNtpPeerDelay_Type = Integer32
_MbgOsNtpPeerDelay_Object = MibTableColumn
mbgOsNtpPeerDelay = _MbgOsNtpPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 9),
    _MbgOsNtpPeerDelay_Type()
)
mbgOsNtpPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpPeerDelay.setUnits("ns")
_MbgOsNtpPeerDispersion_Type = Integer32
_MbgOsNtpPeerDispersion_Object = MibTableColumn
mbgOsNtpPeerDispersion = _MbgOsNtpPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 10),
    _MbgOsNtpPeerDispersion_Type()
)
mbgOsNtpPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpPeerDispersion.setUnits("us")
_MbgOsNtpPeerJitter_Type = Integer32
_MbgOsNtpPeerJitter_Object = MibTableColumn
mbgOsNtpPeerJitter = _MbgOsNtpPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 1, 2, 3, 1, 1, 11),
    _MbgOsNtpPeerJitter_Type()
)
mbgOsNtpPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsNtpPeerJitter.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsNtpPeerJitter.setUnits("us")
_MbgOsSlot_ObjectIdentity = ObjectIdentity
mbgOsSlot = _MbgOsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2)
)
_MbgOsSlotTable_Object = MibTable
mbgOsSlotTable = _MbgOsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mbgOsSlotTable.setStatus("current")
_MbgOsSlotTableEntry_Object = MibTableRow
mbgOsSlotTableEntry = _MbgOsSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1, 1)
)
mbgOsSlotTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsSlotIndex"),
)
if mibBuilder.loadTexts:
    mbgOsSlotTableEntry.setStatus("current")
_MbgOsSlotIndex_Type = Unsigned32
_MbgOsSlotIndex_Object = MibTableColumn
mbgOsSlotIndex = _MbgOsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1, 1, 1),
    _MbgOsSlotIndex_Type()
)
mbgOsSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsSlotIndex.setStatus("current")


class _MbgOsSlotState_Type(Integer32):
    """Custom type mbgOsSlotState based on Integer32"""
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
        *(("unknown", 0),
          ("notAvailable", 1),
          ("initializing", 2),
          ("available", 3),
          ("disconnected", 4))
    )


_MbgOsSlotState_Type.__name__ = "Integer32"
_MbgOsSlotState_Object = MibTableColumn
mbgOsSlotState = _MbgOsSlotState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1, 1, 2),
    _MbgOsSlotState_Type()
)
mbgOsSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSlotState.setStatus("current")
_MbgOsSlotName_Type = DisplayString
_MbgOsSlotName_Object = MibTableColumn
mbgOsSlotName = _MbgOsSlotName_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1, 1, 3),
    _MbgOsSlotName_Type()
)
mbgOsSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSlotName.setStatus("current")
_MbgOsSlotCard_Type = DisplayString
_MbgOsSlotCard_Object = MibTableColumn
mbgOsSlotCard = _MbgOsSlotCard_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 2, 1, 1, 4),
    _MbgOsSlotCard_Type()
)
mbgOsSlotCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSlotCard.setStatus("current")
_MbgOsReceiver_ObjectIdentity = ObjectIdentity
mbgOsReceiver = _MbgOsReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3)
)
_MbgOsReceiverTable_Object = MibTable
mbgOsReceiverTable = _MbgOsReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mbgOsReceiverTable.setStatus("current")
_MbgOsReceiverTableEntry_Object = MibTableRow
mbgOsReceiverTableEntry = _MbgOsReceiverTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1)
)
mbgOsReceiverTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsReceiverIndex"),
)
if mibBuilder.loadTexts:
    mbgOsReceiverTableEntry.setStatus("current")
_MbgOsReceiverIndex_Type = Unsigned32
_MbgOsReceiverIndex_Object = MibTableColumn
mbgOsReceiverIndex = _MbgOsReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 1),
    _MbgOsReceiverIndex_Type()
)
mbgOsReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsReceiverIndex.setStatus("current")
_MbgOsReceiverSlot_Type = DisplayString
_MbgOsReceiverSlot_Object = MibTableColumn
mbgOsReceiverSlot = _MbgOsReceiverSlot_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 2),
    _MbgOsReceiverSlot_Type()
)
mbgOsReceiverSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverSlot.setStatus("current")


class _MbgOsReceiverState_Type(Integer32):
    """Custom type mbgOsReceiverState based on Integer32"""
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
        *(("noData", 0),
          ("waitingForData", 1),
          ("antennaShortCircuit", 2),
          ("antennaDisconnected", 3),
          ("coldBoot", 4),
          ("warmBoot", 5),
          ("synchronized", 6))
    )


_MbgOsReceiverState_Type.__name__ = "Integer32"
_MbgOsReceiverState_Object = MibTableColumn
mbgOsReceiverState = _MbgOsReceiverState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 3),
    _MbgOsReceiverState_Type()
)
mbgOsReceiverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverState.setStatus("current")
_MbgOsReceiverIsGnss_Type = YesNo
_MbgOsReceiverIsGnss_Object = MibTableColumn
mbgOsReceiverIsGnss = _MbgOsReceiverIsGnss_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 4),
    _MbgOsReceiverIsGnss_Type()
)
mbgOsReceiverIsGnss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverIsGnss.setStatus("current")


class _MbgOsReceiverPosition_Type(DisplayString):
    """Custom type mbgOsReceiverPosition based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgOsReceiverPosition_Type.__name__ = "DisplayString"
_MbgOsReceiverPosition_Object = MibTableColumn
mbgOsReceiverPosition = _MbgOsReceiverPosition_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 5),
    _MbgOsReceiverPosition_Type()
)
mbgOsReceiverPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverPosition.setStatus("current")


class _MbgOsReceiverGoodSv_Type(Integer32):
    """Custom type mbgOsReceiverGoodSv based on Integer32"""
    defaultValue = -1


_MbgOsReceiverGoodSv_Type.__name__ = "Integer32"
_MbgOsReceiverGoodSv_Object = MibTableColumn
mbgOsReceiverGoodSv = _MbgOsReceiverGoodSv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 6),
    _MbgOsReceiverGoodSv_Type()
)
mbgOsReceiverGoodSv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverGoodSv.setStatus("current")


class _MbgOsReceiverSv_Type(Integer32):
    """Custom type mbgOsReceiverSv based on Integer32"""
    defaultValue = -1


_MbgOsReceiverSv_Type.__name__ = "Integer32"
_MbgOsReceiverSv_Object = MibTableColumn
mbgOsReceiverSv = _MbgOsReceiverSv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 7),
    _MbgOsReceiverSv_Type()
)
mbgOsReceiverSv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverSv.setStatus("current")


class _MbgOsReceiverUtcTime_Type(DisplayString):
    """Custom type mbgOsReceiverUtcTime based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgOsReceiverUtcTime_Type.__name__ = "DisplayString"
_MbgOsReceiverUtcTime_Object = MibTableColumn
mbgOsReceiverUtcTime = _MbgOsReceiverUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 8),
    _MbgOsReceiverUtcTime_Type()
)
mbgOsReceiverUtcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverUtcTime.setStatus("current")


class _MbgOsReceiverLeapAnn_Type(Integer32):
    """Custom type mbgOsReceiverLeapAnn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noData", 0),
          ("no", 1),
          ("yes", 2))
    )


_MbgOsReceiverLeapAnn_Type.__name__ = "Integer32"
_MbgOsReceiverLeapAnn_Object = MibTableColumn
mbgOsReceiverLeapAnn = _MbgOsReceiverLeapAnn_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 3, 1, 1, 9),
    _MbgOsReceiverLeapAnn_Type()
)
mbgOsReceiverLeapAnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsReceiverLeapAnn.setStatus("current")
_MbgOsSysref_ObjectIdentity = ObjectIdentity
mbgOsSysref = _MbgOsSysref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4)
)
_MbgOsSysrefConfig_ObjectIdentity = ObjectIdentity
mbgOsSysrefConfig = _MbgOsSysrefConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 1)
)
_MbgOsSysrefState_ObjectIdentity = ObjectIdentity
mbgOsSysrefState = _MbgOsSysrefState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2)
)
_MbgOsSysrefGlbState_ObjectIdentity = ObjectIdentity
mbgOsSysrefGlbState = _MbgOsSysrefGlbState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1)
)


class _MbgOsSysrefGlbStateMasterRef_Type(DisplayString):
    """Custom type mbgOsSysrefGlbStateMasterRef based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgOsSysrefGlbStateMasterRef_Type.__name__ = "DisplayString"
_MbgOsSysrefGlbStateMasterRef_Object = MibScalar
mbgOsSysrefGlbStateMasterRef = _MbgOsSysrefGlbStateMasterRef_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1, 1),
    _MbgOsSysrefGlbStateMasterRef_Type()
)
mbgOsSysrefGlbStateMasterRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateMasterRef.setStatus("current")


class _MbgOsSysrefGlbStateMasterRefBits_Type(Bits):
    """Custom type mbgOsSysrefGlbStateMasterRefBits based on Bits"""
    namedValues = NamedValues(
        *(("dstChange", 0),
          ("dstEnabled", 1),
          ("leapSecondAnnounced", 2),
          ("secondIsLeapSecond", 3),
          ("leapSecondIsNegative", 4),
          ("invalidTime", 5),
          ("externalSync", 6),
          ("inHoldoverAfterSync", 7),
          ("antennaShortCircuit", 8),
          ("oscillatorWarmedUp", 9),
          ("antennaConnected", 10),
          ("clockSynchronized", 11),
          ("timeSyncVerified", 12),
          ("positionVerified", 13))
    )

_MbgOsSysrefGlbStateMasterRefBits_Type.__name__ = "Bits"
_MbgOsSysrefGlbStateMasterRefBits_Object = MibScalar
mbgOsSysrefGlbStateMasterRefBits = _MbgOsSysrefGlbStateMasterRefBits_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1, 2),
    _MbgOsSysrefGlbStateMasterRefBits_Type()
)
mbgOsSysrefGlbStateMasterRefBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateMasterRefBits.setStatus("current")
_MbgOsSysrefGlbStateMasterRefAccuracy_Type = Unsigned32
_MbgOsSysrefGlbStateMasterRefAccuracy_Object = MibScalar
mbgOsSysrefGlbStateMasterRefAccuracy = _MbgOsSysrefGlbStateMasterRefAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1, 3),
    _MbgOsSysrefGlbStateMasterRefAccuracy_Type()
)
mbgOsSysrefGlbStateMasterRefAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateMasterRefAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateMasterRefAccuracy.setUnits("ns")
_MbgOsSysrefGlbStateMasterRefVariance_Type = Unsigned32
_MbgOsSysrefGlbStateMasterRefVariance_Object = MibScalar
mbgOsSysrefGlbStateMasterRefVariance = _MbgOsSysrefGlbStateMasterRefVariance_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1, 4),
    _MbgOsSysrefGlbStateMasterRefVariance_Type()
)
mbgOsSysrefGlbStateMasterRefVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateMasterRefVariance.setStatus("current")


class _MbgOsSysrefGlbStateSysSync_Type(Integer32):
    """Custom type mbgOsSysrefGlbStateSysSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSynchronized", 0),
          ("synchronized", 1))
    )


_MbgOsSysrefGlbStateSysSync_Type.__name__ = "Integer32"
_MbgOsSysrefGlbStateSysSync_Object = MibScalar
mbgOsSysrefGlbStateSysSync = _MbgOsSysrefGlbStateSysSync_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 1, 5),
    _MbgOsSysrefGlbStateSysSync_Type()
)
mbgOsSysrefGlbStateSysSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefGlbStateSysSync.setStatus("current")
_MbgOsSysrefSrcState_ObjectIdentity = ObjectIdentity
mbgOsSysrefSrcState = _MbgOsSysrefSrcState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2)
)
_MbgOsSysrefSrcStateTable_Object = MibTable
mbgOsSysrefSrcStateTable = _MbgOsSysrefSrcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateTable.setStatus("current")
_MbgOsSysrefSrcStateTableEntry_Object = MibTableRow
mbgOsSysrefSrcStateTableEntry = _MbgOsSysrefSrcStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1)
)
mbgOsSysrefSrcStateTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsSysrefSrcStateIndex"),
)
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateTableEntry.setStatus("current")
_MbgOsSysrefSrcStateIndex_Type = Unsigned32
_MbgOsSysrefSrcStateIndex_Object = MibTableColumn
mbgOsSysrefSrcStateIndex = _MbgOsSysrefSrcStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1, 1),
    _MbgOsSysrefSrcStateIndex_Type()
)
mbgOsSysrefSrcStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateIndex.setStatus("current")
_MbgOsSysrefSrcStateId_Type = DisplayString
_MbgOsSysrefSrcStateId_Object = MibTableColumn
mbgOsSysrefSrcStateId = _MbgOsSysrefSrcStateId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1, 2),
    _MbgOsSysrefSrcStateId_Type()
)
mbgOsSysrefSrcStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateId.setStatus("current")
_MbgOsSysrefSrcStatePriority_Type = Unsigned32
_MbgOsSysrefSrcStatePriority_Object = MibTableColumn
mbgOsSysrefSrcStatePriority = _MbgOsSysrefSrcStatePriority_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1, 3),
    _MbgOsSysrefSrcStatePriority_Type()
)
mbgOsSysrefSrcStatePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStatePriority.setStatus("current")


class _MbgOsSysrefSrcStateBits_Type(Bits):
    """Custom type mbgOsSysrefSrcStateBits based on Bits"""
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("noConnection", 1),
          ("noSignal", 2),
          ("isMaster", 3),
          ("isLocked", 4),
          ("isAccurate", 5),
          ("notSettled", 6),
          ("notPhaseLocked", 7),
          ("numberOfSourcesExceeded", 8),
          ("isExternal", 9),
          ("lowJitter", 10),
          ("ituLimitViolated", 11),
          ("trsLimitViolated", 12))
    )

_MbgOsSysrefSrcStateBits_Type.__name__ = "Bits"
_MbgOsSysrefSrcStateBits_Object = MibTableColumn
mbgOsSysrefSrcStateBits = _MbgOsSysrefSrcStateBits_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1, 4),
    _MbgOsSysrefSrcStateBits_Type()
)
mbgOsSysrefSrcStateBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateBits.setStatus("current")
_MbgOsSysrefSrcStateOffset_Type = Integer32
_MbgOsSysrefSrcStateOffset_Object = MibTableColumn
mbgOsSysrefSrcStateOffset = _MbgOsSysrefSrcStateOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 4, 2, 2, 1, 1, 5),
    _MbgOsSysrefSrcStateOffset_Type()
)
mbgOsSysrefSrcStateOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsSysrefSrcStateOffset.setUnits("ns")
_MbgOsPtp_ObjectIdentity = ObjectIdentity
mbgOsPtp = _MbgOsPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5)
)
_MbgOsPtpConfig_ObjectIdentity = ObjectIdentity
mbgOsPtpConfig = _MbgOsPtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 1)
)
_MbgOsPtpState_ObjectIdentity = ObjectIdentity
mbgOsPtpState = _MbgOsPtpState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2)
)
_MbgOsPtpMiscTable_Object = MibTable
mbgOsPtpMiscTable = _MbgOsPtpMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mbgOsPtpMiscTable.setStatus("current")
_MbgOsPtpMiscTableEntry_Object = MibTableRow
mbgOsPtpMiscTableEntry = _MbgOsPtpMiscTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1)
)
mbgOsPtpMiscTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpMiscIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpMiscTableEntry.setStatus("current")
_MbgOsPtpMiscIndex_Type = Unsigned32
_MbgOsPtpMiscIndex_Object = MibTableColumn
mbgOsPtpMiscIndex = _MbgOsPtpMiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 1),
    _MbgOsPtpMiscIndex_Type()
)
mbgOsPtpMiscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpMiscIndex.setStatus("current")
_MbgOsPtpMiscRunning_Type = YesNo
_MbgOsPtpMiscRunning_Object = MibTableColumn
mbgOsPtpMiscRunning = _MbgOsPtpMiscRunning_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 2),
    _MbgOsPtpMiscRunning_Type()
)
mbgOsPtpMiscRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscRunning.setStatus("current")
_MbgOsPtpMiscNetworkIntfLabel_Type = DisplayString
_MbgOsPtpMiscNetworkIntfLabel_Object = MibTableColumn
mbgOsPtpMiscNetworkIntfLabel = _MbgOsPtpMiscNetworkIntfLabel_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 3),
    _MbgOsPtpMiscNetworkIntfLabel_Type()
)
mbgOsPtpMiscNetworkIntfLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscNetworkIntfLabel.setStatus("current")
_MbgOsPtpMiscUnicastSlaves_Type = Unsigned32
_MbgOsPtpMiscUnicastSlaves_Object = MibTableColumn
mbgOsPtpMiscUnicastSlaves = _MbgOsPtpMiscUnicastSlaves_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 4),
    _MbgOsPtpMiscUnicastSlaves_Type()
)
mbgOsPtpMiscUnicastSlaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscUnicastSlaves.setStatus("current")


class _MbgOsPtpMiscUtilization_Type(Unsigned32):
    """Custom type mbgOsPtpMiscUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MbgOsPtpMiscUtilization_Type.__name__ = "Unsigned32"
_MbgOsPtpMiscUtilization_Object = MibTableColumn
mbgOsPtpMiscUtilization = _MbgOsPtpMiscUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 5),
    _MbgOsPtpMiscUtilization_Type()
)
mbgOsPtpMiscUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscUtilization.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpMiscUtilization.setUnits("%")
_MbgOsPtpMiscTotalRxPkts_Type = Unsigned32
_MbgOsPtpMiscTotalRxPkts_Object = MibTableColumn
mbgOsPtpMiscTotalRxPkts = _MbgOsPtpMiscTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 6),
    _MbgOsPtpMiscTotalRxPkts_Type()
)
mbgOsPtpMiscTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscTotalRxPkts.setStatus("current")
_MbgOsPtpMiscRxPktsPerSec_Type = Unsigned32
_MbgOsPtpMiscRxPktsPerSec_Object = MibTableColumn
mbgOsPtpMiscRxPktsPerSec = _MbgOsPtpMiscRxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 7),
    _MbgOsPtpMiscRxPktsPerSec_Type()
)
mbgOsPtpMiscRxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscRxPktsPerSec.setStatus("current")
_MbgOsPtpMiscTotalTxPkts_Type = Unsigned32
_MbgOsPtpMiscTotalTxPkts_Object = MibTableColumn
mbgOsPtpMiscTotalTxPkts = _MbgOsPtpMiscTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 8),
    _MbgOsPtpMiscTotalTxPkts_Type()
)
mbgOsPtpMiscTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscTotalTxPkts.setStatus("current")
_MbgOsPtpMiscTxPktsPerSec_Type = Unsigned32
_MbgOsPtpMiscTxPktsPerSec_Object = MibTableColumn
mbgOsPtpMiscTxPktsPerSec = _MbgOsPtpMiscTxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 9),
    _MbgOsPtpMiscTxPktsPerSec_Type()
)
mbgOsPtpMiscTxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscTxPktsPerSec.setStatus("current")
_MbgOsPtpMiscStackAlias_Type = DisplayString
_MbgOsPtpMiscStackAlias_Object = MibTableColumn
mbgOsPtpMiscStackAlias = _MbgOsPtpMiscStackAlias_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 1, 1, 10),
    _MbgOsPtpMiscStackAlias_Type()
)
mbgOsPtpMiscStackAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpMiscStackAlias.setStatus("current")
_MbgOsPtpCurrentDsTable_Object = MibTable
mbgOsPtpCurrentDsTable = _MbgOsPtpCurrentDsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsTable.setStatus("current")
_MbgOsPtpCurrentDsTableEntry_Object = MibTableRow
mbgOsPtpCurrentDsTableEntry = _MbgOsPtpCurrentDsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1)
)
mbgOsPtpCurrentDsTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpCurrentDsIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsTableEntry.setStatus("current")
_MbgOsPtpCurrentDsIndex_Type = Unsigned32
_MbgOsPtpCurrentDsIndex_Object = MibTableColumn
mbgOsPtpCurrentDsIndex = _MbgOsPtpCurrentDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 1),
    _MbgOsPtpCurrentDsIndex_Type()
)
mbgOsPtpCurrentDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsIndex.setStatus("current")
_MbgOsPtpCurrentDsStepsRemoved_Type = Unsigned32
_MbgOsPtpCurrentDsStepsRemoved_Object = MibTableColumn
mbgOsPtpCurrentDsStepsRemoved = _MbgOsPtpCurrentDsStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 2),
    _MbgOsPtpCurrentDsStepsRemoved_Type()
)
mbgOsPtpCurrentDsStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsStepsRemoved.setStatus("current")
_MbgOsPtpCurrentDsOffsetFromMaster_Type = Nanoseconds32
_MbgOsPtpCurrentDsOffsetFromMaster_Object = MibTableColumn
mbgOsPtpCurrentDsOffsetFromMaster = _MbgOsPtpCurrentDsOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 3),
    _MbgOsPtpCurrentDsOffsetFromMaster_Type()
)
mbgOsPtpCurrentDsOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsOffsetFromMaster.setUnits("ns")
_MbgOsPtpCurrentDsOffsetFromMasterStr_Type = DisplayString
_MbgOsPtpCurrentDsOffsetFromMasterStr_Object = MibTableColumn
mbgOsPtpCurrentDsOffsetFromMasterStr = _MbgOsPtpCurrentDsOffsetFromMasterStr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 4),
    _MbgOsPtpCurrentDsOffsetFromMasterStr_Type()
)
mbgOsPtpCurrentDsOffsetFromMasterStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsOffsetFromMasterStr.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsOffsetFromMasterStr.setUnits("ns")
_MbgOsPtpCurrentDsMeanPathDelay_Type = Nanoseconds32
_MbgOsPtpCurrentDsMeanPathDelay_Object = MibTableColumn
mbgOsPtpCurrentDsMeanPathDelay = _MbgOsPtpCurrentDsMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 5),
    _MbgOsPtpCurrentDsMeanPathDelay_Type()
)
mbgOsPtpCurrentDsMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsMeanPathDelay.setUnits("ns")
_MbgOsPtpCurrentDsMeanPathDelayStr_Type = DisplayString
_MbgOsPtpCurrentDsMeanPathDelayStr_Object = MibTableColumn
mbgOsPtpCurrentDsMeanPathDelayStr = _MbgOsPtpCurrentDsMeanPathDelayStr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 2, 1, 6),
    _MbgOsPtpCurrentDsMeanPathDelayStr_Type()
)
mbgOsPtpCurrentDsMeanPathDelayStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsMeanPathDelayStr.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpCurrentDsMeanPathDelayStr.setUnits("ns")
_MbgOsPtpParentDsTable_Object = MibTable
mbgOsPtpParentDsTable = _MbgOsPtpParentDsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    mbgOsPtpParentDsTable.setStatus("current")
_MbgOsPtpParentDsTableEntry_Object = MibTableRow
mbgOsPtpParentDsTableEntry = _MbgOsPtpParentDsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1)
)
mbgOsPtpParentDsTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpCurrentDsIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpParentDsTableEntry.setStatus("current")
_MbgOsPtpParentDsIndex_Type = Unsigned32
_MbgOsPtpParentDsIndex_Object = MibTableColumn
mbgOsPtpParentDsIndex = _MbgOsPtpParentDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 1),
    _MbgOsPtpParentDsIndex_Type()
)
mbgOsPtpParentDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsIndex.setStatus("current")
_MbgOsPtpParentDsPortIdentity_Type = DisplayString
_MbgOsPtpParentDsPortIdentity_Object = MibTableColumn
mbgOsPtpParentDsPortIdentity = _MbgOsPtpParentDsPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 2),
    _MbgOsPtpParentDsPortIdentity_Type()
)
mbgOsPtpParentDsPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsPortIdentity.setStatus("current")
_MbgOsPtpParentDsGmClockId_Type = DisplayString
_MbgOsPtpParentDsGmClockId_Object = MibTableColumn
mbgOsPtpParentDsGmClockId = _MbgOsPtpParentDsGmClockId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 3),
    _MbgOsPtpParentDsGmClockId_Type()
)
mbgOsPtpParentDsGmClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmClockId.setStatus("current")


class _MbgOsPtpParentDsGmPrio1_Type(Unsigned32):
    """Custom type mbgOsPtpParentDsGmPrio1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpParentDsGmPrio1_Type.__name__ = "Unsigned32"
_MbgOsPtpParentDsGmPrio1_Object = MibTableColumn
mbgOsPtpParentDsGmPrio1 = _MbgOsPtpParentDsGmPrio1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 4),
    _MbgOsPtpParentDsGmPrio1_Type()
)
mbgOsPtpParentDsGmPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmPrio1.setStatus("current")


class _MbgOsPtpParentDsGmPrio2_Type(Unsigned32):
    """Custom type mbgOsPtpParentDsGmPrio2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpParentDsGmPrio2_Type.__name__ = "Unsigned32"
_MbgOsPtpParentDsGmPrio2_Object = MibTableColumn
mbgOsPtpParentDsGmPrio2 = _MbgOsPtpParentDsGmPrio2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 5),
    _MbgOsPtpParentDsGmPrio2_Type()
)
mbgOsPtpParentDsGmPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmPrio2.setStatus("current")


class _MbgOsPtpParentDsGmClockClass_Type(Unsigned32):
    """Custom type mbgOsPtpParentDsGmClockClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpParentDsGmClockClass_Type.__name__ = "Unsigned32"
_MbgOsPtpParentDsGmClockClass_Object = MibTableColumn
mbgOsPtpParentDsGmClockClass = _MbgOsPtpParentDsGmClockClass_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 6),
    _MbgOsPtpParentDsGmClockClass_Type()
)
mbgOsPtpParentDsGmClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmClockClass.setStatus("current")
_MbgOsPtpParentDsGmClockAccuracy_Type = PtpClockAccuracy
_MbgOsPtpParentDsGmClockAccuracy_Object = MibTableColumn
mbgOsPtpParentDsGmClockAccuracy = _MbgOsPtpParentDsGmClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 7),
    _MbgOsPtpParentDsGmClockAccuracy_Type()
)
mbgOsPtpParentDsGmClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmClockAccuracy.setStatus("current")
_MbgOsPtpParentDsGmClockVariance_Type = Unsigned32
_MbgOsPtpParentDsGmClockVariance_Object = MibTableColumn
mbgOsPtpParentDsGmClockVariance = _MbgOsPtpParentDsGmClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 3, 1, 8),
    _MbgOsPtpParentDsGmClockVariance_Type()
)
mbgOsPtpParentDsGmClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpParentDsGmClockVariance.setStatus("current")
_MbgOsPtpDefaultDsTable_Object = MibTable
mbgOsPtpDefaultDsTable = _MbgOsPtpDefaultDsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsTable.setStatus("current")
_MbgOsPtpDefaultDsTableEntry_Object = MibTableRow
mbgOsPtpDefaultDsTableEntry = _MbgOsPtpDefaultDsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1)
)
mbgOsPtpDefaultDsTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpDefaultDsIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsTableEntry.setStatus("current")
_MbgOsPtpDefaultDsIndex_Type = Unsigned32
_MbgOsPtpDefaultDsIndex_Object = MibTableColumn
mbgOsPtpDefaultDsIndex = _MbgOsPtpDefaultDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 1),
    _MbgOsPtpDefaultDsIndex_Type()
)
mbgOsPtpDefaultDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsIndex.setStatus("current")
_MbgOsPtpDefaultDsNumberOfPorts_Type = Unsigned32
_MbgOsPtpDefaultDsNumberOfPorts_Object = MibTableColumn
mbgOsPtpDefaultDsNumberOfPorts = _MbgOsPtpDefaultDsNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 2),
    _MbgOsPtpDefaultDsNumberOfPorts_Type()
)
mbgOsPtpDefaultDsNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsNumberOfPorts.setStatus("current")
_MbgOsPtpDefaultDsTwoStep_Type = YesNo
_MbgOsPtpDefaultDsTwoStep_Object = MibTableColumn
mbgOsPtpDefaultDsTwoStep = _MbgOsPtpDefaultDsTwoStep_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 3),
    _MbgOsPtpDefaultDsTwoStep_Type()
)
mbgOsPtpDefaultDsTwoStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsTwoStep.setStatus("current")
_MbgOsPtpDefaultDsSlaveOnly_Type = YesNo
_MbgOsPtpDefaultDsSlaveOnly_Object = MibTableColumn
mbgOsPtpDefaultDsSlaveOnly = _MbgOsPtpDefaultDsSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 4),
    _MbgOsPtpDefaultDsSlaveOnly_Type()
)
mbgOsPtpDefaultDsSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsSlaveOnly.setStatus("current")


class _MbgOsPtpDefaultDsPrio1_Type(Unsigned32):
    """Custom type mbgOsPtpDefaultDsPrio1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpDefaultDsPrio1_Type.__name__ = "Unsigned32"
_MbgOsPtpDefaultDsPrio1_Object = MibTableColumn
mbgOsPtpDefaultDsPrio1 = _MbgOsPtpDefaultDsPrio1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 5),
    _MbgOsPtpDefaultDsPrio1_Type()
)
mbgOsPtpDefaultDsPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsPrio1.setStatus("current")


class _MbgOsPtpDefaultDsPrio2_Type(Unsigned32):
    """Custom type mbgOsPtpDefaultDsPrio2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpDefaultDsPrio2_Type.__name__ = "Unsigned32"
_MbgOsPtpDefaultDsPrio2_Object = MibTableColumn
mbgOsPtpDefaultDsPrio2 = _MbgOsPtpDefaultDsPrio2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 6),
    _MbgOsPtpDefaultDsPrio2_Type()
)
mbgOsPtpDefaultDsPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsPrio2.setStatus("current")


class _MbgOsPtpDefaultDsClockClass_Type(Unsigned32):
    """Custom type mbgOsPtpDefaultDsClockClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpDefaultDsClockClass_Type.__name__ = "Unsigned32"
_MbgOsPtpDefaultDsClockClass_Object = MibTableColumn
mbgOsPtpDefaultDsClockClass = _MbgOsPtpDefaultDsClockClass_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 7),
    _MbgOsPtpDefaultDsClockClass_Type()
)
mbgOsPtpDefaultDsClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsClockClass.setStatus("current")
_MbgOsPtpDefaultDsClockAccuracy_Type = PtpClockAccuracy
_MbgOsPtpDefaultDsClockAccuracy_Object = MibTableColumn
mbgOsPtpDefaultDsClockAccuracy = _MbgOsPtpDefaultDsClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 8),
    _MbgOsPtpDefaultDsClockAccuracy_Type()
)
mbgOsPtpDefaultDsClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsClockAccuracy.setStatus("current")
_MbgOsPtpDefaultDsClockVariance_Type = Unsigned32
_MbgOsPtpDefaultDsClockVariance_Object = MibTableColumn
mbgOsPtpDefaultDsClockVariance = _MbgOsPtpDefaultDsClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 9),
    _MbgOsPtpDefaultDsClockVariance_Type()
)
mbgOsPtpDefaultDsClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsClockVariance.setStatus("current")
_MbgOsPtpDefaultDsClockIdentity_Type = DisplayString
_MbgOsPtpDefaultDsClockIdentity_Object = MibTableColumn
mbgOsPtpDefaultDsClockIdentity = _MbgOsPtpDefaultDsClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 10),
    _MbgOsPtpDefaultDsClockIdentity_Type()
)
mbgOsPtpDefaultDsClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsClockIdentity.setStatus("current")


class _MbgOsPtpDefaultDsDomainNumber_Type(Unsigned32):
    """Custom type mbgOsPtpDefaultDsDomainNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgOsPtpDefaultDsDomainNumber_Type.__name__ = "Unsigned32"
_MbgOsPtpDefaultDsDomainNumber_Object = MibTableColumn
mbgOsPtpDefaultDsDomainNumber = _MbgOsPtpDefaultDsDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 4, 1, 11),
    _MbgOsPtpDefaultDsDomainNumber_Type()
)
mbgOsPtpDefaultDsDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpDefaultDsDomainNumber.setStatus("current")
_MbgOsPtpTimePropDsTable_Object = MibTable
mbgOsPtpTimePropDsTable = _MbgOsPtpTimePropDsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5)
)
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsTable.setStatus("current")
_MbgOsPtpTimePropDsTableEntry_Object = MibTableRow
mbgOsPtpTimePropDsTableEntry = _MbgOsPtpTimePropDsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1)
)
mbgOsPtpTimePropDsTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpTimePropDsIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsTableEntry.setStatus("current")
_MbgOsPtpTimePropDsIndex_Type = Unsigned32
_MbgOsPtpTimePropDsIndex_Object = MibTableColumn
mbgOsPtpTimePropDsIndex = _MbgOsPtpTimePropDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 1),
    _MbgOsPtpTimePropDsIndex_Type()
)
mbgOsPtpTimePropDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsIndex.setStatus("current")
_MbgOsPtpTimePropDsUTCOffset_Type = Unsigned32
_MbgOsPtpTimePropDsUTCOffset_Object = MibTableColumn
mbgOsPtpTimePropDsUTCOffset = _MbgOsPtpTimePropDsUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 2),
    _MbgOsPtpTimePropDsUTCOffset_Type()
)
mbgOsPtpTimePropDsUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsUTCOffset.setStatus("current")
_MbgOsPtpTimePropDsLeap61_Type = YesNo
_MbgOsPtpTimePropDsLeap61_Object = MibTableColumn
mbgOsPtpTimePropDsLeap61 = _MbgOsPtpTimePropDsLeap61_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 3),
    _MbgOsPtpTimePropDsLeap61_Type()
)
mbgOsPtpTimePropDsLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsLeap61.setStatus("current")
_MbgOsPtpTimePropDsLeap59_Type = YesNo
_MbgOsPtpTimePropDsLeap59_Object = MibTableColumn
mbgOsPtpTimePropDsLeap59 = _MbgOsPtpTimePropDsLeap59_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 4),
    _MbgOsPtpTimePropDsLeap59_Type()
)
mbgOsPtpTimePropDsLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsLeap59.setStatus("current")
_MbgOsPtpTimePropDsUTCOffsetValid_Type = YesNo
_MbgOsPtpTimePropDsUTCOffsetValid_Object = MibTableColumn
mbgOsPtpTimePropDsUTCOffsetValid = _MbgOsPtpTimePropDsUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 5),
    _MbgOsPtpTimePropDsUTCOffsetValid_Type()
)
mbgOsPtpTimePropDsUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsUTCOffsetValid.setStatus("current")
_MbgOsPtpTimePropDsPTPTimescale_Type = YesNo
_MbgOsPtpTimePropDsPTPTimescale_Object = MibTableColumn
mbgOsPtpTimePropDsPTPTimescale = _MbgOsPtpTimePropDsPTPTimescale_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 6),
    _MbgOsPtpTimePropDsPTPTimescale_Type()
)
mbgOsPtpTimePropDsPTPTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsPTPTimescale.setStatus("current")
_MbgOsPtpTimePropDsTimeTraceable_Type = YesNo
_MbgOsPtpTimePropDsTimeTraceable_Object = MibTableColumn
mbgOsPtpTimePropDsTimeTraceable = _MbgOsPtpTimePropDsTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 7),
    _MbgOsPtpTimePropDsTimeTraceable_Type()
)
mbgOsPtpTimePropDsTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsTimeTraceable.setStatus("current")
_MbgOsPtpTimePropDsFrequencyTraceable_Type = YesNo
_MbgOsPtpTimePropDsFrequencyTraceable_Object = MibTableColumn
mbgOsPtpTimePropDsFrequencyTraceable = _MbgOsPtpTimePropDsFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 8),
    _MbgOsPtpTimePropDsFrequencyTraceable_Type()
)
mbgOsPtpTimePropDsFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsFrequencyTraceable.setStatus("current")


class _MbgOsPtpTimePropDsTimeSource_Type(Integer32):
    """Custom type mbgOsPtpTimePropDsTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160))
    )


_MbgOsPtpTimePropDsTimeSource_Type.__name__ = "Integer32"
_MbgOsPtpTimePropDsTimeSource_Object = MibTableColumn
mbgOsPtpTimePropDsTimeSource = _MbgOsPtpTimePropDsTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 5, 1, 9),
    _MbgOsPtpTimePropDsTimeSource_Type()
)
mbgOsPtpTimePropDsTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpTimePropDsTimeSource.setStatus("current")
_MbgOsPtpPortDsTable_Object = MibTable
mbgOsPtpPortDsTable = _MbgOsPtpPortDsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6)
)
if mibBuilder.loadTexts:
    mbgOsPtpPortDsTable.setStatus("current")
_MbgOsPtpPortDsTableEntry_Object = MibTableRow
mbgOsPtpPortDsTableEntry = _MbgOsPtpPortDsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1)
)
mbgOsPtpPortDsTableEntry.setIndexNames(
    (0, "MEINBERG-OS-MIB", "mbgOsPtpPortDsIndex"),
)
if mibBuilder.loadTexts:
    mbgOsPtpPortDsTableEntry.setStatus("current")
_MbgOsPtpPortDsIndex_Type = Unsigned32
_MbgOsPtpPortDsIndex_Object = MibTableColumn
mbgOsPtpPortDsIndex = _MbgOsPtpPortDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 1),
    _MbgOsPtpPortDsIndex_Type()
)
mbgOsPtpPortDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsIndex.setStatus("current")
_MbgOsPtpPortDsPortIdentity_Type = DisplayString
_MbgOsPtpPortDsPortIdentity_Object = MibTableColumn
mbgOsPtpPortDsPortIdentity = _MbgOsPtpPortDsPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 2),
    _MbgOsPtpPortDsPortIdentity_Type()
)
mbgOsPtpPortDsPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsPortIdentity.setStatus("current")


class _MbgOsPtpPortDsPortState_Type(Integer32):
    """Custom type mbgOsPtpPortDsPortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("uninitialized", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )


_MbgOsPtpPortDsPortState_Type.__name__ = "Integer32"
_MbgOsPtpPortDsPortState_Object = MibTableColumn
mbgOsPtpPortDsPortState = _MbgOsPtpPortDsPortState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 3),
    _MbgOsPtpPortDsPortState_Type()
)
mbgOsPtpPortDsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsPortState.setStatus("current")
_MbgOsPtpPortDsMinDlyReqIntv_Type = Integer32
_MbgOsPtpPortDsMinDlyReqIntv_Object = MibTableColumn
mbgOsPtpPortDsMinDlyReqIntv = _MbgOsPtpPortDsMinDlyReqIntv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 4),
    _MbgOsPtpPortDsMinDlyReqIntv_Type()
)
mbgOsPtpPortDsMinDlyReqIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsMinDlyReqIntv.setStatus("current")
_MbgOsPtpPortDsPeerMeanPathDly_Type = Integer32
_MbgOsPtpPortDsPeerMeanPathDly_Object = MibTableColumn
mbgOsPtpPortDsPeerMeanPathDly = _MbgOsPtpPortDsPeerMeanPathDly_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 5),
    _MbgOsPtpPortDsPeerMeanPathDly_Type()
)
mbgOsPtpPortDsPeerMeanPathDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsPeerMeanPathDly.setStatus("current")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsPeerMeanPathDly.setUnits("ns")
_MbgOsPtpPortDsAnnIntv_Type = Integer32
_MbgOsPtpPortDsAnnIntv_Object = MibTableColumn
mbgOsPtpPortDsAnnIntv = _MbgOsPtpPortDsAnnIntv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 6),
    _MbgOsPtpPortDsAnnIntv_Type()
)
mbgOsPtpPortDsAnnIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsAnnIntv.setStatus("current")
_MbgOsPtpPortDsAnnReceiptTimeout_Type = Unsigned32
_MbgOsPtpPortDsAnnReceiptTimeout_Object = MibTableColumn
mbgOsPtpPortDsAnnReceiptTimeout = _MbgOsPtpPortDsAnnReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 7),
    _MbgOsPtpPortDsAnnReceiptTimeout_Type()
)
mbgOsPtpPortDsAnnReceiptTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsAnnReceiptTimeout.setStatus("current")
_MbgOsPtpPortDsSyncIntv_Type = Integer32
_MbgOsPtpPortDsSyncIntv_Object = MibTableColumn
mbgOsPtpPortDsSyncIntv = _MbgOsPtpPortDsSyncIntv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 8),
    _MbgOsPtpPortDsSyncIntv_Type()
)
mbgOsPtpPortDsSyncIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsSyncIntv.setStatus("current")


class _MbgOsPtpPortDsDlyMech_Type(Integer32):
    """Custom type mbgOsPtpPortDsDlyMech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 0),
          ("peer2peer", 1))
    )


_MbgOsPtpPortDsDlyMech_Type.__name__ = "Integer32"
_MbgOsPtpPortDsDlyMech_Object = MibTableColumn
mbgOsPtpPortDsDlyMech = _MbgOsPtpPortDsDlyMech_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 9),
    _MbgOsPtpPortDsDlyMech_Type()
)
mbgOsPtpPortDsDlyMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsDlyMech.setStatus("current")
_MbgOsPtpPortDsMinPeerDlyReqIntv_Type = Integer32
_MbgOsPtpPortDsMinPeerDlyReqIntv_Object = MibTableColumn
mbgOsPtpPortDsMinPeerDlyReqIntv = _MbgOsPtpPortDsMinPeerDlyReqIntv_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 10),
    _MbgOsPtpPortDsMinPeerDlyReqIntv_Type()
)
mbgOsPtpPortDsMinPeerDlyReqIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsMinPeerDlyReqIntv.setStatus("current")
_MbgOsPtpPortDsVersionNumber_Type = Unsigned32
_MbgOsPtpPortDsVersionNumber_Object = MibTableColumn
mbgOsPtpPortDsVersionNumber = _MbgOsPtpPortDsVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 5, 2, 6, 1, 11),
    _MbgOsPtpPortDsVersionNumber_Type()
)
mbgOsPtpPortDsVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgOsPtpPortDsVersionNumber.setStatus("current")
_MbgOsNotifications_ObjectIdentity = ObjectIdentity
mbgOsNotifications = _MbgOsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 3)
)
_MbgOsTraps_ObjectIdentity = ObjectIdentity
mbgOsTraps = _MbgOsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 3, 0)
)
_MbgOsConformance_ObjectIdentity = ObjectIdentity
mbgOsConformance = _MbgOsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024)
)
_MbgOsCompliances_ObjectIdentity = ObjectIdentity
mbgOsCompliances = _MbgOsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024, 1)
)
_MbgOsGroups_ObjectIdentity = ObjectIdentity
mbgOsGroups = _MbgOsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024, 2)
)

# Managed Objects groups

mbgOsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024, 2, 1)
)
mbgOsObjectsGroup.setObjects(
      *(("MEINBERG-OS-MIB", "mbgOsPayload"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateMain"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateRefId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateStratum"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateLeapIndicator"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateAssocId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateTime"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateRootDelay"),
        ("MEINBERG-OS-MIB", "mbgOsNtpSysStateRootDispersion"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateValid"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateRefId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateStratum"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateReach"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateAssocId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkStateTime"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkOffset"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkDelay"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkDispersion"),
        ("MEINBERG-OS-MIB", "mbgOsNtpRefclkJitter"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateValid"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateRefId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateStratum"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateReach"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateAssocId"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerStateTime"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerOffset"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerDelay"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerDispersion"),
        ("MEINBERG-OS-MIB", "mbgOsNtpPeerJitter"),
        ("MEINBERG-OS-MIB", "mbgOsSlotState"),
        ("MEINBERG-OS-MIB", "mbgOsSlotName"),
        ("MEINBERG-OS-MIB", "mbgOsSlotCard"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverSlot"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverState"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverIsGnss"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverPosition"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverGoodSv"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverSv"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverUtcTime"),
        ("MEINBERG-OS-MIB", "mbgOsReceiverLeapAnn"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefGlbStateMasterRef"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefGlbStateMasterRefBits"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefGlbStateMasterRefAccuracy"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefGlbStateMasterRefVariance"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefGlbStateSysSync"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefSrcStateId"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefSrcStatePriority"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefSrcStateBits"),
        ("MEINBERG-OS-MIB", "mbgOsSysrefSrcStateOffset"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscRunning"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscNetworkIntfLabel"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscUnicastSlaves"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscUtilization"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscTotalRxPkts"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscRxPktsPerSec"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscTotalTxPkts"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscTxPktsPerSec"),
        ("MEINBERG-OS-MIB", "mbgOsPtpMiscStackAlias"),
        ("MEINBERG-OS-MIB", "mbgOsPtpCurrentDsStepsRemoved"),
        ("MEINBERG-OS-MIB", "mbgOsPtpCurrentDsOffsetFromMaster"),
        ("MEINBERG-OS-MIB", "mbgOsPtpCurrentDsOffsetFromMasterStr"),
        ("MEINBERG-OS-MIB", "mbgOsPtpCurrentDsMeanPathDelay"),
        ("MEINBERG-OS-MIB", "mbgOsPtpCurrentDsMeanPathDelayStr"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsPortIdentity"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmClockId"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmPrio1"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmPrio2"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmClockClass"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmClockAccuracy"),
        ("MEINBERG-OS-MIB", "mbgOsPtpParentDsGmClockVariance"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsNumberOfPorts"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsTwoStep"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsSlaveOnly"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsPrio1"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsPrio2"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsClockClass"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsClockAccuracy"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsClockVariance"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsClockIdentity"),
        ("MEINBERG-OS-MIB", "mbgOsPtpDefaultDsDomainNumber"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsUTCOffset"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsLeap61"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsLeap59"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsUTCOffsetValid"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsPTPTimescale"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsTimeTraceable"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsFrequencyTraceable"),
        ("MEINBERG-OS-MIB", "mbgOsPtpTimePropDsTimeSource"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsPortIdentity"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsPortState"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsMinDlyReqIntv"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsPeerMeanPathDly"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsAnnIntv"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsAnnReceiptTimeout"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsSyncIntv"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsDlyMech"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsMinPeerDlyReqIntv"),
        ("MEINBERG-OS-MIB", "mbgOsPtpPortDsVersionNumber"))
)
if mibBuilder.loadTexts:
    mbgOsObjectsGroup.setStatus("current")


# Notification objects

mbgOsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 7, 3, 0, 1)
)
mbgOsTrap.setObjects(
    ("MEINBERG-OS-MIB", "mbgOsPayload")
)
if mibBuilder.loadTexts:
    mbgOsTrap.setStatus(
        "current"
    )


# Notifications groups

mbgOsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024, 2, 2)
)
mbgOsNotificationGroup.setObjects(
    ("MEINBERG-OS-MIB", "mbgOsTrap")
)
if mibBuilder.loadTexts:
    mbgOsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgOsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1024, 1, 1)
)
mbgOsCompliance.setObjects(
      *(("MEINBERG-OS-MIB", "mbgOsObjectsGroup"),
        ("MEINBERG-OS-MIB", "mbgOsNotificationGroup"))
)
if mibBuilder.loadTexts:
    mbgOsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEINBERG-OS-MIB",
    **{"NtpTimestamp": NtpTimestamp,
       "YesNo": YesNo,
       "NtpReach": NtpReach,
       "Nanoseconds32": Nanoseconds32,
       "PtpClockAccuracy": PtpClockAccuracy,
       "meinbergOS": meinbergOS,
       "mbgOsHelper": mbgOsHelper,
       "mbgOsPayload": mbgOsPayload,
       "mbgOsObjects": mbgOsObjects,
       "mbgOsNtp": mbgOsNtp,
       "mbgOsNtpConfig": mbgOsNtpConfig,
       "mbgOsNtpState": mbgOsNtpState,
       "mbgOsNtpSysState": mbgOsNtpSysState,
       "mbgOsNtpSysStateMain": mbgOsNtpSysStateMain,
       "mbgOsNtpSysStateRefId": mbgOsNtpSysStateRefId,
       "mbgOsNtpSysStateStratum": mbgOsNtpSysStateStratum,
       "mbgOsNtpSysStateLeapIndicator": mbgOsNtpSysStateLeapIndicator,
       "mbgOsNtpSysStateAssocId": mbgOsNtpSysStateAssocId,
       "mbgOsNtpSysStateTime": mbgOsNtpSysStateTime,
       "mbgOsNtpSysStateRootDelay": mbgOsNtpSysStateRootDelay,
       "mbgOsNtpSysStateRootDispersion": mbgOsNtpSysStateRootDispersion,
       "mbgOsNtpRefclkStates": mbgOsNtpRefclkStates,
       "mbgOsNtpRefclkStateTable": mbgOsNtpRefclkStateTable,
       "mbgOsNtpRefclkStateTableEntry": mbgOsNtpRefclkStateTableEntry,
       "mbgOsNtpRefclkStateIndex": mbgOsNtpRefclkStateIndex,
       "mbgOsNtpRefclkStateValid": mbgOsNtpRefclkStateValid,
       "mbgOsNtpRefclkStateRefId": mbgOsNtpRefclkStateRefId,
       "mbgOsNtpRefclkStateStratum": mbgOsNtpRefclkStateStratum,
       "mbgOsNtpRefclkStateReach": mbgOsNtpRefclkStateReach,
       "mbgOsNtpRefclkStateAssocId": mbgOsNtpRefclkStateAssocId,
       "mbgOsNtpRefclkStateTime": mbgOsNtpRefclkStateTime,
       "mbgOsNtpRefclkOffset": mbgOsNtpRefclkOffset,
       "mbgOsNtpRefclkDelay": mbgOsNtpRefclkDelay,
       "mbgOsNtpRefclkDispersion": mbgOsNtpRefclkDispersion,
       "mbgOsNtpRefclkJitter": mbgOsNtpRefclkJitter,
       "mbgOsNtpPeerStates": mbgOsNtpPeerStates,
       "mbgOsNtpPeerStateTable": mbgOsNtpPeerStateTable,
       "mbgOsNtpPeerStateTableEntry": mbgOsNtpPeerStateTableEntry,
       "mbgOsNtpPeerStateIndex": mbgOsNtpPeerStateIndex,
       "mbgOsNtpPeerStateValid": mbgOsNtpPeerStateValid,
       "mbgOsNtpPeerStateRefId": mbgOsNtpPeerStateRefId,
       "mbgOsNtpPeerStateStratum": mbgOsNtpPeerStateStratum,
       "mbgOsNtpPeerStateReach": mbgOsNtpPeerStateReach,
       "mbgOsNtpPeerStateAssocId": mbgOsNtpPeerStateAssocId,
       "mbgOsNtpPeerStateTime": mbgOsNtpPeerStateTime,
       "mbgOsNtpPeerOffset": mbgOsNtpPeerOffset,
       "mbgOsNtpPeerDelay": mbgOsNtpPeerDelay,
       "mbgOsNtpPeerDispersion": mbgOsNtpPeerDispersion,
       "mbgOsNtpPeerJitter": mbgOsNtpPeerJitter,
       "mbgOsSlot": mbgOsSlot,
       "mbgOsSlotTable": mbgOsSlotTable,
       "mbgOsSlotTableEntry": mbgOsSlotTableEntry,
       "mbgOsSlotIndex": mbgOsSlotIndex,
       "mbgOsSlotState": mbgOsSlotState,
       "mbgOsSlotName": mbgOsSlotName,
       "mbgOsSlotCard": mbgOsSlotCard,
       "mbgOsReceiver": mbgOsReceiver,
       "mbgOsReceiverTable": mbgOsReceiverTable,
       "mbgOsReceiverTableEntry": mbgOsReceiverTableEntry,
       "mbgOsReceiverIndex": mbgOsReceiverIndex,
       "mbgOsReceiverSlot": mbgOsReceiverSlot,
       "mbgOsReceiverState": mbgOsReceiverState,
       "mbgOsReceiverIsGnss": mbgOsReceiverIsGnss,
       "mbgOsReceiverPosition": mbgOsReceiverPosition,
       "mbgOsReceiverGoodSv": mbgOsReceiverGoodSv,
       "mbgOsReceiverSv": mbgOsReceiverSv,
       "mbgOsReceiverUtcTime": mbgOsReceiverUtcTime,
       "mbgOsReceiverLeapAnn": mbgOsReceiverLeapAnn,
       "mbgOsSysref": mbgOsSysref,
       "mbgOsSysrefConfig": mbgOsSysrefConfig,
       "mbgOsSysrefState": mbgOsSysrefState,
       "mbgOsSysrefGlbState": mbgOsSysrefGlbState,
       "mbgOsSysrefGlbStateMasterRef": mbgOsSysrefGlbStateMasterRef,
       "mbgOsSysrefGlbStateMasterRefBits": mbgOsSysrefGlbStateMasterRefBits,
       "mbgOsSysrefGlbStateMasterRefAccuracy": mbgOsSysrefGlbStateMasterRefAccuracy,
       "mbgOsSysrefGlbStateMasterRefVariance": mbgOsSysrefGlbStateMasterRefVariance,
       "mbgOsSysrefGlbStateSysSync": mbgOsSysrefGlbStateSysSync,
       "mbgOsSysrefSrcState": mbgOsSysrefSrcState,
       "mbgOsSysrefSrcStateTable": mbgOsSysrefSrcStateTable,
       "mbgOsSysrefSrcStateTableEntry": mbgOsSysrefSrcStateTableEntry,
       "mbgOsSysrefSrcStateIndex": mbgOsSysrefSrcStateIndex,
       "mbgOsSysrefSrcStateId": mbgOsSysrefSrcStateId,
       "mbgOsSysrefSrcStatePriority": mbgOsSysrefSrcStatePriority,
       "mbgOsSysrefSrcStateBits": mbgOsSysrefSrcStateBits,
       "mbgOsSysrefSrcStateOffset": mbgOsSysrefSrcStateOffset,
       "mbgOsPtp": mbgOsPtp,
       "mbgOsPtpConfig": mbgOsPtpConfig,
       "mbgOsPtpState": mbgOsPtpState,
       "mbgOsPtpMiscTable": mbgOsPtpMiscTable,
       "mbgOsPtpMiscTableEntry": mbgOsPtpMiscTableEntry,
       "mbgOsPtpMiscIndex": mbgOsPtpMiscIndex,
       "mbgOsPtpMiscRunning": mbgOsPtpMiscRunning,
       "mbgOsPtpMiscNetworkIntfLabel": mbgOsPtpMiscNetworkIntfLabel,
       "mbgOsPtpMiscUnicastSlaves": mbgOsPtpMiscUnicastSlaves,
       "mbgOsPtpMiscUtilization": mbgOsPtpMiscUtilization,
       "mbgOsPtpMiscTotalRxPkts": mbgOsPtpMiscTotalRxPkts,
       "mbgOsPtpMiscRxPktsPerSec": mbgOsPtpMiscRxPktsPerSec,
       "mbgOsPtpMiscTotalTxPkts": mbgOsPtpMiscTotalTxPkts,
       "mbgOsPtpMiscTxPktsPerSec": mbgOsPtpMiscTxPktsPerSec,
       "mbgOsPtpMiscStackAlias": mbgOsPtpMiscStackAlias,
       "mbgOsPtpCurrentDsTable": mbgOsPtpCurrentDsTable,
       "mbgOsPtpCurrentDsTableEntry": mbgOsPtpCurrentDsTableEntry,
       "mbgOsPtpCurrentDsIndex": mbgOsPtpCurrentDsIndex,
       "mbgOsPtpCurrentDsStepsRemoved": mbgOsPtpCurrentDsStepsRemoved,
       "mbgOsPtpCurrentDsOffsetFromMaster": mbgOsPtpCurrentDsOffsetFromMaster,
       "mbgOsPtpCurrentDsOffsetFromMasterStr": mbgOsPtpCurrentDsOffsetFromMasterStr,
       "mbgOsPtpCurrentDsMeanPathDelay": mbgOsPtpCurrentDsMeanPathDelay,
       "mbgOsPtpCurrentDsMeanPathDelayStr": mbgOsPtpCurrentDsMeanPathDelayStr,
       "mbgOsPtpParentDsTable": mbgOsPtpParentDsTable,
       "mbgOsPtpParentDsTableEntry": mbgOsPtpParentDsTableEntry,
       "mbgOsPtpParentDsIndex": mbgOsPtpParentDsIndex,
       "mbgOsPtpParentDsPortIdentity": mbgOsPtpParentDsPortIdentity,
       "mbgOsPtpParentDsGmClockId": mbgOsPtpParentDsGmClockId,
       "mbgOsPtpParentDsGmPrio1": mbgOsPtpParentDsGmPrio1,
       "mbgOsPtpParentDsGmPrio2": mbgOsPtpParentDsGmPrio2,
       "mbgOsPtpParentDsGmClockClass": mbgOsPtpParentDsGmClockClass,
       "mbgOsPtpParentDsGmClockAccuracy": mbgOsPtpParentDsGmClockAccuracy,
       "mbgOsPtpParentDsGmClockVariance": mbgOsPtpParentDsGmClockVariance,
       "mbgOsPtpDefaultDsTable": mbgOsPtpDefaultDsTable,
       "mbgOsPtpDefaultDsTableEntry": mbgOsPtpDefaultDsTableEntry,
       "mbgOsPtpDefaultDsIndex": mbgOsPtpDefaultDsIndex,
       "mbgOsPtpDefaultDsNumberOfPorts": mbgOsPtpDefaultDsNumberOfPorts,
       "mbgOsPtpDefaultDsTwoStep": mbgOsPtpDefaultDsTwoStep,
       "mbgOsPtpDefaultDsSlaveOnly": mbgOsPtpDefaultDsSlaveOnly,
       "mbgOsPtpDefaultDsPrio1": mbgOsPtpDefaultDsPrio1,
       "mbgOsPtpDefaultDsPrio2": mbgOsPtpDefaultDsPrio2,
       "mbgOsPtpDefaultDsClockClass": mbgOsPtpDefaultDsClockClass,
       "mbgOsPtpDefaultDsClockAccuracy": mbgOsPtpDefaultDsClockAccuracy,
       "mbgOsPtpDefaultDsClockVariance": mbgOsPtpDefaultDsClockVariance,
       "mbgOsPtpDefaultDsClockIdentity": mbgOsPtpDefaultDsClockIdentity,
       "mbgOsPtpDefaultDsDomainNumber": mbgOsPtpDefaultDsDomainNumber,
       "mbgOsPtpTimePropDsTable": mbgOsPtpTimePropDsTable,
       "mbgOsPtpTimePropDsTableEntry": mbgOsPtpTimePropDsTableEntry,
       "mbgOsPtpTimePropDsIndex": mbgOsPtpTimePropDsIndex,
       "mbgOsPtpTimePropDsUTCOffset": mbgOsPtpTimePropDsUTCOffset,
       "mbgOsPtpTimePropDsLeap61": mbgOsPtpTimePropDsLeap61,
       "mbgOsPtpTimePropDsLeap59": mbgOsPtpTimePropDsLeap59,
       "mbgOsPtpTimePropDsUTCOffsetValid": mbgOsPtpTimePropDsUTCOffsetValid,
       "mbgOsPtpTimePropDsPTPTimescale": mbgOsPtpTimePropDsPTPTimescale,
       "mbgOsPtpTimePropDsTimeTraceable": mbgOsPtpTimePropDsTimeTraceable,
       "mbgOsPtpTimePropDsFrequencyTraceable": mbgOsPtpTimePropDsFrequencyTraceable,
       "mbgOsPtpTimePropDsTimeSource": mbgOsPtpTimePropDsTimeSource,
       "mbgOsPtpPortDsTable": mbgOsPtpPortDsTable,
       "mbgOsPtpPortDsTableEntry": mbgOsPtpPortDsTableEntry,
       "mbgOsPtpPortDsIndex": mbgOsPtpPortDsIndex,
       "mbgOsPtpPortDsPortIdentity": mbgOsPtpPortDsPortIdentity,
       "mbgOsPtpPortDsPortState": mbgOsPtpPortDsPortState,
       "mbgOsPtpPortDsMinDlyReqIntv": mbgOsPtpPortDsMinDlyReqIntv,
       "mbgOsPtpPortDsPeerMeanPathDly": mbgOsPtpPortDsPeerMeanPathDly,
       "mbgOsPtpPortDsAnnIntv": mbgOsPtpPortDsAnnIntv,
       "mbgOsPtpPortDsAnnReceiptTimeout": mbgOsPtpPortDsAnnReceiptTimeout,
       "mbgOsPtpPortDsSyncIntv": mbgOsPtpPortDsSyncIntv,
       "mbgOsPtpPortDsDlyMech": mbgOsPtpPortDsDlyMech,
       "mbgOsPtpPortDsMinPeerDlyReqIntv": mbgOsPtpPortDsMinPeerDlyReqIntv,
       "mbgOsPtpPortDsVersionNumber": mbgOsPtpPortDsVersionNumber,
       "mbgOsNotifications": mbgOsNotifications,
       "mbgOsTraps": mbgOsTraps,
       "mbgOsTrap": mbgOsTrap,
       "mbgOsConformance": mbgOsConformance,
       "mbgOsCompliances": mbgOsCompliances,
       "mbgOsCompliance": mbgOsCompliance,
       "mbgOsGroups": mbgOsGroups,
       "mbgOsObjectsGroup": mbgOsObjectsGroup,
       "mbgOsNotificationGroup": mbgOsNotificationGroup}
)
