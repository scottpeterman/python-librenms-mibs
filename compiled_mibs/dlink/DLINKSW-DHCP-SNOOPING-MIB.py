# SNMP MIB module (DLINKSW-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:53 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

dlinkSwDhcpSnpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131)
)
if mibBuilder.loadTexts:
    dlinkSwDhcpSnpMIB.setRevisions(
        ("2013-07-19 00:00",
         "2013-09-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcpSnpMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcpSnpMIBNotifications = _DDhcpSnpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 0)
)
_DDhcpSnpMIBObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpMIBObjects = _DDhcpSnpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1)
)
_DDhcpSnpGlobalObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpGlobalObjects = _DDhcpSnpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1)
)


class _DDhcpSnpGlobalEnabled_Type(TruthValue):
    """Custom type dDhcpSnpGlobalEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpSnpGlobalEnabled_Type.__name__ = "TruthValue"
_DDhcpSnpGlobalEnabled_Object = MibScalar
dDhcpSnpGlobalEnabled = _DDhcpSnpGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1, 1),
    _DDhcpSnpGlobalEnabled_Type()
)
dDhcpSnpGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpGlobalEnabled.setStatus("current")


class _DDhcpSnpVerifyMacAddressEnabled_Type(TruthValue):
    """Custom type dDhcpSnpVerifyMacAddressEnabled based on TruthValue"""
    defaultValue = 1


_DDhcpSnpVerifyMacAddressEnabled_Type.__name__ = "TruthValue"
_DDhcpSnpVerifyMacAddressEnabled_Object = MibScalar
dDhcpSnpVerifyMacAddressEnabled = _DDhcpSnpVerifyMacAddressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1, 2),
    _DDhcpSnpVerifyMacAddressEnabled_Type()
)
dDhcpSnpVerifyMacAddressEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpVerifyMacAddressEnabled.setStatus("current")


class _DDhcpSnpStationMoveDenyEnabled_Type(TruthValue):
    """Custom type dDhcpSnpStationMoveDenyEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpSnpStationMoveDenyEnabled_Type.__name__ = "TruthValue"
_DDhcpSnpStationMoveDenyEnabled_Object = MibScalar
dDhcpSnpStationMoveDenyEnabled = _DDhcpSnpStationMoveDenyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1, 3),
    _DDhcpSnpStationMoveDenyEnabled_Type()
)
dDhcpSnpStationMoveDenyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpStationMoveDenyEnabled.setStatus("current")


class _DDhcpSnpOption82AllowUntrust_Type(TruthValue):
    """Custom type dDhcpSnpOption82AllowUntrust based on TruthValue"""
    defaultValue = 2


_DDhcpSnpOption82AllowUntrust_Type.__name__ = "TruthValue"
_DDhcpSnpOption82AllowUntrust_Object = MibScalar
dDhcpSnpOption82AllowUntrust = _DDhcpSnpOption82AllowUntrust_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1, 4),
    _DDhcpSnpOption82AllowUntrust_Type()
)
dDhcpSnpOption82AllowUntrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpOption82AllowUntrust.setStatus("current")


class _DDhcpSnpBootpBindEnabled_Type(TruthValue):
    """Custom type dDhcpSnpBootpBindEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpSnpBootpBindEnabled_Type.__name__ = "TruthValue"
_DDhcpSnpBootpBindEnabled_Object = MibScalar
dDhcpSnpBootpBindEnabled = _DDhcpSnpBootpBindEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 1, 5),
    _DDhcpSnpBootpBindEnabled_Type()
)
dDhcpSnpBootpBindEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBootpBindEnabled.setStatus("current")
_DDhcpSnpDatabaseObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpDatabaseObjects = _DDhcpSnpDatabaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2)
)
_DDhcpSnpDatabaseUrl_Type = SnmpAdminString
_DDhcpSnpDatabaseUrl_Object = MibScalar
dDhcpSnpDatabaseUrl = _DDhcpSnpDatabaseUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 1),
    _DDhcpSnpDatabaseUrl_Type()
)
dDhcpSnpDatabaseUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpDatabaseUrl.setStatus("current")


class _DDhcpSnpDatabaseUpdateInterval_Type(Integer32):
    """Custom type dDhcpSnpDatabaseUpdateInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_DDhcpSnpDatabaseUpdateInterval_Type.__name__ = "Integer32"
_DDhcpSnpDatabaseUpdateInterval_Object = MibScalar
dDhcpSnpDatabaseUpdateInterval = _DDhcpSnpDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 2),
    _DDhcpSnpDatabaseUpdateInterval_Type()
)
dDhcpSnpDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpDatabaseUpdateInterval.setStatus("current")
_DDhcpSnpRenewDatabaseUrl_Type = SnmpAdminString
_DDhcpSnpRenewDatabaseUrl_Object = MibScalar
dDhcpSnpRenewDatabaseUrl = _DDhcpSnpRenewDatabaseUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 3),
    _DDhcpSnpRenewDatabaseUrl_Type()
)
dDhcpSnpRenewDatabaseUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpRenewDatabaseUrl.setStatus("current")


class _DDhcpSnpRenewValidateDbEnabled_Type(TruthValue):
    """Custom type dDhcpSnpRenewValidateDbEnabled based on TruthValue"""
    defaultValue = 1


_DDhcpSnpRenewValidateDbEnabled_Type.__name__ = "TruthValue"
_DDhcpSnpRenewValidateDbEnabled_Object = MibScalar
dDhcpSnpRenewValidateDbEnabled = _DDhcpSnpRenewValidateDbEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 4),
    _DDhcpSnpRenewValidateDbEnabled_Type()
)
dDhcpSnpRenewValidateDbEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpRenewValidateDbEnabled.setStatus("current")


class _DDhcpSnpRenewDatabase_Type(Integer32):
    """Custom type dDhcpSnpRenewDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("renew", 1),
          ("noOp", 2))
    )


_DDhcpSnpRenewDatabase_Type.__name__ = "Integer32"
_DDhcpSnpRenewDatabase_Object = MibScalar
dDhcpSnpRenewDatabase = _DDhcpSnpRenewDatabase_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 5),
    _DDhcpSnpRenewDatabase_Type()
)
dDhcpSnpRenewDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpRenewDatabase.setStatus("current")
_DDhcpSnpDbLastSucceeded_Type = DateAndTime
_DDhcpSnpDbLastSucceeded_Object = MibScalar
dDhcpSnpDbLastSucceeded = _DDhcpSnpDbLastSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 6),
    _DDhcpSnpDbLastSucceeded_Type()
)
dDhcpSnpDbLastSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpDbLastSucceeded.setStatus("current")
_DDhcpSnpDbLastFailed_Type = DateAndTime
_DDhcpSnpDbLastFailed_Object = MibScalar
dDhcpSnpDbLastFailed = _DDhcpSnpDbLastFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 7),
    _DDhcpSnpDbLastFailed_Type()
)
dDhcpSnpDbLastFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpDbLastFailed.setStatus("current")


class _DDhcpSnpClearDatabaseStatistics_Type(Integer32):
    """Custom type dDhcpSnpClearDatabaseStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDhcpSnpClearDatabaseStatistics_Type.__name__ = "Integer32"
_DDhcpSnpClearDatabaseStatistics_Object = MibScalar
dDhcpSnpClearDatabaseStatistics = _DDhcpSnpClearDatabaseStatistics_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 8),
    _DDhcpSnpClearDatabaseStatistics_Type()
)
dDhcpSnpClearDatabaseStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpClearDatabaseStatistics.setStatus("current")
_DDhcpSnpDbLastIgnoredCounters_ObjectIdentity = ObjectIdentity
dDhcpSnpDbLastIgnoredCounters = _DDhcpSnpDbLastIgnoredCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9)
)
_DDhcpSnpStatBindingCollision_Type = Counter32
_DDhcpSnpStatBindingCollision_Object = MibScalar
dDhcpSnpStatBindingCollision = _DDhcpSnpStatBindingCollision_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 1),
    _DDhcpSnpStatBindingCollision_Type()
)
dDhcpSnpStatBindingCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatBindingCollision.setStatus("current")
_DDhcpSnpStatExpiredLease_Type = Counter32
_DDhcpSnpStatExpiredLease_Object = MibScalar
dDhcpSnpStatExpiredLease = _DDhcpSnpStatExpiredLease_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 2),
    _DDhcpSnpStatExpiredLease_Type()
)
dDhcpSnpStatExpiredLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatExpiredLease.setStatus("current")
_DDhcpSnpStatInvalidInterfaces_Type = Counter32
_DDhcpSnpStatInvalidInterfaces_Object = MibScalar
dDhcpSnpStatInvalidInterfaces = _DDhcpSnpStatInvalidInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 3),
    _DDhcpSnpStatInvalidInterfaces_Type()
)
dDhcpSnpStatInvalidInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatInvalidInterfaces.setStatus("current")
_DDhcpSnpStatUnsupportedVlans_Type = Counter32
_DDhcpSnpStatUnsupportedVlans_Object = MibScalar
dDhcpSnpStatUnsupportedVlans = _DDhcpSnpStatUnsupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 4),
    _DDhcpSnpStatUnsupportedVlans_Type()
)
dDhcpSnpStatUnsupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatUnsupportedVlans.setStatus("current")
_DDhcpSnpStatParsingFailures_Type = Counter32
_DDhcpSnpStatParsingFailures_Object = MibScalar
dDhcpSnpStatParsingFailures = _DDhcpSnpStatParsingFailures_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 5),
    _DDhcpSnpStatParsingFailures_Type()
)
dDhcpSnpStatParsingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatParsingFailures.setStatus("current")
_DDhcpSnpStatChecksumErrors_Type = Counter32
_DDhcpSnpStatChecksumErrors_Object = MibScalar
dDhcpSnpStatChecksumErrors = _DDhcpSnpStatChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 2, 9, 6),
    _DDhcpSnpStatChecksumErrors_Type()
)
dDhcpSnpStatChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSnpStatChecksumErrors.setStatus("current")
_DDhcpSnpVlanObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpVlanObjects = _DDhcpSnpVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 3)
)
_DDhcpSnpVlanCrlFirst2K_Type = Dlink2kVlanList
_DDhcpSnpVlanCrlFirst2K_Object = MibScalar
dDhcpSnpVlanCrlFirst2K = _DDhcpSnpVlanCrlFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 3, 1),
    _DDhcpSnpVlanCrlFirst2K_Type()
)
dDhcpSnpVlanCrlFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpVlanCrlFirst2K.setStatus("current")
_DDhcpSnpVlanCrlSecond2K_Type = Dlink2kVlanList
_DDhcpSnpVlanCrlSecond2K_Object = MibScalar
dDhcpSnpVlanCrlSecond2K = _DDhcpSnpVlanCrlSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 3, 2),
    _DDhcpSnpVlanCrlSecond2K_Type()
)
dDhcpSnpVlanCrlSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpVlanCrlSecond2K.setStatus("current")
_DDhcpSnpIfObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpIfObjects = _DDhcpSnpIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4)
)
_DDhcpSnpIfTrustTable_Object = MibTable
dDhcpSnpIfTrustTable = _DDhcpSnpIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDhcpSnpIfTrustTable.setStatus("current")
_DDhcpSnpIfTrustEntry_Object = MibTableRow
dDhcpSnpIfTrustEntry = _DDhcpSnpIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 1, 1)
)
dDhcpSnpIfTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSnpIfTrustEntry.setStatus("current")
_DDhcpSnpIfTrustEnabled_Type = TruthValue
_DDhcpSnpIfTrustEnabled_Object = MibTableColumn
dDhcpSnpIfTrustEnabled = _DDhcpSnpIfTrustEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 1, 1, 1),
    _DDhcpSnpIfTrustEnabled_Type()
)
dDhcpSnpIfTrustEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpIfTrustEnabled.setStatus("current")
_DDhcpSnpIfRateLimitTable_Object = MibTable
dDhcpSnpIfRateLimitTable = _DDhcpSnpIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dDhcpSnpIfRateLimitTable.setStatus("current")
_DDhcpSnpIfRateLimitEntry_Object = MibTableRow
dDhcpSnpIfRateLimitEntry = _DDhcpSnpIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 2, 1)
)
dDhcpSnpIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSnpIfRateLimitEntry.setStatus("current")


class _DDhcpSnpIfRateLimit_Type(Integer32):
    """Custom type dDhcpSnpIfRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 300),
    )


_DDhcpSnpIfRateLimit_Type.__name__ = "Integer32"
_DDhcpSnpIfRateLimit_Object = MibTableColumn
dDhcpSnpIfRateLimit = _DDhcpSnpIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 2, 1, 1),
    _DDhcpSnpIfRateLimit_Type()
)
dDhcpSnpIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    dDhcpSnpIfRateLimit.setUnits("packets per second")
_DDhcpSnpIfBindingsLimitTable_Object = MibTable
dDhcpSnpIfBindingsLimitTable = _DDhcpSnpIfBindingsLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dDhcpSnpIfBindingsLimitTable.setStatus("current")
_DDhcpSnpIfBindingsLimitEntry_Object = MibTableRow
dDhcpSnpIfBindingsLimitEntry = _DDhcpSnpIfBindingsLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 3, 1)
)
dDhcpSnpIfBindingsLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSnpIfBindingsLimitEntry.setStatus("current")


class _DDhcpSnpIfBindingsLimit_Type(Integer32):
    """Custom type dDhcpSnpIfBindingsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1024),
    )


_DDhcpSnpIfBindingsLimit_Type.__name__ = "Integer32"
_DDhcpSnpIfBindingsLimit_Object = MibTableColumn
dDhcpSnpIfBindingsLimit = _DDhcpSnpIfBindingsLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 4, 3, 1, 1),
    _DDhcpSnpIfBindingsLimit_Type()
)
dDhcpSnpIfBindingsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpIfBindingsLimit.setStatus("current")
if mibBuilder.loadTexts:
    dDhcpSnpIfBindingsLimit.setUnits("bindings per port")
_DDhcpSnpBindingsObjects_ObjectIdentity = ObjectIdentity
dDhcpSnpBindingsObjects = _DDhcpSnpBindingsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5)
)
_DDhcpSnpBindingsTable_Object = MibTable
dDhcpSnpBindingsTable = _DDhcpSnpBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsTable.setStatus("current")
_DDhcpSnpBindingsEntry_Object = MibTableRow
dDhcpSnpBindingsEntry = _DDhcpSnpBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1)
)
dDhcpSnpBindingsEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsMacAddress"),
    (0, "DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsVlan"),
    (0, "DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsIpAddress"),
    (0, "DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsInterface"),
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsEntry.setStatus("current")
_DDhcpSnpBindingsMacAddress_Type = MacAddress
_DDhcpSnpBindingsMacAddress_Object = MibTableColumn
dDhcpSnpBindingsMacAddress = _DDhcpSnpBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 1),
    _DDhcpSnpBindingsMacAddress_Type()
)
dDhcpSnpBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsMacAddress.setStatus("current")
_DDhcpSnpBindingsVlan_Type = VlanId
_DDhcpSnpBindingsVlan_Object = MibTableColumn
dDhcpSnpBindingsVlan = _DDhcpSnpBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 2),
    _DDhcpSnpBindingsVlan_Type()
)
dDhcpSnpBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsVlan.setStatus("current")
_DDhcpSnpBindingsIpAddress_Type = IpAddress
_DDhcpSnpBindingsIpAddress_Object = MibTableColumn
dDhcpSnpBindingsIpAddress = _DDhcpSnpBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 3),
    _DDhcpSnpBindingsIpAddress_Type()
)
dDhcpSnpBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsIpAddress.setStatus("current")
_DDhcpSnpBindingsInterface_Type = InterfaceIndex
_DDhcpSnpBindingsInterface_Object = MibTableColumn
dDhcpSnpBindingsInterface = _DDhcpSnpBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 4),
    _DDhcpSnpBindingsInterface_Type()
)
dDhcpSnpBindingsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsInterface.setStatus("current")


class _DDhcpSnpBindingsLeasedTime_Type(Unsigned32):
    """Custom type dDhcpSnpBindingsLeasedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcpSnpBindingsLeasedTime_Type.__name__ = "Unsigned32"
_DDhcpSnpBindingsLeasedTime_Object = MibTableColumn
dDhcpSnpBindingsLeasedTime = _DDhcpSnpBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 5),
    _DDhcpSnpBindingsLeasedTime_Type()
)
dDhcpSnpBindingsLeasedTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsLeasedTime.setStatus("current")
_DDhcpSnpBindingsStatus_Type = RowStatus
_DDhcpSnpBindingsStatus_Object = MibTableColumn
dDhcpSnpBindingsStatus = _DDhcpSnpBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 1, 1, 99),
    _DDhcpSnpBindingsStatus_Type()
)
dDhcpSnpBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsStatus.setStatus("current")
_DDhcpSnpBindingsClearTable_Object = MibTable
dDhcpSnpBindingsClearTable = _DDhcpSnpBindingsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearTable.setStatus("current")
_DDhcpSnpBindingsClearEntry_Object = MibTableRow
dDhcpSnpBindingsClearEntry = _DDhcpSnpBindingsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1)
)
dDhcpSnpBindingsClearEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearEntry.setStatus("current")


class _DDhcpSnpBindingsClearIndex_Type(Unsigned32):
    """Custom type dDhcpSnpBindingsClearIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DDhcpSnpBindingsClearIndex_Type.__name__ = "Unsigned32"
_DDhcpSnpBindingsClearIndex_Object = MibTableColumn
dDhcpSnpBindingsClearIndex = _DDhcpSnpBindingsClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 1),
    _DDhcpSnpBindingsClearIndex_Type()
)
dDhcpSnpBindingsClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearIndex.setStatus("current")
_DDhcpSnpBindingsClearByMacAddr_Type = MacAddress
_DDhcpSnpBindingsClearByMacAddr_Object = MibTableColumn
dDhcpSnpBindingsClearByMacAddr = _DDhcpSnpBindingsClearByMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 2),
    _DDhcpSnpBindingsClearByMacAddr_Type()
)
dDhcpSnpBindingsClearByMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearByMacAddr.setStatus("current")
_DDhcpSnpBindingsClearByVlan_Type = VlanIdOrNone
_DDhcpSnpBindingsClearByVlan_Object = MibTableColumn
dDhcpSnpBindingsClearByVlan = _DDhcpSnpBindingsClearByVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 3),
    _DDhcpSnpBindingsClearByVlan_Type()
)
dDhcpSnpBindingsClearByVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearByVlan.setStatus("current")
_DDhcpSnpBindingsClearByIpAddress_Type = IpAddress
_DDhcpSnpBindingsClearByIpAddress_Object = MibTableColumn
dDhcpSnpBindingsClearByIpAddress = _DDhcpSnpBindingsClearByIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 4),
    _DDhcpSnpBindingsClearByIpAddress_Type()
)
dDhcpSnpBindingsClearByIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearByIpAddress.setStatus("current")
_DDhcpSnpBindingsClearByInterface_Type = InterfaceIndexOrZero
_DDhcpSnpBindingsClearByInterface_Object = MibTableColumn
dDhcpSnpBindingsClearByInterface = _DDhcpSnpBindingsClearByInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 5),
    _DDhcpSnpBindingsClearByInterface_Type()
)
dDhcpSnpBindingsClearByInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearByInterface.setStatus("current")


class _DDhcpSnpBindingsClearStatus_Type(Integer32):
    """Custom type dDhcpSnpBindingsClearStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDhcpSnpBindingsClearStatus_Type.__name__ = "Integer32"
_DDhcpSnpBindingsClearStatus_Object = MibTableColumn
dDhcpSnpBindingsClearStatus = _DDhcpSnpBindingsClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 1, 5, 2, 1, 99),
    _DDhcpSnpBindingsClearStatus_Type()
)
dDhcpSnpBindingsClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearStatus.setStatus("current")
_DDhcpSnpMIBConformance_ObjectIdentity = ObjectIdentity
dDhcpSnpMIBConformance = _DDhcpSnpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2)
)
_DDhcpSnpCompliances_ObjectIdentity = ObjectIdentity
dDhcpSnpCompliances = _DDhcpSnpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 1)
)
_DDhcpSnpGroups_ObjectIdentity = ObjectIdentity
dDhcpSnpGroups = _DDhcpSnpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2)
)

# Managed Objects groups

dDhcpSnpGlobalEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 1)
)
dDhcpSnpGlobalEnableGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpGlobalEnabled")
)
if mibBuilder.loadTexts:
    dDhcpSnpGlobalEnableGroup.setStatus("current")

dDhcpSnpVlanEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 2)
)
dDhcpSnpVlanEnableGroup.setObjects(
      *(("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpVlanCrlFirst2K"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpVlanCrlSecond2K"))
)
if mibBuilder.loadTexts:
    dDhcpSnpVlanEnableGroup.setStatus("current")

dDhcpSnpIfTrustGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 3)
)
dDhcpSnpIfTrustGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfTrustEnabled")
)
if mibBuilder.loadTexts:
    dDhcpSnpIfTrustGroup.setStatus("current")

dDhcpSnpBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 4)
)
dDhcpSnpBindingsGroup.setObjects(
      *(("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsLeasedTime"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsGroup.setStatus("current")

dDhcpSnpBindingsClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 5)
)
dDhcpSnpBindingsClearGroup.setObjects(
      *(("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearStatus"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearByMacAddr"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearByVlan"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearByIpAddress"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearByInterface"))
)
if mibBuilder.loadTexts:
    dDhcpSnpBindingsClearGroup.setStatus("current")

dDhcpSnpVerifyMacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 6)
)
dDhcpSnpVerifyMacAddressGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpVerifyMacAddressEnabled")
)
if mibBuilder.loadTexts:
    dDhcpSnpVerifyMacAddressGroup.setStatus("current")

dDhcpSnpStationMoveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 7)
)
dDhcpSnpStationMoveGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStationMoveDenyEnabled")
)
if mibBuilder.loadTexts:
    dDhcpSnpStationMoveGroup.setStatus("current")

dDhcpSnpBootpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 8)
)
dDhcpSnpBootpBindGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBootpBindEnabled")
)
if mibBuilder.loadTexts:
    dDhcpSnpBootpBindGroup.setStatus("current")

dDhcpSnpRelayAgentInfoAllowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 9)
)
dDhcpSnpRelayAgentInfoAllowGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpOption82AllowUntrust")
)
if mibBuilder.loadTexts:
    dDhcpSnpRelayAgentInfoAllowGroup.setStatus("current")

dDhcpSnpDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 10)
)
dDhcpSnpDatabaseGroup.setObjects(
      *(("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpDatabaseUrl"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpDatabaseUpdateInterval"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpRenewDatabaseUrl"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpRenewValidateDbEnabled"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpRenewDatabase"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpDbLastSucceeded"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpDbLastFailed"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpClearDatabaseStatistics"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatBindingCollision"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatExpiredLease"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatInvalidInterfaces"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatUnsupportedVlans"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatParsingFailures"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStatChecksumErrors"))
)
if mibBuilder.loadTexts:
    dDhcpSnpDatabaseGroup.setStatus("current")

dDhcpSnpIfRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 11)
)
dDhcpSnpIfRateLimitGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfRateLimit")
)
if mibBuilder.loadTexts:
    dDhcpSnpIfRateLimitGroup.setStatus("current")

dDhcpSnpIfBindingsLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 2, 12)
)
dDhcpSnpIfBindingsLimitGroup.setObjects(
    ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfBindingsLimit")
)
if mibBuilder.loadTexts:
    dDhcpSnpIfBindingsLimitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcpSnpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 131, 2, 1, 1)
)
dDhcpSnpCompliance.setObjects(
      *(("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpGlobalEnableGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpVlanEnableGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfTrustGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBindingsClearGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpVerifyMacAddressGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpStationMoveGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpBootpBindGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpRelayAgentInfoAllowGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpDatabaseGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfRateLimitGroup"),
        ("DLINKSW-DHCP-SNOOPING-MIB", "dDhcpSnpIfBindingsLimitGroup"))
)
if mibBuilder.loadTexts:
    dDhcpSnpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP-SNOOPING-MIB",
    **{"dlinkSwDhcpSnpMIB": dlinkSwDhcpSnpMIB,
       "dDhcpSnpMIBNotifications": dDhcpSnpMIBNotifications,
       "dDhcpSnpMIBObjects": dDhcpSnpMIBObjects,
       "dDhcpSnpGlobalObjects": dDhcpSnpGlobalObjects,
       "dDhcpSnpGlobalEnabled": dDhcpSnpGlobalEnabled,
       "dDhcpSnpVerifyMacAddressEnabled": dDhcpSnpVerifyMacAddressEnabled,
       "dDhcpSnpStationMoveDenyEnabled": dDhcpSnpStationMoveDenyEnabled,
       "dDhcpSnpOption82AllowUntrust": dDhcpSnpOption82AllowUntrust,
       "dDhcpSnpBootpBindEnabled": dDhcpSnpBootpBindEnabled,
       "dDhcpSnpDatabaseObjects": dDhcpSnpDatabaseObjects,
       "dDhcpSnpDatabaseUrl": dDhcpSnpDatabaseUrl,
       "dDhcpSnpDatabaseUpdateInterval": dDhcpSnpDatabaseUpdateInterval,
       "dDhcpSnpRenewDatabaseUrl": dDhcpSnpRenewDatabaseUrl,
       "dDhcpSnpRenewValidateDbEnabled": dDhcpSnpRenewValidateDbEnabled,
       "dDhcpSnpRenewDatabase": dDhcpSnpRenewDatabase,
       "dDhcpSnpDbLastSucceeded": dDhcpSnpDbLastSucceeded,
       "dDhcpSnpDbLastFailed": dDhcpSnpDbLastFailed,
       "dDhcpSnpClearDatabaseStatistics": dDhcpSnpClearDatabaseStatistics,
       "dDhcpSnpDbLastIgnoredCounters": dDhcpSnpDbLastIgnoredCounters,
       "dDhcpSnpStatBindingCollision": dDhcpSnpStatBindingCollision,
       "dDhcpSnpStatExpiredLease": dDhcpSnpStatExpiredLease,
       "dDhcpSnpStatInvalidInterfaces": dDhcpSnpStatInvalidInterfaces,
       "dDhcpSnpStatUnsupportedVlans": dDhcpSnpStatUnsupportedVlans,
       "dDhcpSnpStatParsingFailures": dDhcpSnpStatParsingFailures,
       "dDhcpSnpStatChecksumErrors": dDhcpSnpStatChecksumErrors,
       "dDhcpSnpVlanObjects": dDhcpSnpVlanObjects,
       "dDhcpSnpVlanCrlFirst2K": dDhcpSnpVlanCrlFirst2K,
       "dDhcpSnpVlanCrlSecond2K": dDhcpSnpVlanCrlSecond2K,
       "dDhcpSnpIfObjects": dDhcpSnpIfObjects,
       "dDhcpSnpIfTrustTable": dDhcpSnpIfTrustTable,
       "dDhcpSnpIfTrustEntry": dDhcpSnpIfTrustEntry,
       "dDhcpSnpIfTrustEnabled": dDhcpSnpIfTrustEnabled,
       "dDhcpSnpIfRateLimitTable": dDhcpSnpIfRateLimitTable,
       "dDhcpSnpIfRateLimitEntry": dDhcpSnpIfRateLimitEntry,
       "dDhcpSnpIfRateLimit": dDhcpSnpIfRateLimit,
       "dDhcpSnpIfBindingsLimitTable": dDhcpSnpIfBindingsLimitTable,
       "dDhcpSnpIfBindingsLimitEntry": dDhcpSnpIfBindingsLimitEntry,
       "dDhcpSnpIfBindingsLimit": dDhcpSnpIfBindingsLimit,
       "dDhcpSnpBindingsObjects": dDhcpSnpBindingsObjects,
       "dDhcpSnpBindingsTable": dDhcpSnpBindingsTable,
       "dDhcpSnpBindingsEntry": dDhcpSnpBindingsEntry,
       "dDhcpSnpBindingsMacAddress": dDhcpSnpBindingsMacAddress,
       "dDhcpSnpBindingsVlan": dDhcpSnpBindingsVlan,
       "dDhcpSnpBindingsIpAddress": dDhcpSnpBindingsIpAddress,
       "dDhcpSnpBindingsInterface": dDhcpSnpBindingsInterface,
       "dDhcpSnpBindingsLeasedTime": dDhcpSnpBindingsLeasedTime,
       "dDhcpSnpBindingsStatus": dDhcpSnpBindingsStatus,
       "dDhcpSnpBindingsClearTable": dDhcpSnpBindingsClearTable,
       "dDhcpSnpBindingsClearEntry": dDhcpSnpBindingsClearEntry,
       "dDhcpSnpBindingsClearIndex": dDhcpSnpBindingsClearIndex,
       "dDhcpSnpBindingsClearByMacAddr": dDhcpSnpBindingsClearByMacAddr,
       "dDhcpSnpBindingsClearByVlan": dDhcpSnpBindingsClearByVlan,
       "dDhcpSnpBindingsClearByIpAddress": dDhcpSnpBindingsClearByIpAddress,
       "dDhcpSnpBindingsClearByInterface": dDhcpSnpBindingsClearByInterface,
       "dDhcpSnpBindingsClearStatus": dDhcpSnpBindingsClearStatus,
       "dDhcpSnpMIBConformance": dDhcpSnpMIBConformance,
       "dDhcpSnpCompliances": dDhcpSnpCompliances,
       "dDhcpSnpCompliance": dDhcpSnpCompliance,
       "dDhcpSnpGroups": dDhcpSnpGroups,
       "dDhcpSnpGlobalEnableGroup": dDhcpSnpGlobalEnableGroup,
       "dDhcpSnpVlanEnableGroup": dDhcpSnpVlanEnableGroup,
       "dDhcpSnpIfTrustGroup": dDhcpSnpIfTrustGroup,
       "dDhcpSnpBindingsGroup": dDhcpSnpBindingsGroup,
       "dDhcpSnpBindingsClearGroup": dDhcpSnpBindingsClearGroup,
       "dDhcpSnpVerifyMacAddressGroup": dDhcpSnpVerifyMacAddressGroup,
       "dDhcpSnpStationMoveGroup": dDhcpSnpStationMoveGroup,
       "dDhcpSnpBootpBindGroup": dDhcpSnpBootpBindGroup,
       "dDhcpSnpRelayAgentInfoAllowGroup": dDhcpSnpRelayAgentInfoAllowGroup,
       "dDhcpSnpDatabaseGroup": dDhcpSnpDatabaseGroup,
       "dDhcpSnpIfRateLimitGroup": dDhcpSnpIfRateLimitGroup,
       "dDhcpSnpIfBindingsLimitGroup": dDhcpSnpIfBindingsLimitGroup}
)
