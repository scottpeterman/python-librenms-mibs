# SNMP MIB module (DLINKSW-DHCP6-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP6-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:57 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDhcp6ServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223)
)
if mibBuilder.loadTexts:
    dlinkSwDhcp6ServerMIB.setRevisions(
        ("2013-01-18 00:00",
         "2013-10-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcp6ServerMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcp6ServerMIBNotifications = _DDhcp6ServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 0)
)
_DDhcp6ServerMIBObjects_ObjectIdentity = ObjectIdentity
dDhcp6ServerMIBObjects = _DDhcp6ServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1)
)
_DDhcp6ServGeneral_ObjectIdentity = ObjectIdentity
dDhcp6ServGeneral = _DDhcp6ServGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1)
)


class _DDhcp6ServiceEnabled_Type(TruthValue):
    """Custom type dDhcp6ServiceEnabled based on TruthValue"""
    defaultValue = 2


_DDhcp6ServiceEnabled_Type.__name__ = "TruthValue"
_DDhcp6ServiceEnabled_Object = MibScalar
dDhcp6ServiceEnabled = _DDhcp6ServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 1),
    _DDhcp6ServiceEnabled_Type()
)
dDhcp6ServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6ServiceEnabled.setStatus("current")
_DDhcp6SCfgChanged_Type = OctetString
_DDhcp6SCfgChanged_Object = MibScalar
dDhcp6SCfgChanged = _DDhcp6SCfgChanged_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 2),
    _DDhcp6SCfgChanged_Type()
)
dDhcp6SCfgChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SCfgChanged.setStatus("current")
_DDhcp6SExcludedAddressTable_Object = MibTable
dDhcp6SExcludedAddressTable = _DDhcp6SExcludedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dDhcp6SExcludedAddressTable.setStatus("current")
_DDhcp6SExcludedAddressEntry_Object = MibTableRow
dDhcp6SExcludedAddressEntry = _DDhcp6SExcludedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 3, 1)
)
dDhcp6SExcludedAddressEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SExcludedAddressBeginAddr"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SExcludedAddressEndAddr"),
)
if mibBuilder.loadTexts:
    dDhcp6SExcludedAddressEntry.setStatus("current")
_DDhcp6SExcludedAddressBeginAddr_Type = InetAddressIPv6
_DDhcp6SExcludedAddressBeginAddr_Object = MibTableColumn
dDhcp6SExcludedAddressBeginAddr = _DDhcp6SExcludedAddressBeginAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 3, 1, 1),
    _DDhcp6SExcludedAddressBeginAddr_Type()
)
dDhcp6SExcludedAddressBeginAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SExcludedAddressBeginAddr.setStatus("current")
_DDhcp6SExcludedAddressEndAddr_Type = InetAddressIPv6
_DDhcp6SExcludedAddressEndAddr_Object = MibTableColumn
dDhcp6SExcludedAddressEndAddr = _DDhcp6SExcludedAddressEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 3, 1, 2),
    _DDhcp6SExcludedAddressEndAddr_Type()
)
dDhcp6SExcludedAddressEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SExcludedAddressEndAddr.setStatus("current")
_DDhcp6SExcludedAddressRowStatus_Type = RowStatus
_DDhcp6SExcludedAddressRowStatus_Object = MibTableColumn
dDhcp6SExcludedAddressRowStatus = _DDhcp6SExcludedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 3, 1, 3),
    _DDhcp6SExcludedAddressRowStatus_Type()
)
dDhcp6SExcludedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SExcludedAddressRowStatus.setStatus("current")
_DDhcp6SLocalPoolTable_Object = MibTable
dDhcp6SLocalPoolTable = _DDhcp6SLocalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolTable.setStatus("current")
_DDhcp6SLocalPoolEntry_Object = MibTableRow
dDhcp6SLocalPoolEntry = _DDhcp6SLocalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1)
)
dDhcp6SLocalPoolEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolName"),
)
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolEntry.setStatus("current")


class _DDhcp6SLocalPoolName_Type(DisplayString):
    """Custom type dDhcp6SLocalPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6SLocalPoolName_Type.__name__ = "DisplayString"
_DDhcp6SLocalPoolName_Object = MibTableColumn
dDhcp6SLocalPoolName = _DDhcp6SLocalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 1),
    _DDhcp6SLocalPoolName_Type()
)
dDhcp6SLocalPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolName.setStatus("current")
_DDhcp6SLocalPoolPrefix_Type = InetAddressIPv6
_DDhcp6SLocalPoolPrefix_Object = MibTableColumn
dDhcp6SLocalPoolPrefix = _DDhcp6SLocalPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 2),
    _DDhcp6SLocalPoolPrefix_Type()
)
dDhcp6SLocalPoolPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolPrefix.setStatus("current")
_DDhcp6SLocalPoolPrefixLen_Type = InetAddressPrefixLength
_DDhcp6SLocalPoolPrefixLen_Object = MibTableColumn
dDhcp6SLocalPoolPrefixLen = _DDhcp6SLocalPoolPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 3),
    _DDhcp6SLocalPoolPrefixLen_Type()
)
dDhcp6SLocalPoolPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolPrefixLen.setStatus("current")
_DDhcp6SLocalPoolPrefixAssignLen_Type = InetAddressPrefixLength
_DDhcp6SLocalPoolPrefixAssignLen_Object = MibTableColumn
dDhcp6SLocalPoolPrefixAssignLen = _DDhcp6SLocalPoolPrefixAssignLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 4),
    _DDhcp6SLocalPoolPrefixAssignLen_Type()
)
dDhcp6SLocalPoolPrefixAssignLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolPrefixAssignLen.setStatus("current")
_DDhcp6SLocalPoolFreeAddrNum_Type = Unsigned32
_DDhcp6SLocalPoolFreeAddrNum_Object = MibTableColumn
dDhcp6SLocalPoolFreeAddrNum = _DDhcp6SLocalPoolFreeAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 5),
    _DDhcp6SLocalPoolFreeAddrNum_Type()
)
dDhcp6SLocalPoolFreeAddrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolFreeAddrNum.setStatus("current")
_DDhcp6SLocalPoolInUseAddrNum_Type = Unsigned32
_DDhcp6SLocalPoolInUseAddrNum_Object = MibTableColumn
dDhcp6SLocalPoolInUseAddrNum = _DDhcp6SLocalPoolInUseAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 6),
    _DDhcp6SLocalPoolInUseAddrNum_Type()
)
dDhcp6SLocalPoolInUseAddrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolInUseAddrNum.setStatus("current")
_DDhcp6SLocalPoolRowStatus_Type = RowStatus
_DDhcp6SLocalPoolRowStatus_Object = MibTableColumn
dDhcp6SLocalPoolRowStatus = _DDhcp6SLocalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 1, 4, 1, 7),
    _DDhcp6SLocalPoolRowStatus_Type()
)
dDhcp6SLocalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolRowStatus.setStatus("current")
_DDhcp6ServPoolMgmt_ObjectIdentity = ObjectIdentity
dDhcp6ServPoolMgmt = _DDhcp6ServPoolMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2)
)
_DDhcp6SPoolTable_Object = MibTable
dDhcp6SPoolTable = _DDhcp6SPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolTable.setStatus("current")
_DDhcp6SPoolEntry_Object = MibTableRow
dDhcp6SPoolEntry = _DDhcp6SPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 1, 1)
)
dDhcp6SPoolEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolEntry.setStatus("current")


class _DDhcp6SPoolName_Type(DisplayString):
    """Custom type dDhcp6SPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6SPoolName_Type.__name__ = "DisplayString"
_DDhcp6SPoolName_Object = MibTableColumn
dDhcp6SPoolName = _DDhcp6SPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 1, 1, 1),
    _DDhcp6SPoolName_Type()
)
dDhcp6SPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SPoolName.setStatus("current")
_DDhcp6SPoolRowStatus_Type = RowStatus
_DDhcp6SPoolRowStatus_Object = MibTableColumn
dDhcp6SPoolRowStatus = _DDhcp6SPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 1, 1, 2),
    _DDhcp6SPoolRowStatus_Type()
)
dDhcp6SPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolRowStatus.setStatus("current")
_DDhcp6SPoolDomainNameTable_Object = MibTable
dDhcp6SPoolDomainNameTable = _DDhcp6SPoolDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolDomainNameTable.setStatus("current")
_DDhcp6SPoolDomainNameEntry_Object = MibTableRow
dDhcp6SPoolDomainNameEntry = _DDhcp6SPoolDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 2, 1)
)
dDhcp6SPoolDomainNameEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolDomainNameAdminIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolDomainNameEntry.setStatus("current")


class _DDhcp6SPoolDomainNameAdminIndex_Type(Unsigned32):
    """Custom type dDhcp6SPoolDomainNameAdminIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DDhcp6SPoolDomainNameAdminIndex_Type.__name__ = "Unsigned32"
_DDhcp6SPoolDomainNameAdminIndex_Object = MibTableColumn
dDhcp6SPoolDomainNameAdminIndex = _DDhcp6SPoolDomainNameAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 2, 1, 1),
    _DDhcp6SPoolDomainNameAdminIndex_Type()
)
dDhcp6SPoolDomainNameAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SPoolDomainNameAdminIndex.setStatus("current")


class _DDhcp6SPoolDomainName_Type(DisplayString):
    """Custom type dDhcp6SPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6SPoolDomainName_Type.__name__ = "DisplayString"
_DDhcp6SPoolDomainName_Object = MibTableColumn
dDhcp6SPoolDomainName = _DDhcp6SPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 2, 1, 2),
    _DDhcp6SPoolDomainName_Type()
)
dDhcp6SPoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolDomainName.setStatus("current")
_Dhcp6ServerDomainNameRowStatus_Type = RowStatus
_Dhcp6ServerDomainNameRowStatus_Object = MibTableColumn
dhcp6ServerDomainNameRowStatus = _Dhcp6ServerDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 2, 1, 3),
    _Dhcp6ServerDomainNameRowStatus_Type()
)
dhcp6ServerDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcp6ServerDomainNameRowStatus.setStatus("current")
_DDhcp6SPoolDnsServerTable_Object = MibTable
dDhcp6SPoolDnsServerTable = _DDhcp6SPoolDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolDnsServerTable.setStatus("current")
_DDhcp6SPoolDnsServerEntry_Object = MibTableRow
dDhcp6SPoolDnsServerEntry = _DDhcp6SPoolDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 3, 1)
)
dDhcp6SPoolDnsServerEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolDnsServerIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolDnsServerEntry.setStatus("current")


class _DDhcp6SPoolDnsServerIndex_Type(Unsigned32):
    """Custom type dDhcp6SPoolDnsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DDhcp6SPoolDnsServerIndex_Type.__name__ = "Unsigned32"
_DDhcp6SPoolDnsServerIndex_Object = MibTableColumn
dDhcp6SPoolDnsServerIndex = _DDhcp6SPoolDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 3, 1, 1),
    _DDhcp6SPoolDnsServerIndex_Type()
)
dDhcp6SPoolDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SPoolDnsServerIndex.setStatus("current")
_DDhcp6SPoolDnsServerAddr_Type = InetAddressIPv6
_DDhcp6SPoolDnsServerAddr_Object = MibTableColumn
dDhcp6SPoolDnsServerAddr = _DDhcp6SPoolDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 3, 1, 2),
    _DDhcp6SPoolDnsServerAddr_Type()
)
dDhcp6SPoolDnsServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolDnsServerAddr.setStatus("current")
_DDhcp6SPoolDnsServerRowStatus_Type = RowStatus
_DDhcp6SPoolDnsServerRowStatus_Object = MibTableColumn
dDhcp6SPoolDnsServerRowStatus = _DDhcp6SPoolDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 3, 1, 3),
    _DDhcp6SPoolDnsServerRowStatus_Type()
)
dDhcp6SPoolDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolDnsServerRowStatus.setStatus("current")
_DDhcp6SPoolAddrPrefixTable_Object = MibTable
dDhcp6SPoolAddrPrefixTable = _DDhcp6SPoolAddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixTable.setStatus("current")
_DDhcp6SPoolAddrPrefixEntry_Object = MibTableRow
dDhcp6SPoolAddrPrefixEntry = _DDhcp6SPoolAddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1)
)
dDhcp6SPoolAddrPrefixEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixEntry.setStatus("current")
_DDhcp6SPoolAddrPrefixAddr_Type = InetAddressIPv6
_DDhcp6SPoolAddrPrefixAddr_Object = MibTableColumn
dDhcp6SPoolAddrPrefixAddr = _DDhcp6SPoolAddrPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1, 1),
    _DDhcp6SPoolAddrPrefixAddr_Type()
)
dDhcp6SPoolAddrPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixAddr.setStatus("current")
_DDhcp6SPoolAddrPrefixLength_Type = InetAddressPrefixLength
_DDhcp6SPoolAddrPrefixLength_Object = MibTableColumn
dDhcp6SPoolAddrPrefixLength = _DDhcp6SPoolAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1, 2),
    _DDhcp6SPoolAddrPrefixLength_Type()
)
dDhcp6SPoolAddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixLength.setStatus("current")


class _DDhcp6SPoolAddrPrefixVLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolAddrPrefixVLtime based on Unsigned32"""
    defaultValue = 2592000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolAddrPrefixVLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolAddrPrefixVLtime_Object = MibTableColumn
dDhcp6SPoolAddrPrefixVLtime = _DDhcp6SPoolAddrPrefixVLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1, 3),
    _DDhcp6SPoolAddrPrefixVLtime_Type()
)
dDhcp6SPoolAddrPrefixVLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixVLtime.setStatus("current")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixVLtime.setUnits("seconds")


class _DDhcp6SPoolAddrPrefixPLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolAddrPrefixPLtime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolAddrPrefixPLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolAddrPrefixPLtime_Object = MibTableColumn
dDhcp6SPoolAddrPrefixPLtime = _DDhcp6SPoolAddrPrefixPLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1, 4),
    _DDhcp6SPoolAddrPrefixPLtime_Type()
)
dDhcp6SPoolAddrPrefixPLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixPLtime.setStatus("current")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixPLtime.setUnits("seconds")
_DDhcp6SPoolAddrPrefixRowStatus_Type = RowStatus
_DDhcp6SPoolAddrPrefixRowStatus_Object = MibTableColumn
dDhcp6SPoolAddrPrefixRowStatus = _DDhcp6SPoolAddrPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 4, 1, 5),
    _DDhcp6SPoolAddrPrefixRowStatus_Type()
)
dDhcp6SPoolAddrPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrPrefixRowStatus.setStatus("current")
_DDhcp6SPoolAddrAssignTable_Object = MibTable
dDhcp6SPoolAddrAssignTable = _DDhcp6SPoolAddrAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignTable.setStatus("current")
_DDhcp6SPoolAddrAssignEntry_Object = MibTableRow
dDhcp6SPoolAddrAssignEntry = _DDhcp6SPoolAddrAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1)
)
dDhcp6SPoolAddrAssignEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignAddr"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignEntry.setStatus("current")
_DDhcp6SPoolAddrAssignAddr_Type = InetAddressIPv6
_DDhcp6SPoolAddrAssignAddr_Object = MibTableColumn
dDhcp6SPoolAddrAssignAddr = _DDhcp6SPoolAddrAssignAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 1),
    _DDhcp6SPoolAddrAssignAddr_Type()
)
dDhcp6SPoolAddrAssignAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignAddr.setStatus("current")
_DDhcp6SPoolAddrAssignLength_Type = InetAddressPrefixLength
_DDhcp6SPoolAddrAssignLength_Object = MibTableColumn
dDhcp6SPoolAddrAssignLength = _DDhcp6SPoolAddrAssignLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 2),
    _DDhcp6SPoolAddrAssignLength_Type()
)
dDhcp6SPoolAddrAssignLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignLength.setStatus("current")
_DDhcp6SPoolAddrAssignClientDuid_Type = OctetString
_DDhcp6SPoolAddrAssignClientDuid_Object = MibTableColumn
dDhcp6SPoolAddrAssignClientDuid = _DDhcp6SPoolAddrAssignClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 3),
    _DDhcp6SPoolAddrAssignClientDuid_Type()
)
dDhcp6SPoolAddrAssignClientDuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignClientDuid.setStatus("current")


class _DDhcp6SPoolAddrAssignSetIaid_Type(TruthValue):
    """Custom type dDhcp6SPoolAddrAssignSetIaid based on TruthValue"""
    defaultValue = 2


_DDhcp6SPoolAddrAssignSetIaid_Type.__name__ = "TruthValue"
_DDhcp6SPoolAddrAssignSetIaid_Object = MibTableColumn
dDhcp6SPoolAddrAssignSetIaid = _DDhcp6SPoolAddrAssignSetIaid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 4),
    _DDhcp6SPoolAddrAssignSetIaid_Type()
)
dDhcp6SPoolAddrAssignSetIaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignSetIaid.setStatus("current")
_DDhcp6SPoolAddrAssignIaid_Type = Unsigned32
_DDhcp6SPoolAddrAssignIaid_Object = MibTableColumn
dDhcp6SPoolAddrAssignIaid = _DDhcp6SPoolAddrAssignIaid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 5),
    _DDhcp6SPoolAddrAssignIaid_Type()
)
dDhcp6SPoolAddrAssignIaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignIaid.setStatus("current")


class _DDhcp6SPoolAddrAssignVLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolAddrAssignVLtime based on Unsigned32"""
    defaultValue = 2592000


_DDhcp6SPoolAddrAssignVLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolAddrAssignVLtime_Object = MibTableColumn
dDhcp6SPoolAddrAssignVLtime = _DDhcp6SPoolAddrAssignVLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 6),
    _DDhcp6SPoolAddrAssignVLtime_Type()
)
dDhcp6SPoolAddrAssignVLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignVLtime.setStatus("current")


class _DDhcp6SPoolAddrAssignPLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolAddrAssignPLtime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolAddrAssignPLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolAddrAssignPLtime_Object = MibTableColumn
dDhcp6SPoolAddrAssignPLtime = _DDhcp6SPoolAddrAssignPLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 7),
    _DDhcp6SPoolAddrAssignPLtime_Type()
)
dDhcp6SPoolAddrAssignPLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignPLtime.setStatus("current")
_DDhcp6SPoolAddrAssignRowStatus_Type = RowStatus
_DDhcp6SPoolAddrAssignRowStatus_Object = MibTableColumn
dDhcp6SPoolAddrAssignRowStatus = _DDhcp6SPoolAddrAssignRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 6, 1, 8),
    _DDhcp6SPoolAddrAssignRowStatus_Type()
)
dDhcp6SPoolAddrAssignRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolAddrAssignRowStatus.setStatus("current")
_DDhcp6SPoolPdTable_Object = MibTable
dDhcp6SPoolPdTable = _DDhcp6SPoolPdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolPdTable.setStatus("current")
_DDhcp6SPoolPdEntry_Object = MibTableRow
dDhcp6SPoolPdEntry = _DDhcp6SPoolPdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1)
)
dDhcp6SPoolPdEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdPrefix"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdPrefixLength"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolPdEntry.setStatus("current")
_DDhcp6SPoolPdPrefix_Type = InetAddressIPv6
_DDhcp6SPoolPdPrefix_Object = MibTableColumn
dDhcp6SPoolPdPrefix = _DDhcp6SPoolPdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 1),
    _DDhcp6SPoolPdPrefix_Type()
)
dDhcp6SPoolPdPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdPrefix.setStatus("current")
_DDhcp6SPoolPdPrefixLength_Type = InetAddressPrefixLength
_DDhcp6SPoolPdPrefixLength_Object = MibTableColumn
dDhcp6SPoolPdPrefixLength = _DDhcp6SPoolPdPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 2),
    _DDhcp6SPoolPdPrefixLength_Type()
)
dDhcp6SPoolPdPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdPrefixLength.setStatus("current")
_DDhcp6SPoolPdClientDuid_Type = OctetString
_DDhcp6SPoolPdClientDuid_Object = MibTableColumn
dDhcp6SPoolPdClientDuid = _DDhcp6SPoolPdClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 3),
    _DDhcp6SPoolPdClientDuid_Type()
)
dDhcp6SPoolPdClientDuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdClientDuid.setStatus("current")


class _DDhcp6SPoolPdSetIaid_Type(TruthValue):
    """Custom type dDhcp6SPoolPdSetIaid based on TruthValue"""
    defaultValue = 2


_DDhcp6SPoolPdSetIaid_Type.__name__ = "TruthValue"
_DDhcp6SPoolPdSetIaid_Object = MibTableColumn
dDhcp6SPoolPdSetIaid = _DDhcp6SPoolPdSetIaid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 4),
    _DDhcp6SPoolPdSetIaid_Type()
)
dDhcp6SPoolPdSetIaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdSetIaid.setStatus("current")
_DDhcp6SPoolPdIaid_Type = Unsigned32
_DDhcp6SPoolPdIaid_Object = MibTableColumn
dDhcp6SPoolPdIaid = _DDhcp6SPoolPdIaid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 5),
    _DDhcp6SPoolPdIaid_Type()
)
dDhcp6SPoolPdIaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdIaid.setStatus("current")


class _DDhcp6SPoolPdVLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolPdVLtime based on Unsigned32"""
    defaultValue = 2592000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolPdVLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolPdVLtime_Object = MibTableColumn
dDhcp6SPoolPdVLtime = _DDhcp6SPoolPdVLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 6),
    _DDhcp6SPoolPdVLtime_Type()
)
dDhcp6SPoolPdVLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdVLtime.setStatus("current")


class _DDhcp6SPoolPdPLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolPdPLtime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolPdPLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolPdPLtime_Object = MibTableColumn
dDhcp6SPoolPdPLtime = _DDhcp6SPoolPdPLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 7),
    _DDhcp6SPoolPdPLtime_Type()
)
dDhcp6SPoolPdPLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdPLtime.setStatus("current")
_DDhcp6SPoolPdRowStatus_Type = RowStatus
_DDhcp6SPoolPdRowStatus_Object = MibTableColumn
dDhcp6SPoolPdRowStatus = _DDhcp6SPoolPdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 7, 1, 8),
    _DDhcp6SPoolPdRowStatus_Type()
)
dDhcp6SPoolPdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdRowStatus.setStatus("current")
_DDhcp6SPoolPdLocPoolTable_Object = MibTable
dDhcp6SPoolPdLocPoolTable = _DDhcp6SPoolPdLocPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8)
)
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolTable.setStatus("current")
_DDhcp6SPoolPdLocPoolEntry_Object = MibTableRow
dDhcp6SPoolPdLocPoolEntry = _DDhcp6SPoolPdLocPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8, 1)
)
dDhcp6SPoolPdLocPoolEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolName"),
)
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolEntry.setStatus("current")


class _DDhcp6SPoolPdLocPoolName_Type(DisplayString):
    """Custom type dDhcp6SPoolPdLocPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6SPoolPdLocPoolName_Type.__name__ = "DisplayString"
_DDhcp6SPoolPdLocPoolName_Object = MibTableColumn
dDhcp6SPoolPdLocPoolName = _DDhcp6SPoolPdLocPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8, 1, 1),
    _DDhcp6SPoolPdLocPoolName_Type()
)
dDhcp6SPoolPdLocPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolName.setStatus("current")


class _DDhcp6SPoolPdLocPoolVLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolPdLocPoolVLtime based on Unsigned32"""
    defaultValue = 2592000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolPdLocPoolVLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolPdLocPoolVLtime_Object = MibTableColumn
dDhcp6SPoolPdLocPoolVLtime = _DDhcp6SPoolPdLocPoolVLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8, 1, 2),
    _DDhcp6SPoolPdLocPoolVLtime_Type()
)
dDhcp6SPoolPdLocPoolVLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolVLtime.setStatus("current")


class _DDhcp6SPoolPdLocPoolPLtime_Type(Unsigned32):
    """Custom type dDhcp6SPoolPdLocPoolPLtime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SPoolPdLocPoolPLtime_Type.__name__ = "Unsigned32"
_DDhcp6SPoolPdLocPoolPLtime_Object = MibTableColumn
dDhcp6SPoolPdLocPoolPLtime = _DDhcp6SPoolPdLocPoolPLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8, 1, 3),
    _DDhcp6SPoolPdLocPoolPLtime_Type()
)
dDhcp6SPoolPdLocPoolPLtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolPLtime.setStatus("current")
_DDhcp6SPoolPdLocPoolRowStatus_Type = RowStatus
_DDhcp6SPoolPdLocPoolRowStatus_Object = MibTableColumn
dDhcp6SPoolPdLocPoolRowStatus = _DDhcp6SPoolPdLocPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 2, 8, 1, 4),
    _DDhcp6SPoolPdLocPoolRowStatus_Type()
)
dDhcp6SPoolPdLocPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6SPoolPdLocPoolRowStatus.setStatus("current")
_DDhcp6ServIfMgmt_ObjectIdentity = ObjectIdentity
dDhcp6ServIfMgmt = _DDhcp6ServIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3)
)
_DDhcp6ServIfTable_Object = MibTable
dDhcp6ServIfTable = _DDhcp6ServIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDhcp6ServIfTable.setStatus("current")
_DDhcp6ServIfEntry_Object = MibTableRow
dDhcp6ServIfEntry = _DDhcp6ServIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1)
)
dDhcp6ServIfEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6ServIfEntry.setStatus("current")
_DDhcp6ServIfIndex_Type = InterfaceIndex
_DDhcp6ServIfIndex_Object = MibTableColumn
dDhcp6ServIfIndex = _DDhcp6ServIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 1),
    _DDhcp6ServIfIndex_Type()
)
dDhcp6ServIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6ServIfIndex.setStatus("current")


class _DDhcp6ServIfPoolName_Type(DisplayString):
    """Custom type dDhcp6ServIfPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6ServIfPoolName_Type.__name__ = "DisplayString"
_DDhcp6ServIfPoolName_Object = MibTableColumn
dDhcp6ServIfPoolName = _DDhcp6ServIfPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 2),
    _DDhcp6ServIfPoolName_Type()
)
dDhcp6ServIfPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6ServIfPoolName.setStatus("current")


class _DDhcp6ServIfRapidCommit_Type(TruthValue):
    """Custom type dDhcp6ServIfRapidCommit based on TruthValue"""
    defaultValue = 2


_DDhcp6ServIfRapidCommit_Type.__name__ = "TruthValue"
_DDhcp6ServIfRapidCommit_Object = MibTableColumn
dDhcp6ServIfRapidCommit = _DDhcp6ServIfRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 3),
    _DDhcp6ServIfRapidCommit_Type()
)
dDhcp6ServIfRapidCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6ServIfRapidCommit.setStatus("current")


class _DDhcp6ServIfAllowHint_Type(TruthValue):
    """Custom type dDhcp6ServIfAllowHint based on TruthValue"""
    defaultValue = 2


_DDhcp6ServIfAllowHint_Type.__name__ = "TruthValue"
_DDhcp6ServIfAllowHint_Object = MibTableColumn
dDhcp6ServIfAllowHint = _DDhcp6ServIfAllowHint_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 4),
    _DDhcp6ServIfAllowHint_Type()
)
dDhcp6ServIfAllowHint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6ServIfAllowHint.setStatus("current")


class _DDhcp6ServIfPreference_Type(Unsigned32):
    """Custom type dDhcp6ServIfPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DDhcp6ServIfPreference_Type.__name__ = "Unsigned32"
_DDhcp6ServIfPreference_Object = MibTableColumn
dDhcp6ServIfPreference = _DDhcp6ServIfPreference_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 5),
    _DDhcp6ServIfPreference_Type()
)
dDhcp6ServIfPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6ServIfPreference.setStatus("current")
_DDhcp6ServIfRowStatus_Type = RowStatus
_DDhcp6ServIfRowStatus_Object = MibTableColumn
dDhcp6ServIfRowStatus = _DDhcp6ServIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 3, 1, 1, 6),
    _DDhcp6ServIfRowStatus_Type()
)
dDhcp6ServIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6ServIfRowStatus.setStatus("current")
_DDhcp6ServInfo_ObjectIdentity = ObjectIdentity
dDhcp6ServInfo = _DDhcp6ServInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4)
)
_DDhcp6SBindingTable_Object = MibTable
dDhcp6SBindingTable = _DDhcp6SBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDhcp6SBindingTable.setStatus("current")
_DDhcp6SBindingEntry_Object = MibTableRow
dDhcp6SBindingEntry = _DDhcp6SBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1)
)
dDhcp6SBindingEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindIfIndex"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindClientDuid"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindIaType"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindIaId"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindAddrOrPrefix"),
    (0, "DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindAddrOrPrefixLen"),
)
if mibBuilder.loadTexts:
    dDhcp6SBindingEntry.setStatus("current")
_DDhcp6SBindIfIndex_Type = InterfaceIndex
_DDhcp6SBindIfIndex_Object = MibTableColumn
dDhcp6SBindIfIndex = _DDhcp6SBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 1),
    _DDhcp6SBindIfIndex_Type()
)
dDhcp6SBindIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindIfIndex.setStatus("current")
_DDhcp6SBindClientDuid_Type = OctetString
_DDhcp6SBindClientDuid_Object = MibTableColumn
dDhcp6SBindClientDuid = _DDhcp6SBindClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 2),
    _DDhcp6SBindClientDuid_Type()
)
dDhcp6SBindClientDuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindClientDuid.setStatus("current")


class _DDhcp6SBindIaType_Type(Integer32):
    """Custom type dDhcp6SBindIaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("iapd", 1),
          ("iana", 2))
    )


_DDhcp6SBindIaType_Type.__name__ = "Integer32"
_DDhcp6SBindIaType_Object = MibTableColumn
dDhcp6SBindIaType = _DDhcp6SBindIaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 3),
    _DDhcp6SBindIaType_Type()
)
dDhcp6SBindIaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindIaType.setStatus("current")


class _DDhcp6SBindIaId_Type(Unsigned32):
    """Custom type dDhcp6SBindIaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_DDhcp6SBindIaId_Type.__name__ = "Unsigned32"
_DDhcp6SBindIaId_Object = MibTableColumn
dDhcp6SBindIaId = _DDhcp6SBindIaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 4),
    _DDhcp6SBindIaId_Type()
)
dDhcp6SBindIaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindIaId.setStatus("current")
_DDhcp6SBindAddrOrPrefix_Type = InetAddressIPv6
_DDhcp6SBindAddrOrPrefix_Object = MibTableColumn
dDhcp6SBindAddrOrPrefix = _DDhcp6SBindAddrOrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 5),
    _DDhcp6SBindAddrOrPrefix_Type()
)
dDhcp6SBindAddrOrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindAddrOrPrefix.setStatus("current")
_DDhcp6SBindAddrOrPrefixLen_Type = InetAddressPrefixLength
_DDhcp6SBindAddrOrPrefixLen_Object = MibTableColumn
dDhcp6SBindAddrOrPrefixLen = _DDhcp6SBindAddrOrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 6),
    _DDhcp6SBindAddrOrPrefixLen_Type()
)
dDhcp6SBindAddrOrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6SBindAddrOrPrefixLen.setStatus("current")
_DDhcp6SBindClientLinkLocalAddr_Type = InetAddressIPv6
_DDhcp6SBindClientLinkLocalAddr_Object = MibTableColumn
dDhcp6SBindClientLinkLocalAddr = _DDhcp6SBindClientLinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 7),
    _DDhcp6SBindClientLinkLocalAddr_Type()
)
dDhcp6SBindClientLinkLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindClientLinkLocalAddr.setStatus("current")
_DDhcp6SBindIaT1_Type = Unsigned32
_DDhcp6SBindIaT1_Object = MibTableColumn
dDhcp6SBindIaT1 = _DDhcp6SBindIaT1_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 8),
    _DDhcp6SBindIaT1_Type()
)
dDhcp6SBindIaT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindIaT1.setStatus("current")
_DDhcp6SBindIaT2_Type = Unsigned32
_DDhcp6SBindIaT2_Object = MibTableColumn
dDhcp6SBindIaT2 = _DDhcp6SBindIaT2_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 9),
    _DDhcp6SBindIaT2_Type()
)
dDhcp6SBindIaT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindIaT2.setStatus("current")
_DDhcp6SBindVLtime_Type = Unsigned32
_DDhcp6SBindVLtime_Object = MibTableColumn
dDhcp6SBindVLtime = _DDhcp6SBindVLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 10),
    _DDhcp6SBindVLtime_Type()
)
dDhcp6SBindVLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindVLtime.setStatus("current")
_DDhcp6SBindPLtime_Type = Unsigned32
_DDhcp6SBindPLtime_Object = MibTableColumn
dDhcp6SBindPLtime = _DDhcp6SBindPLtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 11),
    _DDhcp6SBindPLtime_Type()
)
dDhcp6SBindPLtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindPLtime.setStatus("current")
_DDhcp6SBindExpire_Type = DateAndTime
_DDhcp6SBindExpire_Object = MibTableColumn
dDhcp6SBindExpire = _DDhcp6SBindExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 12),
    _DDhcp6SBindExpire_Type()
)
dDhcp6SBindExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6SBindExpire.setStatus("current")


class _DDhcp6SBindClear_Type(Integer32):
    """Custom type dDhcp6SBindClear based on Integer32"""
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


_DDhcp6SBindClear_Type.__name__ = "Integer32"
_DDhcp6SBindClear_Object = MibTableColumn
dDhcp6SBindClear = _DDhcp6SBindClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 1, 4, 1, 1, 13),
    _DDhcp6SBindClear_Type()
)
dDhcp6SBindClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6SBindClear.setStatus("current")
_DDhcp6ServerMIBConformance_ObjectIdentity = ObjectIdentity
dDhcp6ServerMIBConformance = _DDhcp6ServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2)
)
_DDhcp6ServerCompliances_ObjectIdentity = ObjectIdentity
dDhcp6ServerCompliances = _DDhcp6ServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 1)
)
_DDhcp6ServerGroups_ObjectIdentity = ObjectIdentity
dDhcp6ServerGroups = _DDhcp6ServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2)
)

# Managed Objects groups

dDhcp6SGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 1)
)
dDhcp6SGblCfgGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServiceEnabled"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SCfgChanged"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SExcludedAddressRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SGblCfgGroup.setStatus("current")

dDhcp6SLocalPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 2)
)
dDhcp6SLocalPoolGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolPrefix"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolPrefixLen"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolPrefixAssignLen"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SLocalPoolGroup.setStatus("current")

dDhcp6SPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 3)
)
dDhcp6SPoolGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolRowStatus"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolDomainName"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dhcp6ServerDomainNameRowStatus"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolDnsServerAddr"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolDnsServerRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SPoolGroup.setStatus("current")

dDhcp6SInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 4)
)
dDhcp6SInterfaceGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfPoolName"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfRapidCommit"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfAllowHint"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfPreference"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6ServIfRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SInterfaceGroup.setStatus("current")

dDhcp6SNonTempAddrAssignGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 5)
)
dDhcp6SNonTempAddrAssignGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrPrefixAddr"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrPrefixLength"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrPrefixVLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrPrefixPLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrPrefixRowStatus"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignAddr"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignLength"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignClientDuid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignSetIaid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignIaid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignVLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignPLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolAddrAssignRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SNonTempAddrAssignGroup.setStatus("current")

dDhcp6SPrefixDelegationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 6)
)
dDhcp6SPrefixDelegationGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdPrefix"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdPrefixLength"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdClientDuid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdSetIaid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdIaid"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdVLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdPLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdRowStatus"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdLocPoolName"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdLocPoolVLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdLocPoolPLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolPdLocPoolRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6SPrefixDelegationGroup.setStatus("current")

dDhcp6SInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 2, 7)
)
dDhcp6SInfoGroup.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolFreeAddrNum"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolInUseAddrNum"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindClientLinkLocalAddr"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindIaT1"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindIaT2"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindVLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindPLtime"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindExpire"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SBindClear"))
)
if mibBuilder.loadTexts:
    dDhcp6SInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcp6ServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 223, 2, 1, 1)
)
dDhcp6ServerCompliance.setObjects(
      *(("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SGblCfgGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SLocalPoolGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPoolGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SInterfaceGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SNonTempAddrAssignGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SInfoGroup"),
        ("DLINKSW-DHCP6-SERVER-MIB", "dDhcp6SPrefixDelegationGroup"))
)
if mibBuilder.loadTexts:
    dDhcp6ServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP6-SERVER-MIB",
    **{"dlinkSwDhcp6ServerMIB": dlinkSwDhcp6ServerMIB,
       "dDhcp6ServerMIBNotifications": dDhcp6ServerMIBNotifications,
       "dDhcp6ServerMIBObjects": dDhcp6ServerMIBObjects,
       "dDhcp6ServGeneral": dDhcp6ServGeneral,
       "dDhcp6ServiceEnabled": dDhcp6ServiceEnabled,
       "dDhcp6SCfgChanged": dDhcp6SCfgChanged,
       "dDhcp6SExcludedAddressTable": dDhcp6SExcludedAddressTable,
       "dDhcp6SExcludedAddressEntry": dDhcp6SExcludedAddressEntry,
       "dDhcp6SExcludedAddressBeginAddr": dDhcp6SExcludedAddressBeginAddr,
       "dDhcp6SExcludedAddressEndAddr": dDhcp6SExcludedAddressEndAddr,
       "dDhcp6SExcludedAddressRowStatus": dDhcp6SExcludedAddressRowStatus,
       "dDhcp6SLocalPoolTable": dDhcp6SLocalPoolTable,
       "dDhcp6SLocalPoolEntry": dDhcp6SLocalPoolEntry,
       "dDhcp6SLocalPoolName": dDhcp6SLocalPoolName,
       "dDhcp6SLocalPoolPrefix": dDhcp6SLocalPoolPrefix,
       "dDhcp6SLocalPoolPrefixLen": dDhcp6SLocalPoolPrefixLen,
       "dDhcp6SLocalPoolPrefixAssignLen": dDhcp6SLocalPoolPrefixAssignLen,
       "dDhcp6SLocalPoolFreeAddrNum": dDhcp6SLocalPoolFreeAddrNum,
       "dDhcp6SLocalPoolInUseAddrNum": dDhcp6SLocalPoolInUseAddrNum,
       "dDhcp6SLocalPoolRowStatus": dDhcp6SLocalPoolRowStatus,
       "dDhcp6ServPoolMgmt": dDhcp6ServPoolMgmt,
       "dDhcp6SPoolTable": dDhcp6SPoolTable,
       "dDhcp6SPoolEntry": dDhcp6SPoolEntry,
       "dDhcp6SPoolName": dDhcp6SPoolName,
       "dDhcp6SPoolRowStatus": dDhcp6SPoolRowStatus,
       "dDhcp6SPoolDomainNameTable": dDhcp6SPoolDomainNameTable,
       "dDhcp6SPoolDomainNameEntry": dDhcp6SPoolDomainNameEntry,
       "dDhcp6SPoolDomainNameAdminIndex": dDhcp6SPoolDomainNameAdminIndex,
       "dDhcp6SPoolDomainName": dDhcp6SPoolDomainName,
       "dhcp6ServerDomainNameRowStatus": dhcp6ServerDomainNameRowStatus,
       "dDhcp6SPoolDnsServerTable": dDhcp6SPoolDnsServerTable,
       "dDhcp6SPoolDnsServerEntry": dDhcp6SPoolDnsServerEntry,
       "dDhcp6SPoolDnsServerIndex": dDhcp6SPoolDnsServerIndex,
       "dDhcp6SPoolDnsServerAddr": dDhcp6SPoolDnsServerAddr,
       "dDhcp6SPoolDnsServerRowStatus": dDhcp6SPoolDnsServerRowStatus,
       "dDhcp6SPoolAddrPrefixTable": dDhcp6SPoolAddrPrefixTable,
       "dDhcp6SPoolAddrPrefixEntry": dDhcp6SPoolAddrPrefixEntry,
       "dDhcp6SPoolAddrPrefixAddr": dDhcp6SPoolAddrPrefixAddr,
       "dDhcp6SPoolAddrPrefixLength": dDhcp6SPoolAddrPrefixLength,
       "dDhcp6SPoolAddrPrefixVLtime": dDhcp6SPoolAddrPrefixVLtime,
       "dDhcp6SPoolAddrPrefixPLtime": dDhcp6SPoolAddrPrefixPLtime,
       "dDhcp6SPoolAddrPrefixRowStatus": dDhcp6SPoolAddrPrefixRowStatus,
       "dDhcp6SPoolAddrAssignTable": dDhcp6SPoolAddrAssignTable,
       "dDhcp6SPoolAddrAssignEntry": dDhcp6SPoolAddrAssignEntry,
       "dDhcp6SPoolAddrAssignAddr": dDhcp6SPoolAddrAssignAddr,
       "dDhcp6SPoolAddrAssignLength": dDhcp6SPoolAddrAssignLength,
       "dDhcp6SPoolAddrAssignClientDuid": dDhcp6SPoolAddrAssignClientDuid,
       "dDhcp6SPoolAddrAssignSetIaid": dDhcp6SPoolAddrAssignSetIaid,
       "dDhcp6SPoolAddrAssignIaid": dDhcp6SPoolAddrAssignIaid,
       "dDhcp6SPoolAddrAssignVLtime": dDhcp6SPoolAddrAssignVLtime,
       "dDhcp6SPoolAddrAssignPLtime": dDhcp6SPoolAddrAssignPLtime,
       "dDhcp6SPoolAddrAssignRowStatus": dDhcp6SPoolAddrAssignRowStatus,
       "dDhcp6SPoolPdTable": dDhcp6SPoolPdTable,
       "dDhcp6SPoolPdEntry": dDhcp6SPoolPdEntry,
       "dDhcp6SPoolPdPrefix": dDhcp6SPoolPdPrefix,
       "dDhcp6SPoolPdPrefixLength": dDhcp6SPoolPdPrefixLength,
       "dDhcp6SPoolPdClientDuid": dDhcp6SPoolPdClientDuid,
       "dDhcp6SPoolPdSetIaid": dDhcp6SPoolPdSetIaid,
       "dDhcp6SPoolPdIaid": dDhcp6SPoolPdIaid,
       "dDhcp6SPoolPdVLtime": dDhcp6SPoolPdVLtime,
       "dDhcp6SPoolPdPLtime": dDhcp6SPoolPdPLtime,
       "dDhcp6SPoolPdRowStatus": dDhcp6SPoolPdRowStatus,
       "dDhcp6SPoolPdLocPoolTable": dDhcp6SPoolPdLocPoolTable,
       "dDhcp6SPoolPdLocPoolEntry": dDhcp6SPoolPdLocPoolEntry,
       "dDhcp6SPoolPdLocPoolName": dDhcp6SPoolPdLocPoolName,
       "dDhcp6SPoolPdLocPoolVLtime": dDhcp6SPoolPdLocPoolVLtime,
       "dDhcp6SPoolPdLocPoolPLtime": dDhcp6SPoolPdLocPoolPLtime,
       "dDhcp6SPoolPdLocPoolRowStatus": dDhcp6SPoolPdLocPoolRowStatus,
       "dDhcp6ServIfMgmt": dDhcp6ServIfMgmt,
       "dDhcp6ServIfTable": dDhcp6ServIfTable,
       "dDhcp6ServIfEntry": dDhcp6ServIfEntry,
       "dDhcp6ServIfIndex": dDhcp6ServIfIndex,
       "dDhcp6ServIfPoolName": dDhcp6ServIfPoolName,
       "dDhcp6ServIfRapidCommit": dDhcp6ServIfRapidCommit,
       "dDhcp6ServIfAllowHint": dDhcp6ServIfAllowHint,
       "dDhcp6ServIfPreference": dDhcp6ServIfPreference,
       "dDhcp6ServIfRowStatus": dDhcp6ServIfRowStatus,
       "dDhcp6ServInfo": dDhcp6ServInfo,
       "dDhcp6SBindingTable": dDhcp6SBindingTable,
       "dDhcp6SBindingEntry": dDhcp6SBindingEntry,
       "dDhcp6SBindIfIndex": dDhcp6SBindIfIndex,
       "dDhcp6SBindClientDuid": dDhcp6SBindClientDuid,
       "dDhcp6SBindIaType": dDhcp6SBindIaType,
       "dDhcp6SBindIaId": dDhcp6SBindIaId,
       "dDhcp6SBindAddrOrPrefix": dDhcp6SBindAddrOrPrefix,
       "dDhcp6SBindAddrOrPrefixLen": dDhcp6SBindAddrOrPrefixLen,
       "dDhcp6SBindClientLinkLocalAddr": dDhcp6SBindClientLinkLocalAddr,
       "dDhcp6SBindIaT1": dDhcp6SBindIaT1,
       "dDhcp6SBindIaT2": dDhcp6SBindIaT2,
       "dDhcp6SBindVLtime": dDhcp6SBindVLtime,
       "dDhcp6SBindPLtime": dDhcp6SBindPLtime,
       "dDhcp6SBindExpire": dDhcp6SBindExpire,
       "dDhcp6SBindClear": dDhcp6SBindClear,
       "dDhcp6ServerMIBConformance": dDhcp6ServerMIBConformance,
       "dDhcp6ServerCompliances": dDhcp6ServerCompliances,
       "dDhcp6ServerCompliance": dDhcp6ServerCompliance,
       "dDhcp6ServerGroups": dDhcp6ServerGroups,
       "dDhcp6SGblCfgGroup": dDhcp6SGblCfgGroup,
       "dDhcp6SLocalPoolGroup": dDhcp6SLocalPoolGroup,
       "dDhcp6SPoolGroup": dDhcp6SPoolGroup,
       "dDhcp6SInterfaceGroup": dDhcp6SInterfaceGroup,
       "dDhcp6SNonTempAddrAssignGroup": dDhcp6SNonTempAddrAssignGroup,
       "dDhcp6SPrefixDelegationGroup": dDhcp6SPrefixDelegationGroup,
       "dDhcp6SInfoGroup": dDhcp6SInfoGroup}
)
