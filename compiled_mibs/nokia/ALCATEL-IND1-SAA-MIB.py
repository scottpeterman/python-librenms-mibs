# SNMP MIB module (ALCATEL-IND1-SAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-SAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:05 2025
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

(softentIND1Saa,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Saa")

(Dot1agCfmMaintAssocName,
 Dot1agCfmMaintDomainName) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintDomainName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1SaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIB.setRevisions(
        ("2009-07-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SaaNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1SaaNotifications = _AlcatelIND1SaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaNotifications.setStatus("current")
_AlcatelIND1SaaMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SaaMIBObjects = _AlcatelIND1SaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIBObjects.setStatus("current")
_AlaSaaCtrlConfig_ObjectIdentity = ObjectIdentity
alaSaaCtrlConfig = _AlaSaaCtrlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1)
)
_AlaSaaCtrlTable_Object = MibTable
alaSaaCtrlTable = _AlaSaaCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaSaaCtrlTable.setStatus("current")
_AlaSaaCtrlEntry_Object = MibTableRow
alaSaaCtrlEntry = _AlaSaaCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1)
)
alaSaaCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaCtrlTestIndex"),
)
if mibBuilder.loadTexts:
    alaSaaCtrlEntry.setStatus("current")


class _AlaSaaCtrlOwnerIndex_Type(SnmpAdminString):
    """Custom type alaSaaCtrlOwnerIndex based on SnmpAdminString"""
    defaultValue = OctetString("USER")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaSaaCtrlOwnerIndex_Type.__name__ = "SnmpAdminString"
_AlaSaaCtrlOwnerIndex_Object = MibTableColumn
alaSaaCtrlOwnerIndex = _AlaSaaCtrlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 1),
    _AlaSaaCtrlOwnerIndex_Type()
)
alaSaaCtrlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaCtrlOwnerIndex.setStatus("current")


class _AlaSaaCtrlTestIndex_Type(SnmpAdminString):
    """Custom type alaSaaCtrlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaSaaCtrlTestIndex_Type.__name__ = "SnmpAdminString"
_AlaSaaCtrlTestIndex_Object = MibTableColumn
alaSaaCtrlTestIndex = _AlaSaaCtrlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 2),
    _AlaSaaCtrlTestIndex_Type()
)
alaSaaCtrlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaCtrlTestIndex.setStatus("current")
_AlaSaaCtrlRowStatus_Type = RowStatus
_AlaSaaCtrlRowStatus_Object = MibTableColumn
alaSaaCtrlRowStatus = _AlaSaaCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 3),
    _AlaSaaCtrlRowStatus_Type()
)
alaSaaCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlRowStatus.setStatus("current")


class _AlaSaaCtrlDescr_Type(DisplayString):
    """Custom type alaSaaCtrlDescr based on DisplayString"""
    defaultValue = OctetString("DEFAULT")


_AlaSaaCtrlDescr_Type.__name__ = "DisplayString"
_AlaSaaCtrlDescr_Object = MibTableColumn
alaSaaCtrlDescr = _AlaSaaCtrlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 4),
    _AlaSaaCtrlDescr_Type()
)
alaSaaCtrlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlDescr.setStatus("current")


class _AlaSaaCtrlAdminStatus_Type(Integer32):
    """Custom type alaSaaCtrlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_AlaSaaCtrlAdminStatus_Type.__name__ = "Integer32"
_AlaSaaCtrlAdminStatus_Object = MibTableColumn
alaSaaCtrlAdminStatus = _AlaSaaCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 5),
    _AlaSaaCtrlAdminStatus_Type()
)
alaSaaCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlAdminStatus.setStatus("current")


class _AlaSaaCtrlTestMode_Type(Integer32):
    """Custom type alaSaaCtrlTestMode based on Integer32"""
    defaultValue = 0

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
          ("ipSaa", 1),
          ("ethSaa", 2))
    )


_AlaSaaCtrlTestMode_Type.__name__ = "Integer32"
_AlaSaaCtrlTestMode_Object = MibTableColumn
alaSaaCtrlTestMode = _AlaSaaCtrlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 6),
    _AlaSaaCtrlTestMode_Type()
)
alaSaaCtrlTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlTestMode.setStatus("current")
_AlaSaaCtrlRuns_Type = Counter32
_AlaSaaCtrlRuns_Object = MibTableColumn
alaSaaCtrlRuns = _AlaSaaCtrlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 7),
    _AlaSaaCtrlRuns_Type()
)
alaSaaCtrlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlRuns.setStatus("current")
_AlaSaaCtrlFailures_Type = Counter32
_AlaSaaCtrlFailures_Object = MibTableColumn
alaSaaCtrlFailures = _AlaSaaCtrlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 8),
    _AlaSaaCtrlFailures_Type()
)
alaSaaCtrlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlFailures.setStatus("current")


class _AlaSaaCtrlLastRunResult_Type(Integer32):
    """Custom type alaSaaCtrlLastRunResult based on Integer32"""
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
        *(("undetermined", 0),
          ("success", 1),
          ("failed", 2),
          ("aborted", 3))
    )


_AlaSaaCtrlLastRunResult_Type.__name__ = "Integer32"
_AlaSaaCtrlLastRunResult_Object = MibTableColumn
alaSaaCtrlLastRunResult = _AlaSaaCtrlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 9),
    _AlaSaaCtrlLastRunResult_Type()
)
alaSaaCtrlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlLastRunResult.setStatus("current")
_AlaSaaCtrlLastRunTime_Type = DateAndTime
_AlaSaaCtrlLastRunTime_Object = MibTableColumn
alaSaaCtrlLastRunTime = _AlaSaaCtrlLastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 10),
    _AlaSaaCtrlLastRunTime_Type()
)
alaSaaCtrlLastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlLastRunTime.setStatus("current")


class _AlaSaaCtrlInterval_Type(Integer32):
    """Custom type alaSaaCtrlInterval based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1500),
    )


_AlaSaaCtrlInterval_Type.__name__ = "Integer32"
_AlaSaaCtrlInterval_Object = MibTableColumn
alaSaaCtrlInterval = _AlaSaaCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 11),
    _AlaSaaCtrlInterval_Type()
)
alaSaaCtrlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaSaaCtrlInterval.setUnits("minutes")


class _AlaSaaCtrlStartAt_Type(DateAndTime):
    """Custom type alaSaaCtrlStartAt based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AlaSaaCtrlStartAt_Type.__name__ = "DateAndTime"
_AlaSaaCtrlStartAt_Object = MibTableColumn
alaSaaCtrlStartAt = _AlaSaaCtrlStartAt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 12),
    _AlaSaaCtrlStartAt_Type()
)
alaSaaCtrlStartAt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlStartAt.setStatus("current")


class _AlaSaaCtrlStopAt_Type(DateAndTime):
    """Custom type alaSaaCtrlStopAt based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AlaSaaCtrlStopAt_Type.__name__ = "DateAndTime"
_AlaSaaCtrlStopAt_Object = MibTableColumn
alaSaaCtrlStopAt = _AlaSaaCtrlStopAt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 13),
    _AlaSaaCtrlStopAt_Type()
)
alaSaaCtrlStopAt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaCtrlStopAt.setStatus("current")


class _AlaSaaCtrlMaxHistoryRows_Type(Integer32):
    """Custom type alaSaaCtrlMaxHistoryRows based on Integer32"""
    defaultValue = 5


_AlaSaaCtrlMaxHistoryRows_Type.__name__ = "Integer32"
_AlaSaaCtrlMaxHistoryRows_Object = MibTableColumn
alaSaaCtrlMaxHistoryRows = _AlaSaaCtrlMaxHistoryRows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 1, 1, 1, 14),
    _AlaSaaCtrlMaxHistoryRows_Type()
)
alaSaaCtrlMaxHistoryRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaCtrlMaxHistoryRows.setStatus("current")
_AlaSaaIpCtrlConfig_ObjectIdentity = ObjectIdentity
alaSaaIpCtrlConfig = _AlaSaaIpCtrlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2)
)
_AlaSaaIpCtrlTable_Object = MibTable
alaSaaIpCtrlTable = _AlaSaaIpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaSaaIpCtrlTable.setStatus("current")
_AlaSaaIpCtrlEntry_Object = MibTableRow
alaSaaIpCtrlEntry = _AlaSaaIpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1)
)
alaSaaIpCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTestIndex"),
)
if mibBuilder.loadTexts:
    alaSaaIpCtrlEntry.setStatus("current")


class _AlaSaaIpCtrlOwnerIndex_Type(SnmpAdminString):
    """Custom type alaSaaIpCtrlOwnerIndex based on SnmpAdminString"""
    defaultValue = OctetString("USER")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaSaaIpCtrlOwnerIndex_Type.__name__ = "SnmpAdminString"
_AlaSaaIpCtrlOwnerIndex_Object = MibTableColumn
alaSaaIpCtrlOwnerIndex = _AlaSaaIpCtrlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 1),
    _AlaSaaIpCtrlOwnerIndex_Type()
)
alaSaaIpCtrlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaIpCtrlOwnerIndex.setStatus("current")


class _AlaSaaIpCtrlTestIndex_Type(SnmpAdminString):
    """Custom type alaSaaIpCtrlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaSaaIpCtrlTestIndex_Type.__name__ = "SnmpAdminString"
_AlaSaaIpCtrlTestIndex_Object = MibTableColumn
alaSaaIpCtrlTestIndex = _AlaSaaIpCtrlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 2),
    _AlaSaaIpCtrlTestIndex_Type()
)
alaSaaIpCtrlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTestIndex.setStatus("current")
_AlaSaaIpCtrlRowStatus_Type = RowStatus
_AlaSaaIpCtrlRowStatus_Object = MibTableColumn
alaSaaIpCtrlRowStatus = _AlaSaaIpCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 3),
    _AlaSaaIpCtrlRowStatus_Type()
)
alaSaaIpCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlRowStatus.setStatus("current")


class _AlaSaaIpCtrlTestMode_Type(Integer32):
    """Custom type alaSaaIpCtrlTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("icmpEcho", 1)
    )


_AlaSaaIpCtrlTestMode_Type.__name__ = "Integer32"
_AlaSaaIpCtrlTestMode_Object = MibTableColumn
alaSaaIpCtrlTestMode = _AlaSaaIpCtrlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 4),
    _AlaSaaIpCtrlTestMode_Type()
)
alaSaaIpCtrlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTestMode.setStatus("current")


class _AlaSaaIpCtrlTgtAddrType_Type(InetAddressType):
    """Custom type alaSaaIpCtrlTgtAddrType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaSaaIpCtrlTgtAddrType_Type.__name__ = "InetAddressType"
_AlaSaaIpCtrlTgtAddrType_Object = MibTableColumn
alaSaaIpCtrlTgtAddrType = _AlaSaaIpCtrlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 5),
    _AlaSaaIpCtrlTgtAddrType_Type()
)
alaSaaIpCtrlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTgtAddrType.setStatus("current")
_AlaSaaIpCtrlTgtAddress_Type = InetAddress
_AlaSaaIpCtrlTgtAddress_Object = MibTableColumn
alaSaaIpCtrlTgtAddress = _AlaSaaIpCtrlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 6),
    _AlaSaaIpCtrlTgtAddress_Type()
)
alaSaaIpCtrlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTgtAddress.setStatus("current")


class _AlaSaaIpCtrlSrcAddrType_Type(InetAddressType):
    """Custom type alaSaaIpCtrlSrcAddrType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaSaaIpCtrlSrcAddrType_Type.__name__ = "InetAddressType"
_AlaSaaIpCtrlSrcAddrType_Object = MibTableColumn
alaSaaIpCtrlSrcAddrType = _AlaSaaIpCtrlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 7),
    _AlaSaaIpCtrlSrcAddrType_Type()
)
alaSaaIpCtrlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlSrcAddrType.setStatus("current")
_AlaSaaIpCtrlSrcAddress_Type = InetAddress
_AlaSaaIpCtrlSrcAddress_Object = MibTableColumn
alaSaaIpCtrlSrcAddress = _AlaSaaIpCtrlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 8),
    _AlaSaaIpCtrlSrcAddress_Type()
)
alaSaaIpCtrlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlSrcAddress.setStatus("current")


class _AlaSaaIpCtrlPayloadSize_Type(Integer32):
    """Custom type alaSaaIpCtrlPayloadSize based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 1472),
    )


_AlaSaaIpCtrlPayloadSize_Type.__name__ = "Integer32"
_AlaSaaIpCtrlPayloadSize_Object = MibTableColumn
alaSaaIpCtrlPayloadSize = _AlaSaaIpCtrlPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 9),
    _AlaSaaIpCtrlPayloadSize_Type()
)
alaSaaIpCtrlPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlPayloadSize.setStatus("current")


class _AlaSaaIpCtrlNumPkts_Type(Integer32):
    """Custom type alaSaaIpCtrlNumPkts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaSaaIpCtrlNumPkts_Type.__name__ = "Integer32"
_AlaSaaIpCtrlNumPkts_Object = MibTableColumn
alaSaaIpCtrlNumPkts = _AlaSaaIpCtrlNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 10),
    _AlaSaaIpCtrlNumPkts_Type()
)
alaSaaIpCtrlNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlNumPkts.setStatus("current")


class _AlaSaaIpCtrlInterPktDelay_Type(Integer32):
    """Custom type alaSaaIpCtrlInterPktDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AlaSaaIpCtrlInterPktDelay_Type.__name__ = "Integer32"
_AlaSaaIpCtrlInterPktDelay_Object = MibTableColumn
alaSaaIpCtrlInterPktDelay = _AlaSaaIpCtrlInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 11),
    _AlaSaaIpCtrlInterPktDelay_Type()
)
alaSaaIpCtrlInterPktDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlInterPktDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaSaaIpCtrlInterPktDelay.setUnits("milli-seconds")


class _AlaSaaIpCtrlTypeOfService_Type(Integer32):
    """Custom type alaSaaIpCtrlTypeOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaSaaIpCtrlTypeOfService_Type.__name__ = "Integer32"
_AlaSaaIpCtrlTypeOfService_Object = MibTableColumn
alaSaaIpCtrlTypeOfService = _AlaSaaIpCtrlTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 12),
    _AlaSaaIpCtrlTypeOfService_Type()
)
alaSaaIpCtrlTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTypeOfService.setStatus("current")


class _AlaSaaIpCtrlVRFId_Type(Integer32):
    """Custom type alaSaaIpCtrlVRFId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AlaSaaIpCtrlVRFId_Type.__name__ = "Integer32"
_AlaSaaIpCtrlVRFId_Object = MibTableColumn
alaSaaIpCtrlVRFId = _AlaSaaIpCtrlVRFId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 13),
    _AlaSaaIpCtrlVRFId_Type()
)
alaSaaIpCtrlVRFId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaIpCtrlVRFId.setStatus("current")
_AlaSaaIpCtrlTotalPktsSent_Type = Counter32
_AlaSaaIpCtrlTotalPktsSent_Object = MibTableColumn
alaSaaIpCtrlTotalPktsSent = _AlaSaaIpCtrlTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 14),
    _AlaSaaIpCtrlTotalPktsSent_Type()
)
alaSaaIpCtrlTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTotalPktsSent.setStatus("current")
_AlaSaaIpCtrlTotalPktsRcvd_Type = Counter32
_AlaSaaIpCtrlTotalPktsRcvd_Object = MibTableColumn
alaSaaIpCtrlTotalPktsRcvd = _AlaSaaIpCtrlTotalPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 15),
    _AlaSaaIpCtrlTotalPktsRcvd_Type()
)
alaSaaIpCtrlTotalPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTotalPktsRcvd.setStatus("current")
_AlaSaaIpCtrlMinRTT_Type = Integer32
_AlaSaaIpCtrlMinRTT_Object = MibTableColumn
alaSaaIpCtrlMinRTT = _AlaSaaIpCtrlMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 16),
    _AlaSaaIpCtrlMinRTT_Type()
)
alaSaaIpCtrlMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlMinRTT.setStatus("current")
_AlaSaaIpCtrlAvgRTT_Type = Integer32
_AlaSaaIpCtrlAvgRTT_Object = MibTableColumn
alaSaaIpCtrlAvgRTT = _AlaSaaIpCtrlAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 17),
    _AlaSaaIpCtrlAvgRTT_Type()
)
alaSaaIpCtrlAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlAvgRTT.setStatus("current")
_AlaSaaIpCtrlMaxRTT_Type = Integer32
_AlaSaaIpCtrlMaxRTT_Object = MibTableColumn
alaSaaIpCtrlMaxRTT = _AlaSaaIpCtrlMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 18),
    _AlaSaaIpCtrlMaxRTT_Type()
)
alaSaaIpCtrlMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlMaxRTT.setStatus("current")
_AlaSaaIpCtrlMinJitter_Type = Integer32
_AlaSaaIpCtrlMinJitter_Object = MibTableColumn
alaSaaIpCtrlMinJitter = _AlaSaaIpCtrlMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 19),
    _AlaSaaIpCtrlMinJitter_Type()
)
alaSaaIpCtrlMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlMinJitter.setStatus("current")
_AlaSaaIpCtrlAvgJitter_Type = Integer32
_AlaSaaIpCtrlAvgJitter_Object = MibTableColumn
alaSaaIpCtrlAvgJitter = _AlaSaaIpCtrlAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 20),
    _AlaSaaIpCtrlAvgJitter_Type()
)
alaSaaIpCtrlAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlAvgJitter.setStatus("current")
_AlaSaaIpCtrlMaxJitter_Type = Integer32
_AlaSaaIpCtrlMaxJitter_Object = MibTableColumn
alaSaaIpCtrlMaxJitter = _AlaSaaIpCtrlMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 21),
    _AlaSaaIpCtrlMaxJitter_Type()
)
alaSaaIpCtrlMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlMaxJitter.setStatus("current")
_AlaSaaIpCtrlTSMinRTT_Type = DateAndTime
_AlaSaaIpCtrlTSMinRTT_Object = MibTableColumn
alaSaaIpCtrlTSMinRTT = _AlaSaaIpCtrlTSMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 22),
    _AlaSaaIpCtrlTSMinRTT_Type()
)
alaSaaIpCtrlTSMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTSMinRTT.setStatus("current")
_AlaSaaIpCtrlTSMaxRTT_Type = DateAndTime
_AlaSaaIpCtrlTSMaxRTT_Object = MibTableColumn
alaSaaIpCtrlTSMaxRTT = _AlaSaaIpCtrlTSMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 23),
    _AlaSaaIpCtrlTSMaxRTT_Type()
)
alaSaaIpCtrlTSMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTSMaxRTT.setStatus("current")
_AlaSaaIpCtrlTSMinJitter_Type = DateAndTime
_AlaSaaIpCtrlTSMinJitter_Object = MibTableColumn
alaSaaIpCtrlTSMinJitter = _AlaSaaIpCtrlTSMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 24),
    _AlaSaaIpCtrlTSMinJitter_Type()
)
alaSaaIpCtrlTSMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTSMinJitter.setStatus("current")
_AlaSaaIpCtrlTSMaxJitter_Type = DateAndTime
_AlaSaaIpCtrlTSMaxJitter_Object = MibTableColumn
alaSaaIpCtrlTSMaxJitter = _AlaSaaIpCtrlTSMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 2, 1, 1, 25),
    _AlaSaaIpCtrlTSMaxJitter_Type()
)
alaSaaIpCtrlTSMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpCtrlTSMaxJitter.setStatus("current")
_AlaSaaIpResults_ObjectIdentity = ObjectIdentity
alaSaaIpResults = _AlaSaaIpResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3)
)
_AlaSaaIpResultsTable_Object = MibTable
alaSaaIpResultsTable = _AlaSaaIpResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaSaaIpResultsTable.setStatus("current")
_AlaSaaIpResultsEntry_Object = MibTableRow
alaSaaIpResultsEntry = _AlaSaaIpResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1)
)
alaSaaIpResultsEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTestIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    alaSaaIpResultsEntry.setStatus("current")


class _AlaSaaIpResultsTestRunIndex_Type(Unsigned32):
    """Custom type alaSaaIpResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlaSaaIpResultsTestRunIndex_Type.__name__ = "Unsigned32"
_AlaSaaIpResultsTestRunIndex_Object = MibTableColumn
alaSaaIpResultsTestRunIndex = _AlaSaaIpResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 1),
    _AlaSaaIpResultsTestRunIndex_Type()
)
alaSaaIpResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaIpResultsTestRunIndex.setStatus("current")
_AlaSaaIpResultsPktsSent_Type = Counter32
_AlaSaaIpResultsPktsSent_Object = MibTableColumn
alaSaaIpResultsPktsSent = _AlaSaaIpResultsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 2),
    _AlaSaaIpResultsPktsSent_Type()
)
alaSaaIpResultsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsPktsSent.setStatus("current")
_AlaSaaIpResultsPktsRcvd_Type = Counter32
_AlaSaaIpResultsPktsRcvd_Object = MibTableColumn
alaSaaIpResultsPktsRcvd = _AlaSaaIpResultsPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 3),
    _AlaSaaIpResultsPktsRcvd_Type()
)
alaSaaIpResultsPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsPktsRcvd.setStatus("current")
_AlaSaaIpResultsInterPktDelay_Type = Integer32
_AlaSaaIpResultsInterPktDelay_Object = MibTableColumn
alaSaaIpResultsInterPktDelay = _AlaSaaIpResultsInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 4),
    _AlaSaaIpResultsInterPktDelay_Type()
)
alaSaaIpResultsInterPktDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsInterPktDelay.setStatus("current")


class _AlaSaaIpResultsRunResult_Type(Integer32):
    """Custom type alaSaaIpResultsRunResult based on Integer32"""
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
        *(("undetermined", 0),
          ("success", 1),
          ("failed", 2),
          ("aborted", 3))
    )


_AlaSaaIpResultsRunResult_Type.__name__ = "Integer32"
_AlaSaaIpResultsRunResult_Object = MibTableColumn
alaSaaIpResultsRunResult = _AlaSaaIpResultsRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 5),
    _AlaSaaIpResultsRunResult_Type()
)
alaSaaIpResultsRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsRunResult.setStatus("current")
_AlaSaaIpResultsRunResultReason_Type = OctetString
_AlaSaaIpResultsRunResultReason_Object = MibTableColumn
alaSaaIpResultsRunResultReason = _AlaSaaIpResultsRunResultReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 6),
    _AlaSaaIpResultsRunResultReason_Type()
)
alaSaaIpResultsRunResultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsRunResultReason.setStatus("current")
_AlaSaaIpResultsRunTime_Type = DateAndTime
_AlaSaaIpResultsRunTime_Object = MibTableColumn
alaSaaIpResultsRunTime = _AlaSaaIpResultsRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 7),
    _AlaSaaIpResultsRunTime_Type()
)
alaSaaIpResultsRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsRunTime.setStatus("current")
_AlaSaaIpResultsMinRTT_Type = Integer32
_AlaSaaIpResultsMinRTT_Object = MibTableColumn
alaSaaIpResultsMinRTT = _AlaSaaIpResultsMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 8),
    _AlaSaaIpResultsMinRTT_Type()
)
alaSaaIpResultsMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsMinRTT.setStatus("current")
_AlaSaaIpResultsAvgRTT_Type = Integer32
_AlaSaaIpResultsAvgRTT_Object = MibTableColumn
alaSaaIpResultsAvgRTT = _AlaSaaIpResultsAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 9),
    _AlaSaaIpResultsAvgRTT_Type()
)
alaSaaIpResultsAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsAvgRTT.setStatus("current")
_AlaSaaIpResultsMaxRTT_Type = Integer32
_AlaSaaIpResultsMaxRTT_Object = MibTableColumn
alaSaaIpResultsMaxRTT = _AlaSaaIpResultsMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 10),
    _AlaSaaIpResultsMaxRTT_Type()
)
alaSaaIpResultsMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsMaxRTT.setStatus("current")
_AlaSaaIpResultsMinJitter_Type = Integer32
_AlaSaaIpResultsMinJitter_Object = MibTableColumn
alaSaaIpResultsMinJitter = _AlaSaaIpResultsMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 11),
    _AlaSaaIpResultsMinJitter_Type()
)
alaSaaIpResultsMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsMinJitter.setStatus("current")
_AlaSaaIpResultsAvgJitter_Type = Integer32
_AlaSaaIpResultsAvgJitter_Object = MibTableColumn
alaSaaIpResultsAvgJitter = _AlaSaaIpResultsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 12),
    _AlaSaaIpResultsAvgJitter_Type()
)
alaSaaIpResultsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsAvgJitter.setStatus("current")
_AlaSaaIpResultsMaxJitter_Type = Integer32
_AlaSaaIpResultsMaxJitter_Object = MibTableColumn
alaSaaIpResultsMaxJitter = _AlaSaaIpResultsMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 3, 1, 1, 13),
    _AlaSaaIpResultsMaxJitter_Type()
)
alaSaaIpResultsMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpResultsMaxJitter.setStatus("current")
_AlaSaaIpHistory_ObjectIdentity = ObjectIdentity
alaSaaIpHistory = _AlaSaaIpHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4)
)
_AlaSaaIpHistoryTable_Object = MibTable
alaSaaIpHistoryTable = _AlaSaaIpHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaSaaIpHistoryTable.setStatus("current")
_AlaSaaIpHistoryEntry_Object = MibTableRow
alaSaaIpHistoryEntry = _AlaSaaIpHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4, 1, 1)
)
alaSaaIpHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTestIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsTestRunIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaIpHistoryIndex"),
)
if mibBuilder.loadTexts:
    alaSaaIpHistoryEntry.setStatus("current")
_AlaSaaIpHistoryIndex_Type = Unsigned32
_AlaSaaIpHistoryIndex_Object = MibTableColumn
alaSaaIpHistoryIndex = _AlaSaaIpHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4, 1, 1, 1),
    _AlaSaaIpHistoryIndex_Type()
)
alaSaaIpHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaIpHistoryIndex.setStatus("current")
_AlaSaaIpHistoryPktRTT_Type = Integer32
_AlaSaaIpHistoryPktRTT_Object = MibTableColumn
alaSaaIpHistoryPktRTT = _AlaSaaIpHistoryPktRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4, 1, 1, 2),
    _AlaSaaIpHistoryPktRTT_Type()
)
alaSaaIpHistoryPktRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpHistoryPktRTT.setStatus("current")
_AlaSaaIpHistoryPktJitter_Type = Integer32
_AlaSaaIpHistoryPktJitter_Object = MibTableColumn
alaSaaIpHistoryPktJitter = _AlaSaaIpHistoryPktJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 4, 1, 1, 3),
    _AlaSaaIpHistoryPktJitter_Type()
)
alaSaaIpHistoryPktJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaIpHistoryPktJitter.setStatus("current")
_AlaSaaEthoamCtrlConfig_ObjectIdentity = ObjectIdentity
alaSaaEthoamCtrlConfig = _AlaSaaEthoamCtrlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5)
)
_AlaSaaEthoamCtrlTable_Object = MibTable
alaSaaEthoamCtrlTable = _AlaSaaEthoamCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTable.setStatus("current")
_AlaSaaEthoamCtrlEntry_Object = MibTableRow
alaSaaEthoamCtrlEntry = _AlaSaaEthoamCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1)
)
alaSaaEthoamCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTestIndex"),
)
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlEntry.setStatus("current")


class _AlaSaaEthoamCtrlOwnerIndex_Type(SnmpAdminString):
    """Custom type alaSaaEthoamCtrlOwnerIndex based on SnmpAdminString"""
    defaultValue = OctetString("USER")


_AlaSaaEthoamCtrlOwnerIndex_Type.__name__ = "SnmpAdminString"
_AlaSaaEthoamCtrlOwnerIndex_Object = MibTableColumn
alaSaaEthoamCtrlOwnerIndex = _AlaSaaEthoamCtrlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 1),
    _AlaSaaEthoamCtrlOwnerIndex_Type()
)
alaSaaEthoamCtrlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlOwnerIndex.setStatus("current")
_AlaSaaEthoamCtrlTestIndex_Type = SnmpAdminString
_AlaSaaEthoamCtrlTestIndex_Object = MibTableColumn
alaSaaEthoamCtrlTestIndex = _AlaSaaEthoamCtrlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 2),
    _AlaSaaEthoamCtrlTestIndex_Type()
)
alaSaaEthoamCtrlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTestIndex.setStatus("current")
_AlaSaaEthoamCtrlRowStatus_Type = RowStatus
_AlaSaaEthoamCtrlRowStatus_Object = MibTableColumn
alaSaaEthoamCtrlRowStatus = _AlaSaaEthoamCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 3),
    _AlaSaaEthoamCtrlRowStatus_Type()
)
alaSaaEthoamCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlRowStatus.setStatus("current")


class _AlaSaaEthoamCtrlTestMode_Type(Integer32):
    """Custom type alaSaaEthoamCtrlTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetLoopback", 1),
          ("ethernetDmm", 2))
    )


_AlaSaaEthoamCtrlTestMode_Type.__name__ = "Integer32"
_AlaSaaEthoamCtrlTestMode_Object = MibTableColumn
alaSaaEthoamCtrlTestMode = _AlaSaaEthoamCtrlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 4),
    _AlaSaaEthoamCtrlTestMode_Type()
)
alaSaaEthoamCtrlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTestMode.setStatus("current")
_AlaSaaEthoamCtrlTgtMepId_Type = Integer32
_AlaSaaEthoamCtrlTgtMepId_Object = MibTableColumn
alaSaaEthoamCtrlTgtMepId = _AlaSaaEthoamCtrlTgtMepId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 5),
    _AlaSaaEthoamCtrlTgtMepId_Type()
)
alaSaaEthoamCtrlTgtMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTgtMepId.setStatus("current")
_AlaSaaEthoamCtrlTgtMAC_Type = MacAddress
_AlaSaaEthoamCtrlTgtMAC_Object = MibTableColumn
alaSaaEthoamCtrlTgtMAC = _AlaSaaEthoamCtrlTgtMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 6),
    _AlaSaaEthoamCtrlTgtMAC_Type()
)
alaSaaEthoamCtrlTgtMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTgtMAC.setStatus("current")
_AlaSaaEthoamCtrlSrcMepId_Type = Integer32
_AlaSaaEthoamCtrlSrcMepId_Object = MibTableColumn
alaSaaEthoamCtrlSrcMepId = _AlaSaaEthoamCtrlSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 7),
    _AlaSaaEthoamCtrlSrcMepId_Type()
)
alaSaaEthoamCtrlSrcMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlSrcMepId.setStatus("current")
_AlaSaaEthoamCtrlDomainName_Type = Dot1agCfmMaintDomainName
_AlaSaaEthoamCtrlDomainName_Object = MibTableColumn
alaSaaEthoamCtrlDomainName = _AlaSaaEthoamCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 8),
    _AlaSaaEthoamCtrlDomainName_Type()
)
alaSaaEthoamCtrlDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlDomainName.setStatus("current")
_AlaSaaEthoamCtrlAssociationName_Type = Dot1agCfmMaintAssocName
_AlaSaaEthoamCtrlAssociationName_Object = MibTableColumn
alaSaaEthoamCtrlAssociationName = _AlaSaaEthoamCtrlAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 9),
    _AlaSaaEthoamCtrlAssociationName_Type()
)
alaSaaEthoamCtrlAssociationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlAssociationName.setStatus("current")
_AlaSaaEthoamCtrlPktTimeOut_Type = Integer32
_AlaSaaEthoamCtrlPktTimeOut_Object = MibTableColumn
alaSaaEthoamCtrlPktTimeOut = _AlaSaaEthoamCtrlPktTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 10),
    _AlaSaaEthoamCtrlPktTimeOut_Type()
)
alaSaaEthoamCtrlPktTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlPktTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlPktTimeOut.setUnits("milli-seconds")


class _AlaSaaEthoamCtrlNumPkts_Type(Integer32):
    """Custom type alaSaaEthoamCtrlNumPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaSaaEthoamCtrlNumPkts_Type.__name__ = "Integer32"
_AlaSaaEthoamCtrlNumPkts_Object = MibTableColumn
alaSaaEthoamCtrlNumPkts = _AlaSaaEthoamCtrlNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 11),
    _AlaSaaEthoamCtrlNumPkts_Type()
)
alaSaaEthoamCtrlNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlNumPkts.setStatus("current")


class _AlaSaaEthoamCtrlInterPktDelay_Type(Integer32):
    """Custom type alaSaaEthoamCtrlInterPktDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AlaSaaEthoamCtrlInterPktDelay_Type.__name__ = "Integer32"
_AlaSaaEthoamCtrlInterPktDelay_Object = MibTableColumn
alaSaaEthoamCtrlInterPktDelay = _AlaSaaEthoamCtrlInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 12),
    _AlaSaaEthoamCtrlInterPktDelay_Type()
)
alaSaaEthoamCtrlInterPktDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlInterPktDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlInterPktDelay.setUnits("milli-seconds")


class _AlaSaaEthoamCtrlPktData_Type(OctetString):
    """Custom type alaSaaEthoamCtrlPktData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaSaaEthoamCtrlPktData_Type.__name__ = "OctetString"
_AlaSaaEthoamCtrlPktData_Object = MibTableColumn
alaSaaEthoamCtrlPktData = _AlaSaaEthoamCtrlPktData_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 13),
    _AlaSaaEthoamCtrlPktData_Type()
)
alaSaaEthoamCtrlPktData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlPktData.setStatus("current")


class _AlaSaaEthoamCtrlVlanPriority_Type(Integer32):
    """Custom type alaSaaEthoamCtrlVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaSaaEthoamCtrlVlanPriority_Type.__name__ = "Integer32"
_AlaSaaEthoamCtrlVlanPriority_Object = MibTableColumn
alaSaaEthoamCtrlVlanPriority = _AlaSaaEthoamCtrlVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 14),
    _AlaSaaEthoamCtrlVlanPriority_Type()
)
alaSaaEthoamCtrlVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlVlanPriority.setStatus("current")


class _AlaSaaEthoamCtrlDropEligible_Type(TruthValue):
    """Custom type alaSaaEthoamCtrlDropEligible based on TruthValue"""
    defaultValue = 2


_AlaSaaEthoamCtrlDropEligible_Type.__name__ = "TruthValue"
_AlaSaaEthoamCtrlDropEligible_Object = MibTableColumn
alaSaaEthoamCtrlDropEligible = _AlaSaaEthoamCtrlDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 15),
    _AlaSaaEthoamCtrlDropEligible_Type()
)
alaSaaEthoamCtrlDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlDropEligible.setStatus("current")
_AlaSaaEthoamCtrlTotalPktsRcvd_Type = Unsigned32
_AlaSaaEthoamCtrlTotalPktsRcvd_Object = MibTableColumn
alaSaaEthoamCtrlTotalPktsRcvd = _AlaSaaEthoamCtrlTotalPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 16),
    _AlaSaaEthoamCtrlTotalPktsRcvd_Type()
)
alaSaaEthoamCtrlTotalPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTotalPktsRcvd.setStatus("current")
_AlaSaaEthoamCtrlTotalPktsSent_Type = Unsigned32
_AlaSaaEthoamCtrlTotalPktsSent_Object = MibTableColumn
alaSaaEthoamCtrlTotalPktsSent = _AlaSaaEthoamCtrlTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 17),
    _AlaSaaEthoamCtrlTotalPktsSent_Type()
)
alaSaaEthoamCtrlTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTotalPktsSent.setStatus("current")
_AlaSaaEthoamCtrlMinRTT_Type = Integer32
_AlaSaaEthoamCtrlMinRTT_Object = MibTableColumn
alaSaaEthoamCtrlMinRTT = _AlaSaaEthoamCtrlMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 18),
    _AlaSaaEthoamCtrlMinRTT_Type()
)
alaSaaEthoamCtrlMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlMinRTT.setStatus("current")
_AlaSaaEthoamCtrlAvgRTT_Type = Integer32
_AlaSaaEthoamCtrlAvgRTT_Object = MibTableColumn
alaSaaEthoamCtrlAvgRTT = _AlaSaaEthoamCtrlAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 19),
    _AlaSaaEthoamCtrlAvgRTT_Type()
)
alaSaaEthoamCtrlAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlAvgRTT.setStatus("current")
_AlaSaaEthoamCtrlMaxRTT_Type = Integer32
_AlaSaaEthoamCtrlMaxRTT_Object = MibTableColumn
alaSaaEthoamCtrlMaxRTT = _AlaSaaEthoamCtrlMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 20),
    _AlaSaaEthoamCtrlMaxRTT_Type()
)
alaSaaEthoamCtrlMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlMaxRTT.setStatus("current")
_AlaSaaEthoamCtrlMinJitter_Type = Integer32
_AlaSaaEthoamCtrlMinJitter_Object = MibTableColumn
alaSaaEthoamCtrlMinJitter = _AlaSaaEthoamCtrlMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 21),
    _AlaSaaEthoamCtrlMinJitter_Type()
)
alaSaaEthoamCtrlMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlMinJitter.setStatus("current")
_AlaSaaEthoamCtrlAvgJitter_Type = Integer32
_AlaSaaEthoamCtrlAvgJitter_Object = MibTableColumn
alaSaaEthoamCtrlAvgJitter = _AlaSaaEthoamCtrlAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 22),
    _AlaSaaEthoamCtrlAvgJitter_Type()
)
alaSaaEthoamCtrlAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlAvgJitter.setStatus("current")
_AlaSaaEthoamCtrlMaxJitter_Type = Integer32
_AlaSaaEthoamCtrlMaxJitter_Object = MibTableColumn
alaSaaEthoamCtrlMaxJitter = _AlaSaaEthoamCtrlMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 23),
    _AlaSaaEthoamCtrlMaxJitter_Type()
)
alaSaaEthoamCtrlMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlMaxJitter.setStatus("current")
_AlaSaaEthoamCtrlTSMinRTT_Type = DateAndTime
_AlaSaaEthoamCtrlTSMinRTT_Object = MibTableColumn
alaSaaEthoamCtrlTSMinRTT = _AlaSaaEthoamCtrlTSMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 24),
    _AlaSaaEthoamCtrlTSMinRTT_Type()
)
alaSaaEthoamCtrlTSMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTSMinRTT.setStatus("current")
_AlaSaaEthoamCtrlTSMaxRTT_Type = DateAndTime
_AlaSaaEthoamCtrlTSMaxRTT_Object = MibTableColumn
alaSaaEthoamCtrlTSMaxRTT = _AlaSaaEthoamCtrlTSMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 25),
    _AlaSaaEthoamCtrlTSMaxRTT_Type()
)
alaSaaEthoamCtrlTSMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTSMaxRTT.setStatus("current")
_AlaSaaEthoamCtrlTSMinJitter_Type = DateAndTime
_AlaSaaEthoamCtrlTSMinJitter_Object = MibTableColumn
alaSaaEthoamCtrlTSMinJitter = _AlaSaaEthoamCtrlTSMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 26),
    _AlaSaaEthoamCtrlTSMinJitter_Type()
)
alaSaaEthoamCtrlTSMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTSMinJitter.setStatus("current")
_AlaSaaEthoamCtrlTSMaxJitter_Type = DateAndTime
_AlaSaaEthoamCtrlTSMaxJitter_Object = MibTableColumn
alaSaaEthoamCtrlTSMaxJitter = _AlaSaaEthoamCtrlTSMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 5, 1, 1, 27),
    _AlaSaaEthoamCtrlTSMaxJitter_Type()
)
alaSaaEthoamCtrlTSMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlTSMaxJitter.setStatus("current")
_AlaSaaEthoamResults_ObjectIdentity = ObjectIdentity
alaSaaEthoamResults = _AlaSaaEthoamResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6)
)
_AlaSaaEthoamResultsTable_Object = MibTable
alaSaaEthoamResultsTable = _AlaSaaEthoamResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaSaaEthoamResultsTable.setStatus("current")
_AlaSaaEthoamResultsEntry_Object = MibTableRow
alaSaaEthoamResultsEntry = _AlaSaaEthoamResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1)
)
alaSaaEthoamResultsEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTestIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    alaSaaEthoamResultsEntry.setStatus("current")
_AlaSaaEthoamResultsTestRunIndex_Type = Unsigned32
_AlaSaaEthoamResultsTestRunIndex_Object = MibTableColumn
alaSaaEthoamResultsTestRunIndex = _AlaSaaEthoamResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 1),
    _AlaSaaEthoamResultsTestRunIndex_Type()
)
alaSaaEthoamResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsTestRunIndex.setStatus("current")
_AlaSaaEthoamResultsPktsSent_Type = Unsigned32
_AlaSaaEthoamResultsPktsSent_Object = MibTableColumn
alaSaaEthoamResultsPktsSent = _AlaSaaEthoamResultsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 2),
    _AlaSaaEthoamResultsPktsSent_Type()
)
alaSaaEthoamResultsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsPktsSent.setStatus("current")
_AlaSaaEthoamResultsPktsRcvd_Type = Unsigned32
_AlaSaaEthoamResultsPktsRcvd_Object = MibTableColumn
alaSaaEthoamResultsPktsRcvd = _AlaSaaEthoamResultsPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 3),
    _AlaSaaEthoamResultsPktsRcvd_Type()
)
alaSaaEthoamResultsPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsPktsRcvd.setStatus("current")
_AlaSaaEthoamResultsInterPktDelay_Type = Integer32
_AlaSaaEthoamResultsInterPktDelay_Object = MibTableColumn
alaSaaEthoamResultsInterPktDelay = _AlaSaaEthoamResultsInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 4),
    _AlaSaaEthoamResultsInterPktDelay_Type()
)
alaSaaEthoamResultsInterPktDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsInterPktDelay.setStatus("current")


class _AlaSaaEthoamResultsRunResult_Type(Integer32):
    """Custom type alaSaaEthoamResultsRunResult based on Integer32"""
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
        *(("undetermined", 0),
          ("success", 1),
          ("failed", 2),
          ("aborted", 3))
    )


_AlaSaaEthoamResultsRunResult_Type.__name__ = "Integer32"
_AlaSaaEthoamResultsRunResult_Object = MibTableColumn
alaSaaEthoamResultsRunResult = _AlaSaaEthoamResultsRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 5),
    _AlaSaaEthoamResultsRunResult_Type()
)
alaSaaEthoamResultsRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsRunResult.setStatus("current")
_AlaSaaEthoamResultsRunResultReason_Type = OctetString
_AlaSaaEthoamResultsRunResultReason_Object = MibTableColumn
alaSaaEthoamResultsRunResultReason = _AlaSaaEthoamResultsRunResultReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 6),
    _AlaSaaEthoamResultsRunResultReason_Type()
)
alaSaaEthoamResultsRunResultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsRunResultReason.setStatus("current")
_AlaSaaEthoamResultsRunTime_Type = DateAndTime
_AlaSaaEthoamResultsRunTime_Object = MibTableColumn
alaSaaEthoamResultsRunTime = _AlaSaaEthoamResultsRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 7),
    _AlaSaaEthoamResultsRunTime_Type()
)
alaSaaEthoamResultsRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsRunTime.setStatus("current")
_AlaSaaEthoamResultsMinRTT_Type = Integer32
_AlaSaaEthoamResultsMinRTT_Object = MibTableColumn
alaSaaEthoamResultsMinRTT = _AlaSaaEthoamResultsMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 8),
    _AlaSaaEthoamResultsMinRTT_Type()
)
alaSaaEthoamResultsMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsMinRTT.setStatus("current")
_AlaSaaEthoamResultsAvgRTT_Type = Integer32
_AlaSaaEthoamResultsAvgRTT_Object = MibTableColumn
alaSaaEthoamResultsAvgRTT = _AlaSaaEthoamResultsAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 9),
    _AlaSaaEthoamResultsAvgRTT_Type()
)
alaSaaEthoamResultsAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsAvgRTT.setStatus("current")
_AlaSaaEthoamResultsMaxRTT_Type = Integer32
_AlaSaaEthoamResultsMaxRTT_Object = MibTableColumn
alaSaaEthoamResultsMaxRTT = _AlaSaaEthoamResultsMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 10),
    _AlaSaaEthoamResultsMaxRTT_Type()
)
alaSaaEthoamResultsMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsMaxRTT.setStatus("current")
_AlaSaaEthoamResultsMinJitter_Type = Integer32
_AlaSaaEthoamResultsMinJitter_Object = MibTableColumn
alaSaaEthoamResultsMinJitter = _AlaSaaEthoamResultsMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 11),
    _AlaSaaEthoamResultsMinJitter_Type()
)
alaSaaEthoamResultsMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsMinJitter.setStatus("current")
_AlaSaaEthoamResultsAvgJitter_Type = Integer32
_AlaSaaEthoamResultsAvgJitter_Object = MibTableColumn
alaSaaEthoamResultsAvgJitter = _AlaSaaEthoamResultsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 12),
    _AlaSaaEthoamResultsAvgJitter_Type()
)
alaSaaEthoamResultsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsAvgJitter.setStatus("current")
_AlaSaaEthoamResultsMaxJitter_Type = Integer32
_AlaSaaEthoamResultsMaxJitter_Object = MibTableColumn
alaSaaEthoamResultsMaxJitter = _AlaSaaEthoamResultsMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 6, 1, 1, 13),
    _AlaSaaEthoamResultsMaxJitter_Type()
)
alaSaaEthoamResultsMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamResultsMaxJitter.setStatus("current")
_AlaSaaEthoamHistory_ObjectIdentity = ObjectIdentity
alaSaaEthoamHistory = _AlaSaaEthoamHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7)
)
_AlaSaaEthoamHistoryTable_Object = MibTable
alaSaaEthoamHistoryTable = _AlaSaaEthoamHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryTable.setStatus("current")
_AlaSaaEthoamHistoryEntry_Object = MibTableRow
alaSaaEthoamHistoryEntry = _AlaSaaEthoamHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7, 1, 1)
)
alaSaaEthoamHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlOwnerIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTestIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsTestRunIndex"),
    (0, "ALCATEL-IND1-SAA-MIB", "alaSaaEthoamHistoryIndex"),
)
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryEntry.setStatus("current")
_AlaSaaEthoamHistoryIndex_Type = Unsigned32
_AlaSaaEthoamHistoryIndex_Object = MibTableColumn
alaSaaEthoamHistoryIndex = _AlaSaaEthoamHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7, 1, 1, 1),
    _AlaSaaEthoamHistoryIndex_Type()
)
alaSaaEthoamHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryIndex.setStatus("current")
_AlaSaaEthoamHistoryPktRTT_Type = Integer32
_AlaSaaEthoamHistoryPktRTT_Object = MibTableColumn
alaSaaEthoamHistoryPktRTT = _AlaSaaEthoamHistoryPktRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7, 1, 1, 2),
    _AlaSaaEthoamHistoryPktRTT_Type()
)
alaSaaEthoamHistoryPktRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryPktRTT.setStatus("current")
_AlaSaaEthoamHistoryPktJitter_Type = Integer32
_AlaSaaEthoamHistoryPktJitter_Object = MibTableColumn
alaSaaEthoamHistoryPktJitter = _AlaSaaEthoamHistoryPktJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 1, 7, 1, 1, 3),
    _AlaSaaEthoamHistoryPktJitter_Type()
)
alaSaaEthoamHistoryPktJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryPktJitter.setStatus("current")
_AlcatelIND1SaaMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SaaMIBConformance = _AlcatelIND1SaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIBConformance.setStatus("current")
_AlcatelIND1SaaMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SaaMIBGroups = _AlcatelIND1SaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIBGroups.setStatus("current")
_AlcatelIND1SaaMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SaaMIBCompliances = _AlcatelIND1SaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIBCompliances.setStatus("current")

# Managed Objects groups

alaSaaCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 1)
)
alaSaaCtrlConfigGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlRowStatus"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlDescr"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlAdminStatus"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlTestMode"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlRuns"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlFailures"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlLastRunResult"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlLastRunTime"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlInterval"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlStartAt"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlStopAt"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlMaxHistoryRows"))
)
if mibBuilder.loadTexts:
    alaSaaCtrlConfigGroup.setStatus("current")

alaSaaIpCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 2)
)
alaSaaIpCtrlConfigGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlRowStatus"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTestMode"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTgtAddrType"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTgtAddress"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlSrcAddrType"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlSrcAddress"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlPayloadSize"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlNumPkts"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlInterPktDelay"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTypeOfService"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlVRFId"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTotalPktsSent"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTotalPktsRcvd"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlAvgRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlAvgJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlMaxJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTSMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTSMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTSMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlTSMaxJitter"))
)
if mibBuilder.loadTexts:
    alaSaaIpCtrlConfigGroup.setStatus("current")

alaSaaIpResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 3)
)
alaSaaIpResultsGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsPktsSent"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsPktsRcvd"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsInterPktDelay"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsRunResult"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsRunResultReason"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsRunTime"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsAvgRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsAvgJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsMaxJitter"))
)
if mibBuilder.loadTexts:
    alaSaaIpResultsGroup.setStatus("current")

alaSaaIpHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 4)
)
alaSaaIpHistoryGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaIpHistoryPktRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpHistoryPktJitter"))
)
if mibBuilder.loadTexts:
    alaSaaIpHistoryGroup.setStatus("current")

alaSaaEthoamCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 5)
)
alaSaaEthoamCtrlConfigGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlRowStatus"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTestMode"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTgtMepId"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTgtMAC"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlSrcMepId"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlDomainName"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlAssociationName"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlPktTimeOut"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlNumPkts"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlInterPktDelay"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlPktData"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlVlanPriority"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlDropEligible"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTotalPktsRcvd"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTotalPktsSent"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlAvgRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlAvgJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlMaxJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTSMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTSMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTSMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlTSMaxJitter"))
)
if mibBuilder.loadTexts:
    alaSaaEthoamCtrlConfigGroup.setStatus("current")

alaSaaEthoamResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 6)
)
alaSaaEthoamResultsGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsPktsSent"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsPktsRcvd"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsInterPktDelay"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsRunResult"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsRunResultReason"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsRunTime"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsMinRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsAvgRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsMaxRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsMinJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsAvgJitter"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsMaxJitter"))
)
if mibBuilder.loadTexts:
    alaSaaEthoamResultsGroup.setStatus("current")

alaSaaEthoamHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 1, 7)
)
alaSaaEthoamHistoryGroup.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamHistoryPktRTT"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamHistoryPktJitter"))
)
if mibBuilder.loadTexts:
    alaSaaEthoamHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1SaaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 55, 1, 2, 2, 1)
)
alcatelIND1SaaMIBCompliance.setObjects(
      *(("ALCATEL-IND1-SAA-MIB", "alaSaaCtrlConfigGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpCtrlConfigGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpResultsGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaIpHistoryGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamCtrlConfigGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamResultsGroup"),
        ("ALCATEL-IND1-SAA-MIB", "alaSaaEthoamHistoryGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1SaaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SAA-MIB",
    **{"alcatelIND1SaaMIB": alcatelIND1SaaMIB,
       "alcatelIND1SaaNotifications": alcatelIND1SaaNotifications,
       "alcatelIND1SaaMIBObjects": alcatelIND1SaaMIBObjects,
       "alaSaaCtrlConfig": alaSaaCtrlConfig,
       "alaSaaCtrlTable": alaSaaCtrlTable,
       "alaSaaCtrlEntry": alaSaaCtrlEntry,
       "alaSaaCtrlOwnerIndex": alaSaaCtrlOwnerIndex,
       "alaSaaCtrlTestIndex": alaSaaCtrlTestIndex,
       "alaSaaCtrlRowStatus": alaSaaCtrlRowStatus,
       "alaSaaCtrlDescr": alaSaaCtrlDescr,
       "alaSaaCtrlAdminStatus": alaSaaCtrlAdminStatus,
       "alaSaaCtrlTestMode": alaSaaCtrlTestMode,
       "alaSaaCtrlRuns": alaSaaCtrlRuns,
       "alaSaaCtrlFailures": alaSaaCtrlFailures,
       "alaSaaCtrlLastRunResult": alaSaaCtrlLastRunResult,
       "alaSaaCtrlLastRunTime": alaSaaCtrlLastRunTime,
       "alaSaaCtrlInterval": alaSaaCtrlInterval,
       "alaSaaCtrlStartAt": alaSaaCtrlStartAt,
       "alaSaaCtrlStopAt": alaSaaCtrlStopAt,
       "alaSaaCtrlMaxHistoryRows": alaSaaCtrlMaxHistoryRows,
       "alaSaaIpCtrlConfig": alaSaaIpCtrlConfig,
       "alaSaaIpCtrlTable": alaSaaIpCtrlTable,
       "alaSaaIpCtrlEntry": alaSaaIpCtrlEntry,
       "alaSaaIpCtrlOwnerIndex": alaSaaIpCtrlOwnerIndex,
       "alaSaaIpCtrlTestIndex": alaSaaIpCtrlTestIndex,
       "alaSaaIpCtrlRowStatus": alaSaaIpCtrlRowStatus,
       "alaSaaIpCtrlTestMode": alaSaaIpCtrlTestMode,
       "alaSaaIpCtrlTgtAddrType": alaSaaIpCtrlTgtAddrType,
       "alaSaaIpCtrlTgtAddress": alaSaaIpCtrlTgtAddress,
       "alaSaaIpCtrlSrcAddrType": alaSaaIpCtrlSrcAddrType,
       "alaSaaIpCtrlSrcAddress": alaSaaIpCtrlSrcAddress,
       "alaSaaIpCtrlPayloadSize": alaSaaIpCtrlPayloadSize,
       "alaSaaIpCtrlNumPkts": alaSaaIpCtrlNumPkts,
       "alaSaaIpCtrlInterPktDelay": alaSaaIpCtrlInterPktDelay,
       "alaSaaIpCtrlTypeOfService": alaSaaIpCtrlTypeOfService,
       "alaSaaIpCtrlVRFId": alaSaaIpCtrlVRFId,
       "alaSaaIpCtrlTotalPktsSent": alaSaaIpCtrlTotalPktsSent,
       "alaSaaIpCtrlTotalPktsRcvd": alaSaaIpCtrlTotalPktsRcvd,
       "alaSaaIpCtrlMinRTT": alaSaaIpCtrlMinRTT,
       "alaSaaIpCtrlAvgRTT": alaSaaIpCtrlAvgRTT,
       "alaSaaIpCtrlMaxRTT": alaSaaIpCtrlMaxRTT,
       "alaSaaIpCtrlMinJitter": alaSaaIpCtrlMinJitter,
       "alaSaaIpCtrlAvgJitter": alaSaaIpCtrlAvgJitter,
       "alaSaaIpCtrlMaxJitter": alaSaaIpCtrlMaxJitter,
       "alaSaaIpCtrlTSMinRTT": alaSaaIpCtrlTSMinRTT,
       "alaSaaIpCtrlTSMaxRTT": alaSaaIpCtrlTSMaxRTT,
       "alaSaaIpCtrlTSMinJitter": alaSaaIpCtrlTSMinJitter,
       "alaSaaIpCtrlTSMaxJitter": alaSaaIpCtrlTSMaxJitter,
       "alaSaaIpResults": alaSaaIpResults,
       "alaSaaIpResultsTable": alaSaaIpResultsTable,
       "alaSaaIpResultsEntry": alaSaaIpResultsEntry,
       "alaSaaIpResultsTestRunIndex": alaSaaIpResultsTestRunIndex,
       "alaSaaIpResultsPktsSent": alaSaaIpResultsPktsSent,
       "alaSaaIpResultsPktsRcvd": alaSaaIpResultsPktsRcvd,
       "alaSaaIpResultsInterPktDelay": alaSaaIpResultsInterPktDelay,
       "alaSaaIpResultsRunResult": alaSaaIpResultsRunResult,
       "alaSaaIpResultsRunResultReason": alaSaaIpResultsRunResultReason,
       "alaSaaIpResultsRunTime": alaSaaIpResultsRunTime,
       "alaSaaIpResultsMinRTT": alaSaaIpResultsMinRTT,
       "alaSaaIpResultsAvgRTT": alaSaaIpResultsAvgRTT,
       "alaSaaIpResultsMaxRTT": alaSaaIpResultsMaxRTT,
       "alaSaaIpResultsMinJitter": alaSaaIpResultsMinJitter,
       "alaSaaIpResultsAvgJitter": alaSaaIpResultsAvgJitter,
       "alaSaaIpResultsMaxJitter": alaSaaIpResultsMaxJitter,
       "alaSaaIpHistory": alaSaaIpHistory,
       "alaSaaIpHistoryTable": alaSaaIpHistoryTable,
       "alaSaaIpHistoryEntry": alaSaaIpHistoryEntry,
       "alaSaaIpHistoryIndex": alaSaaIpHistoryIndex,
       "alaSaaIpHistoryPktRTT": alaSaaIpHistoryPktRTT,
       "alaSaaIpHistoryPktJitter": alaSaaIpHistoryPktJitter,
       "alaSaaEthoamCtrlConfig": alaSaaEthoamCtrlConfig,
       "alaSaaEthoamCtrlTable": alaSaaEthoamCtrlTable,
       "alaSaaEthoamCtrlEntry": alaSaaEthoamCtrlEntry,
       "alaSaaEthoamCtrlOwnerIndex": alaSaaEthoamCtrlOwnerIndex,
       "alaSaaEthoamCtrlTestIndex": alaSaaEthoamCtrlTestIndex,
       "alaSaaEthoamCtrlRowStatus": alaSaaEthoamCtrlRowStatus,
       "alaSaaEthoamCtrlTestMode": alaSaaEthoamCtrlTestMode,
       "alaSaaEthoamCtrlTgtMepId": alaSaaEthoamCtrlTgtMepId,
       "alaSaaEthoamCtrlTgtMAC": alaSaaEthoamCtrlTgtMAC,
       "alaSaaEthoamCtrlSrcMepId": alaSaaEthoamCtrlSrcMepId,
       "alaSaaEthoamCtrlDomainName": alaSaaEthoamCtrlDomainName,
       "alaSaaEthoamCtrlAssociationName": alaSaaEthoamCtrlAssociationName,
       "alaSaaEthoamCtrlPktTimeOut": alaSaaEthoamCtrlPktTimeOut,
       "alaSaaEthoamCtrlNumPkts": alaSaaEthoamCtrlNumPkts,
       "alaSaaEthoamCtrlInterPktDelay": alaSaaEthoamCtrlInterPktDelay,
       "alaSaaEthoamCtrlPktData": alaSaaEthoamCtrlPktData,
       "alaSaaEthoamCtrlVlanPriority": alaSaaEthoamCtrlVlanPriority,
       "alaSaaEthoamCtrlDropEligible": alaSaaEthoamCtrlDropEligible,
       "alaSaaEthoamCtrlTotalPktsRcvd": alaSaaEthoamCtrlTotalPktsRcvd,
       "alaSaaEthoamCtrlTotalPktsSent": alaSaaEthoamCtrlTotalPktsSent,
       "alaSaaEthoamCtrlMinRTT": alaSaaEthoamCtrlMinRTT,
       "alaSaaEthoamCtrlAvgRTT": alaSaaEthoamCtrlAvgRTT,
       "alaSaaEthoamCtrlMaxRTT": alaSaaEthoamCtrlMaxRTT,
       "alaSaaEthoamCtrlMinJitter": alaSaaEthoamCtrlMinJitter,
       "alaSaaEthoamCtrlAvgJitter": alaSaaEthoamCtrlAvgJitter,
       "alaSaaEthoamCtrlMaxJitter": alaSaaEthoamCtrlMaxJitter,
       "alaSaaEthoamCtrlTSMinRTT": alaSaaEthoamCtrlTSMinRTT,
       "alaSaaEthoamCtrlTSMaxRTT": alaSaaEthoamCtrlTSMaxRTT,
       "alaSaaEthoamCtrlTSMinJitter": alaSaaEthoamCtrlTSMinJitter,
       "alaSaaEthoamCtrlTSMaxJitter": alaSaaEthoamCtrlTSMaxJitter,
       "alaSaaEthoamResults": alaSaaEthoamResults,
       "alaSaaEthoamResultsTable": alaSaaEthoamResultsTable,
       "alaSaaEthoamResultsEntry": alaSaaEthoamResultsEntry,
       "alaSaaEthoamResultsTestRunIndex": alaSaaEthoamResultsTestRunIndex,
       "alaSaaEthoamResultsPktsSent": alaSaaEthoamResultsPktsSent,
       "alaSaaEthoamResultsPktsRcvd": alaSaaEthoamResultsPktsRcvd,
       "alaSaaEthoamResultsInterPktDelay": alaSaaEthoamResultsInterPktDelay,
       "alaSaaEthoamResultsRunResult": alaSaaEthoamResultsRunResult,
       "alaSaaEthoamResultsRunResultReason": alaSaaEthoamResultsRunResultReason,
       "alaSaaEthoamResultsRunTime": alaSaaEthoamResultsRunTime,
       "alaSaaEthoamResultsMinRTT": alaSaaEthoamResultsMinRTT,
       "alaSaaEthoamResultsAvgRTT": alaSaaEthoamResultsAvgRTT,
       "alaSaaEthoamResultsMaxRTT": alaSaaEthoamResultsMaxRTT,
       "alaSaaEthoamResultsMinJitter": alaSaaEthoamResultsMinJitter,
       "alaSaaEthoamResultsAvgJitter": alaSaaEthoamResultsAvgJitter,
       "alaSaaEthoamResultsMaxJitter": alaSaaEthoamResultsMaxJitter,
       "alaSaaEthoamHistory": alaSaaEthoamHistory,
       "alaSaaEthoamHistoryTable": alaSaaEthoamHistoryTable,
       "alaSaaEthoamHistoryEntry": alaSaaEthoamHistoryEntry,
       "alaSaaEthoamHistoryIndex": alaSaaEthoamHistoryIndex,
       "alaSaaEthoamHistoryPktRTT": alaSaaEthoamHistoryPktRTT,
       "alaSaaEthoamHistoryPktJitter": alaSaaEthoamHistoryPktJitter,
       "alcatelIND1SaaMIBConformance": alcatelIND1SaaMIBConformance,
       "alcatelIND1SaaMIBGroups": alcatelIND1SaaMIBGroups,
       "alaSaaCtrlConfigGroup": alaSaaCtrlConfigGroup,
       "alaSaaIpCtrlConfigGroup": alaSaaIpCtrlConfigGroup,
       "alaSaaIpResultsGroup": alaSaaIpResultsGroup,
       "alaSaaIpHistoryGroup": alaSaaIpHistoryGroup,
       "alaSaaEthoamCtrlConfigGroup": alaSaaEthoamCtrlConfigGroup,
       "alaSaaEthoamResultsGroup": alaSaaEthoamResultsGroup,
       "alaSaaEthoamHistoryGroup": alaSaaEthoamHistoryGroup,
       "alcatelIND1SaaMIBCompliances": alcatelIND1SaaMIBCompliances,
       "alcatelIND1SaaMIBCompliance": alcatelIND1SaaMIBCompliance}
)
