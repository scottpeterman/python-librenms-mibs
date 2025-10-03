# SNMP MIB module (DLINKSW-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:51 2025
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

dlinkSwDhcpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39)
)
if mibBuilder.loadTexts:
    dlinkSwDhcpServerMIB.setRevisions(
        ("2013-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcpServerMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcpServerMIBNotifications = _DDhcpServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 0)
)
_DDhcpServerMIBObjects_ObjectIdentity = ObjectIdentity
dDhcpServerMIBObjects = _DDhcpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1)
)
_DDhcpServerGblCfg_ObjectIdentity = ObjectIdentity
dDhcpServerGblCfg = _DDhcpServerGblCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1)
)


class _DDhcpServiceEnabled_Type(TruthValue):
    """Custom type dDhcpServiceEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpServiceEnabled_Type.__name__ = "TruthValue"
_DDhcpServiceEnabled_Object = MibScalar
dDhcpServiceEnabled = _DDhcpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 1),
    _DDhcpServiceEnabled_Type()
)
dDhcpServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServiceEnabled.setStatus("current")


class _DDhcpServerPingPktNumber_Type(Unsigned32):
    """Custom type dDhcpServerPingPktNumber based on Unsigned32"""
    defaultValue = 2


_DDhcpServerPingPktNumber_Type.__name__ = "Unsigned32"
_DDhcpServerPingPktNumber_Object = MibScalar
dDhcpServerPingPktNumber = _DDhcpServerPingPktNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 2),
    _DDhcpServerPingPktNumber_Type()
)
dDhcpServerPingPktNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServerPingPktNumber.setStatus("current")


class _DDhcpServerPingTimeOut_Type(Unsigned32):
    """Custom type dDhcpServerPingTimeOut based on Unsigned32"""
    defaultValue = 500


_DDhcpServerPingTimeOut_Type.__name__ = "Unsigned32"
_DDhcpServerPingTimeOut_Object = MibScalar
dDhcpServerPingTimeOut = _DDhcpServerPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 3),
    _DDhcpServerPingTimeOut_Type()
)
dDhcpServerPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServerPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    dDhcpServerPingTimeOut.setUnits("milliseconds")
_DDhcpSExcludedAddressTable_Object = MibTable
dDhcpSExcludedAddressTable = _DDhcpSExcludedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressTable.setStatus("current")
_DDhcpSExcludedAddressEntry_Object = MibTableRow
dDhcpSExcludedAddressEntry = _DDhcpSExcludedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4, 1)
)
dDhcpSExcludedAddressEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSExcludedAddressVrfName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSExcludedAddressBeginAddr"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSExcludedAddressEndAddr"),
)
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressEntry.setStatus("current")


class _DDhcpSExcludedAddressVrfName_Type(DisplayString):
    """Custom type dDhcpSExcludedAddressVrfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpSExcludedAddressVrfName_Type.__name__ = "DisplayString"
_DDhcpSExcludedAddressVrfName_Object = MibTableColumn
dDhcpSExcludedAddressVrfName = _DDhcpSExcludedAddressVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4, 1, 1),
    _DDhcpSExcludedAddressVrfName_Type()
)
dDhcpSExcludedAddressVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressVrfName.setStatus("current")
_DDhcpSExcludedAddressBeginAddr_Type = IpAddress
_DDhcpSExcludedAddressBeginAddr_Object = MibTableColumn
dDhcpSExcludedAddressBeginAddr = _DDhcpSExcludedAddressBeginAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4, 1, 2),
    _DDhcpSExcludedAddressBeginAddr_Type()
)
dDhcpSExcludedAddressBeginAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressBeginAddr.setStatus("current")
_DDhcpSExcludedAddressEndAddr_Type = IpAddress
_DDhcpSExcludedAddressEndAddr_Object = MibTableColumn
dDhcpSExcludedAddressEndAddr = _DDhcpSExcludedAddressEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4, 1, 3),
    _DDhcpSExcludedAddressEndAddr_Type()
)
dDhcpSExcludedAddressEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressEndAddr.setStatus("current")
_DDhcpSExcludedAddressRowStatus_Type = RowStatus
_DDhcpSExcludedAddressRowStatus_Object = MibTableColumn
dDhcpSExcludedAddressRowStatus = _DDhcpSExcludedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 1, 4, 1, 99),
    _DDhcpSExcludedAddressRowStatus_Type()
)
dDhcpSExcludedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSExcludedAddressRowStatus.setStatus("current")
_DDhcpServerClass_ObjectIdentity = ObjectIdentity
dDhcpServerClass = _DDhcpServerClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2)
)
_DDhcpServerUseClassEnabled_Type = TruthValue
_DDhcpServerUseClassEnabled_Object = MibScalar
dDhcpServerUseClassEnabled = _DDhcpServerUseClassEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 1),
    _DDhcpServerUseClassEnabled_Type()
)
dDhcpServerUseClassEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServerUseClassEnabled.setStatus("current")
_DDhcpSClassTable_Object = MibTable
dDhcpSClassTable = _DDhcpSClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dDhcpSClassTable.setStatus("current")
_DDhcpSClassEntry_Object = MibTableRow
dDhcpSClassEntry = _DDhcpSClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 2, 1)
)
dDhcpSClassEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassName"),
)
if mibBuilder.loadTexts:
    dDhcpSClassEntry.setStatus("current")
_DDhcpSClassName_Type = DisplayString
_DDhcpSClassName_Object = MibTableColumn
dDhcpSClassName = _DDhcpSClassName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 2, 1, 1),
    _DDhcpSClassName_Type()
)
dDhcpSClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSClassName.setStatus("current")
_DDhcpSClassRowStatus_Type = RowStatus
_DDhcpSClassRowStatus_Object = MibTableColumn
dDhcpSClassRowStatus = _DDhcpSClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 2, 1, 99),
    _DDhcpSClassRowStatus_Type()
)
dDhcpSClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSClassRowStatus.setStatus("current")
_DDhcpSClassOptionTable_Object = MibTable
dDhcpSClassOptionTable = _DDhcpSClassOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dDhcpSClassOptionTable.setStatus("current")
_DDhcpSClassOptionEntry_Object = MibTableRow
dDhcpSClassOptionEntry = _DDhcpSClassOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1)
)
dDhcpSClassOptionEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassOptionCode"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassOptionPatternValue"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassOptionWildcardMatch"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassOptionMaskValue"),
)
if mibBuilder.loadTexts:
    dDhcpSClassOptionEntry.setStatus("current")


class _DDhcpSClassOptionCode_Type(Integer32):
    """Custom type dDhcpSClassOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DDhcpSClassOptionCode_Type.__name__ = "Integer32"
_DDhcpSClassOptionCode_Object = MibTableColumn
dDhcpSClassOptionCode = _DDhcpSClassOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1, 1),
    _DDhcpSClassOptionCode_Type()
)
dDhcpSClassOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSClassOptionCode.setStatus("current")
_DDhcpSClassOptionPatternValue_Type = OctetString
_DDhcpSClassOptionPatternValue_Object = MibTableColumn
dDhcpSClassOptionPatternValue = _DDhcpSClassOptionPatternValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1, 2),
    _DDhcpSClassOptionPatternValue_Type()
)
dDhcpSClassOptionPatternValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSClassOptionPatternValue.setStatus("current")
_DDhcpSClassOptionWildcardMatch_Type = TruthValue
_DDhcpSClassOptionWildcardMatch_Object = MibTableColumn
dDhcpSClassOptionWildcardMatch = _DDhcpSClassOptionWildcardMatch_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1, 3),
    _DDhcpSClassOptionWildcardMatch_Type()
)
dDhcpSClassOptionWildcardMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSClassOptionWildcardMatch.setStatus("current")
_DDhcpSClassOptionMaskValue_Type = OctetString
_DDhcpSClassOptionMaskValue_Object = MibTableColumn
dDhcpSClassOptionMaskValue = _DDhcpSClassOptionMaskValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1, 4),
    _DDhcpSClassOptionMaskValue_Type()
)
dDhcpSClassOptionMaskValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSClassOptionMaskValue.setStatus("current")
_DDhcpSClassOptionRowStatus_Type = RowStatus
_DDhcpSClassOptionRowStatus_Object = MibTableColumn
dDhcpSClassOptionRowStatus = _DDhcpSClassOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 2, 3, 1, 99),
    _DDhcpSClassOptionRowStatus_Type()
)
dDhcpSClassOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSClassOptionRowStatus.setStatus("current")
_DDhcpServerPoolMgmt_ObjectIdentity = ObjectIdentity
dDhcpServerPoolMgmt = _DDhcpServerPoolMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3)
)
_DDhcpSPoolTable_Object = MibTable
dDhcpSPoolTable = _DDhcpSPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDhcpSPoolTable.setStatus("current")
_DDhcpSPoolEntry_Object = MibTableRow
dDhcpSPoolEntry = _DDhcpSPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 1, 1)
)
dDhcpSPoolEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolEntry.setStatus("current")
_DDhcpSPoolName_Type = DisplayString
_DDhcpSPoolName_Object = MibTableColumn
dDhcpSPoolName = _DDhcpSPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 1, 1, 1),
    _DDhcpSPoolName_Type()
)
dDhcpSPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolName.setStatus("current")
_DDhcpSPoolRowStatus_Type = RowStatus
_DDhcpSPoolRowStatus_Object = MibTableColumn
dDhcpSPoolRowStatus = _DDhcpSPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 1, 1, 99),
    _DDhcpSPoolRowStatus_Type()
)
dDhcpSPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolRowStatus.setStatus("current")
_DDhcpSPoolCfgTable_Object = MibTable
dDhcpSPoolCfgTable = _DDhcpSPoolCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dDhcpSPoolCfgTable.setStatus("current")
_DDhcpSPoolCfgEntry_Object = MibTableRow
dDhcpSPoolCfgEntry = _DDhcpSPoolCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1)
)
dDhcpSPoolCfgEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolCfgEntry.setStatus("current")


class _DDhcpSPoolCfgDomainName_Type(DisplayString):
    """Custom type dDhcpSPoolCfgDomainName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DDhcpSPoolCfgDomainName_Type.__name__ = "DisplayString"
_DDhcpSPoolCfgDomainName_Object = MibTableColumn
dDhcpSPoolCfgDomainName = _DDhcpSPoolCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 1),
    _DDhcpSPoolCfgDomainName_Type()
)
dDhcpSPoolCfgDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgDomainName.setStatus("current")


class _DDhcpSPoolCfgNetBIOSNodeType_Type(Integer32):
    """Custom type dDhcpSPoolCfgNetBIOSNodeType based on Integer32"""
    defaultValue = 0

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
        *(("notSpecified", 0),
          ("broadcast", 1),
          ("peertopeer", 2),
          ("mixed", 3),
          ("hybid", 4))
    )


_DDhcpSPoolCfgNetBIOSNodeType_Type.__name__ = "Integer32"
_DDhcpSPoolCfgNetBIOSNodeType_Object = MibTableColumn
dDhcpSPoolCfgNetBIOSNodeType = _DDhcpSPoolCfgNetBIOSNodeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 2),
    _DDhcpSPoolCfgNetBIOSNodeType_Type()
)
dDhcpSPoolCfgNetBIOSNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgNetBIOSNodeType.setStatus("current")


class _DDhcpSPoolCfgLeaseState_Type(Integer32):
    """Custom type dDhcpSPoolCfgLeaseState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("predefined", 1),
          ("infinite", 2))
    )


_DDhcpSPoolCfgLeaseState_Type.__name__ = "Integer32"
_DDhcpSPoolCfgLeaseState_Object = MibTableColumn
dDhcpSPoolCfgLeaseState = _DDhcpSPoolCfgLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 3),
    _DDhcpSPoolCfgLeaseState_Type()
)
dDhcpSPoolCfgLeaseState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgLeaseState.setStatus("current")


class _DDhcpSPoolCfgLeaseDay_Type(Integer32):
    """Custom type dDhcpSPoolCfgLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_DDhcpSPoolCfgLeaseDay_Type.__name__ = "Integer32"
_DDhcpSPoolCfgLeaseDay_Object = MibTableColumn
dDhcpSPoolCfgLeaseDay = _DDhcpSPoolCfgLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 4),
    _DDhcpSPoolCfgLeaseDay_Type()
)
dDhcpSPoolCfgLeaseDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgLeaseDay.setStatus("current")


class _DDhcpSPoolCfgLeaseHour_Type(Integer32):
    """Custom type dDhcpSPoolCfgLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DDhcpSPoolCfgLeaseHour_Type.__name__ = "Integer32"
_DDhcpSPoolCfgLeaseHour_Object = MibTableColumn
dDhcpSPoolCfgLeaseHour = _DDhcpSPoolCfgLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 5),
    _DDhcpSPoolCfgLeaseHour_Type()
)
dDhcpSPoolCfgLeaseHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgLeaseHour.setStatus("current")


class _DDhcpSPoolCfgLeaseMinute_Type(Integer32):
    """Custom type dDhcpSPoolCfgLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DDhcpSPoolCfgLeaseMinute_Type.__name__ = "Integer32"
_DDhcpSPoolCfgLeaseMinute_Object = MibTableColumn
dDhcpSPoolCfgLeaseMinute = _DDhcpSPoolCfgLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 6),
    _DDhcpSPoolCfgLeaseMinute_Type()
)
dDhcpSPoolCfgLeaseMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgLeaseMinute.setStatus("current")


class _DDhcpSPoolCfgBootFile_Type(DisplayString):
    """Custom type dDhcpSPoolCfgBootFile based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DDhcpSPoolCfgBootFile_Type.__name__ = "DisplayString"
_DDhcpSPoolCfgBootFile_Object = MibTableColumn
dDhcpSPoolCfgBootFile = _DDhcpSPoolCfgBootFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 7),
    _DDhcpSPoolCfgBootFile_Type()
)
dDhcpSPoolCfgBootFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgBootFile.setStatus("current")
_DDhcpSPoolCfgNextServer_Type = IpAddress
_DDhcpSPoolCfgNextServer_Object = MibTableColumn
dDhcpSPoolCfgNextServer = _DDhcpSPoolCfgNextServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 8),
    _DDhcpSPoolCfgNextServer_Type()
)
dDhcpSPoolCfgNextServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgNextServer.setStatus("current")


class _DDhcpSPoolCfgVrfName_Type(DisplayString):
    """Custom type dDhcpSPoolCfgVrfName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpSPoolCfgVrfName_Type.__name__ = "DisplayString"
_DDhcpSPoolCfgVrfName_Object = MibTableColumn
dDhcpSPoolCfgVrfName = _DDhcpSPoolCfgVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 2, 1, 9),
    _DDhcpSPoolCfgVrfName_Type()
)
dDhcpSPoolCfgVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolCfgVrfName.setStatus("current")
_DDhcpSPoolAddrAllocTable_Object = MibTable
dDhcpSPoolAddrAllocTable = _DDhcpSPoolAddrAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dDhcpSPoolAddrAllocTable.setStatus("current")
_DDhcpSPoolAddrAllocEntry_Object = MibTableRow
dDhcpSPoolAddrAllocEntry = _DDhcpSPoolAddrAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 3, 1)
)
dDhcpSPoolAddrAllocEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolAddrAllocNetwork"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolAddrAllocEntry.setStatus("current")
_DDhcpSPoolAddrAllocNetwork_Type = IpAddress
_DDhcpSPoolAddrAllocNetwork_Object = MibTableColumn
dDhcpSPoolAddrAllocNetwork = _DDhcpSPoolAddrAllocNetwork_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 3, 1, 1),
    _DDhcpSPoolAddrAllocNetwork_Type()
)
dDhcpSPoolAddrAllocNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolAddrAllocNetwork.setStatus("current")
_DDhcpSPoolAddrAllocNetworkMask_Type = IpAddress
_DDhcpSPoolAddrAllocNetworkMask_Object = MibTableColumn
dDhcpSPoolAddrAllocNetworkMask = _DDhcpSPoolAddrAllocNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 3, 1, 2),
    _DDhcpSPoolAddrAllocNetworkMask_Type()
)
dDhcpSPoolAddrAllocNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolAddrAllocNetworkMask.setStatus("current")
_DDhcpSPoolAddrAllocRowStatus_Type = RowStatus
_DDhcpSPoolAddrAllocRowStatus_Object = MibTableColumn
dDhcpSPoolAddrAllocRowStatus = _DDhcpSPoolAddrAllocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 3, 1, 99),
    _DDhcpSPoolAddrAllocRowStatus_Type()
)
dDhcpSPoolAddrAllocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolAddrAllocRowStatus.setStatus("current")
_DDhcpSPoolManualBindTable_Object = MibTable
dDhcpSPoolManualBindTable = _DDhcpSPoolManualBindTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindTable.setStatus("current")
_DDhcpSPoolManualBindEntry_Object = MibTableRow
dDhcpSPoolManualBindEntry = _DDhcpSPoolManualBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1)
)
dDhcpSPoolManualBindEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindEntry.setStatus("current")
_DDhcpSPoolManualBindHostIp_Type = IpAddress
_DDhcpSPoolManualBindHostIp_Object = MibTableColumn
dDhcpSPoolManualBindHostIp = _DDhcpSPoolManualBindHostIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1, 1),
    _DDhcpSPoolManualBindHostIp_Type()
)
dDhcpSPoolManualBindHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindHostIp.setStatus("current")
_DDhcpSPoolManualBindHostIpMask_Type = IpAddress
_DDhcpSPoolManualBindHostIpMask_Object = MibTableColumn
dDhcpSPoolManualBindHostIpMask = _DDhcpSPoolManualBindHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1, 2),
    _DDhcpSPoolManualBindHostIpMask_Type()
)
dDhcpSPoolManualBindHostIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindHostIpMask.setStatus("current")
_DDhcpSPoolManualBindHAddr_Type = MacAddress
_DDhcpSPoolManualBindHAddr_Object = MibTableColumn
dDhcpSPoolManualBindHAddr = _DDhcpSPoolManualBindHAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1, 3),
    _DDhcpSPoolManualBindHAddr_Type()
)
dDhcpSPoolManualBindHAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindHAddr.setStatus("current")
_DDhcpSPoolManualBindClientId_Type = OctetString
_DDhcpSPoolManualBindClientId_Object = MibTableColumn
dDhcpSPoolManualBindClientId = _DDhcpSPoolManualBindClientId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1, 4),
    _DDhcpSPoolManualBindClientId_Type()
)
dDhcpSPoolManualBindClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindClientId.setStatus("current")
_DDhcpSPoolManualBindRowStatus_Type = RowStatus
_DDhcpSPoolManualBindRowStatus_Object = MibTableColumn
dDhcpSPoolManualBindRowStatus = _DDhcpSPoolManualBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 4, 1, 99),
    _DDhcpSPoolManualBindRowStatus_Type()
)
dDhcpSPoolManualBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindRowStatus.setStatus("current")
_DDhcpSPoolClassAddrTable_Object = MibTable
dDhcpSPoolClassAddrTable = _DDhcpSPoolClassAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dDhcpSPoolClassAddrTable.setStatus("current")
_DDhcpSPoolClassAddrEntry_Object = MibTableRow
dDhcpSPoolClassAddrEntry = _DDhcpSPoolClassAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 5, 1)
)
dDhcpSPoolClassAddrEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolClassAddrBeginAddr"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolClassAddrEndAddr"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolClassAddrEntry.setStatus("current")
_DDhcpSPoolClassAddrBeginAddr_Type = IpAddress
_DDhcpSPoolClassAddrBeginAddr_Object = MibTableColumn
dDhcpSPoolClassAddrBeginAddr = _DDhcpSPoolClassAddrBeginAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 5, 1, 1),
    _DDhcpSPoolClassAddrBeginAddr_Type()
)
dDhcpSPoolClassAddrBeginAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolClassAddrBeginAddr.setStatus("current")
_DDhcpSPoolClassAddrEndAddr_Type = IpAddress
_DDhcpSPoolClassAddrEndAddr_Object = MibTableColumn
dDhcpSPoolClassAddrEndAddr = _DDhcpSPoolClassAddrEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 5, 1, 2),
    _DDhcpSPoolClassAddrEndAddr_Type()
)
dDhcpSPoolClassAddrEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolClassAddrEndAddr.setStatus("current")
_DDhcpSPoolClassAddrRowStatus_Type = RowStatus
_DDhcpSPoolClassAddrRowStatus_Object = MibTableColumn
dDhcpSPoolClassAddrRowStatus = _DDhcpSPoolClassAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 5, 1, 99),
    _DDhcpSPoolClassAddrRowStatus_Type()
)
dDhcpSPoolClassAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolClassAddrRowStatus.setStatus("current")
_DDhcpSPoolOptionTable_Object = MibTable
dDhcpSPoolOptionTable = _DDhcpSPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6)
)
if mibBuilder.loadTexts:
    dDhcpSPoolOptionTable.setStatus("current")
_DDhcpSPoolOptionEntry_Object = MibTableRow
dDhcpSPoolOptionEntry = _DDhcpSPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6, 1)
)
dDhcpSPoolOptionEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolOptionCode"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolOptionEntry.setStatus("current")


class _DDhcpSPoolOptionCode_Type(Integer32):
    """Custom type dDhcpSPoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_DDhcpSPoolOptionCode_Type.__name__ = "Integer32"
_DDhcpSPoolOptionCode_Object = MibTableColumn
dDhcpSPoolOptionCode = _DDhcpSPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6, 1, 1),
    _DDhcpSPoolOptionCode_Type()
)
dDhcpSPoolOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolOptionCode.setStatus("current")


class _DDhcpSPoolOptionType_Type(Integer32):
    """Custom type dDhcpSPoolOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2),
          ("ip", 3))
    )


_DDhcpSPoolOptionType_Type.__name__ = "Integer32"
_DDhcpSPoolOptionType_Object = MibTableColumn
dDhcpSPoolOptionType = _DDhcpSPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6, 1, 2),
    _DDhcpSPoolOptionType_Type()
)
dDhcpSPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolOptionType.setStatus("current")
_DDhcpSPoolOptionValue_Type = DisplayString
_DDhcpSPoolOptionValue_Object = MibTableColumn
dDhcpSPoolOptionValue = _DDhcpSPoolOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6, 1, 3),
    _DDhcpSPoolOptionValue_Type()
)
dDhcpSPoolOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolOptionValue.setStatus("current")
_DDhcpSPoolOptionRowStatus_Type = RowStatus
_DDhcpSPoolOptionRowStatus_Object = MibTableColumn
dDhcpSPoolOptionRowStatus = _DDhcpSPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 6, 1, 99),
    _DDhcpSPoolOptionRowStatus_Type()
)
dDhcpSPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolOptionRowStatus.setStatus("current")
_DDhcpSPoolDefaultRouterTable_Object = MibTable
dDhcpSPoolDefaultRouterTable = _DDhcpSPoolDefaultRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 7)
)
if mibBuilder.loadTexts:
    dDhcpSPoolDefaultRouterTable.setStatus("current")
_DDhcpSPoolDefaultRouterEntry_Object = MibTableRow
dDhcpSPoolDefaultRouterEntry = _DDhcpSPoolDefaultRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 7, 1)
)
dDhcpSPoolDefaultRouterEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDefaultRouterIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolDefaultRouterEntry.setStatus("current")


class _DDhcpSPoolDefaultRouterIndex_Type(Unsigned32):
    """Custom type dDhcpSPoolDefaultRouterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DDhcpSPoolDefaultRouterIndex_Type.__name__ = "Unsigned32"
_DDhcpSPoolDefaultRouterIndex_Object = MibTableColumn
dDhcpSPoolDefaultRouterIndex = _DDhcpSPoolDefaultRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 7, 1, 1),
    _DDhcpSPoolDefaultRouterIndex_Type()
)
dDhcpSPoolDefaultRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolDefaultRouterIndex.setStatus("current")
_DDhcpSPoolDefaultRouterAddr_Type = IpAddress
_DDhcpSPoolDefaultRouterAddr_Object = MibTableColumn
dDhcpSPoolDefaultRouterAddr = _DDhcpSPoolDefaultRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 7, 1, 2),
    _DDhcpSPoolDefaultRouterAddr_Type()
)
dDhcpSPoolDefaultRouterAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolDefaultRouterAddr.setStatus("current")
_DDhcpSPoolDefaultRouterRowStatus_Type = RowStatus
_DDhcpSPoolDefaultRouterRowStatus_Object = MibTableColumn
dDhcpSPoolDefaultRouterRowStatus = _DDhcpSPoolDefaultRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 7, 1, 99),
    _DDhcpSPoolDefaultRouterRowStatus_Type()
)
dDhcpSPoolDefaultRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolDefaultRouterRowStatus.setStatus("current")
_DDhcpSPoolDnsServerTable_Object = MibTable
dDhcpSPoolDnsServerTable = _DDhcpSPoolDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 8)
)
if mibBuilder.loadTexts:
    dDhcpSPoolDnsServerTable.setStatus("current")
_DDhcpSPoolDnsServerEntry_Object = MibTableRow
dDhcpSPoolDnsServerEntry = _DDhcpSPoolDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 8, 1)
)
dDhcpSPoolDnsServerEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDnsServerIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolDnsServerEntry.setStatus("current")


class _DDhcpSPoolDnsServerIndex_Type(Unsigned32):
    """Custom type dDhcpSPoolDnsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DDhcpSPoolDnsServerIndex_Type.__name__ = "Unsigned32"
_DDhcpSPoolDnsServerIndex_Object = MibTableColumn
dDhcpSPoolDnsServerIndex = _DDhcpSPoolDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 8, 1, 1),
    _DDhcpSPoolDnsServerIndex_Type()
)
dDhcpSPoolDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolDnsServerIndex.setStatus("current")
_DDhcpSPoolDnsServerAddr_Type = IpAddress
_DDhcpSPoolDnsServerAddr_Object = MibTableColumn
dDhcpSPoolDnsServerAddr = _DDhcpSPoolDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 8, 1, 2),
    _DDhcpSPoolDnsServerAddr_Type()
)
dDhcpSPoolDnsServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolDnsServerAddr.setStatus("current")
_DDhcpSPoolDnsServerRowStatus_Type = RowStatus
_DDhcpSPoolDnsServerRowStatus_Object = MibTableColumn
dDhcpSPoolDnsServerRowStatus = _DDhcpSPoolDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 8, 1, 99),
    _DDhcpSPoolDnsServerRowStatus_Type()
)
dDhcpSPoolDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolDnsServerRowStatus.setStatus("current")
_DDhcpSPoolWinsServerTable_Object = MibTable
dDhcpSPoolWinsServerTable = _DDhcpSPoolWinsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 9)
)
if mibBuilder.loadTexts:
    dDhcpSPoolWinsServerTable.setStatus("current")
_DDhcpSPoolWinsServerEntry_Object = MibTableRow
dDhcpSPoolWinsServerEntry = _DDhcpSPoolWinsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 9, 1)
)
dDhcpSPoolWinsServerEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolWinsServerIndex"),
)
if mibBuilder.loadTexts:
    dDhcpSPoolWinsServerEntry.setStatus("current")


class _DDhcpSPoolWinsServerIndex_Type(Unsigned32):
    """Custom type dDhcpSPoolWinsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DDhcpSPoolWinsServerIndex_Type.__name__ = "Unsigned32"
_DDhcpSPoolWinsServerIndex_Object = MibTableColumn
dDhcpSPoolWinsServerIndex = _DDhcpSPoolWinsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 9, 1, 1),
    _DDhcpSPoolWinsServerIndex_Type()
)
dDhcpSPoolWinsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSPoolWinsServerIndex.setStatus("current")
_DDhcpSPoolWinsServerAddr_Type = IpAddress
_DDhcpSPoolWinsServerAddr_Object = MibTableColumn
dDhcpSPoolWinsServerAddr = _DDhcpSPoolWinsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 9, 1, 2),
    _DDhcpSPoolWinsServerAddr_Type()
)
dDhcpSPoolWinsServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolWinsServerAddr.setStatus("current")
_DDhcpSPoolWinsServerRowStatus_Type = RowStatus
_DDhcpSPoolWinsServerRowStatus_Object = MibTableColumn
dDhcpSPoolWinsServerRowStatus = _DDhcpSPoolWinsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 3, 9, 1, 99),
    _DDhcpSPoolWinsServerRowStatus_Type()
)
dDhcpSPoolWinsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpSPoolWinsServerRowStatus.setStatus("current")
_DDhcpServerInfo_ObjectIdentity = ObjectIdentity
dDhcpServerInfo = _DDhcpServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4)
)
_DDhcpServerPktStatistics_ObjectIdentity = ObjectIdentity
dDhcpServerPktStatistics = _DDhcpServerPktStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1)
)


class _DDhcpServerClearStatistics_Type(Integer32):
    """Custom type dDhcpServerClearStatistics based on Integer32"""
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


_DDhcpServerClearStatistics_Type.__name__ = "Integer32"
_DDhcpServerClearStatistics_Object = MibScalar
dDhcpServerClearStatistics = _DDhcpServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 1),
    _DDhcpServerClearStatistics_Type()
)
dDhcpServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServerClearStatistics.setStatus("current")
_DDhcpServerRecvBootRequest_Type = Counter64
_DDhcpServerRecvBootRequest_Object = MibScalar
dDhcpServerRecvBootRequest = _DDhcpServerRecvBootRequest_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 2),
    _DDhcpServerRecvBootRequest_Type()
)
dDhcpServerRecvBootRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvBootRequest.setStatus("current")
_DDhcpServerRecvMalformedPkt_Type = Counter64
_DDhcpServerRecvMalformedPkt_Object = MibScalar
dDhcpServerRecvMalformedPkt = _DDhcpServerRecvMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 3),
    _DDhcpServerRecvMalformedPkt_Type()
)
dDhcpServerRecvMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvMalformedPkt.setStatus("current")
_DDhcpServerRecvRenewPkt_Type = Counter64
_DDhcpServerRecvRenewPkt_Object = MibScalar
dDhcpServerRecvRenewPkt = _DDhcpServerRecvRenewPkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 4),
    _DDhcpServerRecvRenewPkt_Type()
)
dDhcpServerRecvRenewPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvRenewPkt.setStatus("current")
_DDhcpServerRecvDiscover_Type = Counter64
_DDhcpServerRecvDiscover_Object = MibScalar
dDhcpServerRecvDiscover = _DDhcpServerRecvDiscover_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 5),
    _DDhcpServerRecvDiscover_Type()
)
dDhcpServerRecvDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvDiscover.setStatus("current")
_DDhcpServerRecvRequest_Type = Counter64
_DDhcpServerRecvRequest_Object = MibScalar
dDhcpServerRecvRequest = _DDhcpServerRecvRequest_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 6),
    _DDhcpServerRecvRequest_Type()
)
dDhcpServerRecvRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvRequest.setStatus("current")
_DDhcpServerRecvDecline_Type = Counter64
_DDhcpServerRecvDecline_Object = MibScalar
dDhcpServerRecvDecline = _DDhcpServerRecvDecline_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 7),
    _DDhcpServerRecvDecline_Type()
)
dDhcpServerRecvDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvDecline.setStatus("current")
_DDhcpServerRecvRelease_Type = Counter64
_DDhcpServerRecvRelease_Object = MibScalar
dDhcpServerRecvRelease = _DDhcpServerRecvRelease_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 8),
    _DDhcpServerRecvRelease_Type()
)
dDhcpServerRecvRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvRelease.setStatus("current")
_DDhcpServerRecvInform_Type = Counter64
_DDhcpServerRecvInform_Object = MibScalar
dDhcpServerRecvInform = _DDhcpServerRecvInform_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 9),
    _DDhcpServerRecvInform_Type()
)
dDhcpServerRecvInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerRecvInform.setStatus("current")
_DDhcpServerSendBootReply_Type = Counter64
_DDhcpServerSendBootReply_Object = MibScalar
dDhcpServerSendBootReply = _DDhcpServerSendBootReply_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 10),
    _DDhcpServerSendBootReply_Type()
)
dDhcpServerSendBootReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerSendBootReply.setStatus("current")
_DDhcpServerSendOffer_Type = Counter64
_DDhcpServerSendOffer_Object = MibScalar
dDhcpServerSendOffer = _DDhcpServerSendOffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 11),
    _DDhcpServerSendOffer_Type()
)
dDhcpServerSendOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerSendOffer.setStatus("current")
_DDhcpServerSendAck_Type = Counter64
_DDhcpServerSendAck_Object = MibScalar
dDhcpServerSendAck = _DDhcpServerSendAck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 12),
    _DDhcpServerSendAck_Type()
)
dDhcpServerSendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerSendAck.setStatus("current")
_DDhcpServerSendNak_Type = Counter64
_DDhcpServerSendNak_Object = MibScalar
dDhcpServerSendNak = _DDhcpServerSendNak_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 1, 13),
    _DDhcpServerSendNak_Type()
)
dDhcpServerSendNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerSendNak.setStatus("current")
_DDhcpServerBindingTable_Object = MibTable
dDhcpServerBindingTable = _DDhcpServerBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dDhcpServerBindingTable.setStatus("current")
_DDhcpServerBindingEntry_Object = MibTableRow
dDhcpServerBindingEntry = _DDhcpServerBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1)
)
dDhcpServerBindingEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpServerBindingVrfName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpServerBindingIpAddress"),
)
if mibBuilder.loadTexts:
    dDhcpServerBindingEntry.setStatus("current")


class _DDhcpServerBindingVrfName_Type(DisplayString):
    """Custom type dDhcpServerBindingVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpServerBindingVrfName_Type.__name__ = "DisplayString"
_DDhcpServerBindingVrfName_Object = MibTableColumn
dDhcpServerBindingVrfName = _DDhcpServerBindingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 1),
    _DDhcpServerBindingVrfName_Type()
)
dDhcpServerBindingVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpServerBindingVrfName.setStatus("current")
_DDhcpServerBindingIpAddress_Type = IpAddress
_DDhcpServerBindingIpAddress_Object = MibTableColumn
dDhcpServerBindingIpAddress = _DDhcpServerBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 2),
    _DDhcpServerBindingIpAddress_Type()
)
dDhcpServerBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpServerBindingIpAddress.setStatus("current")
_DDhcpSBindingHwAddrOrClientId_Type = OctetString
_DDhcpSBindingHwAddrOrClientId_Object = MibTableColumn
dDhcpSBindingHwAddrOrClientId = _DDhcpSBindingHwAddrOrClientId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 3),
    _DDhcpSBindingHwAddrOrClientId_Type()
)
dDhcpSBindingHwAddrOrClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSBindingHwAddrOrClientId.setStatus("current")


class _DDhcpServerBindingState_Type(Integer32):
    """Custom type dDhcpServerBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2),
          ("offering", 3),
          ("bootp", 4))
    )


_DDhcpServerBindingState_Type.__name__ = "Integer32"
_DDhcpServerBindingState_Object = MibTableColumn
dDhcpServerBindingState = _DDhcpServerBindingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 4),
    _DDhcpServerBindingState_Type()
)
dDhcpServerBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerBindingState.setStatus("current")
_DDhcpServerBindingLeaseExpire_Type = DateAndTime
_DDhcpServerBindingLeaseExpire_Object = MibTableColumn
dDhcpServerBindingLeaseExpire = _DDhcpServerBindingLeaseExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 5),
    _DDhcpServerBindingLeaseExpire_Type()
)
dDhcpServerBindingLeaseExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpServerBindingLeaseExpire.setStatus("current")


class _DDhcpServerBindingClear_Type(Integer32):
    """Custom type dDhcpServerBindingClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("clear", 2))
    )


_DDhcpServerBindingClear_Type.__name__ = "Integer32"
_DDhcpServerBindingClear_Object = MibTableColumn
dDhcpServerBindingClear = _DDhcpServerBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 2, 1, 6),
    _DDhcpServerBindingClear_Type()
)
dDhcpServerBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpServerBindingClear.setStatus("current")
_DDhcpSConflictIpTable_Object = MibTable
dDhcpSConflictIpTable = _DDhcpSConflictIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dDhcpSConflictIpTable.setStatus("current")
_DDhcpSConflictIpEntry_Object = MibTableRow
dDhcpSConflictIpEntry = _DDhcpSConflictIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1)
)
dDhcpSConflictIpEntry.setIndexNames(
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSConflictIpVrfName"),
    (0, "DLINKSW-DHCP-SERVER-MIB", "dDhcpSConflictIpAddr"),
)
if mibBuilder.loadTexts:
    dDhcpSConflictIpEntry.setStatus("current")


class _DDhcpSConflictIpVrfName_Type(DisplayString):
    """Custom type dDhcpSConflictIpVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpSConflictIpVrfName_Type.__name__ = "DisplayString"
_DDhcpSConflictIpVrfName_Object = MibTableColumn
dDhcpSConflictIpVrfName = _DDhcpSConflictIpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1, 1),
    _DDhcpSConflictIpVrfName_Type()
)
dDhcpSConflictIpVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSConflictIpVrfName.setStatus("current")
_DDhcpSConflictIpAddr_Type = IpAddress
_DDhcpSConflictIpAddr_Object = MibTableColumn
dDhcpSConflictIpAddr = _DDhcpSConflictIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1, 2),
    _DDhcpSConflictIpAddr_Type()
)
dDhcpSConflictIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpSConflictIpAddr.setStatus("current")


class _DDhcpSConflictIpDetectMethod_Type(Integer32):
    """Custom type dDhcpSConflictIpDetectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ping", 1),
          ("gratuitousArp", 2))
    )


_DDhcpSConflictIpDetectMethod_Type.__name__ = "Integer32"
_DDhcpSConflictIpDetectMethod_Object = MibTableColumn
dDhcpSConflictIpDetectMethod = _DDhcpSConflictIpDetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1, 3),
    _DDhcpSConflictIpDetectMethod_Type()
)
dDhcpSConflictIpDetectMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSConflictIpDetectMethod.setStatus("current")
_DDhcpSConflictIpDetectTime_Type = DateAndTime
_DDhcpSConflictIpDetectTime_Object = MibTableColumn
dDhcpSConflictIpDetectTime = _DDhcpSConflictIpDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1, 4),
    _DDhcpSConflictIpDetectTime_Type()
)
dDhcpSConflictIpDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpSConflictIpDetectTime.setStatus("current")


class _DDhcpSConflictIpClear_Type(Integer32):
    """Custom type dDhcpSConflictIpClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("clear", 2))
    )


_DDhcpSConflictIpClear_Type.__name__ = "Integer32"
_DDhcpSConflictIpClear_Object = MibTableColumn
dDhcpSConflictIpClear = _DDhcpSConflictIpClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 1, 4, 3, 1, 5),
    _DDhcpSConflictIpClear_Type()
)
dDhcpSConflictIpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpSConflictIpClear.setStatus("current")
_DDhcpServerMIBConformance_ObjectIdentity = ObjectIdentity
dDhcpServerMIBConformance = _DDhcpServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2)
)
_DDhcpServerCompliances_ObjectIdentity = ObjectIdentity
dDhcpServerCompliances = _DDhcpServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 1)
)
_DDhcpServerGroups_ObjectIdentity = ObjectIdentity
dDhcpServerGroups = _DDhcpServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2)
)

# Managed Objects groups

dDhcpSGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 1)
)
dDhcpSGblCfgGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpServiceEnabled"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerPingTimeOut"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerPingPktNumber"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSExcludedAddressRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSGblCfgGroup.setStatus("current")

dDhcpSClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 2)
)
dDhcpSClassGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerUseClassEnabled"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSClassGroup.setStatus("current")

dDhcpSClassCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 3)
)
dDhcpSClassCfgGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassOptionRowStatus"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolClassAddrRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSClassCfgGroup.setStatus("current")

dDhcpSPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 4)
)
dDhcpSPoolGroup.setObjects(
    ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolRowStatus")
)
if mibBuilder.loadTexts:
    dDhcpSPoolGroup.setStatus("current")

dDhcpSPoolCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 5)
)
dDhcpSPoolCfgGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgDomainName"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgNetBIOSNodeType"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgLeaseState"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgLeaseDay"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgLeaseHour"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgLeaseMinute"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgBootFile"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgNextServer"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgVrfName"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolOptionType"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolOptionValue"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolOptionRowStatus"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDefaultRouterAddr"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDefaultRouterRowStatus"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDnsServerAddr"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolDnsServerRowStatus"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolWinsServerAddr"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolWinsServerRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSPoolCfgGroup.setStatus("current")

dDhcpSPoolNetworkCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 6)
)
dDhcpSPoolNetworkCfgGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolAddrAllocNetworkMask"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolAddrAllocRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSPoolNetworkCfgGroup.setStatus("current")

dDhcpSPoolManualBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 7)
)
dDhcpSPoolManualBindingGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindHostIp"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindHostIpMask"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindHAddr"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindClientId"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpSPoolManualBindingGroup.setStatus("current")

dDhcpSStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 8)
)
dDhcpSStatisticsGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerClearStatistics"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvBootRequest"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvMalformedPkt"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvRenewPkt"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvDiscover"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvRequest"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvDecline"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvRelease"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerRecvInform"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerSendBootReply"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerSendOffer"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerSendAck"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerSendNak"))
)
if mibBuilder.loadTexts:
    dDhcpSStatisticsGroup.setStatus("current")

dDhcpSGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 2, 9)
)
dDhcpSGeneralInfoGroup.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSBindingHwAddrOrClientId"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerBindingState"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerBindingLeaseExpire"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpServerBindingClear"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSConflictIpDetectMethod"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSConflictIpDetectTime"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSConflictIpClear"))
)
if mibBuilder.loadTexts:
    dDhcpSGeneralInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcpServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 39, 2, 1, 1)
)
dDhcpServerCompliance.setObjects(
      *(("DLINKSW-DHCP-SERVER-MIB", "dDhcpSGblCfgGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSClassCfgGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolCfgGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolNetworkCfgGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSPoolManualBindingGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSStatisticsGroup"),
        ("DLINKSW-DHCP-SERVER-MIB", "dDhcpSGeneralInfoGroup"))
)
if mibBuilder.loadTexts:
    dDhcpServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP-SERVER-MIB",
    **{"dlinkSwDhcpServerMIB": dlinkSwDhcpServerMIB,
       "dDhcpServerMIBNotifications": dDhcpServerMIBNotifications,
       "dDhcpServerMIBObjects": dDhcpServerMIBObjects,
       "dDhcpServerGblCfg": dDhcpServerGblCfg,
       "dDhcpServiceEnabled": dDhcpServiceEnabled,
       "dDhcpServerPingPktNumber": dDhcpServerPingPktNumber,
       "dDhcpServerPingTimeOut": dDhcpServerPingTimeOut,
       "dDhcpSExcludedAddressTable": dDhcpSExcludedAddressTable,
       "dDhcpSExcludedAddressEntry": dDhcpSExcludedAddressEntry,
       "dDhcpSExcludedAddressVrfName": dDhcpSExcludedAddressVrfName,
       "dDhcpSExcludedAddressBeginAddr": dDhcpSExcludedAddressBeginAddr,
       "dDhcpSExcludedAddressEndAddr": dDhcpSExcludedAddressEndAddr,
       "dDhcpSExcludedAddressRowStatus": dDhcpSExcludedAddressRowStatus,
       "dDhcpServerClass": dDhcpServerClass,
       "dDhcpServerUseClassEnabled": dDhcpServerUseClassEnabled,
       "dDhcpSClassTable": dDhcpSClassTable,
       "dDhcpSClassEntry": dDhcpSClassEntry,
       "dDhcpSClassName": dDhcpSClassName,
       "dDhcpSClassRowStatus": dDhcpSClassRowStatus,
       "dDhcpSClassOptionTable": dDhcpSClassOptionTable,
       "dDhcpSClassOptionEntry": dDhcpSClassOptionEntry,
       "dDhcpSClassOptionCode": dDhcpSClassOptionCode,
       "dDhcpSClassOptionPatternValue": dDhcpSClassOptionPatternValue,
       "dDhcpSClassOptionWildcardMatch": dDhcpSClassOptionWildcardMatch,
       "dDhcpSClassOptionMaskValue": dDhcpSClassOptionMaskValue,
       "dDhcpSClassOptionRowStatus": dDhcpSClassOptionRowStatus,
       "dDhcpServerPoolMgmt": dDhcpServerPoolMgmt,
       "dDhcpSPoolTable": dDhcpSPoolTable,
       "dDhcpSPoolEntry": dDhcpSPoolEntry,
       "dDhcpSPoolName": dDhcpSPoolName,
       "dDhcpSPoolRowStatus": dDhcpSPoolRowStatus,
       "dDhcpSPoolCfgTable": dDhcpSPoolCfgTable,
       "dDhcpSPoolCfgEntry": dDhcpSPoolCfgEntry,
       "dDhcpSPoolCfgDomainName": dDhcpSPoolCfgDomainName,
       "dDhcpSPoolCfgNetBIOSNodeType": dDhcpSPoolCfgNetBIOSNodeType,
       "dDhcpSPoolCfgLeaseState": dDhcpSPoolCfgLeaseState,
       "dDhcpSPoolCfgLeaseDay": dDhcpSPoolCfgLeaseDay,
       "dDhcpSPoolCfgLeaseHour": dDhcpSPoolCfgLeaseHour,
       "dDhcpSPoolCfgLeaseMinute": dDhcpSPoolCfgLeaseMinute,
       "dDhcpSPoolCfgBootFile": dDhcpSPoolCfgBootFile,
       "dDhcpSPoolCfgNextServer": dDhcpSPoolCfgNextServer,
       "dDhcpSPoolCfgVrfName": dDhcpSPoolCfgVrfName,
       "dDhcpSPoolAddrAllocTable": dDhcpSPoolAddrAllocTable,
       "dDhcpSPoolAddrAllocEntry": dDhcpSPoolAddrAllocEntry,
       "dDhcpSPoolAddrAllocNetwork": dDhcpSPoolAddrAllocNetwork,
       "dDhcpSPoolAddrAllocNetworkMask": dDhcpSPoolAddrAllocNetworkMask,
       "dDhcpSPoolAddrAllocRowStatus": dDhcpSPoolAddrAllocRowStatus,
       "dDhcpSPoolManualBindTable": dDhcpSPoolManualBindTable,
       "dDhcpSPoolManualBindEntry": dDhcpSPoolManualBindEntry,
       "dDhcpSPoolManualBindHostIp": dDhcpSPoolManualBindHostIp,
       "dDhcpSPoolManualBindHostIpMask": dDhcpSPoolManualBindHostIpMask,
       "dDhcpSPoolManualBindHAddr": dDhcpSPoolManualBindHAddr,
       "dDhcpSPoolManualBindClientId": dDhcpSPoolManualBindClientId,
       "dDhcpSPoolManualBindRowStatus": dDhcpSPoolManualBindRowStatus,
       "dDhcpSPoolClassAddrTable": dDhcpSPoolClassAddrTable,
       "dDhcpSPoolClassAddrEntry": dDhcpSPoolClassAddrEntry,
       "dDhcpSPoolClassAddrBeginAddr": dDhcpSPoolClassAddrBeginAddr,
       "dDhcpSPoolClassAddrEndAddr": dDhcpSPoolClassAddrEndAddr,
       "dDhcpSPoolClassAddrRowStatus": dDhcpSPoolClassAddrRowStatus,
       "dDhcpSPoolOptionTable": dDhcpSPoolOptionTable,
       "dDhcpSPoolOptionEntry": dDhcpSPoolOptionEntry,
       "dDhcpSPoolOptionCode": dDhcpSPoolOptionCode,
       "dDhcpSPoolOptionType": dDhcpSPoolOptionType,
       "dDhcpSPoolOptionValue": dDhcpSPoolOptionValue,
       "dDhcpSPoolOptionRowStatus": dDhcpSPoolOptionRowStatus,
       "dDhcpSPoolDefaultRouterTable": dDhcpSPoolDefaultRouterTable,
       "dDhcpSPoolDefaultRouterEntry": dDhcpSPoolDefaultRouterEntry,
       "dDhcpSPoolDefaultRouterIndex": dDhcpSPoolDefaultRouterIndex,
       "dDhcpSPoolDefaultRouterAddr": dDhcpSPoolDefaultRouterAddr,
       "dDhcpSPoolDefaultRouterRowStatus": dDhcpSPoolDefaultRouterRowStatus,
       "dDhcpSPoolDnsServerTable": dDhcpSPoolDnsServerTable,
       "dDhcpSPoolDnsServerEntry": dDhcpSPoolDnsServerEntry,
       "dDhcpSPoolDnsServerIndex": dDhcpSPoolDnsServerIndex,
       "dDhcpSPoolDnsServerAddr": dDhcpSPoolDnsServerAddr,
       "dDhcpSPoolDnsServerRowStatus": dDhcpSPoolDnsServerRowStatus,
       "dDhcpSPoolWinsServerTable": dDhcpSPoolWinsServerTable,
       "dDhcpSPoolWinsServerEntry": dDhcpSPoolWinsServerEntry,
       "dDhcpSPoolWinsServerIndex": dDhcpSPoolWinsServerIndex,
       "dDhcpSPoolWinsServerAddr": dDhcpSPoolWinsServerAddr,
       "dDhcpSPoolWinsServerRowStatus": dDhcpSPoolWinsServerRowStatus,
       "dDhcpServerInfo": dDhcpServerInfo,
       "dDhcpServerPktStatistics": dDhcpServerPktStatistics,
       "dDhcpServerClearStatistics": dDhcpServerClearStatistics,
       "dDhcpServerRecvBootRequest": dDhcpServerRecvBootRequest,
       "dDhcpServerRecvMalformedPkt": dDhcpServerRecvMalformedPkt,
       "dDhcpServerRecvRenewPkt": dDhcpServerRecvRenewPkt,
       "dDhcpServerRecvDiscover": dDhcpServerRecvDiscover,
       "dDhcpServerRecvRequest": dDhcpServerRecvRequest,
       "dDhcpServerRecvDecline": dDhcpServerRecvDecline,
       "dDhcpServerRecvRelease": dDhcpServerRecvRelease,
       "dDhcpServerRecvInform": dDhcpServerRecvInform,
       "dDhcpServerSendBootReply": dDhcpServerSendBootReply,
       "dDhcpServerSendOffer": dDhcpServerSendOffer,
       "dDhcpServerSendAck": dDhcpServerSendAck,
       "dDhcpServerSendNak": dDhcpServerSendNak,
       "dDhcpServerBindingTable": dDhcpServerBindingTable,
       "dDhcpServerBindingEntry": dDhcpServerBindingEntry,
       "dDhcpServerBindingVrfName": dDhcpServerBindingVrfName,
       "dDhcpServerBindingIpAddress": dDhcpServerBindingIpAddress,
       "dDhcpSBindingHwAddrOrClientId": dDhcpSBindingHwAddrOrClientId,
       "dDhcpServerBindingState": dDhcpServerBindingState,
       "dDhcpServerBindingLeaseExpire": dDhcpServerBindingLeaseExpire,
       "dDhcpServerBindingClear": dDhcpServerBindingClear,
       "dDhcpSConflictIpTable": dDhcpSConflictIpTable,
       "dDhcpSConflictIpEntry": dDhcpSConflictIpEntry,
       "dDhcpSConflictIpVrfName": dDhcpSConflictIpVrfName,
       "dDhcpSConflictIpAddr": dDhcpSConflictIpAddr,
       "dDhcpSConflictIpDetectMethod": dDhcpSConflictIpDetectMethod,
       "dDhcpSConflictIpDetectTime": dDhcpSConflictIpDetectTime,
       "dDhcpSConflictIpClear": dDhcpSConflictIpClear,
       "dDhcpServerMIBConformance": dDhcpServerMIBConformance,
       "dDhcpServerCompliances": dDhcpServerCompliances,
       "dDhcpServerCompliance": dDhcpServerCompliance,
       "dDhcpServerGroups": dDhcpServerGroups,
       "dDhcpSGblCfgGroup": dDhcpSGblCfgGroup,
       "dDhcpSClassGroup": dDhcpSClassGroup,
       "dDhcpSClassCfgGroup": dDhcpSClassCfgGroup,
       "dDhcpSPoolGroup": dDhcpSPoolGroup,
       "dDhcpSPoolCfgGroup": dDhcpSPoolCfgGroup,
       "dDhcpSPoolNetworkCfgGroup": dDhcpSPoolNetworkCfgGroup,
       "dDhcpSPoolManualBindingGroup": dDhcpSPoolManualBindingGroup,
       "dDhcpSStatisticsGroup": dDhcpSStatisticsGroup,
       "dDhcpSGeneralInfoGroup": dDhcpSGeneralInfoGroup}
)
