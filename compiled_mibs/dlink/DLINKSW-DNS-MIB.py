# SNMP MIB module (DLINKSW-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:59 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77)
)
if mibBuilder.loadTexts:
    dlinkSwDnsMIB.setRevisions(
        ("2013-05-09 00:00",
         "2013-08-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DnsTime(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "4d"


# MIB Managed Objects in the order of their OIDs

_DDnsMIBNotifications_ObjectIdentity = ObjectIdentity
dDnsMIBNotifications = _DDnsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 0)
)
_DDnsMIBObjects_ObjectIdentity = ObjectIdentity
dDnsMIBObjects = _DDnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1)
)
_DDnsGlobal_ObjectIdentity = ObjectIdentity
dDnsGlobal = _DDnsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1)
)
_DDnsResolverEnabled_Type = TruthValue
_DDnsResolverEnabled_Object = MibScalar
dDnsResolverEnabled = _DDnsResolverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 1),
    _DDnsResolverEnabled_Type()
)
dDnsResolverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsResolverEnabled.setStatus("current")
_DDnsResolverSourceInterface_Type = InterfaceIndexOrZero
_DDnsResolverSourceInterface_Object = MibScalar
dDnsResolverSourceInterface = _DDnsResolverSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 2),
    _DDnsResolverSourceInterface_Type()
)
dDnsResolverSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsResolverSourceInterface.setStatus("current")
_DDnsResolverDomainName_Type = SnmpAdminString
_DDnsResolverDomainName_Object = MibScalar
dDnsResolverDomainName = _DDnsResolverDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 3),
    _DDnsResolverDomainName_Type()
)
dDnsResolverDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsResolverDomainName.setStatus("current")


class _DDnsResolverTimeOut_Type(Unsigned32):
    """Custom type dDnsResolverTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DDnsResolverTimeOut_Type.__name__ = "Unsigned32"
_DDnsResolverTimeOut_Object = MibScalar
dDnsResolverTimeOut = _DDnsResolverTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 4),
    _DDnsResolverTimeOut_Type()
)
dDnsResolverTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsResolverTimeOut.setStatus("current")
_DDnsCacheSrvEnabled_Type = TruthValue
_DDnsCacheSrvEnabled_Object = MibScalar
dDnsCacheSrvEnabled = _DDnsCacheSrvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 5),
    _DDnsCacheSrvEnabled_Type()
)
dDnsCacheSrvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsCacheSrvEnabled.setStatus("current")


class _DDnsCacheSrvMaxForwarderQueue_Type(Unsigned32):
    """Custom type dDnsCacheSrvMaxForwarderQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DDnsCacheSrvMaxForwarderQueue_Type.__name__ = "Unsigned32"
_DDnsCacheSrvMaxForwarderQueue_Object = MibScalar
dDnsCacheSrvMaxForwarderQueue = _DDnsCacheSrvMaxForwarderQueue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 6),
    _DDnsCacheSrvMaxForwarderQueue_Type()
)
dDnsCacheSrvMaxForwarderQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsCacheSrvMaxForwarderQueue.setStatus("current")
_DDnsStaticHostLookupEnabled_Type = TruthValue
_DDnsStaticHostLookupEnabled_Object = MibScalar
dDnsStaticHostLookupEnabled = _DDnsStaticHostLookupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 7),
    _DDnsStaticHostLookupEnabled_Type()
)
dDnsStaticHostLookupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsStaticHostLookupEnabled.setStatus("current")
_DDnsDynamicHostLookupEnabled_Type = TruthValue
_DDnsDynamicHostLookupEnabled_Object = MibScalar
dDnsDynamicHostLookupEnabled = _DDnsDynamicHostLookupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 1, 8),
    _DDnsDynamicHostLookupEnabled_Type()
)
dDnsDynamicHostLookupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsDynamicHostLookupEnabled.setStatus("current")
_DDnsNameSrv_ObjectIdentity = ObjectIdentity
dDnsNameSrv = _DDnsNameSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9)
)
_DDnsStaticNameSrvTable_Object = MibTable
dDnsStaticNameSrvTable = _DDnsStaticNameSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1)
)
if mibBuilder.loadTexts:
    dDnsStaticNameSrvTable.setStatus("current")
_DDnsStaticNameSrvEntry_Object = MibTableRow
dDnsStaticNameSrvEntry = _DDnsStaticNameSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1)
)
dDnsStaticNameSrvEntry.setIndexNames(
    (0, "DLINKSW-DNS-MIB", "dDnsStaticNameSrvIpVrfName"),
    (0, "DLINKSW-DNS-MIB", "dDnsStaticNameSrvIpType"),
    (0, "DLINKSW-DNS-MIB", "dDnsStaticNameSrvIpAddr"),
)
if mibBuilder.loadTexts:
    dDnsStaticNameSrvEntry.setStatus("current")


class _DDnsStaticNameSrvIpVrfName_Type(SnmpAdminString):
    """Custom type dDnsStaticNameSrvIpVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDnsStaticNameSrvIpVrfName_Type.__name__ = "SnmpAdminString"
_DDnsStaticNameSrvIpVrfName_Object = MibTableColumn
dDnsStaticNameSrvIpVrfName = _DDnsStaticNameSrvIpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1, 1),
    _DDnsStaticNameSrvIpVrfName_Type()
)
dDnsStaticNameSrvIpVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsStaticNameSrvIpVrfName.setStatus("current")
_DDnsStaticNameSrvIpType_Type = InetAddressType
_DDnsStaticNameSrvIpType_Object = MibTableColumn
dDnsStaticNameSrvIpType = _DDnsStaticNameSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1, 2),
    _DDnsStaticNameSrvIpType_Type()
)
dDnsStaticNameSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsStaticNameSrvIpType.setStatus("current")
_DDnsStaticNameSrvIpAddr_Type = InetAddress
_DDnsStaticNameSrvIpAddr_Object = MibTableColumn
dDnsStaticNameSrvIpAddr = _DDnsStaticNameSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1, 3),
    _DDnsStaticNameSrvIpAddr_Type()
)
dDnsStaticNameSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsStaticNameSrvIpAddr.setStatus("current")


class _DDnsStaticNameSrvIpPriority_Type(Integer32):
    """Custom type dDnsStaticNameSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DDnsStaticNameSrvIpPriority_Type.__name__ = "Integer32"
_DDnsStaticNameSrvIpPriority_Object = MibTableColumn
dDnsStaticNameSrvIpPriority = _DDnsStaticNameSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1, 4),
    _DDnsStaticNameSrvIpPriority_Type()
)
dDnsStaticNameSrvIpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticNameSrvIpPriority.setStatus("current")
_DDnsStaticNameSrvIpRowStatus_Type = RowStatus
_DDnsStaticNameSrvIpRowStatus_Object = MibTableColumn
dDnsStaticNameSrvIpRowStatus = _DDnsStaticNameSrvIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 1, 1, 5),
    _DDnsStaticNameSrvIpRowStatus_Type()
)
dDnsStaticNameSrvIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticNameSrvIpRowStatus.setStatus("current")
_DDnsDynamicNameSrvTable_Object = MibTable
dDnsDynamicNameSrvTable = _DDnsDynamicNameSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2)
)
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvTable.setStatus("current")
_DDnsDynamicNameSrvEntry_Object = MibTableRow
dDnsDynamicNameSrvEntry = _DDnsDynamicNameSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2, 1)
)
dDnsDynamicNameSrvEntry.setIndexNames(
    (0, "DLINKSW-DNS-MIB", "dDnsDynamicNameSrvIpVrfName"),
    (0, "DLINKSW-DNS-MIB", "dDnsDynamicNameSrvIpType"),
    (0, "DLINKSW-DNS-MIB", "dDnsDynamicNameSrvIpAddr"),
)
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvEntry.setStatus("current")


class _DDnsDynamicNameSrvIpVrfName_Type(SnmpAdminString):
    """Custom type dDnsDynamicNameSrvIpVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDnsDynamicNameSrvIpVrfName_Type.__name__ = "SnmpAdminString"
_DDnsDynamicNameSrvIpVrfName_Object = MibTableColumn
dDnsDynamicNameSrvIpVrfName = _DDnsDynamicNameSrvIpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2, 1, 1),
    _DDnsDynamicNameSrvIpVrfName_Type()
)
dDnsDynamicNameSrvIpVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvIpVrfName.setStatus("current")
_DDnsDynamicNameSrvIpType_Type = InetAddressType
_DDnsDynamicNameSrvIpType_Object = MibTableColumn
dDnsDynamicNameSrvIpType = _DDnsDynamicNameSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2, 1, 2),
    _DDnsDynamicNameSrvIpType_Type()
)
dDnsDynamicNameSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvIpType.setStatus("current")


class _DDnsDynamicNameSrvIpAddr_Type(InetAddress):
    """Custom type dDnsDynamicNameSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DDnsDynamicNameSrvIpAddr_Type.__name__ = "InetAddress"
_DDnsDynamicNameSrvIpAddr_Object = MibTableColumn
dDnsDynamicNameSrvIpAddr = _DDnsDynamicNameSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2, 1, 3),
    _DDnsDynamicNameSrvIpAddr_Type()
)
dDnsDynamicNameSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvIpAddr.setStatus("current")


class _DDnsDynamicNameSrvIpPriority_Type(Integer32):
    """Custom type dDnsDynamicNameSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DDnsDynamicNameSrvIpPriority_Type.__name__ = "Integer32"
_DDnsDynamicNameSrvIpPriority_Object = MibTableColumn
dDnsDynamicNameSrvIpPriority = _DDnsDynamicNameSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 9, 2, 1, 4),
    _DDnsDynamicNameSrvIpPriority_Type()
)
dDnsDynamicNameSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvIpPriority.setStatus("current")
_DDnsHost_ObjectIdentity = ObjectIdentity
dDnsHost = _DDnsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10)
)
_DDnsStaticHostTable_Object = MibTable
dDnsStaticHostTable = _DDnsStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2)
)
if mibBuilder.loadTexts:
    dDnsStaticHostTable.setStatus("current")
_DDnsStaticHostEntry_Object = MibTableRow
dDnsStaticHostEntry = _DDnsStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1)
)
dDnsStaticHostEntry.setIndexNames(
    (0, "DLINKSW-DNS-MIB", "dDnsStaticHostIndex"),
)
if mibBuilder.loadTexts:
    dDnsStaticHostEntry.setStatus("current")


class _DDnsStaticHostIndex_Type(Integer32):
    """Custom type dDnsStaticHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DDnsStaticHostIndex_Type.__name__ = "Integer32"
_DDnsStaticHostIndex_Object = MibTableColumn
dDnsStaticHostIndex = _DDnsStaticHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 1),
    _DDnsStaticHostIndex_Type()
)
dDnsStaticHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsStaticHostIndex.setStatus("current")
_DDnsStaticHostVrfName_Type = SnmpAdminString
_DDnsStaticHostVrfName_Object = MibTableColumn
dDnsStaticHostVrfName = _DDnsStaticHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 2),
    _DDnsStaticHostVrfName_Type()
)
dDnsStaticHostVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticHostVrfName.setStatus("current")
_DDnsStaticHostName_Type = SnmpAdminString
_DDnsStaticHostName_Object = MibTableColumn
dDnsStaticHostName = _DDnsStaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 3),
    _DDnsStaticHostName_Type()
)
dDnsStaticHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticHostName.setStatus("current")
_DDnsStaticHostIPType_Type = InetAddressType
_DDnsStaticHostIPType_Object = MibTableColumn
dDnsStaticHostIPType = _DDnsStaticHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 4),
    _DDnsStaticHostIPType_Type()
)
dDnsStaticHostIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticHostIPType.setStatus("current")


class _DDnsStaticHostIPAddr_Type(InetAddress):
    """Custom type dDnsStaticHostIPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DDnsStaticHostIPAddr_Type.__name__ = "InetAddress"
_DDnsStaticHostIPAddr_Object = MibTableColumn
dDnsStaticHostIPAddr = _DDnsStaticHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 5),
    _DDnsStaticHostIPAddr_Type()
)
dDnsStaticHostIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticHostIPAddr.setStatus("current")
_DDnsStaticHostRowStatus_Type = RowStatus
_DDnsStaticHostRowStatus_Object = MibTableColumn
dDnsStaticHostRowStatus = _DDnsStaticHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 2, 1, 7),
    _DDnsStaticHostRowStatus_Type()
)
dDnsStaticHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDnsStaticHostRowStatus.setStatus("current")
_DDnsDynamicHostTable_Object = MibTable
dDnsDynamicHostTable = _DDnsDynamicHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5)
)
if mibBuilder.loadTexts:
    dDnsDynamicHostTable.setStatus("current")
_DDnsDynamicHostEntry_Object = MibTableRow
dDnsDynamicHostEntry = _DDnsDynamicHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1)
)
dDnsDynamicHostEntry.setIndexNames(
    (0, "DLINKSW-DNS-MIB", "dDnsDynamicHostIndex"),
)
if mibBuilder.loadTexts:
    dDnsDynamicHostEntry.setStatus("current")


class _DDnsDynamicHostIndex_Type(Integer32):
    """Custom type dDnsDynamicHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DDnsDynamicHostIndex_Type.__name__ = "Integer32"
_DDnsDynamicHostIndex_Object = MibTableColumn
dDnsDynamicHostIndex = _DDnsDynamicHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 1),
    _DDnsDynamicHostIndex_Type()
)
dDnsDynamicHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDnsDynamicHostIndex.setStatus("current")
_DDnsDynamicHostVrfName_Type = SnmpAdminString
_DDnsDynamicHostVrfName_Object = MibTableColumn
dDnsDynamicHostVrfName = _DDnsDynamicHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 2),
    _DDnsDynamicHostVrfName_Type()
)
dDnsDynamicHostVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicHostVrfName.setStatus("current")
_DDnsDynamicHostName_Type = SnmpAdminString
_DDnsDynamicHostName_Object = MibTableColumn
dDnsDynamicHostName = _DDnsDynamicHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 3),
    _DDnsDynamicHostName_Type()
)
dDnsDynamicHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicHostName.setStatus("current")
_DDnsDynamicHostTTL_Type = DnsTime
_DDnsDynamicHostTTL_Object = MibTableColumn
dDnsDynamicHostTTL = _DDnsDynamicHostTTL_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 4),
    _DDnsDynamicHostTTL_Type()
)
dDnsDynamicHostTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicHostTTL.setStatus("current")
_DDnsDynamicHostIPType_Type = InetAddressType
_DDnsDynamicHostIPType_Object = MibTableColumn
dDnsDynamicHostIPType = _DDnsDynamicHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 5),
    _DDnsDynamicHostIPType_Type()
)
dDnsDynamicHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicHostIPType.setStatus("current")
_DDnsDynamicHostIPAddr_Type = InetAddress
_DDnsDynamicHostIPAddr_Object = MibTableColumn
dDnsDynamicHostIPAddr = _DDnsDynamicHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 6),
    _DDnsDynamicHostIPAddr_Type()
)
dDnsDynamicHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDnsDynamicHostIPAddr.setStatus("current")


class _DDnsDynamicHostClearCtrl_Type(Integer32):
    """Custom type dDnsDynamicHostClearCtrl based on Integer32"""
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


_DDnsDynamicHostClearCtrl_Type.__name__ = "Integer32"
_DDnsDynamicHostClearCtrl_Object = MibTableColumn
dDnsDynamicHostClearCtrl = _DDnsDynamicHostClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 1, 10, 5, 1, 8),
    _DDnsDynamicHostClearCtrl_Type()
)
dDnsDynamicHostClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDnsDynamicHostClearCtrl.setStatus("current")
_DDnsMIBConformance_ObjectIdentity = ObjectIdentity
dDnsMIBConformance = _DDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2)
)
_DDnsMIBCompliances_ObjectIdentity = ObjectIdentity
dDnsMIBCompliances = _DDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 1)
)
_DDnsMIBGroups_ObjectIdentity = ObjectIdentity
dDnsMIBGroups = _DDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2)
)

# Managed Objects groups

dDnsResolverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 1)
)
dDnsResolverGroup.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsResolverSourceInterface"),
        ("DLINKSW-DNS-MIB", "dDnsResolverDomainName"),
        ("DLINKSW-DNS-MIB", "dDnsResolverTimeOut"),
        ("DLINKSW-DNS-MIB", "dDnsResolverEnabled"))
)
if mibBuilder.loadTexts:
    dDnsResolverGroup.setStatus("current")

dDnsCacheSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 2)
)
dDnsCacheSrvGroup.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsCacheSrvMaxForwarderQueue"),
        ("DLINKSW-DNS-MIB", "dDnsCacheSrvEnabled"))
)
if mibBuilder.loadTexts:
    dDnsCacheSrvGroup.setStatus("current")

dDnsStaticHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 3)
)
dDnsStaticHostGroup.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsStaticHostVrfName"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostName"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostRowStatus"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostLookupEnabled"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostIPType"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostIPAddr"))
)
if mibBuilder.loadTexts:
    dDnsStaticHostGroup.setStatus("current")

dDnsDynamicHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 4)
)
dDnsDynamicHostGroup.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsDynamicHostVrfName"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostName"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostTTL"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostClearCtrl"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostLookupEnabled"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostIPType"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostIPAddr"))
)
if mibBuilder.loadTexts:
    dDnsDynamicHostGroup.setStatus("current")

dDnsStaticNameSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 5)
)
dDnsStaticNameSrvGroup.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsStaticNameSrvIpPriority"),
        ("DLINKSW-DNS-MIB", "dDnsStaticNameSrvIpRowStatus"))
)
if mibBuilder.loadTexts:
    dDnsStaticNameSrvGroup.setStatus("current")

dDnsDynamicNameSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 2, 6)
)
dDnsDynamicNameSrvGroup.setObjects(
    ("DLINKSW-DNS-MIB", "dDnsDynamicNameSrvIpPriority")
)
if mibBuilder.loadTexts:
    dDnsDynamicNameSrvGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 77, 2, 1, 1)
)
dDnsMIBCompliance.setObjects(
      *(("DLINKSW-DNS-MIB", "dDnsResolverGroup"),
        ("DLINKSW-DNS-MIB", "dDnsStaticHostGroup"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicHostGroup"),
        ("DLINKSW-DNS-MIB", "dDnsStaticNameSrvGroup"),
        ("DLINKSW-DNS-MIB", "dDnsDynamicNameSrvGroup"),
        ("DLINKSW-DNS-MIB", "dDnsCacheSrvGroup"))
)
if mibBuilder.loadTexts:
    dDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DNS-MIB",
    **{"DnsTime": DnsTime,
       "dlinkSwDnsMIB": dlinkSwDnsMIB,
       "dDnsMIBNotifications": dDnsMIBNotifications,
       "dDnsMIBObjects": dDnsMIBObjects,
       "dDnsGlobal": dDnsGlobal,
       "dDnsResolverEnabled": dDnsResolverEnabled,
       "dDnsResolverSourceInterface": dDnsResolverSourceInterface,
       "dDnsResolverDomainName": dDnsResolverDomainName,
       "dDnsResolverTimeOut": dDnsResolverTimeOut,
       "dDnsCacheSrvEnabled": dDnsCacheSrvEnabled,
       "dDnsCacheSrvMaxForwarderQueue": dDnsCacheSrvMaxForwarderQueue,
       "dDnsStaticHostLookupEnabled": dDnsStaticHostLookupEnabled,
       "dDnsDynamicHostLookupEnabled": dDnsDynamicHostLookupEnabled,
       "dDnsNameSrv": dDnsNameSrv,
       "dDnsStaticNameSrvTable": dDnsStaticNameSrvTable,
       "dDnsStaticNameSrvEntry": dDnsStaticNameSrvEntry,
       "dDnsStaticNameSrvIpVrfName": dDnsStaticNameSrvIpVrfName,
       "dDnsStaticNameSrvIpType": dDnsStaticNameSrvIpType,
       "dDnsStaticNameSrvIpAddr": dDnsStaticNameSrvIpAddr,
       "dDnsStaticNameSrvIpPriority": dDnsStaticNameSrvIpPriority,
       "dDnsStaticNameSrvIpRowStatus": dDnsStaticNameSrvIpRowStatus,
       "dDnsDynamicNameSrvTable": dDnsDynamicNameSrvTable,
       "dDnsDynamicNameSrvEntry": dDnsDynamicNameSrvEntry,
       "dDnsDynamicNameSrvIpVrfName": dDnsDynamicNameSrvIpVrfName,
       "dDnsDynamicNameSrvIpType": dDnsDynamicNameSrvIpType,
       "dDnsDynamicNameSrvIpAddr": dDnsDynamicNameSrvIpAddr,
       "dDnsDynamicNameSrvIpPriority": dDnsDynamicNameSrvIpPriority,
       "dDnsHost": dDnsHost,
       "dDnsStaticHostTable": dDnsStaticHostTable,
       "dDnsStaticHostEntry": dDnsStaticHostEntry,
       "dDnsStaticHostIndex": dDnsStaticHostIndex,
       "dDnsStaticHostVrfName": dDnsStaticHostVrfName,
       "dDnsStaticHostName": dDnsStaticHostName,
       "dDnsStaticHostIPType": dDnsStaticHostIPType,
       "dDnsStaticHostIPAddr": dDnsStaticHostIPAddr,
       "dDnsStaticHostRowStatus": dDnsStaticHostRowStatus,
       "dDnsDynamicHostTable": dDnsDynamicHostTable,
       "dDnsDynamicHostEntry": dDnsDynamicHostEntry,
       "dDnsDynamicHostIndex": dDnsDynamicHostIndex,
       "dDnsDynamicHostVrfName": dDnsDynamicHostVrfName,
       "dDnsDynamicHostName": dDnsDynamicHostName,
       "dDnsDynamicHostTTL": dDnsDynamicHostTTL,
       "dDnsDynamicHostIPType": dDnsDynamicHostIPType,
       "dDnsDynamicHostIPAddr": dDnsDynamicHostIPAddr,
       "dDnsDynamicHostClearCtrl": dDnsDynamicHostClearCtrl,
       "dDnsMIBConformance": dDnsMIBConformance,
       "dDnsMIBCompliances": dDnsMIBCompliances,
       "dDnsMIBCompliance": dDnsMIBCompliance,
       "dDnsMIBGroups": dDnsMIBGroups,
       "dDnsResolverGroup": dDnsResolverGroup,
       "dDnsCacheSrvGroup": dDnsCacheSrvGroup,
       "dDnsStaticHostGroup": dDnsStaticHostGroup,
       "dDnsDynamicHostGroup": dDnsDynamicHostGroup,
       "dDnsStaticNameSrvGroup": dDnsStaticNameSrvGroup,
       "dDnsDynamicNameSrvGroup": dDnsDynamicNameSrvGroup}
)
