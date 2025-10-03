# SNMP MIB module (SLE-DHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DHCPV6-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:26 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleDhcp6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleDhcp6Base_ObjectIdentity = ObjectIdentity
sleDhcp6Base = _SleDhcp6Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1)
)
_SleDhcp6BaseInfo_ObjectIdentity = ObjectIdentity
sleDhcp6BaseInfo = _SleDhcp6BaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 1)
)
_SleDhcp6Duid_Type = OctetString
_SleDhcp6Duid_Object = MibScalar
sleDhcp6Duid = _SleDhcp6Duid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 1, 1),
    _SleDhcp6Duid_Type()
)
sleDhcp6Duid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6Duid.setStatus("current")
_SleDhcp6DatabaseAddr_Type = IpAddress
_SleDhcp6DatabaseAddr_Object = MibScalar
sleDhcp6DatabaseAddr = _SleDhcp6DatabaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 1, 2),
    _SleDhcp6DatabaseAddr_Type()
)
sleDhcp6DatabaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6DatabaseAddr.setStatus("current")


class _SleDhcp6DatabaseInterval_Type(Integer32):
    """Custom type sleDhcp6DatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 315360000),
    )


_SleDhcp6DatabaseInterval_Type.__name__ = "Integer32"
_SleDhcp6DatabaseInterval_Object = MibScalar
sleDhcp6DatabaseInterval = _SleDhcp6DatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 1, 3),
    _SleDhcp6DatabaseInterval_Type()
)
sleDhcp6DatabaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6DatabaseInterval.setStatus("current")
_SleDhcp6BaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6BaseControl = _SleDhcp6BaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2)
)


class _SleDhcp6BaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6BaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Database", 1),
          ("destroyDhcp6Database", 2))
    )


_SleDhcp6BaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6BaseControlRequest_Object = MibScalar
sleDhcp6BaseControlRequest = _SleDhcp6BaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 1),
    _SleDhcp6BaseControlRequest_Type()
)
sleDhcp6BaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlRequest.setStatus("current")
_SleDhcp6BaseControlStatus_Type = SleControlStatusType
_SleDhcp6BaseControlStatus_Object = MibScalar
sleDhcp6BaseControlStatus = _SleDhcp6BaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 2),
    _SleDhcp6BaseControlStatus_Type()
)
sleDhcp6BaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlStatus.setStatus("current")
_SleDhcp6BaseControlTimer_Type = Gauge32
_SleDhcp6BaseControlTimer_Object = MibScalar
sleDhcp6BaseControlTimer = _SleDhcp6BaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 3),
    _SleDhcp6BaseControlTimer_Type()
)
sleDhcp6BaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlTimer.setStatus("current")
_SleDhcp6BaseControlTimeStamp_Type = TimeTicks
_SleDhcp6BaseControlTimeStamp_Object = MibScalar
sleDhcp6BaseControlTimeStamp = _SleDhcp6BaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 4),
    _SleDhcp6BaseControlTimeStamp_Type()
)
sleDhcp6BaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlTimeStamp.setStatus("current")
_SleDhcp6BaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6BaseControlReqResult_Object = MibScalar
sleDhcp6BaseControlReqResult = _SleDhcp6BaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 5),
    _SleDhcp6BaseControlReqResult_Type()
)
sleDhcp6BaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlReqResult.setStatus("current")
_SleDhcp6BaseControlDatabaseAddr_Type = IpAddress
_SleDhcp6BaseControlDatabaseAddr_Object = MibScalar
sleDhcp6BaseControlDatabaseAddr = _SleDhcp6BaseControlDatabaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 6),
    _SleDhcp6BaseControlDatabaseAddr_Type()
)
sleDhcp6BaseControlDatabaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlDatabaseAddr.setStatus("current")


class _SleDhcp6BaseControlDatabaseInterval_Type(Integer32):
    """Custom type sleDhcp6BaseControlDatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 315360000),
    )


_SleDhcp6BaseControlDatabaseInterval_Type.__name__ = "Integer32"
_SleDhcp6BaseControlDatabaseInterval_Object = MibScalar
sleDhcp6BaseControlDatabaseInterval = _SleDhcp6BaseControlDatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 2, 7),
    _SleDhcp6BaseControlDatabaseInterval_Type()
)
sleDhcp6BaseControlDatabaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BaseControlDatabaseInterval.setStatus("current")
_SleDhcp6BaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6BaseNotification = _SleDhcp6BaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 3)
)
_SleDhcp6Pool_ObjectIdentity = ObjectIdentity
sleDhcp6Pool = _SleDhcp6Pool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2)
)
_SleDhcp6PoolBase_ObjectIdentity = ObjectIdentity
sleDhcp6PoolBase = _SleDhcp6PoolBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1)
)
_SleDhcp6PoolTable_Object = MibTable
sleDhcp6PoolTable = _SleDhcp6PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6PoolTable.setStatus("current")
_SleDhcp6PoolEntry_Object = MibTableRow
sleDhcp6PoolEntry = _SleDhcp6PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1)
)
sleDhcp6PoolEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6PoolEntry.setStatus("current")


class _SleDhcp6PoolIndex_Type(Integer32):
    """Custom type sleDhcp6PoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6PoolIndex_Type.__name__ = "Integer32"
_SleDhcp6PoolIndex_Object = MibTableColumn
sleDhcp6PoolIndex = _SleDhcp6PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 1),
    _SleDhcp6PoolIndex_Type()
)
sleDhcp6PoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolIndex.setStatus("current")


class _SleDhcp6PoolName_Type(OctetString):
    """Custom type sleDhcp6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6PoolName_Type.__name__ = "OctetString"
_SleDhcp6PoolName_Object = MibTableColumn
sleDhcp6PoolName = _SleDhcp6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 2),
    _SleDhcp6PoolName_Type()
)
sleDhcp6PoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolName.setStatus("current")
_SleDhcp6PoolStaticEntry_Type = Integer32
_SleDhcp6PoolStaticEntry_Object = MibTableColumn
sleDhcp6PoolStaticEntry = _SleDhcp6PoolStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 3),
    _SleDhcp6PoolStaticEntry_Type()
)
sleDhcp6PoolStaticEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolStaticEntry.setStatus("current")
_SleDhcp6PoolDynamicEntry_Type = Integer32
_SleDhcp6PoolDynamicEntry_Object = MibTableColumn
sleDhcp6PoolDynamicEntry = _SleDhcp6PoolDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 4),
    _SleDhcp6PoolDynamicEntry_Type()
)
sleDhcp6PoolDynamicEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolDynamicEntry.setStatus("current")


class _SleDhcp6PoolImportDns_Type(Integer32):
    """Custom type sleDhcp6PoolImportDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportDns_Type.__name__ = "Integer32"
_SleDhcp6PoolImportDns_Object = MibTableColumn
sleDhcp6PoolImportDns = _SleDhcp6PoolImportDns_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 5),
    _SleDhcp6PoolImportDns_Type()
)
sleDhcp6PoolImportDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportDns.setStatus("current")


class _SleDhcp6PoolImportDomain_Type(Integer32):
    """Custom type sleDhcp6PoolImportDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportDomain_Type.__name__ = "Integer32"
_SleDhcp6PoolImportDomain_Object = MibTableColumn
sleDhcp6PoolImportDomain = _SleDhcp6PoolImportDomain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 6),
    _SleDhcp6PoolImportDomain_Type()
)
sleDhcp6PoolImportDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportDomain.setStatus("current")


class _SleDhcp6PoolImportInfoRef_Type(Integer32):
    """Custom type sleDhcp6PoolImportInfoRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportInfoRef_Type.__name__ = "Integer32"
_SleDhcp6PoolImportInfoRef_Object = MibTableColumn
sleDhcp6PoolImportInfoRef = _SleDhcp6PoolImportInfoRef_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 7),
    _SleDhcp6PoolImportInfoRef_Type()
)
sleDhcp6PoolImportInfoRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportInfoRef.setStatus("current")


class _SleDhcp6PoolImportNisAdd_Type(Integer32):
    """Custom type sleDhcp6PoolImportNisAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportNisAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolImportNisAdd_Object = MibTableColumn
sleDhcp6PoolImportNisAdd = _SleDhcp6PoolImportNisAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 8),
    _SleDhcp6PoolImportNisAdd_Type()
)
sleDhcp6PoolImportNisAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportNisAdd.setStatus("current")


class _SleDhcp6PoolImportNisDom_Type(Integer32):
    """Custom type sleDhcp6PoolImportNisDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportNisDom_Type.__name__ = "Integer32"
_SleDhcp6PoolImportNisDom_Object = MibTableColumn
sleDhcp6PoolImportNisDom = _SleDhcp6PoolImportNisDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 9),
    _SleDhcp6PoolImportNisDom_Type()
)
sleDhcp6PoolImportNisDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportNisDom.setStatus("current")


class _SleDhcp6PoolImportNispAdd_Type(Integer32):
    """Custom type sleDhcp6PoolImportNispAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportNispAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolImportNispAdd_Object = MibTableColumn
sleDhcp6PoolImportNispAdd = _SleDhcp6PoolImportNispAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 10),
    _SleDhcp6PoolImportNispAdd_Type()
)
sleDhcp6PoolImportNispAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportNispAdd.setStatus("current")


class _SleDhcp6PoolImportNispDom_Type(Integer32):
    """Custom type sleDhcp6PoolImportNispDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportNispDom_Type.__name__ = "Integer32"
_SleDhcp6PoolImportNispDom_Object = MibTableColumn
sleDhcp6PoolImportNispDom = _SleDhcp6PoolImportNispDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 11),
    _SleDhcp6PoolImportNispDom_Type()
)
sleDhcp6PoolImportNispDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportNispDom.setStatus("current")


class _SleDhcp6PoolImportSipAdd_Type(Integer32):
    """Custom type sleDhcp6PoolImportSipAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportSipAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolImportSipAdd_Object = MibTableColumn
sleDhcp6PoolImportSipAdd = _SleDhcp6PoolImportSipAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 12),
    _SleDhcp6PoolImportSipAdd_Type()
)
sleDhcp6PoolImportSipAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportSipAdd.setStatus("current")


class _SleDhcp6PoolImportSipDom_Type(Integer32):
    """Custom type sleDhcp6PoolImportSipDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportSipDom_Type.__name__ = "Integer32"
_SleDhcp6PoolImportSipDom_Object = MibTableColumn
sleDhcp6PoolImportSipDom = _SleDhcp6PoolImportSipDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 13),
    _SleDhcp6PoolImportSipDom_Type()
)
sleDhcp6PoolImportSipDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportSipDom.setStatus("current")


class _SleDhcp6PoolImportSntpAdd_Type(Integer32):
    """Custom type sleDhcp6PoolImportSntpAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolImportSntpAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolImportSntpAdd_Object = MibTableColumn
sleDhcp6PoolImportSntpAdd = _SleDhcp6PoolImportSntpAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 14),
    _SleDhcp6PoolImportSntpAdd_Type()
)
sleDhcp6PoolImportSntpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolImportSntpAdd.setStatus("current")


class _SleDhcp6PoolInfoRefTime_Type(Integer32):
    """Custom type sleDhcp6PoolInfoRefTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 315360000),
    )


_SleDhcp6PoolInfoRefTime_Type.__name__ = "Integer32"
_SleDhcp6PoolInfoRefTime_Object = MibTableColumn
sleDhcp6PoolInfoRefTime = _SleDhcp6PoolInfoRefTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 15),
    _SleDhcp6PoolInfoRefTime_Type()
)
sleDhcp6PoolInfoRefTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolInfoRefTime.setStatus("current")


class _SleDhcp6PoolAaaValTime_Type(Integer32):
    """Custom type sleDhcp6PoolAaaValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolAaaValTime_Type.__name__ = "Integer32"
_SleDhcp6PoolAaaValTime_Object = MibTableColumn
sleDhcp6PoolAaaValTime = _SleDhcp6PoolAaaValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 16),
    _SleDhcp6PoolAaaValTime_Type()
)
sleDhcp6PoolAaaValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolAaaValTime.setStatus("current")


class _SleDhcp6PoolAaaPreTime_Type(Integer32):
    """Custom type sleDhcp6PoolAaaPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolAaaPreTime_Type.__name__ = "Integer32"
_SleDhcp6PoolAaaPreTime_Object = MibTableColumn
sleDhcp6PoolAaaPreTime = _SleDhcp6PoolAaaPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 17),
    _SleDhcp6PoolAaaPreTime_Type()
)
sleDhcp6PoolAaaPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolAaaPreTime.setStatus("current")
_SleDhcp6PoolPdName_Type = OctetString
_SleDhcp6PoolPdName_Object = MibTableColumn
sleDhcp6PoolPdName = _SleDhcp6PoolPdName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 18),
    _SleDhcp6PoolPdName_Type()
)
sleDhcp6PoolPdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolPdName.setStatus("current")


class _SleDhcp6PoolPdValTime_Type(Integer32):
    """Custom type sleDhcp6PoolPdValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolPdValTime_Type.__name__ = "Integer32"
_SleDhcp6PoolPdValTime_Object = MibTableColumn
sleDhcp6PoolPdValTime = _SleDhcp6PoolPdValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 19),
    _SleDhcp6PoolPdValTime_Type()
)
sleDhcp6PoolPdValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolPdValTime.setStatus("current")


class _SleDhcp6PoolPdPreTime_Type(Integer32):
    """Custom type sleDhcp6PoolPdPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolPdPreTime_Type.__name__ = "Integer32"
_SleDhcp6PoolPdPreTime_Object = MibTableColumn
sleDhcp6PoolPdPreTime = _SleDhcp6PoolPdPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 1, 1, 20),
    _SleDhcp6PoolPdPreTime_Type()
)
sleDhcp6PoolPdPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolPdPreTime.setStatus("current")
_SleDhcp6PoolBaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6PoolBaseControl = _SleDhcp6PoolBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2)
)


class _SleDhcp6PoolBaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlRequest based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Pool", 1),
          ("destroyDhcp6Pool", 2),
          ("setPoolImportDns", 3),
          ("setPoolImportDomain", 4),
          ("setPoolImportInfoRef", 5),
          ("setPoolImportNisAdd", 6),
          ("setPoolImportNisDom", 7),
          ("setPoolImportNispAdd", 8),
          ("setPoolImportNispDom", 9),
          ("setPoolImportSipAdd", 10),
          ("setPoolImportSipDom", 11),
          ("setPoolImportSntpAdd", 12),
          ("setPoolInfoRefTime", 13),
          ("createPoolAaaTime", 14),
          ("destroyPoolAaaTime", 15),
          ("createPdPool", 16),
          ("destroyPdPool", 17))
    )


_SleDhcp6PoolBaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlRequest_Object = MibScalar
sleDhcp6PoolBaseControlRequest = _SleDhcp6PoolBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 1),
    _SleDhcp6PoolBaseControlRequest_Type()
)
sleDhcp6PoolBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlRequest.setStatus("current")
_SleDhcp6PoolBaseControlStatus_Type = SleControlStatusType
_SleDhcp6PoolBaseControlStatus_Object = MibScalar
sleDhcp6PoolBaseControlStatus = _SleDhcp6PoolBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 2),
    _SleDhcp6PoolBaseControlStatus_Type()
)
sleDhcp6PoolBaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlStatus.setStatus("current")
_SleDhcp6PoolBaseControlTimer_Type = Gauge32
_SleDhcp6PoolBaseControlTimer_Object = MibScalar
sleDhcp6PoolBaseControlTimer = _SleDhcp6PoolBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 3),
    _SleDhcp6PoolBaseControlTimer_Type()
)
sleDhcp6PoolBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlTimer.setStatus("current")
_SleDhcp6PoolBaseControlTimeStamp_Type = TimeTicks
_SleDhcp6PoolBaseControlTimeStamp_Object = MibScalar
sleDhcp6PoolBaseControlTimeStamp = _SleDhcp6PoolBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 4),
    _SleDhcp6PoolBaseControlTimeStamp_Type()
)
sleDhcp6PoolBaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlTimeStamp.setStatus("current")
_SleDhcp6PoolBaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6PoolBaseControlReqResult_Object = MibScalar
sleDhcp6PoolBaseControlReqResult = _SleDhcp6PoolBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 5),
    _SleDhcp6PoolBaseControlReqResult_Type()
)
sleDhcp6PoolBaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlReqResult.setStatus("current")
_SleDhcp6PoolBaseControlIndex_Type = Integer32
_SleDhcp6PoolBaseControlIndex_Object = MibScalar
sleDhcp6PoolBaseControlIndex = _SleDhcp6PoolBaseControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 6),
    _SleDhcp6PoolBaseControlIndex_Type()
)
sleDhcp6PoolBaseControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlIndex.setStatus("current")


class _SleDhcp6PoolBaseControlName_Type(OctetString):
    """Custom type sleDhcp6PoolBaseControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6PoolBaseControlName_Type.__name__ = "OctetString"
_SleDhcp6PoolBaseControlName_Object = MibScalar
sleDhcp6PoolBaseControlName = _SleDhcp6PoolBaseControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 7),
    _SleDhcp6PoolBaseControlName_Type()
)
sleDhcp6PoolBaseControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlName.setStatus("current")


class _SleDhcp6PoolBaseControlImportDns_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportDns_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportDns_Object = MibScalar
sleDhcp6PoolBaseControlImportDns = _SleDhcp6PoolBaseControlImportDns_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 8),
    _SleDhcp6PoolBaseControlImportDns_Type()
)
sleDhcp6PoolBaseControlImportDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportDns.setStatus("current")


class _SleDhcp6PoolBaseControlImportDomain_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportDomain_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportDomain_Object = MibScalar
sleDhcp6PoolBaseControlImportDomain = _SleDhcp6PoolBaseControlImportDomain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 9),
    _SleDhcp6PoolBaseControlImportDomain_Type()
)
sleDhcp6PoolBaseControlImportDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportDomain.setStatus("current")


class _SleDhcp6PoolBaseControlImportInfoRef_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportInfoRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportInfoRef_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportInfoRef_Object = MibScalar
sleDhcp6PoolBaseControlImportInfoRef = _SleDhcp6PoolBaseControlImportInfoRef_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 10),
    _SleDhcp6PoolBaseControlImportInfoRef_Type()
)
sleDhcp6PoolBaseControlImportInfoRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportInfoRef.setStatus("current")


class _SleDhcp6PoolBaseControlImportNisAdd_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportNisAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportNisAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportNisAdd_Object = MibScalar
sleDhcp6PoolBaseControlImportNisAdd = _SleDhcp6PoolBaseControlImportNisAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 11),
    _SleDhcp6PoolBaseControlImportNisAdd_Type()
)
sleDhcp6PoolBaseControlImportNisAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportNisAdd.setStatus("current")


class _SleDhcp6PoolBaseControlImportNisDom_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportNisDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportNisDom_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportNisDom_Object = MibScalar
sleDhcp6PoolBaseControlImportNisDom = _SleDhcp6PoolBaseControlImportNisDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 12),
    _SleDhcp6PoolBaseControlImportNisDom_Type()
)
sleDhcp6PoolBaseControlImportNisDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportNisDom.setStatus("current")


class _SleDhcp6PoolBaseControlImportNispAdd_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportNispAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportNispAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportNispAdd_Object = MibScalar
sleDhcp6PoolBaseControlImportNispAdd = _SleDhcp6PoolBaseControlImportNispAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 13),
    _SleDhcp6PoolBaseControlImportNispAdd_Type()
)
sleDhcp6PoolBaseControlImportNispAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportNispAdd.setStatus("current")


class _SleDhcp6PoolBaseControlImportNispDom_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportNispDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportNispDom_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportNispDom_Object = MibScalar
sleDhcp6PoolBaseControlImportNispDom = _SleDhcp6PoolBaseControlImportNispDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 14),
    _SleDhcp6PoolBaseControlImportNispDom_Type()
)
sleDhcp6PoolBaseControlImportNispDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportNispDom.setStatus("current")


class _SleDhcp6PoolBaseControlImportSipAdd_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportSipAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportSipAdd_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportSipAdd_Object = MibScalar
sleDhcp6PoolBaseControlImportSipAdd = _SleDhcp6PoolBaseControlImportSipAdd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 15),
    _SleDhcp6PoolBaseControlImportSipAdd_Type()
)
sleDhcp6PoolBaseControlImportSipAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportSipAdd.setStatus("current")


class _SleDhcp6PoolBaseControlImportSipDom_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportSipDom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportSipDom_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportSipDom_Object = MibScalar
sleDhcp6PoolBaseControlImportSipDom = _SleDhcp6PoolBaseControlImportSipDom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 16),
    _SleDhcp6PoolBaseControlImportSipDom_Type()
)
sleDhcp6PoolBaseControlImportSipDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportSipDom.setStatus("current")


class _SleDhcp6PoolBaseControlImportSntpAddr_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlImportSntpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6PoolBaseControlImportSntpAddr_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlImportSntpAddr_Object = MibScalar
sleDhcp6PoolBaseControlImportSntpAddr = _SleDhcp6PoolBaseControlImportSntpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 17),
    _SleDhcp6PoolBaseControlImportSntpAddr_Type()
)
sleDhcp6PoolBaseControlImportSntpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlImportSntpAddr.setStatus("current")


class _SleDhcp6PoolBaseControlInfoRefTime_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlInfoRefTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 315360000),
    )


_SleDhcp6PoolBaseControlInfoRefTime_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlInfoRefTime_Object = MibScalar
sleDhcp6PoolBaseControlInfoRefTime = _SleDhcp6PoolBaseControlInfoRefTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 18),
    _SleDhcp6PoolBaseControlInfoRefTime_Type()
)
sleDhcp6PoolBaseControlInfoRefTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlInfoRefTime.setStatus("current")


class _SleDhcp6PoolBaseControlAaaValTime_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlAaaValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolBaseControlAaaValTime_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlAaaValTime_Object = MibScalar
sleDhcp6PoolBaseControlAaaValTime = _SleDhcp6PoolBaseControlAaaValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 19),
    _SleDhcp6PoolBaseControlAaaValTime_Type()
)
sleDhcp6PoolBaseControlAaaValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlAaaValTime.setStatus("current")


class _SleDhcp6PoolBaseControlAaaPreTime_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlAaaPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolBaseControlAaaPreTime_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlAaaPreTime_Object = MibScalar
sleDhcp6PoolBaseControlAaaPreTime = _SleDhcp6PoolBaseControlAaaPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 20),
    _SleDhcp6PoolBaseControlAaaPreTime_Type()
)
sleDhcp6PoolBaseControlAaaPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlAaaPreTime.setStatus("current")
_SleDhcp6PoolBaseControlPdName_Type = OctetString
_SleDhcp6PoolBaseControlPdName_Object = MibScalar
sleDhcp6PoolBaseControlPdName = _SleDhcp6PoolBaseControlPdName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 21),
    _SleDhcp6PoolBaseControlPdName_Type()
)
sleDhcp6PoolBaseControlPdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlPdName.setStatus("current")


class _SleDhcp6PoolBaseControlPdValTime_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlPdValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolBaseControlPdValTime_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlPdValTime_Object = MibScalar
sleDhcp6PoolBaseControlPdValTime = _SleDhcp6PoolBaseControlPdValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 22),
    _SleDhcp6PoolBaseControlPdValTime_Type()
)
sleDhcp6PoolBaseControlPdValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlPdValTime.setStatus("current")


class _SleDhcp6PoolBaseControlPdPreTime_Type(Integer32):
    """Custom type sleDhcp6PoolBaseControlPdPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6PoolBaseControlPdPreTime_Type.__name__ = "Integer32"
_SleDhcp6PoolBaseControlPdPreTime_Object = MibScalar
sleDhcp6PoolBaseControlPdPreTime = _SleDhcp6PoolBaseControlPdPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 2, 23),
    _SleDhcp6PoolBaseControlPdPreTime_Type()
)
sleDhcp6PoolBaseControlPdPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6PoolBaseControlPdPreTime.setStatus("current")
_SleDhcp6PoolBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6PoolBaseNotification = _SleDhcp6PoolBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3)
)
_SleDhcp6FixedAddr_ObjectIdentity = ObjectIdentity
sleDhcp6FixedAddr = _SleDhcp6FixedAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2)
)
_SleDhcp6FixedAddrTable_Object = MibTable
sleDhcp6FixedAddrTable = _SleDhcp6FixedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrTable.setStatus("current")
_SleDhcp6FixedAddrEntry_Object = MibTableRow
sleDhcp6FixedAddrEntry = _SleDhcp6FixedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1)
)
sleDhcp6FixedAddrEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6FixedAddrIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrEntry.setStatus("current")


class _SleDhcp6FixedAddrIndex_Type(Integer32):
    """Custom type sleDhcp6FixedAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6FixedAddrIndex_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrIndex_Object = MibTableColumn
sleDhcp6FixedAddrIndex = _SleDhcp6FixedAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1, 1),
    _SleDhcp6FixedAddrIndex_Type()
)
sleDhcp6FixedAddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrIndex.setStatus("current")
_SleDhcp6FixedAddrAddress_Type = OctetString
_SleDhcp6FixedAddrAddress_Object = MibTableColumn
sleDhcp6FixedAddrAddress = _SleDhcp6FixedAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1, 2),
    _SleDhcp6FixedAddrAddress_Type()
)
sleDhcp6FixedAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrAddress.setStatus("current")
_SleDhcp6FixedAddrDuid_Type = OctetString
_SleDhcp6FixedAddrDuid_Object = MibTableColumn
sleDhcp6FixedAddrDuid = _SleDhcp6FixedAddrDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1, 3),
    _SleDhcp6FixedAddrDuid_Type()
)
sleDhcp6FixedAddrDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrDuid.setStatus("current")


class _SleDhcp6FixedAddrValTime_Type(Integer32):
    """Custom type sleDhcp6FixedAddrValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedAddrValTime_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrValTime_Object = MibTableColumn
sleDhcp6FixedAddrValTime = _SleDhcp6FixedAddrValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1, 4),
    _SleDhcp6FixedAddrValTime_Type()
)
sleDhcp6FixedAddrValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrValTime.setStatus("current")


class _SleDhcp6FixedAddrPreTime_Type(Integer32):
    """Custom type sleDhcp6FixedAddrPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedAddrPreTime_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrPreTime_Object = MibTableColumn
sleDhcp6FixedAddrPreTime = _SleDhcp6FixedAddrPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 1, 1, 5),
    _SleDhcp6FixedAddrPreTime_Type()
)
sleDhcp6FixedAddrPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrPreTime.setStatus("current")
_SleDhcp6FixedAddrControl_ObjectIdentity = ObjectIdentity
sleDhcp6FixedAddrControl = _SleDhcp6FixedAddrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2)
)


class _SleDhcp6FixedAddrControlRequest_Type(Integer32):
    """Custom type sleDhcp6FixedAddrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6FixedAddr", 1),
          ("destroyDhcp6FixedAddr", 2))
    )


_SleDhcp6FixedAddrControlRequest_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrControlRequest_Object = MibScalar
sleDhcp6FixedAddrControlRequest = _SleDhcp6FixedAddrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 1),
    _SleDhcp6FixedAddrControlRequest_Type()
)
sleDhcp6FixedAddrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlRequest.setStatus("current")
_SleDhcp6FixedAddrControlStatus_Type = SleControlStatusType
_SleDhcp6FixedAddrControlStatus_Object = MibScalar
sleDhcp6FixedAddrControlStatus = _SleDhcp6FixedAddrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 2),
    _SleDhcp6FixedAddrControlStatus_Type()
)
sleDhcp6FixedAddrControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlStatus.setStatus("current")
_SleDhcp6FixedAddrControlTimer_Type = Gauge32
_SleDhcp6FixedAddrControlTimer_Object = MibScalar
sleDhcp6FixedAddrControlTimer = _SleDhcp6FixedAddrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 3),
    _SleDhcp6FixedAddrControlTimer_Type()
)
sleDhcp6FixedAddrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlTimer.setStatus("current")
_SleDhcp6FixedAddrControlTimeStamp_Type = TimeTicks
_SleDhcp6FixedAddrControlTimeStamp_Object = MibScalar
sleDhcp6FixedAddrControlTimeStamp = _SleDhcp6FixedAddrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 4),
    _SleDhcp6FixedAddrControlTimeStamp_Type()
)
sleDhcp6FixedAddrControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlTimeStamp.setStatus("current")
_SleDhcp6FixedAddrControlReqResult_Type = SleControlRequestResultType
_SleDhcp6FixedAddrControlReqResult_Object = MibScalar
sleDhcp6FixedAddrControlReqResult = _SleDhcp6FixedAddrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 5),
    _SleDhcp6FixedAddrControlReqResult_Type()
)
sleDhcp6FixedAddrControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlReqResult.setStatus("current")
_SleDhcp6FixedAddrControlPoolIndex_Type = Integer32
_SleDhcp6FixedAddrControlPoolIndex_Object = MibScalar
sleDhcp6FixedAddrControlPoolIndex = _SleDhcp6FixedAddrControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 6),
    _SleDhcp6FixedAddrControlPoolIndex_Type()
)
sleDhcp6FixedAddrControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlPoolIndex.setStatus("current")
_SleDhcp6FixedAddrControlIndex_Type = Integer32
_SleDhcp6FixedAddrControlIndex_Object = MibScalar
sleDhcp6FixedAddrControlIndex = _SleDhcp6FixedAddrControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 7),
    _SleDhcp6FixedAddrControlIndex_Type()
)
sleDhcp6FixedAddrControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlIndex.setStatus("current")
_SleDhcp6FixedAddrControlAddress_Type = OctetString
_SleDhcp6FixedAddrControlAddress_Object = MibScalar
sleDhcp6FixedAddrControlAddress = _SleDhcp6FixedAddrControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 8),
    _SleDhcp6FixedAddrControlAddress_Type()
)
sleDhcp6FixedAddrControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlAddress.setStatus("current")
_SleDhcp6FixedAddrControlDuid_Type = OctetString
_SleDhcp6FixedAddrControlDuid_Object = MibScalar
sleDhcp6FixedAddrControlDuid = _SleDhcp6FixedAddrControlDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 9),
    _SleDhcp6FixedAddrControlDuid_Type()
)
sleDhcp6FixedAddrControlDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlDuid.setStatus("current")


class _SleDhcp6FixedAddrControlValTime_Type(Integer32):
    """Custom type sleDhcp6FixedAddrControlValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedAddrControlValTime_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrControlValTime_Object = MibScalar
sleDhcp6FixedAddrControlValTime = _SleDhcp6FixedAddrControlValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 10),
    _SleDhcp6FixedAddrControlValTime_Type()
)
sleDhcp6FixedAddrControlValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlValTime.setStatus("current")


class _SleDhcp6FixedAddrControlPreTime_Type(Integer32):
    """Custom type sleDhcp6FixedAddrControlPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedAddrControlPreTime_Type.__name__ = "Integer32"
_SleDhcp6FixedAddrControlPreTime_Object = MibScalar
sleDhcp6FixedAddrControlPreTime = _SleDhcp6FixedAddrControlPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 2, 11),
    _SleDhcp6FixedAddrControlPreTime_Type()
)
sleDhcp6FixedAddrControlPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrControlPreTime.setStatus("current")
_SleDhcp6FixedAddrNotification_ObjectIdentity = ObjectIdentity
sleDhcp6FixedAddrNotification = _SleDhcp6FixedAddrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 3)
)
_SleDhcp6ServerOption_ObjectIdentity = ObjectIdentity
sleDhcp6ServerOption = _SleDhcp6ServerOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3)
)
_SleDhcp6ServerOptionTable_Object = MibTable
sleDhcp6ServerOptionTable = _SleDhcp6ServerOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionTable.setStatus("current")
_SleDhcp6ServerOptionEntry_Object = MibTableRow
sleDhcp6ServerOptionEntry = _SleDhcp6ServerOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1, 1)
)
sleDhcp6ServerOptionEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ServerOptionIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ServerOptionCode"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionEntry.setStatus("current")


class _SleDhcp6ServerOptionCode_Type(Integer32):
    """Custom type sleDhcp6ServerOptionCode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("nisAddress", 1),
          ("nisDomain", 2),
          ("nispAddress", 3),
          ("nispDomain", 4),
          ("sipAddress", 5),
          ("sipDomain", 6),
          ("sntpAddress", 7),
          ("domainName", 8),
          ("dnsServer", 9))
    )


_SleDhcp6ServerOptionCode_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionCode_Object = MibTableColumn
sleDhcp6ServerOptionCode = _SleDhcp6ServerOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1, 1, 1),
    _SleDhcp6ServerOptionCode_Type()
)
sleDhcp6ServerOptionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionCode.setStatus("current")


class _SleDhcp6ServerOptionIndex_Type(Integer32):
    """Custom type sleDhcp6ServerOptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SleDhcp6ServerOptionIndex_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionIndex_Object = MibTableColumn
sleDhcp6ServerOptionIndex = _SleDhcp6ServerOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1, 1, 2),
    _SleDhcp6ServerOptionIndex_Type()
)
sleDhcp6ServerOptionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionIndex.setStatus("current")


class _SleDhcp6ServerOptionType_Type(Integer32):
    """Custom type sleDhcp6ServerOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6address", 1),
          ("text", 2))
    )


_SleDhcp6ServerOptionType_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionType_Object = MibTableColumn
sleDhcp6ServerOptionType = _SleDhcp6ServerOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1, 1, 3),
    _SleDhcp6ServerOptionType_Type()
)
sleDhcp6ServerOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionType.setStatus("current")
_SleDhcp6ServerOptionValue_Type = OctetString
_SleDhcp6ServerOptionValue_Object = MibTableColumn
sleDhcp6ServerOptionValue = _SleDhcp6ServerOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 1, 1, 4),
    _SleDhcp6ServerOptionValue_Type()
)
sleDhcp6ServerOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionValue.setStatus("current")
_SleDhcp6ServerOptionControl_ObjectIdentity = ObjectIdentity
sleDhcp6ServerOptionControl = _SleDhcp6ServerOptionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2)
)


class _SleDhcp6ServerOptionControlRequest_Type(Integer32):
    """Custom type sleDhcp6ServerOptionControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6ServerOption", 1),
          ("destroyDhcp6ServerOption", 2))
    )


_SleDhcp6ServerOptionControlRequest_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionControlRequest_Object = MibScalar
sleDhcp6ServerOptionControlRequest = _SleDhcp6ServerOptionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 1),
    _SleDhcp6ServerOptionControlRequest_Type()
)
sleDhcp6ServerOptionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlRequest.setStatus("current")
_SleDhcp6ServerOptionControlStatus_Type = SleControlStatusType
_SleDhcp6ServerOptionControlStatus_Object = MibScalar
sleDhcp6ServerOptionControlStatus = _SleDhcp6ServerOptionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 2),
    _SleDhcp6ServerOptionControlStatus_Type()
)
sleDhcp6ServerOptionControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlStatus.setStatus("current")
_SleDhcp6ServerOptionControlTimer_Type = Gauge32
_SleDhcp6ServerOptionControlTimer_Object = MibScalar
sleDhcp6ServerOptionControlTimer = _SleDhcp6ServerOptionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 3),
    _SleDhcp6ServerOptionControlTimer_Type()
)
sleDhcp6ServerOptionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlTimer.setStatus("current")
_SleDhcp6ServerOptionControlTimeStamp_Type = TimeTicks
_SleDhcp6ServerOptionControlTimeStamp_Object = MibScalar
sleDhcp6ServerOptionControlTimeStamp = _SleDhcp6ServerOptionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 4),
    _SleDhcp6ServerOptionControlTimeStamp_Type()
)
sleDhcp6ServerOptionControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlTimeStamp.setStatus("current")
_SleDhcp6ServerOptionControlReqResult_Type = SleControlRequestResultType
_SleDhcp6ServerOptionControlReqResult_Object = MibScalar
sleDhcp6ServerOptionControlReqResult = _SleDhcp6ServerOptionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 5),
    _SleDhcp6ServerOptionControlReqResult_Type()
)
sleDhcp6ServerOptionControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlReqResult.setStatus("current")
_SleDhcp6ServerOptionControlPoolIndex_Type = Integer32
_SleDhcp6ServerOptionControlPoolIndex_Object = MibScalar
sleDhcp6ServerOptionControlPoolIndex = _SleDhcp6ServerOptionControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 6),
    _SleDhcp6ServerOptionControlPoolIndex_Type()
)
sleDhcp6ServerOptionControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlPoolIndex.setStatus("current")


class _SleDhcp6ServerOptionControlCode_Type(Integer32):
    """Custom type sleDhcp6ServerOptionControlCode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("nisAddress", 1),
          ("nisDomain", 2),
          ("nispAddress", 3),
          ("nispDomain", 4),
          ("sipAddress", 5),
          ("sipDomain", 6),
          ("sntpAddress", 7),
          ("domainName", 8),
          ("dnsServer", 9))
    )


_SleDhcp6ServerOptionControlCode_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionControlCode_Object = MibScalar
sleDhcp6ServerOptionControlCode = _SleDhcp6ServerOptionControlCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 7),
    _SleDhcp6ServerOptionControlCode_Type()
)
sleDhcp6ServerOptionControlCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlCode.setStatus("current")
_SleDhcp6ServerOptionControlIndex_Type = Integer32
_SleDhcp6ServerOptionControlIndex_Object = MibScalar
sleDhcp6ServerOptionControlIndex = _SleDhcp6ServerOptionControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 8),
    _SleDhcp6ServerOptionControlIndex_Type()
)
sleDhcp6ServerOptionControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlIndex.setStatus("current")


class _SleDhcp6ServerOptionControlType_Type(Integer32):
    """Custom type sleDhcp6ServerOptionControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6address", 1),
          ("text", 2))
    )


_SleDhcp6ServerOptionControlType_Type.__name__ = "Integer32"
_SleDhcp6ServerOptionControlType_Object = MibScalar
sleDhcp6ServerOptionControlType = _SleDhcp6ServerOptionControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 9),
    _SleDhcp6ServerOptionControlType_Type()
)
sleDhcp6ServerOptionControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlType.setStatus("current")
_SleDhcp6ServerOptionControlValue_Type = OctetString
_SleDhcp6ServerOptionControlValue_Object = MibScalar
sleDhcp6ServerOptionControlValue = _SleDhcp6ServerOptionControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 2, 10),
    _SleDhcp6ServerOptionControlValue_Type()
)
sleDhcp6ServerOptionControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionControlValue.setStatus("current")
_SleDhcp6ServerOptionNotification_ObjectIdentity = ObjectIdentity
sleDhcp6ServerOptionNotification = _SleDhcp6ServerOptionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 3)
)
_SleDhcp6Range_ObjectIdentity = ObjectIdentity
sleDhcp6Range = _SleDhcp6Range_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4)
)
_SleDhcp6RangeTable_Object = MibTable
sleDhcp6RangeTable = _SleDhcp6RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6RangeTable.setStatus("current")
_SleDhcp6RangeEntry_Object = MibTableRow
sleDhcp6RangeEntry = _SleDhcp6RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1)
)
sleDhcp6RangeEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6RangeIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6RangeEntry.setStatus("current")


class _SleDhcp6RangeIndex_Type(Integer32):
    """Custom type sleDhcp6RangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6RangeIndex_Type.__name__ = "Integer32"
_SleDhcp6RangeIndex_Object = MibTableColumn
sleDhcp6RangeIndex = _SleDhcp6RangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1, 1),
    _SleDhcp6RangeIndex_Type()
)
sleDhcp6RangeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeIndex.setStatus("current")
_SleDhcp6RangeStart_Type = OctetString
_SleDhcp6RangeStart_Object = MibTableColumn
sleDhcp6RangeStart = _SleDhcp6RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1, 2),
    _SleDhcp6RangeStart_Type()
)
sleDhcp6RangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeStart.setStatus("current")
_SleDhcp6RangeEnd_Type = OctetString
_SleDhcp6RangeEnd_Object = MibTableColumn
sleDhcp6RangeEnd = _SleDhcp6RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1, 3),
    _SleDhcp6RangeEnd_Type()
)
sleDhcp6RangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeEnd.setStatus("current")


class _SleDhcp6RangeValTime_Type(Integer32):
    """Custom type sleDhcp6RangeValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6RangeValTime_Type.__name__ = "Integer32"
_SleDhcp6RangeValTime_Object = MibTableColumn
sleDhcp6RangeValTime = _SleDhcp6RangeValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1, 4),
    _SleDhcp6RangeValTime_Type()
)
sleDhcp6RangeValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeValTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6RangeValTime.setUnits("s")


class _SleDhcp6RangePreTime_Type(Integer32):
    """Custom type sleDhcp6RangePreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6RangePreTime_Type.__name__ = "Integer32"
_SleDhcp6RangePreTime_Object = MibTableColumn
sleDhcp6RangePreTime = _SleDhcp6RangePreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 1, 1, 5),
    _SleDhcp6RangePreTime_Type()
)
sleDhcp6RangePreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangePreTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6RangePreTime.setUnits("s")
_SleDhcp6RangeControl_ObjectIdentity = ObjectIdentity
sleDhcp6RangeControl = _SleDhcp6RangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2)
)


class _SleDhcp6RangeControlRequest_Type(Integer32):
    """Custom type sleDhcp6RangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Range", 1),
          ("destroyDhcp6Range", 2))
    )


_SleDhcp6RangeControlRequest_Type.__name__ = "Integer32"
_SleDhcp6RangeControlRequest_Object = MibScalar
sleDhcp6RangeControlRequest = _SleDhcp6RangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 1),
    _SleDhcp6RangeControlRequest_Type()
)
sleDhcp6RangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlRequest.setStatus("current")
_SleDhcp6RangeControlStatus_Type = SleControlStatusType
_SleDhcp6RangeControlStatus_Object = MibScalar
sleDhcp6RangeControlStatus = _SleDhcp6RangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 2),
    _SleDhcp6RangeControlStatus_Type()
)
sleDhcp6RangeControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlStatus.setStatus("current")
_SleDhcp6RangeControlTimer_Type = Gauge32
_SleDhcp6RangeControlTimer_Object = MibScalar
sleDhcp6RangeControlTimer = _SleDhcp6RangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 3),
    _SleDhcp6RangeControlTimer_Type()
)
sleDhcp6RangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlTimer.setStatus("current")
_SleDhcp6RangeControlTimeStamp_Type = TimeTicks
_SleDhcp6RangeControlTimeStamp_Object = MibScalar
sleDhcp6RangeControlTimeStamp = _SleDhcp6RangeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 4),
    _SleDhcp6RangeControlTimeStamp_Type()
)
sleDhcp6RangeControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlTimeStamp.setStatus("current")
_SleDhcp6RangeControlReqResult_Type = SleControlRequestResultType
_SleDhcp6RangeControlReqResult_Object = MibScalar
sleDhcp6RangeControlReqResult = _SleDhcp6RangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 5),
    _SleDhcp6RangeControlReqResult_Type()
)
sleDhcp6RangeControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlReqResult.setStatus("current")
_SleDhcp6RangeControlPoolIndex_Type = Integer32
_SleDhcp6RangeControlPoolIndex_Object = MibScalar
sleDhcp6RangeControlPoolIndex = _SleDhcp6RangeControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 6),
    _SleDhcp6RangeControlPoolIndex_Type()
)
sleDhcp6RangeControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlPoolIndex.setStatus("current")
_SleDhcp6RangeControlIndex_Type = Integer32
_SleDhcp6RangeControlIndex_Object = MibScalar
sleDhcp6RangeControlIndex = _SleDhcp6RangeControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 7),
    _SleDhcp6RangeControlIndex_Type()
)
sleDhcp6RangeControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlIndex.setStatus("current")
_SleDhcp6RangeControlStart_Type = OctetString
_SleDhcp6RangeControlStart_Object = MibScalar
sleDhcp6RangeControlStart = _SleDhcp6RangeControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 8),
    _SleDhcp6RangeControlStart_Type()
)
sleDhcp6RangeControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlStart.setStatus("current")
_SleDhcp6RangeControlEnd_Type = OctetString
_SleDhcp6RangeControlEnd_Object = MibScalar
sleDhcp6RangeControlEnd = _SleDhcp6RangeControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 9),
    _SleDhcp6RangeControlEnd_Type()
)
sleDhcp6RangeControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlEnd.setStatus("current")


class _SleDhcp6RangeControlValTime_Type(Integer32):
    """Custom type sleDhcp6RangeControlValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6RangeControlValTime_Type.__name__ = "Integer32"
_SleDhcp6RangeControlValTime_Object = MibScalar
sleDhcp6RangeControlValTime = _SleDhcp6RangeControlValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 10),
    _SleDhcp6RangeControlValTime_Type()
)
sleDhcp6RangeControlValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlValTime.setStatus("current")


class _SleDhcp6RangeControlPreTime_Type(Integer32):
    """Custom type sleDhcp6RangeControlPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6RangeControlPreTime_Type.__name__ = "Integer32"
_SleDhcp6RangeControlPreTime_Object = MibScalar
sleDhcp6RangeControlPreTime = _SleDhcp6RangeControlPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 2, 11),
    _SleDhcp6RangeControlPreTime_Type()
)
sleDhcp6RangeControlPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RangeControlPreTime.setStatus("current")
_SleDhcp6RangeNotification_ObjectIdentity = ObjectIdentity
sleDhcp6RangeNotification = _SleDhcp6RangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 3)
)
_SleDhcp6FixedPrefix_ObjectIdentity = ObjectIdentity
sleDhcp6FixedPrefix = _SleDhcp6FixedPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5)
)
_SleDhcp6FixedPrefixTable_Object = MibTable
sleDhcp6FixedPrefixTable = _SleDhcp6FixedPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixTable.setStatus("current")
_SleDhcp6FixedPrefixEntry_Object = MibTableRow
sleDhcp6FixedPrefixEntry = _SleDhcp6FixedPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1)
)
sleDhcp6FixedPrefixEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixEntry.setStatus("current")


class _SleDhcp6FixedPrefixIndex_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6FixedPrefixIndex_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixIndex_Object = MibTableColumn
sleDhcp6FixedPrefixIndex = _SleDhcp6FixedPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 1),
    _SleDhcp6FixedPrefixIndex_Type()
)
sleDhcp6FixedPrefixIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixIndex.setStatus("current")
_SleDhcp6FixedPrefixValue_Type = OctetString
_SleDhcp6FixedPrefixValue_Object = MibTableColumn
sleDhcp6FixedPrefixValue = _SleDhcp6FixedPrefixValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 2),
    _SleDhcp6FixedPrefixValue_Type()
)
sleDhcp6FixedPrefixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixValue.setStatus("current")


class _SleDhcp6FixedPrefixLen_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleDhcp6FixedPrefixLen_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixLen_Object = MibTableColumn
sleDhcp6FixedPrefixLen = _SleDhcp6FixedPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 3),
    _SleDhcp6FixedPrefixLen_Type()
)
sleDhcp6FixedPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixLen.setStatus("current")
_SleDhcp6FixedPrefixDuid_Type = OctetString
_SleDhcp6FixedPrefixDuid_Object = MibTableColumn
sleDhcp6FixedPrefixDuid = _SleDhcp6FixedPrefixDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 4),
    _SleDhcp6FixedPrefixDuid_Type()
)
sleDhcp6FixedPrefixDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixDuid.setStatus("current")


class _SleDhcp6FixedPrefixValTime_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedPrefixValTime_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixValTime_Object = MibTableColumn
sleDhcp6FixedPrefixValTime = _SleDhcp6FixedPrefixValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 5),
    _SleDhcp6FixedPrefixValTime_Type()
)
sleDhcp6FixedPrefixValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixValTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixValTime.setUnits("s")


class _SleDhcp6FixedPrefixPreTime_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedPrefixPreTime_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixPreTime_Object = MibTableColumn
sleDhcp6FixedPrefixPreTime = _SleDhcp6FixedPrefixPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 1, 1, 6),
    _SleDhcp6FixedPrefixPreTime_Type()
)
sleDhcp6FixedPrefixPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixPreTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixPreTime.setUnits("s")
_SleDhcp6FixedPrefixControl_ObjectIdentity = ObjectIdentity
sleDhcp6FixedPrefixControl = _SleDhcp6FixedPrefixControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2)
)


class _SleDhcp6FixedPrefixControlRequest_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6FixedPrefix", 1),
          ("destroyDhcp6FixedPrefix", 2))
    )


_SleDhcp6FixedPrefixControlRequest_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixControlRequest_Object = MibScalar
sleDhcp6FixedPrefixControlRequest = _SleDhcp6FixedPrefixControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 1),
    _SleDhcp6FixedPrefixControlRequest_Type()
)
sleDhcp6FixedPrefixControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlRequest.setStatus("current")
_SleDhcp6FixedPrefixControlStatus_Type = SleControlStatusType
_SleDhcp6FixedPrefixControlStatus_Object = MibScalar
sleDhcp6FixedPrefixControlStatus = _SleDhcp6FixedPrefixControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 2),
    _SleDhcp6FixedPrefixControlStatus_Type()
)
sleDhcp6FixedPrefixControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlStatus.setStatus("current")
_SleDhcp6FixedPrefixControlTimer_Type = Gauge32
_SleDhcp6FixedPrefixControlTimer_Object = MibScalar
sleDhcp6FixedPrefixControlTimer = _SleDhcp6FixedPrefixControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 3),
    _SleDhcp6FixedPrefixControlTimer_Type()
)
sleDhcp6FixedPrefixControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlTimer.setStatus("current")
_SleDhcp6FixedPrefixControlTimeStamp_Type = TimeTicks
_SleDhcp6FixedPrefixControlTimeStamp_Object = MibScalar
sleDhcp6FixedPrefixControlTimeStamp = _SleDhcp6FixedPrefixControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 4),
    _SleDhcp6FixedPrefixControlTimeStamp_Type()
)
sleDhcp6FixedPrefixControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlTimeStamp.setStatus("current")
_SleDhcp6FixedPrefixControlReqResult_Type = SleControlRequestResultType
_SleDhcp6FixedPrefixControlReqResult_Object = MibScalar
sleDhcp6FixedPrefixControlReqResult = _SleDhcp6FixedPrefixControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 5),
    _SleDhcp6FixedPrefixControlReqResult_Type()
)
sleDhcp6FixedPrefixControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlReqResult.setStatus("current")
_SleDhcp6FixedPrefixControlPoolIndex_Type = Integer32
_SleDhcp6FixedPrefixControlPoolIndex_Object = MibScalar
sleDhcp6FixedPrefixControlPoolIndex = _SleDhcp6FixedPrefixControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 6),
    _SleDhcp6FixedPrefixControlPoolIndex_Type()
)
sleDhcp6FixedPrefixControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlPoolIndex.setStatus("current")
_SleDhcp6FixedPrefixControlIndex_Type = Integer32
_SleDhcp6FixedPrefixControlIndex_Object = MibScalar
sleDhcp6FixedPrefixControlIndex = _SleDhcp6FixedPrefixControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 7),
    _SleDhcp6FixedPrefixControlIndex_Type()
)
sleDhcp6FixedPrefixControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlIndex.setStatus("current")
_SleDhcp6FixedPrefixControlValue_Type = OctetString
_SleDhcp6FixedPrefixControlValue_Object = MibScalar
sleDhcp6FixedPrefixControlValue = _SleDhcp6FixedPrefixControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 8),
    _SleDhcp6FixedPrefixControlValue_Type()
)
sleDhcp6FixedPrefixControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlValue.setStatus("current")
_SleDhcp6FixedPrefixControlLen_Type = Integer32
_SleDhcp6FixedPrefixControlLen_Object = MibScalar
sleDhcp6FixedPrefixControlLen = _SleDhcp6FixedPrefixControlLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 9),
    _SleDhcp6FixedPrefixControlLen_Type()
)
sleDhcp6FixedPrefixControlLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlLen.setStatus("current")
_SleDhcp6FixedPrefixControlDuid_Type = OctetString
_SleDhcp6FixedPrefixControlDuid_Object = MibScalar
sleDhcp6FixedPrefixControlDuid = _SleDhcp6FixedPrefixControlDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 10),
    _SleDhcp6FixedPrefixControlDuid_Type()
)
sleDhcp6FixedPrefixControlDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlDuid.setStatus("current")


class _SleDhcp6FixedPrefixControlValTime_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixControlValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedPrefixControlValTime_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixControlValTime_Object = MibScalar
sleDhcp6FixedPrefixControlValTime = _SleDhcp6FixedPrefixControlValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 11),
    _SleDhcp6FixedPrefixControlValTime_Type()
)
sleDhcp6FixedPrefixControlValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlValTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlValTime.setUnits("s")


class _SleDhcp6FixedPrefixControlPreTime_Type(Integer32):
    """Custom type sleDhcp6FixedPrefixControlPreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6FixedPrefixControlPreTime_Type.__name__ = "Integer32"
_SleDhcp6FixedPrefixControlPreTime_Object = MibScalar
sleDhcp6FixedPrefixControlPreTime = _SleDhcp6FixedPrefixControlPreTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 2, 12),
    _SleDhcp6FixedPrefixControlPreTime_Type()
)
sleDhcp6FixedPrefixControlPreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixControlPreTime.setStatus("current")
_SleDhcp6FixedPrefixNotification_ObjectIdentity = ObjectIdentity
sleDhcp6FixedPrefixNotification = _SleDhcp6FixedPrefixNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 3)
)
_SleDhcp6Binding_ObjectIdentity = ObjectIdentity
sleDhcp6Binding = _SleDhcp6Binding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3)
)
_SleDhcp6BindBase_ObjectIdentity = ObjectIdentity
sleDhcp6BindBase = _SleDhcp6BindBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1)
)
_SleDhcp6BindBaseTable_Object = MibTable
sleDhcp6BindBaseTable = _SleDhcp6BindBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6BindBaseTable.setStatus("current")
_SleDhcp6BindBaseEntry_Object = MibTableRow
sleDhcp6BindBaseEntry = _SleDhcp6BindBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1)
)
sleDhcp6BindBaseEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6BindBaseIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6BindBaseEntry.setStatus("current")


class _SleDhcp6BindBaseIndex_Type(Integer32):
    """Custom type sleDhcp6BindBaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6BindBaseIndex_Type.__name__ = "Integer32"
_SleDhcp6BindBaseIndex_Object = MibTableColumn
sleDhcp6BindBaseIndex = _SleDhcp6BindBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1, 1),
    _SleDhcp6BindBaseIndex_Type()
)
sleDhcp6BindBaseIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseIndex.setStatus("current")
_SleDhcp6BindBaseLinkLocal_Type = OctetString
_SleDhcp6BindBaseLinkLocal_Object = MibTableColumn
sleDhcp6BindBaseLinkLocal = _SleDhcp6BindBaseLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1, 2),
    _SleDhcp6BindBaseLinkLocal_Type()
)
sleDhcp6BindBaseLinkLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseLinkLocal.setStatus("current")
_SleDhcp6BindBaseDuid_Type = OctetString
_SleDhcp6BindBaseDuid_Object = MibTableColumn
sleDhcp6BindBaseDuid = _SleDhcp6BindBaseDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1, 3),
    _SleDhcp6BindBaseDuid_Type()
)
sleDhcp6BindBaseDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseDuid.setStatus("current")


class _SleDhcp6BindBaseIaType_Type(Integer32):
    """Custom type sleDhcp6BindBaseIaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iana", 1),
          ("iapd", 2))
    )


_SleDhcp6BindBaseIaType_Type.__name__ = "Integer32"
_SleDhcp6BindBaseIaType_Object = MibTableColumn
sleDhcp6BindBaseIaType = _SleDhcp6BindBaseIaType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1, 4),
    _SleDhcp6BindBaseIaType_Type()
)
sleDhcp6BindBaseIaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseIaType.setStatus("current")
_SleDhcp6BindBaseIaid_Type = Integer32
_SleDhcp6BindBaseIaid_Object = MibTableColumn
sleDhcp6BindBaseIaid = _SleDhcp6BindBaseIaid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 1, 1, 5),
    _SleDhcp6BindBaseIaid_Type()
)
sleDhcp6BindBaseIaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseIaid.setStatus("current")
_SleDhcp6BindBaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6BindBaseControl = _SleDhcp6BindBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2)
)


class _SleDhcp6BindBaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6BindBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDhcp6Binding", 1)
    )


_SleDhcp6BindBaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6BindBaseControlRequest_Object = MibScalar
sleDhcp6BindBaseControlRequest = _SleDhcp6BindBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2, 1),
    _SleDhcp6BindBaseControlRequest_Type()
)
sleDhcp6BindBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseControlRequest.setStatus("current")
_SleDhcp6BindBaseControlStatus_Type = SleControlStatusType
_SleDhcp6BindBaseControlStatus_Object = MibScalar
sleDhcp6BindBaseControlStatus = _SleDhcp6BindBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2, 2),
    _SleDhcp6BindBaseControlStatus_Type()
)
sleDhcp6BindBaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseControlStatus.setStatus("current")
_SleDhcp6BindBaseControlTimer_Type = Gauge32
_SleDhcp6BindBaseControlTimer_Object = MibScalar
sleDhcp6BindBaseControlTimer = _SleDhcp6BindBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2, 3),
    _SleDhcp6BindBaseControlTimer_Type()
)
sleDhcp6BindBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseControlTimer.setStatus("current")
_SleDhcp6BindBaseControlTimeStamp_Type = TimeTicks
_SleDhcp6BindBaseControlTimeStamp_Object = MibScalar
sleDhcp6BindBaseControlTimeStamp = _SleDhcp6BindBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2, 4),
    _SleDhcp6BindBaseControlTimeStamp_Type()
)
sleDhcp6BindBaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseControlTimeStamp.setStatus("current")
_SleDhcp6BindBaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6BindBaseControlReqResult_Object = MibScalar
sleDhcp6BindBaseControlReqResult = _SleDhcp6BindBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 2, 5),
    _SleDhcp6BindBaseControlReqResult_Type()
)
sleDhcp6BindBaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindBaseControlReqResult.setStatus("current")
_SleDhcp6BindBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6BindBaseNotification = _SleDhcp6BindBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 3)
)
_SleDhcp6BindPd_ObjectIdentity = ObjectIdentity
sleDhcp6BindPd = _SleDhcp6BindPd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2)
)
_SleDhcp6BindPdTable_Object = MibTable
sleDhcp6BindPdTable = _SleDhcp6BindPdTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6BindPdTable.setStatus("current")
_SleDhcp6BindPdEntry_Object = MibTableRow
sleDhcp6BindPdEntry = _SleDhcp6BindPdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1, 1)
)
sleDhcp6BindPdEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6BindBaseIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6BindPdIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6BindPdEntry.setStatus("current")


class _SleDhcp6BindPdIndex_Type(Integer32):
    """Custom type sleDhcp6BindPdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6BindPdIndex_Type.__name__ = "Integer32"
_SleDhcp6BindPdIndex_Object = MibTableColumn
sleDhcp6BindPdIndex = _SleDhcp6BindPdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1, 1, 1),
    _SleDhcp6BindPdIndex_Type()
)
sleDhcp6BindPdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindPdIndex.setStatus("current")
_SleDhcp6BindPdPrefix_Type = OctetString
_SleDhcp6BindPdPrefix_Object = MibTableColumn
sleDhcp6BindPdPrefix = _SleDhcp6BindPdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1, 1, 2),
    _SleDhcp6BindPdPrefix_Type()
)
sleDhcp6BindPdPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindPdPrefix.setStatus("current")


class _SleDhcp6BindPdPrefixLen_Type(Integer32):
    """Custom type sleDhcp6BindPdPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleDhcp6BindPdPrefixLen_Type.__name__ = "Integer32"
_SleDhcp6BindPdPrefixLen_Object = MibTableColumn
sleDhcp6BindPdPrefixLen = _SleDhcp6BindPdPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1, 1, 3),
    _SleDhcp6BindPdPrefixLen_Type()
)
sleDhcp6BindPdPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindPdPrefixLen.setStatus("current")
_SleDhcp6BindPdExpireTime_Type = Integer32
_SleDhcp6BindPdExpireTime_Object = MibTableColumn
sleDhcp6BindPdExpireTime = _SleDhcp6BindPdExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 2, 1, 1, 4),
    _SleDhcp6BindPdExpireTime_Type()
)
sleDhcp6BindPdExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindPdExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6BindPdExpireTime.setUnits("s")
_SleDhcp6BindNa_ObjectIdentity = ObjectIdentity
sleDhcp6BindNa = _SleDhcp6BindNa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3)
)
_SleDhcp6BindNaTable_Object = MibTable
sleDhcp6BindNaTable = _SleDhcp6BindNaTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6BindNaTable.setStatus("current")
_SleDhcp6BindNaEntry_Object = MibTableRow
sleDhcp6BindNaEntry = _SleDhcp6BindNaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3, 1, 1)
)
sleDhcp6BindNaEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6BindBaseIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6BindNaIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6BindNaEntry.setStatus("current")


class _SleDhcp6BindNaIndex_Type(Integer32):
    """Custom type sleDhcp6BindNaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6BindNaIndex_Type.__name__ = "Integer32"
_SleDhcp6BindNaIndex_Object = MibTableColumn
sleDhcp6BindNaIndex = _SleDhcp6BindNaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3, 1, 1, 1),
    _SleDhcp6BindNaIndex_Type()
)
sleDhcp6BindNaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindNaIndex.setStatus("current")
_SleDhcp6BindNaAddress_Type = OctetString
_SleDhcp6BindNaAddress_Object = MibTableColumn
sleDhcp6BindNaAddress = _SleDhcp6BindNaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3, 1, 1, 2),
    _SleDhcp6BindNaAddress_Type()
)
sleDhcp6BindNaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindNaAddress.setStatus("current")
_SleDhcp6BindNaExpireTime_Type = Integer32
_SleDhcp6BindNaExpireTime_Object = MibTableColumn
sleDhcp6BindNaExpireTime = _SleDhcp6BindNaExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 3, 1, 1, 3),
    _SleDhcp6BindNaExpireTime_Type()
)
sleDhcp6BindNaExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6BindNaExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6BindNaExpireTime.setUnits("s")
_SleDhcp6LocalPool_ObjectIdentity = ObjectIdentity
sleDhcp6LocalPool = _SleDhcp6LocalPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4)
)
_SleDhcp6LocalPoolTable_Object = MibTable
sleDhcp6LocalPoolTable = _SleDhcp6LocalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolTable.setStatus("current")
_SleDhcp6LocalPoolEntry_Object = MibTableRow
sleDhcp6LocalPoolEntry = _SleDhcp6LocalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1)
)
sleDhcp6LocalPoolEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6LocalPoolIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolEntry.setStatus("current")


class _SleDhcp6LocalPoolIndex_Type(Integer32):
    """Custom type sleDhcp6LocalPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6LocalPoolIndex_Type.__name__ = "Integer32"
_SleDhcp6LocalPoolIndex_Object = MibTableColumn
sleDhcp6LocalPoolIndex = _SleDhcp6LocalPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 1),
    _SleDhcp6LocalPoolIndex_Type()
)
sleDhcp6LocalPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolIndex.setStatus("current")


class _SleDhcp6LocalPoolName_Type(OctetString):
    """Custom type sleDhcp6LocalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6LocalPoolName_Type.__name__ = "OctetString"
_SleDhcp6LocalPoolName_Object = MibTableColumn
sleDhcp6LocalPoolName = _SleDhcp6LocalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 2),
    _SleDhcp6LocalPoolName_Type()
)
sleDhcp6LocalPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolName.setStatus("current")
_SleDhcp6LocalPoolPrefix_Type = OctetString
_SleDhcp6LocalPoolPrefix_Object = MibTableColumn
sleDhcp6LocalPoolPrefix = _SleDhcp6LocalPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 3),
    _SleDhcp6LocalPoolPrefix_Type()
)
sleDhcp6LocalPoolPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolPrefix.setStatus("current")
_SleDhcp6LocalPoolPrefixLen_Type = Integer32
_SleDhcp6LocalPoolPrefixLen_Object = MibTableColumn
sleDhcp6LocalPoolPrefixLen = _SleDhcp6LocalPoolPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 4),
    _SleDhcp6LocalPoolPrefixLen_Type()
)
sleDhcp6LocalPoolPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolPrefixLen.setStatus("current")


class _SleDhcp6LocalPoolAssignLen_Type(Integer32):
    """Custom type sleDhcp6LocalPoolAssignLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_SleDhcp6LocalPoolAssignLen_Type.__name__ = "Integer32"
_SleDhcp6LocalPoolAssignLen_Object = MibTableColumn
sleDhcp6LocalPoolAssignLen = _SleDhcp6LocalPoolAssignLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 5),
    _SleDhcp6LocalPoolAssignLen_Type()
)
sleDhcp6LocalPoolAssignLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolAssignLen.setStatus("current")
_SleDhcp6LocalPoolUsedCnt_Type = Integer32
_SleDhcp6LocalPoolUsedCnt_Object = MibTableColumn
sleDhcp6LocalPoolUsedCnt = _SleDhcp6LocalPoolUsedCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 6),
    _SleDhcp6LocalPoolUsedCnt_Type()
)
sleDhcp6LocalPoolUsedCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolUsedCnt.setStatus("current")
_SleDhcp6LocalPoolAvailCnt_Type = Integer32
_SleDhcp6LocalPoolAvailCnt_Object = MibTableColumn
sleDhcp6LocalPoolAvailCnt = _SleDhcp6LocalPoolAvailCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 1, 1, 7),
    _SleDhcp6LocalPoolAvailCnt_Type()
)
sleDhcp6LocalPoolAvailCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolAvailCnt.setStatus("current")
_SleDhcp6LocalPoolControl_ObjectIdentity = ObjectIdentity
sleDhcp6LocalPoolControl = _SleDhcp6LocalPoolControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2)
)


class _SleDhcp6LocalPoolControlRequest_Type(Integer32):
    """Custom type sleDhcp6LocalPoolControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6LocalPool", 1),
          ("destroyDhcp6LocalPool", 2))
    )


_SleDhcp6LocalPoolControlRequest_Type.__name__ = "Integer32"
_SleDhcp6LocalPoolControlRequest_Object = MibScalar
sleDhcp6LocalPoolControlRequest = _SleDhcp6LocalPoolControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 1),
    _SleDhcp6LocalPoolControlRequest_Type()
)
sleDhcp6LocalPoolControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlRequest.setStatus("current")
_SleDhcp6LocalPoolControlStatus_Type = SleControlStatusType
_SleDhcp6LocalPoolControlStatus_Object = MibScalar
sleDhcp6LocalPoolControlStatus = _SleDhcp6LocalPoolControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 2),
    _SleDhcp6LocalPoolControlStatus_Type()
)
sleDhcp6LocalPoolControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlStatus.setStatus("current")
_SleDhcp6LocalPoolControlTimer_Type = Gauge32
_SleDhcp6LocalPoolControlTimer_Object = MibScalar
sleDhcp6LocalPoolControlTimer = _SleDhcp6LocalPoolControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 3),
    _SleDhcp6LocalPoolControlTimer_Type()
)
sleDhcp6LocalPoolControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlTimer.setStatus("current")
_SleDhcp6LocalPoolControlTimeStamp_Type = TimeTicks
_SleDhcp6LocalPoolControlTimeStamp_Object = MibScalar
sleDhcp6LocalPoolControlTimeStamp = _SleDhcp6LocalPoolControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 4),
    _SleDhcp6LocalPoolControlTimeStamp_Type()
)
sleDhcp6LocalPoolControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlTimeStamp.setStatus("current")
_SleDhcp6LocalPoolControlReqResult_Type = SleControlRequestResultType
_SleDhcp6LocalPoolControlReqResult_Object = MibScalar
sleDhcp6LocalPoolControlReqResult = _SleDhcp6LocalPoolControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 5),
    _SleDhcp6LocalPoolControlReqResult_Type()
)
sleDhcp6LocalPoolControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlReqResult.setStatus("current")
_SleDhcp6LocalPoolControlIndex_Type = Integer32
_SleDhcp6LocalPoolControlIndex_Object = MibScalar
sleDhcp6LocalPoolControlIndex = _SleDhcp6LocalPoolControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 6),
    _SleDhcp6LocalPoolControlIndex_Type()
)
sleDhcp6LocalPoolControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlIndex.setStatus("current")


class _SleDhcp6LocalPoolControlName_Type(OctetString):
    """Custom type sleDhcp6LocalPoolControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6LocalPoolControlName_Type.__name__ = "OctetString"
_SleDhcp6LocalPoolControlName_Object = MibScalar
sleDhcp6LocalPoolControlName = _SleDhcp6LocalPoolControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 7),
    _SleDhcp6LocalPoolControlName_Type()
)
sleDhcp6LocalPoolControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlName.setStatus("current")
_SleDhcp6LocalPoolControlPrefix_Type = OctetString
_SleDhcp6LocalPoolControlPrefix_Object = MibScalar
sleDhcp6LocalPoolControlPrefix = _SleDhcp6LocalPoolControlPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 8),
    _SleDhcp6LocalPoolControlPrefix_Type()
)
sleDhcp6LocalPoolControlPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlPrefix.setStatus("current")


class _SleDhcp6LocalPoolControlPrefixLen_Type(Integer32):
    """Custom type sleDhcp6LocalPoolControlPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleDhcp6LocalPoolControlPrefixLen_Type.__name__ = "Integer32"
_SleDhcp6LocalPoolControlPrefixLen_Object = MibScalar
sleDhcp6LocalPoolControlPrefixLen = _SleDhcp6LocalPoolControlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 9),
    _SleDhcp6LocalPoolControlPrefixLen_Type()
)
sleDhcp6LocalPoolControlPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlPrefixLen.setStatus("current")


class _SleDhcp6LocalPoolControlAssignLen_Type(Integer32):
    """Custom type sleDhcp6LocalPoolControlAssignLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_SleDhcp6LocalPoolControlAssignLen_Type.__name__ = "Integer32"
_SleDhcp6LocalPoolControlAssignLen_Object = MibScalar
sleDhcp6LocalPoolControlAssignLen = _SleDhcp6LocalPoolControlAssignLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 2, 10),
    _SleDhcp6LocalPoolControlAssignLen_Type()
)
sleDhcp6LocalPoolControlAssignLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolControlAssignLen.setStatus("current")
_SleDhcp6LocalPoolNotification_ObjectIdentity = ObjectIdentity
sleDhcp6LocalPoolNotification = _SleDhcp6LocalPoolNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 3)
)
_SleDhcp6Server_ObjectIdentity = ObjectIdentity
sleDhcp6Server = _SleDhcp6Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5)
)
_SleDhcp6ServerTable_Object = MibTable
sleDhcp6ServerTable = _SleDhcp6ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ServerTable.setStatus("current")
_SleDhcp6ServerEntry_Object = MibTableRow
sleDhcp6ServerEntry = _SleDhcp6ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1)
)
sleDhcp6ServerEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ServerIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6ServerEntry.setStatus("current")


class _SleDhcp6ServerIndex_Type(Integer32):
    """Custom type sleDhcp6ServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6ServerIndex_Type.__name__ = "Integer32"
_SleDhcp6ServerIndex_Object = MibTableColumn
sleDhcp6ServerIndex = _SleDhcp6ServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1, 1),
    _SleDhcp6ServerIndex_Type()
)
sleDhcp6ServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerIndex.setStatus("current")
_SleDhcp6ServerIfName_Type = OctetString
_SleDhcp6ServerIfName_Object = MibTableColumn
sleDhcp6ServerIfName = _SleDhcp6ServerIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1, 2),
    _SleDhcp6ServerIfName_Type()
)
sleDhcp6ServerIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerIfName.setStatus("current")
_SleDhcp6ServerPoolName_Type = OctetString
_SleDhcp6ServerPoolName_Object = MibTableColumn
sleDhcp6ServerPoolName = _SleDhcp6ServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1, 3),
    _SleDhcp6ServerPoolName_Type()
)
sleDhcp6ServerPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerPoolName.setStatus("current")


class _SleDhcp6ServerPreference_Type(Integer32):
    """Custom type sleDhcp6ServerPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6ServerPreference_Type.__name__ = "Integer32"
_SleDhcp6ServerPreference_Object = MibTableColumn
sleDhcp6ServerPreference = _SleDhcp6ServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1, 4),
    _SleDhcp6ServerPreference_Type()
)
sleDhcp6ServerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerPreference.setStatus("current")


class _SleDhcp6ServerRapidCommit_Type(Integer32):
    """Custom type sleDhcp6ServerRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SleDhcp6ServerRapidCommit_Type.__name__ = "Integer32"
_SleDhcp6ServerRapidCommit_Object = MibTableColumn
sleDhcp6ServerRapidCommit = _SleDhcp6ServerRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 1, 1, 5),
    _SleDhcp6ServerRapidCommit_Type()
)
sleDhcp6ServerRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerRapidCommit.setStatus("current")
_SleDhcp6ServerControl_ObjectIdentity = ObjectIdentity
sleDhcp6ServerControl = _SleDhcp6ServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2)
)


class _SleDhcp6ServerControlRequest_Type(Integer32):
    """Custom type sleDhcp6ServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Server", 1),
          ("destroyDhcp6Server", 2))
    )


_SleDhcp6ServerControlRequest_Type.__name__ = "Integer32"
_SleDhcp6ServerControlRequest_Object = MibScalar
sleDhcp6ServerControlRequest = _SleDhcp6ServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 1),
    _SleDhcp6ServerControlRequest_Type()
)
sleDhcp6ServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlRequest.setStatus("current")
_SleDhcp6ServerControlStatus_Type = SleControlStatusType
_SleDhcp6ServerControlStatus_Object = MibScalar
sleDhcp6ServerControlStatus = _SleDhcp6ServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 2),
    _SleDhcp6ServerControlStatus_Type()
)
sleDhcp6ServerControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlStatus.setStatus("current")
_SleDhcp6ServerControlTimer_Type = Gauge32
_SleDhcp6ServerControlTimer_Object = MibScalar
sleDhcp6ServerControlTimer = _SleDhcp6ServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 3),
    _SleDhcp6ServerControlTimer_Type()
)
sleDhcp6ServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlTimer.setStatus("current")
_SleDhcp6ServerControlTimeStamp_Type = TimeTicks
_SleDhcp6ServerControlTimeStamp_Object = MibScalar
sleDhcp6ServerControlTimeStamp = _SleDhcp6ServerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 4),
    _SleDhcp6ServerControlTimeStamp_Type()
)
sleDhcp6ServerControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlTimeStamp.setStatus("current")
_SleDhcp6ServerControlReqResult_Type = SleControlRequestResultType
_SleDhcp6ServerControlReqResult_Object = MibScalar
sleDhcp6ServerControlReqResult = _SleDhcp6ServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 5),
    _SleDhcp6ServerControlReqResult_Type()
)
sleDhcp6ServerControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlReqResult.setStatus("current")
_SleDhcp6ServerControlIndex_Type = Integer32
_SleDhcp6ServerControlIndex_Object = MibScalar
sleDhcp6ServerControlIndex = _SleDhcp6ServerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 6),
    _SleDhcp6ServerControlIndex_Type()
)
sleDhcp6ServerControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlIndex.setStatus("current")
_SleDhcp6ServerControlIfName_Type = OctetString
_SleDhcp6ServerControlIfName_Object = MibScalar
sleDhcp6ServerControlIfName = _SleDhcp6ServerControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 7),
    _SleDhcp6ServerControlIfName_Type()
)
sleDhcp6ServerControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlIfName.setStatus("current")
_SleDhcp6ServerControlPoolName_Type = OctetString
_SleDhcp6ServerControlPoolName_Object = MibScalar
sleDhcp6ServerControlPoolName = _SleDhcp6ServerControlPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 8),
    _SleDhcp6ServerControlPoolName_Type()
)
sleDhcp6ServerControlPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlPoolName.setStatus("current")


class _SleDhcp6ServerControlPreference_Type(Integer32):
    """Custom type sleDhcp6ServerControlPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6ServerControlPreference_Type.__name__ = "Integer32"
_SleDhcp6ServerControlPreference_Object = MibScalar
sleDhcp6ServerControlPreference = _SleDhcp6ServerControlPreference_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 9),
    _SleDhcp6ServerControlPreference_Type()
)
sleDhcp6ServerControlPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlPreference.setStatus("current")


class _SleDhcp6ServerControlRapidCommit_Type(Integer32):
    """Custom type sleDhcp6ServerControlRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SleDhcp6ServerControlRapidCommit_Type.__name__ = "Integer32"
_SleDhcp6ServerControlRapidCommit_Object = MibScalar
sleDhcp6ServerControlRapidCommit = _SleDhcp6ServerControlRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 2, 10),
    _SleDhcp6ServerControlRapidCommit_Type()
)
sleDhcp6ServerControlRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ServerControlRapidCommit.setStatus("current")
_SleDhcp6ServerNotification_ObjectIdentity = ObjectIdentity
sleDhcp6ServerNotification = _SleDhcp6ServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 3)
)
_SleDhcp6Relay_ObjectIdentity = ObjectIdentity
sleDhcp6Relay = _SleDhcp6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6)
)
_SleDhcp6RelayTable_Object = MibTable
sleDhcp6RelayTable = _SleDhcp6RelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6RelayTable.setStatus("current")
_SleDhcp6RelayEntry_Object = MibTableRow
sleDhcp6RelayEntry = _SleDhcp6RelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1, 1)
)
sleDhcp6RelayEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6RelayIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6RelayEntry.setStatus("current")


class _SleDhcp6RelayIndex_Type(Integer32):
    """Custom type sleDhcp6RelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6RelayIndex_Type.__name__ = "Integer32"
_SleDhcp6RelayIndex_Object = MibTableColumn
sleDhcp6RelayIndex = _SleDhcp6RelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1, 1, 1),
    _SleDhcp6RelayIndex_Type()
)
sleDhcp6RelayIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayIndex.setStatus("current")
_SleDhcp6RelayIfName_Type = OctetString
_SleDhcp6RelayIfName_Object = MibTableColumn
sleDhcp6RelayIfName = _SleDhcp6RelayIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1, 1, 2),
    _SleDhcp6RelayIfName_Type()
)
sleDhcp6RelayIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayIfName.setStatus("current")
_SleDhcp6RelayDestAddr_Type = OctetString
_SleDhcp6RelayDestAddr_Object = MibTableColumn
sleDhcp6RelayDestAddr = _SleDhcp6RelayDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1, 1, 3),
    _SleDhcp6RelayDestAddr_Type()
)
sleDhcp6RelayDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayDestAddr.setStatus("current")
_SleDhcp6RelayOutputIfname_Type = OctetString
_SleDhcp6RelayOutputIfname_Object = MibTableColumn
sleDhcp6RelayOutputIfname = _SleDhcp6RelayOutputIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 1, 1, 4),
    _SleDhcp6RelayOutputIfname_Type()
)
sleDhcp6RelayOutputIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayOutputIfname.setStatus("current")
_SleDhcp6RelayControl_ObjectIdentity = ObjectIdentity
sleDhcp6RelayControl = _SleDhcp6RelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2)
)


class _SleDhcp6RelayControlRequest_Type(Integer32):
    """Custom type sleDhcp6RelayControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Relay", 1),
          ("destroyDhcp6Relay", 2))
    )


_SleDhcp6RelayControlRequest_Type.__name__ = "Integer32"
_SleDhcp6RelayControlRequest_Object = MibScalar
sleDhcp6RelayControlRequest = _SleDhcp6RelayControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 1),
    _SleDhcp6RelayControlRequest_Type()
)
sleDhcp6RelayControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlRequest.setStatus("current")
_SleDhcp6RelayControlStatus_Type = SleControlStatusType
_SleDhcp6RelayControlStatus_Object = MibScalar
sleDhcp6RelayControlStatus = _SleDhcp6RelayControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 2),
    _SleDhcp6RelayControlStatus_Type()
)
sleDhcp6RelayControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlStatus.setStatus("current")
_SleDhcp6RelayControlTimer_Type = Gauge32
_SleDhcp6RelayControlTimer_Object = MibScalar
sleDhcp6RelayControlTimer = _SleDhcp6RelayControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 3),
    _SleDhcp6RelayControlTimer_Type()
)
sleDhcp6RelayControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlTimer.setStatus("current")
_SleDhcp6RelayControlTimeStamp_Type = TimeTicks
_SleDhcp6RelayControlTimeStamp_Object = MibScalar
sleDhcp6RelayControlTimeStamp = _SleDhcp6RelayControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 4),
    _SleDhcp6RelayControlTimeStamp_Type()
)
sleDhcp6RelayControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlTimeStamp.setStatus("current")
_SleDhcp6RelayControlReqResult_Type = SleControlRequestResultType
_SleDhcp6RelayControlReqResult_Object = MibScalar
sleDhcp6RelayControlReqResult = _SleDhcp6RelayControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 5),
    _SleDhcp6RelayControlReqResult_Type()
)
sleDhcp6RelayControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlReqResult.setStatus("current")
_SleDhcp6RelayControlIndex_Type = Integer32
_SleDhcp6RelayControlIndex_Object = MibScalar
sleDhcp6RelayControlIndex = _SleDhcp6RelayControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 6),
    _SleDhcp6RelayControlIndex_Type()
)
sleDhcp6RelayControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlIndex.setStatus("current")
_SleDhcp6RelayControlIfName_Type = OctetString
_SleDhcp6RelayControlIfName_Object = MibScalar
sleDhcp6RelayControlIfName = _SleDhcp6RelayControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 7),
    _SleDhcp6RelayControlIfName_Type()
)
sleDhcp6RelayControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlIfName.setStatus("current")
_SleDhcp6RelayControlDestAddr_Type = OctetString
_SleDhcp6RelayControlDestAddr_Object = MibScalar
sleDhcp6RelayControlDestAddr = _SleDhcp6RelayControlDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 8),
    _SleDhcp6RelayControlDestAddr_Type()
)
sleDhcp6RelayControlDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlDestAddr.setStatus("current")
_SleDhcp6RelayControlOutputIfname_Type = OctetString
_SleDhcp6RelayControlOutputIfname_Object = MibScalar
sleDhcp6RelayControlOutputIfname = _SleDhcp6RelayControlOutputIfname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 2, 9),
    _SleDhcp6RelayControlOutputIfname_Type()
)
sleDhcp6RelayControlOutputIfname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6RelayControlOutputIfname.setStatus("current")
_SleDhcp6RelayNotification_ObjectIdentity = ObjectIdentity
sleDhcp6RelayNotification = _SleDhcp6RelayNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 3)
)
_SleDhcp6Client_ObjectIdentity = ObjectIdentity
sleDhcp6Client = _SleDhcp6Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7)
)
_SleDhcp6ClientBase_ObjectIdentity = ObjectIdentity
sleDhcp6ClientBase = _SleDhcp6ClientBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1)
)
_SleDhcp6ClientTable_Object = MibTable
sleDhcp6ClientTable = _SleDhcp6ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ClientTable.setStatus("current")
_SleDhcp6ClientEntry_Object = MibTableRow
sleDhcp6ClientEntry = _SleDhcp6ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1)
)
sleDhcp6ClientEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6ClientEntry.setStatus("current")


class _SleDhcp6ClientIndex_Type(Integer32):
    """Custom type sleDhcp6ClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6ClientIndex_Type.__name__ = "Integer32"
_SleDhcp6ClientIndex_Object = MibTableColumn
sleDhcp6ClientIndex = _SleDhcp6ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 1),
    _SleDhcp6ClientIndex_Type()
)
sleDhcp6ClientIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIndex.setStatus("current")
_SleDhcp6ClientIfName_Type = OctetString
_SleDhcp6ClientIfName_Object = MibTableColumn
sleDhcp6ClientIfName = _SleDhcp6ClientIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 2),
    _SleDhcp6ClientIfName_Type()
)
sleDhcp6ClientIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIfName.setStatus("current")


class _SleDhcp6ClientState_Type(Integer32):
    """Custom type sleDhcp6ClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_SleDhcp6ClientState_Type.__name__ = "Integer32"
_SleDhcp6ClientState_Object = MibTableColumn
sleDhcp6ClientState = _SleDhcp6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 3),
    _SleDhcp6ClientState_Type()
)
sleDhcp6ClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientState.setStatus("current")
_SleDhcp6ClientServerAddr_Type = OctetString
_SleDhcp6ClientServerAddr_Object = MibTableColumn
sleDhcp6ClientServerAddr = _SleDhcp6ClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 4),
    _SleDhcp6ClientServerAddr_Type()
)
sleDhcp6ClientServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientServerAddr.setStatus("current")
_SleDhcp6ClientServerDuid_Type = OctetString
_SleDhcp6ClientServerDuid_Object = MibTableColumn
sleDhcp6ClientServerDuid = _SleDhcp6ClientServerDuid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 5),
    _SleDhcp6ClientServerDuid_Type()
)
sleDhcp6ClientServerDuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientServerDuid.setStatus("current")


class _SleDhcp6ClientServerPref_Type(Integer32):
    """Custom type sleDhcp6ClientServerPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6ClientServerPref_Type.__name__ = "Integer32"
_SleDhcp6ClientServerPref_Object = MibTableColumn
sleDhcp6ClientServerPref = _SleDhcp6ClientServerPref_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 6),
    _SleDhcp6ClientServerPref_Type()
)
sleDhcp6ClientServerPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientServerPref.setStatus("current")


class _SleDhcp6ClientRapidCommit_Type(Integer32):
    """Custom type sleDhcp6ClientRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6ClientRapidCommit_Type.__name__ = "Integer32"
_SleDhcp6ClientRapidCommit_Object = MibTableColumn
sleDhcp6ClientRapidCommit = _SleDhcp6ClientRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 7),
    _SleDhcp6ClientRapidCommit_Type()
)
sleDhcp6ClientRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientRapidCommit.setStatus("current")
_SleDhcp6ClientPdname_Type = OctetString
_SleDhcp6ClientPdname_Object = MibTableColumn
sleDhcp6ClientPdname = _SleDhcp6ClientPdname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 8),
    _SleDhcp6ClientPdname_Type()
)
sleDhcp6ClientPdname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientPdname.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientPdname.setUnits("s")


class _SleDhcp6ClientInfoRefTime_Type(Integer32):
    """Custom type sleDhcp6ClientInfoRefTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 315360000),
    )


_SleDhcp6ClientInfoRefTime_Type.__name__ = "Integer32"
_SleDhcp6ClientInfoRefTime_Object = MibTableColumn
sleDhcp6ClientInfoRefTime = _SleDhcp6ClientInfoRefTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 1, 1, 9),
    _SleDhcp6ClientInfoRefTime_Type()
)
sleDhcp6ClientInfoRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6ClientInfoRefTime.setStatus("current")
_SleDhcp6ClientBaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6ClientBaseControl = _SleDhcp6ClientBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2)
)


class _SleDhcp6ClientBaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("setDhcp6ClientStatelessConfig", 1),
          ("setDhcp6ClientStatefulNa", 2),
          ("setDhcp6ClientStatefulPd", 3),
          ("setDhcp6ClientRefreshMin", 4),
          ("unsetDhcp6ClientRefreshMin", 5),
          ("setDhcp6ClientStatefulPdwithHint", 6),
          ("clearDhcp6Client", 7))
    )


_SleDhcp6ClientBaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlRequest_Object = MibScalar
sleDhcp6ClientBaseControlRequest = _SleDhcp6ClientBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 1),
    _SleDhcp6ClientBaseControlRequest_Type()
)
sleDhcp6ClientBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlRequest.setStatus("current")
_SleDhcp6ClientBaseControlStatus_Type = SleControlStatusType
_SleDhcp6ClientBaseControlStatus_Object = MibScalar
sleDhcp6ClientBaseControlStatus = _SleDhcp6ClientBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 2),
    _SleDhcp6ClientBaseControlStatus_Type()
)
sleDhcp6ClientBaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlStatus.setStatus("current")
_SleDhcp6ClientBaseControlTimer_Type = Gauge32
_SleDhcp6ClientBaseControlTimer_Object = MibScalar
sleDhcp6ClientBaseControlTimer = _SleDhcp6ClientBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 3),
    _SleDhcp6ClientBaseControlTimer_Type()
)
sleDhcp6ClientBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlTimer.setStatus("current")
_SleDhcp6ClientBaseControlTimeStamp_Type = TimeTicks
_SleDhcp6ClientBaseControlTimeStamp_Object = MibScalar
sleDhcp6ClientBaseControlTimeStamp = _SleDhcp6ClientBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 4),
    _SleDhcp6ClientBaseControlTimeStamp_Type()
)
sleDhcp6ClientBaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlTimeStamp.setStatus("current")
_SleDhcp6ClientBaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6ClientBaseControlReqResult_Object = MibScalar
sleDhcp6ClientBaseControlReqResult = _SleDhcp6ClientBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 5),
    _SleDhcp6ClientBaseControlReqResult_Type()
)
sleDhcp6ClientBaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlReqResult.setStatus("current")
_SleDhcp6ClientBaseControlIndex_Type = Integer32
_SleDhcp6ClientBaseControlIndex_Object = MibScalar
sleDhcp6ClientBaseControlIndex = _SleDhcp6ClientBaseControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 6),
    _SleDhcp6ClientBaseControlIndex_Type()
)
sleDhcp6ClientBaseControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlIndex.setStatus("current")
_SleDhcp6ClientBaseControlIfName_Type = OctetString
_SleDhcp6ClientBaseControlIfName_Object = MibScalar
sleDhcp6ClientBaseControlIfName = _SleDhcp6ClientBaseControlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 7),
    _SleDhcp6ClientBaseControlIfName_Type()
)
sleDhcp6ClientBaseControlIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlIfName.setStatus("current")


class _SleDhcp6ClientBaseControlStatelessFlag_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlStatelessFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6ClientBaseControlStatelessFlag_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlStatelessFlag_Object = MibScalar
sleDhcp6ClientBaseControlStatelessFlag = _SleDhcp6ClientBaseControlStatelessFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 8),
    _SleDhcp6ClientBaseControlStatelessFlag_Type()
)
sleDhcp6ClientBaseControlStatelessFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlStatelessFlag.setStatus("current")


class _SleDhcp6ClientBaseControlNaFlag_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlNaFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6ClientBaseControlNaFlag_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlNaFlag_Object = MibScalar
sleDhcp6ClientBaseControlNaFlag = _SleDhcp6ClientBaseControlNaFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 9),
    _SleDhcp6ClientBaseControlNaFlag_Type()
)
sleDhcp6ClientBaseControlNaFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlNaFlag.setStatus("current")


class _SleDhcp6ClientBaseControlPdFlag_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlPdFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2),
          ("pdhint", 3))
    )


_SleDhcp6ClientBaseControlPdFlag_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlPdFlag_Object = MibScalar
sleDhcp6ClientBaseControlPdFlag = _SleDhcp6ClientBaseControlPdFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 10),
    _SleDhcp6ClientBaseControlPdFlag_Type()
)
sleDhcp6ClientBaseControlPdFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlPdFlag.setStatus("current")
_SleDhcp6ClientBaseControlPdHint_Type = OctetString
_SleDhcp6ClientBaseControlPdHint_Object = MibScalar
sleDhcp6ClientBaseControlPdHint = _SleDhcp6ClientBaseControlPdHint_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 11),
    _SleDhcp6ClientBaseControlPdHint_Type()
)
sleDhcp6ClientBaseControlPdHint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlPdHint.setStatus("current")


class _SleDhcp6ClientBaseControlIanaRapidCommit_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlIanaRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6ClientBaseControlIanaRapidCommit_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlIanaRapidCommit_Object = MibScalar
sleDhcp6ClientBaseControlIanaRapidCommit = _SleDhcp6ClientBaseControlIanaRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 12),
    _SleDhcp6ClientBaseControlIanaRapidCommit_Type()
)
sleDhcp6ClientBaseControlIanaRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlIanaRapidCommit.setStatus("current")


class _SleDhcp6ClientBaseControlIapdRapidCommit_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlIapdRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SleDhcp6ClientBaseControlIapdRapidCommit_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlIapdRapidCommit_Object = MibScalar
sleDhcp6ClientBaseControlIapdRapidCommit = _SleDhcp6ClientBaseControlIapdRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 13),
    _SleDhcp6ClientBaseControlIapdRapidCommit_Type()
)
sleDhcp6ClientBaseControlIapdRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlIapdRapidCommit.setStatus("current")


class _SleDhcp6ClientBaseControlRefreshMinimumVal_Type(Integer32):
    """Custom type sleDhcp6ClientBaseControlRefreshMinimumVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 315360000),
    )


_SleDhcp6ClientBaseControlRefreshMinimumVal_Type.__name__ = "Integer32"
_SleDhcp6ClientBaseControlRefreshMinimumVal_Object = MibScalar
sleDhcp6ClientBaseControlRefreshMinimumVal = _SleDhcp6ClientBaseControlRefreshMinimumVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 14),
    _SleDhcp6ClientBaseControlRefreshMinimumVal_Type()
)
sleDhcp6ClientBaseControlRefreshMinimumVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlRefreshMinimumVal.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlRefreshMinimumVal.setUnits("s")
_SleDhcp6ClientBaseControlPdname_Type = OctetString
_SleDhcp6ClientBaseControlPdname_Object = MibScalar
sleDhcp6ClientBaseControlPdname = _SleDhcp6ClientBaseControlPdname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 2, 15),
    _SleDhcp6ClientBaseControlPdname_Type()
)
sleDhcp6ClientBaseControlPdname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientBaseControlPdname.setStatus("current")
_SleDhcp6ClientBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6ClientBaseNotification = _SleDhcp6ClientBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3)
)
_SleDhcp6ClientOption_ObjectIdentity = ObjectIdentity
sleDhcp6ClientOption = _SleDhcp6ClientOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2)
)
_SleDhcp6ClientOptionTable_Object = MibTable
sleDhcp6ClientOptionTable = _SleDhcp6ClientOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ClientOptionTable.setStatus("current")
_SleDhcp6ClientOptionEntry_Object = MibTableRow
sleDhcp6ClientOptionEntry = _SleDhcp6ClientOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2, 1, 1)
)
sleDhcp6ClientOptionEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientOptionCode"),
)
if mibBuilder.loadTexts:
    sleDhcp6ClientOptionEntry.setStatus("current")


class _SleDhcp6ClientOptionCode_Type(Integer32):
    """Custom type sleDhcp6ClientOptionCode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("nisAddress", 1),
          ("nisDomain", 2),
          ("nispAddress", 3),
          ("nispDomain", 4),
          ("sipAddress", 5),
          ("sipDomain", 6),
          ("sntpAddress", 7),
          ("domainName", 8),
          ("dnsServer", 9),
          ("refreshTime", 10))
    )


_SleDhcp6ClientOptionCode_Type.__name__ = "Integer32"
_SleDhcp6ClientOptionCode_Object = MibTableColumn
sleDhcp6ClientOptionCode = _SleDhcp6ClientOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2, 1, 1, 1),
    _SleDhcp6ClientOptionCode_Type()
)
sleDhcp6ClientOptionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientOptionCode.setStatus("current")


class _SleDhcp6ClientOptionType_Type(Integer32):
    """Custom type sleDhcp6ClientOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6address", 1),
          ("text", 2))
    )


_SleDhcp6ClientOptionType_Type.__name__ = "Integer32"
_SleDhcp6ClientOptionType_Object = MibTableColumn
sleDhcp6ClientOptionType = _SleDhcp6ClientOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2, 1, 1, 2),
    _SleDhcp6ClientOptionType_Type()
)
sleDhcp6ClientOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientOptionType.setStatus("current")
_SleDhcp6ClientOptionValue_Type = OctetString
_SleDhcp6ClientOptionValue_Object = MibTableColumn
sleDhcp6ClientOptionValue = _SleDhcp6ClientOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 2, 1, 1, 3),
    _SleDhcp6ClientOptionValue_Type()
)
sleDhcp6ClientOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientOptionValue.setStatus("current")
_SleDhcp6ClientIapd_ObjectIdentity = ObjectIdentity
sleDhcp6ClientIapd = _SleDhcp6ClientIapd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3)
)
_SleDhcp6ClientIapdTable_Object = MibTable
sleDhcp6ClientIapdTable = _SleDhcp6ClientIapdTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdTable.setStatus("current")
_SleDhcp6ClientIapdEntry_Object = MibTableRow
sleDhcp6ClientIapdEntry = _SleDhcp6ClientIapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1)
)
sleDhcp6ClientIapdEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIapdIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdEntry.setStatus("current")


class _SleDhcp6ClientIapdIndex_Type(Integer32):
    """Custom type sleDhcp6ClientIapdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6ClientIapdIndex_Type.__name__ = "Integer32"
_SleDhcp6ClientIapdIndex_Object = MibTableColumn
sleDhcp6ClientIapdIndex = _SleDhcp6ClientIapdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 1),
    _SleDhcp6ClientIapdIndex_Type()
)
sleDhcp6ClientIapdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdIndex.setStatus("current")
_SleDhcp6ClientIapdIaid_Type = Integer32
_SleDhcp6ClientIapdIaid_Object = MibTableColumn
sleDhcp6ClientIapdIaid = _SleDhcp6ClientIapdIaid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 2),
    _SleDhcp6ClientIapdIaid_Type()
)
sleDhcp6ClientIapdIaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdIaid.setStatus("current")
_SleDhcp6ClientIapdT1_Type = Integer32
_SleDhcp6ClientIapdT1_Object = MibTableColumn
sleDhcp6ClientIapdT1 = _SleDhcp6ClientIapdT1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 3),
    _SleDhcp6ClientIapdT1_Type()
)
sleDhcp6ClientIapdT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdT1.setStatus("current")
_SleDhcp6ClientIapdT2_Type = Integer32
_SleDhcp6ClientIapdT2_Object = MibTableColumn
sleDhcp6ClientIapdT2 = _SleDhcp6ClientIapdT2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 4),
    _SleDhcp6ClientIapdT2_Type()
)
sleDhcp6ClientIapdT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdT2.setStatus("current")
_SleDhcp6ClientIapdPrefix_Type = OctetString
_SleDhcp6ClientIapdPrefix_Object = MibTableColumn
sleDhcp6ClientIapdPrefix = _SleDhcp6ClientIapdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 5),
    _SleDhcp6ClientIapdPrefix_Type()
)
sleDhcp6ClientIapdPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdPrefix.setStatus("current")


class _SleDhcp6ClientIapdPrefixLen_Type(Integer32):
    """Custom type sleDhcp6ClientIapdPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleDhcp6ClientIapdPrefixLen_Type.__name__ = "Integer32"
_SleDhcp6ClientIapdPrefixLen_Object = MibTableColumn
sleDhcp6ClientIapdPrefixLen = _SleDhcp6ClientIapdPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 6),
    _SleDhcp6ClientIapdPrefixLen_Type()
)
sleDhcp6ClientIapdPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdPrefixLen.setStatus("current")


class _SleDhcp6ClientIapdLifeTime_Type(Integer32):
    """Custom type sleDhcp6ClientIapdLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6ClientIapdLifeTime_Type.__name__ = "Integer32"
_SleDhcp6ClientIapdLifeTime_Object = MibTableColumn
sleDhcp6ClientIapdLifeTime = _SleDhcp6ClientIapdLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 7),
    _SleDhcp6ClientIapdLifeTime_Type()
)
sleDhcp6ClientIapdLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdLifeTime.setUnits("s")


class _SleDhcp6ClientIapdValidTime_Type(Integer32):
    """Custom type sleDhcp6ClientIapdValidTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6ClientIapdValidTime_Type.__name__ = "Integer32"
_SleDhcp6ClientIapdValidTime_Object = MibTableColumn
sleDhcp6ClientIapdValidTime = _SleDhcp6ClientIapdValidTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 8),
    _SleDhcp6ClientIapdValidTime_Type()
)
sleDhcp6ClientIapdValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdValidTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdValidTime.setUnits("s")
_SleDhcp6ClientIapdExpireTime_Type = Integer32
_SleDhcp6ClientIapdExpireTime_Object = MibTableColumn
sleDhcp6ClientIapdExpireTime = _SleDhcp6ClientIapdExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 3, 1, 1, 9),
    _SleDhcp6ClientIapdExpireTime_Type()
)
sleDhcp6ClientIapdExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIapdExpireTime.setUnits("s")
_SleDhcp6ClientIana_ObjectIdentity = ObjectIdentity
sleDhcp6ClientIana = _SleDhcp6ClientIana_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4)
)
_SleDhcp6ClientIanaTable_Object = MibTable
sleDhcp6ClientIanaTable = _SleDhcp6ClientIanaTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaTable.setStatus("current")
_SleDhcp6ClientIanaEntry_Object = MibTableRow
sleDhcp6ClientIanaEntry = _SleDhcp6ClientIanaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1)
)
sleDhcp6ClientIanaEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6ClientIanaIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaEntry.setStatus("current")


class _SleDhcp6ClientIanaIndex_Type(Integer32):
    """Custom type sleDhcp6ClientIanaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6ClientIanaIndex_Type.__name__ = "Integer32"
_SleDhcp6ClientIanaIndex_Object = MibTableColumn
sleDhcp6ClientIanaIndex = _SleDhcp6ClientIanaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 1),
    _SleDhcp6ClientIanaIndex_Type()
)
sleDhcp6ClientIanaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaIndex.setStatus("current")
_SleDhcp6ClientIanaIaid_Type = Integer32
_SleDhcp6ClientIanaIaid_Object = MibTableColumn
sleDhcp6ClientIanaIaid = _SleDhcp6ClientIanaIaid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 2),
    _SleDhcp6ClientIanaIaid_Type()
)
sleDhcp6ClientIanaIaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaIaid.setStatus("current")
_SleDhcp6ClientIanaT1_Type = Integer32
_SleDhcp6ClientIanaT1_Object = MibTableColumn
sleDhcp6ClientIanaT1 = _SleDhcp6ClientIanaT1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 3),
    _SleDhcp6ClientIanaT1_Type()
)
sleDhcp6ClientIanaT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaT1.setStatus("current")
_SleDhcp6ClientIanaT2_Type = Integer32
_SleDhcp6ClientIanaT2_Object = MibTableColumn
sleDhcp6ClientIanaT2 = _SleDhcp6ClientIanaT2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 4),
    _SleDhcp6ClientIanaT2_Type()
)
sleDhcp6ClientIanaT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaT2.setStatus("current")
_SleDhcp6ClientIanaAddress_Type = OctetString
_SleDhcp6ClientIanaAddress_Object = MibTableColumn
sleDhcp6ClientIanaAddress = _SleDhcp6ClientIanaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 5),
    _SleDhcp6ClientIanaAddress_Type()
)
sleDhcp6ClientIanaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaAddress.setStatus("current")


class _SleDhcp6ClientIanaLifeTime_Type(Integer32):
    """Custom type sleDhcp6ClientIanaLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6ClientIanaLifeTime_Type.__name__ = "Integer32"
_SleDhcp6ClientIanaLifeTime_Object = MibTableColumn
sleDhcp6ClientIanaLifeTime = _SleDhcp6ClientIanaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 6),
    _SleDhcp6ClientIanaLifeTime_Type()
)
sleDhcp6ClientIanaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaLifeTime.setUnits("s")


class _SleDhcp6ClientIanaValidTime_Type(Integer32):
    """Custom type sleDhcp6ClientIanaValidTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 315360000),
    )


_SleDhcp6ClientIanaValidTime_Type.__name__ = "Integer32"
_SleDhcp6ClientIanaValidTime_Object = MibTableColumn
sleDhcp6ClientIanaValidTime = _SleDhcp6ClientIanaValidTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 7),
    _SleDhcp6ClientIanaValidTime_Type()
)
sleDhcp6ClientIanaValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaValidTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaValidTime.setUnits("s")
_SleDhcp6ClientIanaExpireTime_Type = Integer32
_SleDhcp6ClientIanaExpireTime_Object = MibTableColumn
sleDhcp6ClientIanaExpireTime = _SleDhcp6ClientIanaExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 4, 1, 1, 8),
    _SleDhcp6ClientIanaExpireTime_Type()
)
sleDhcp6ClientIanaExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6ClientIanaExpireTime.setUnits("s")
_SleDhcp6Option_ObjectIdentity = ObjectIdentity
sleDhcp6Option = _SleDhcp6Option_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8)
)
_SleDhcp6OptionBase_ObjectIdentity = ObjectIdentity
sleDhcp6OptionBase = _SleDhcp6OptionBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1)
)
_SleDhcp6OptionBaseTable_Object = MibTable
sleDhcp6OptionBaseTable = _SleDhcp6OptionBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseTable.setStatus("current")
_SleDhcp6OptionBaseEntry_Object = MibTableRow
sleDhcp6OptionBaseEntry = _SleDhcp6OptionBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1, 1)
)
sleDhcp6OptionBaseEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6OptionBaseIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseEntry.setStatus("current")


class _SleDhcp6OptionBaseIndex_Type(Integer32):
    """Custom type sleDhcp6OptionBaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleDhcp6OptionBaseIndex_Type.__name__ = "Integer32"
_SleDhcp6OptionBaseIndex_Object = MibTableColumn
sleDhcp6OptionBaseIndex = _SleDhcp6OptionBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1, 1, 1),
    _SleDhcp6OptionBaseIndex_Type()
)
sleDhcp6OptionBaseIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseIndex.setStatus("current")


class _SleDhcp6OptionBaseName_Type(OctetString):
    """Custom type sleDhcp6OptionBaseName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SleDhcp6OptionBaseName_Type.__name__ = "OctetString"
_SleDhcp6OptionBaseName_Object = MibTableColumn
sleDhcp6OptionBaseName = _SleDhcp6OptionBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1, 1, 2),
    _SleDhcp6OptionBaseName_Type()
)
sleDhcp6OptionBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseName.setStatus("current")
_SleDhcp6OptionBaseRawDataLen_Type = Integer32
_SleDhcp6OptionBaseRawDataLen_Object = MibTableColumn
sleDhcp6OptionBaseRawDataLen = _SleDhcp6OptionBaseRawDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1, 1, 3),
    _SleDhcp6OptionBaseRawDataLen_Type()
)
sleDhcp6OptionBaseRawDataLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseRawDataLen.setStatus("current")
_SleDhcp6OptionBaseRawData_Type = OctetString
_SleDhcp6OptionBaseRawData_Object = MibTableColumn
sleDhcp6OptionBaseRawData = _SleDhcp6OptionBaseRawData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 1, 1, 4),
    _SleDhcp6OptionBaseRawData_Type()
)
sleDhcp6OptionBaseRawData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseRawData.setStatus("current")
_SleDhcp6OptionBaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6OptionBaseControl = _SleDhcp6OptionBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2)
)


class _SleDhcp6OptionBaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6OptionBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Option", 1),
          ("destroyDhcp6Option", 2))
    )


_SleDhcp6OptionBaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6OptionBaseControlRequest_Object = MibScalar
sleDhcp6OptionBaseControlRequest = _SleDhcp6OptionBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 1),
    _SleDhcp6OptionBaseControlRequest_Type()
)
sleDhcp6OptionBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlRequest.setStatus("current")
_SleDhcp6OptionBaseControlStatus_Type = SleControlStatusType
_SleDhcp6OptionBaseControlStatus_Object = MibScalar
sleDhcp6OptionBaseControlStatus = _SleDhcp6OptionBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 2),
    _SleDhcp6OptionBaseControlStatus_Type()
)
sleDhcp6OptionBaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlStatus.setStatus("current")
_SleDhcp6OptionBaseControlTimer_Type = Gauge32
_SleDhcp6OptionBaseControlTimer_Object = MibScalar
sleDhcp6OptionBaseControlTimer = _SleDhcp6OptionBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 3),
    _SleDhcp6OptionBaseControlTimer_Type()
)
sleDhcp6OptionBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlTimer.setStatus("current")
_SleDhcp6OptionBaseControlTimeStamp_Type = TimeTicks
_SleDhcp6OptionBaseControlTimeStamp_Object = MibScalar
sleDhcp6OptionBaseControlTimeStamp = _SleDhcp6OptionBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 4),
    _SleDhcp6OptionBaseControlTimeStamp_Type()
)
sleDhcp6OptionBaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlTimeStamp.setStatus("current")
_SleDhcp6OptionBaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6OptionBaseControlReqResult_Object = MibScalar
sleDhcp6OptionBaseControlReqResult = _SleDhcp6OptionBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 5),
    _SleDhcp6OptionBaseControlReqResult_Type()
)
sleDhcp6OptionBaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlReqResult.setStatus("current")
_SleDhcp6OptionBaseControlIndex_Type = Integer32
_SleDhcp6OptionBaseControlIndex_Object = MibScalar
sleDhcp6OptionBaseControlIndex = _SleDhcp6OptionBaseControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 6),
    _SleDhcp6OptionBaseControlIndex_Type()
)
sleDhcp6OptionBaseControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlIndex.setStatus("current")


class _SleDhcp6OptionBaseControlName_Type(OctetString):
    """Custom type sleDhcp6OptionBaseControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SleDhcp6OptionBaseControlName_Type.__name__ = "OctetString"
_SleDhcp6OptionBaseControlName_Object = MibScalar
sleDhcp6OptionBaseControlName = _SleDhcp6OptionBaseControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 2, 7),
    _SleDhcp6OptionBaseControlName_Type()
)
sleDhcp6OptionBaseControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionBaseControlName.setStatus("current")
_SleDhcp6OptionBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6OptionBaseNotification = _SleDhcp6OptionBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 3)
)
_SleDhcp6OptionAttr_ObjectIdentity = ObjectIdentity
sleDhcp6OptionAttr = _SleDhcp6OptionAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2)
)
_SleDhcp6OptionAttrTable_Object = MibTable
sleDhcp6OptionAttrTable = _SleDhcp6OptionAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrTable.setStatus("current")
_SleDhcp6OptionAttrEntry_Object = MibTableRow
sleDhcp6OptionAttrEntry = _SleDhcp6OptionAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1)
)
sleDhcp6OptionAttrEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6OptionBaseIndex"),
    (0, "SLE-DHCPV6-MIB", "sleDhcp6OptionAttrId"),
)
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrEntry.setStatus("current")


class _SleDhcp6OptionAttrId_Type(Integer32):
    """Custom type sleDhcp6OptionAttrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleDhcp6OptionAttrId_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrId_Object = MibTableColumn
sleDhcp6OptionAttrId = _SleDhcp6OptionAttrId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 1),
    _SleDhcp6OptionAttrId_Type()
)
sleDhcp6OptionAttrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrId.setStatus("current")


class _SleDhcp6OptionAttrType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6OptionAttrType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrType_Object = MibTableColumn
sleDhcp6OptionAttrType = _SleDhcp6OptionAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 2),
    _SleDhcp6OptionAttrType_Type()
)
sleDhcp6OptionAttrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrType.setStatus("current")


class _SleDhcp6OptionAttrLengthHidden_Type(Integer32):
    """Custom type sleDhcp6OptionAttrLengthHidden based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SleDhcp6OptionAttrLengthHidden_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrLengthHidden_Object = MibTableColumn
sleDhcp6OptionAttrLengthHidden = _SleDhcp6OptionAttrLengthHidden_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 3),
    _SleDhcp6OptionAttrLengthHidden_Type()
)
sleDhcp6OptionAttrLengthHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrLengthHidden.setStatus("current")


class _SleDhcp6OptionAttrLengthType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrLengthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_SleDhcp6OptionAttrLengthType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrLengthType_Object = MibTableColumn
sleDhcp6OptionAttrLengthType = _SleDhcp6OptionAttrLengthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 4),
    _SleDhcp6OptionAttrLengthType_Type()
)
sleDhcp6OptionAttrLengthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrLengthType.setStatus("current")
_SleDhcp6OptionAttrLengthValue_Type = OctetString
_SleDhcp6OptionAttrLengthValue_Object = MibTableColumn
sleDhcp6OptionAttrLengthValue = _SleDhcp6OptionAttrLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 5),
    _SleDhcp6OptionAttrLengthValue_Type()
)
sleDhcp6OptionAttrLengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrLengthValue.setStatus("current")


class _SleDhcp6OptionAttrValueType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ifipv6", 2),
          ("index", 3),
          ("ipv6", 4),
          ("string", 5))
    )


_SleDhcp6OptionAttrValueType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrValueType_Object = MibTableColumn
sleDhcp6OptionAttrValueType = _SleDhcp6OptionAttrValueType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 6),
    _SleDhcp6OptionAttrValueType_Type()
)
sleDhcp6OptionAttrValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrValueType.setStatus("current")
_SleDhcp6OptionAttrValue_Type = OctetString
_SleDhcp6OptionAttrValue_Object = MibTableColumn
sleDhcp6OptionAttrValue = _SleDhcp6OptionAttrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 1, 1, 7),
    _SleDhcp6OptionAttrValue_Type()
)
sleDhcp6OptionAttrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrValue.setStatus("current")
_SleDhcp6OptionAttrControl_ObjectIdentity = ObjectIdentity
sleDhcp6OptionAttrControl = _SleDhcp6OptionAttrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2)
)


class _SleDhcp6OptionAttrControlRequest_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6OptionAttr", 1),
          ("destroyDhcp6OptionAttr", 2),
          ("changeDhcp6OptionAttr", 3))
    )


_SleDhcp6OptionAttrControlRequest_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlRequest_Object = MibScalar
sleDhcp6OptionAttrControlRequest = _SleDhcp6OptionAttrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 1),
    _SleDhcp6OptionAttrControlRequest_Type()
)
sleDhcp6OptionAttrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlRequest.setStatus("current")
_SleDhcp6OptionAttrControlStatus_Type = SleControlStatusType
_SleDhcp6OptionAttrControlStatus_Object = MibScalar
sleDhcp6OptionAttrControlStatus = _SleDhcp6OptionAttrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 2),
    _SleDhcp6OptionAttrControlStatus_Type()
)
sleDhcp6OptionAttrControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlStatus.setStatus("current")
_SleDhcp6OptionAttrControlTimer_Type = Gauge32
_SleDhcp6OptionAttrControlTimer_Object = MibScalar
sleDhcp6OptionAttrControlTimer = _SleDhcp6OptionAttrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 3),
    _SleDhcp6OptionAttrControlTimer_Type()
)
sleDhcp6OptionAttrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlTimer.setStatus("current")
_SleDhcp6OptionAttrControlTimeStamp_Type = TimeTicks
_SleDhcp6OptionAttrControlTimeStamp_Object = MibScalar
sleDhcp6OptionAttrControlTimeStamp = _SleDhcp6OptionAttrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 4),
    _SleDhcp6OptionAttrControlTimeStamp_Type()
)
sleDhcp6OptionAttrControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlTimeStamp.setStatus("current")
_SleDhcp6OptionAttrControlReqResult_Type = SleControlRequestResultType
_SleDhcp6OptionAttrControlReqResult_Object = MibScalar
sleDhcp6OptionAttrControlReqResult = _SleDhcp6OptionAttrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 5),
    _SleDhcp6OptionAttrControlReqResult_Type()
)
sleDhcp6OptionAttrControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlReqResult.setStatus("current")
_SleDhcp6OptionAttrControlOptionIndex_Type = Integer32
_SleDhcp6OptionAttrControlOptionIndex_Object = MibScalar
sleDhcp6OptionAttrControlOptionIndex = _SleDhcp6OptionAttrControlOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 6),
    _SleDhcp6OptionAttrControlOptionIndex_Type()
)
sleDhcp6OptionAttrControlOptionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlOptionIndex.setStatus("current")


class _SleDhcp6OptionAttrControlId_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleDhcp6OptionAttrControlId_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlId_Object = MibScalar
sleDhcp6OptionAttrControlId = _SleDhcp6OptionAttrControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 7),
    _SleDhcp6OptionAttrControlId_Type()
)
sleDhcp6OptionAttrControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlId.setStatus("current")


class _SleDhcp6OptionAttrControlType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleDhcp6OptionAttrControlType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlType_Object = MibScalar
sleDhcp6OptionAttrControlType = _SleDhcp6OptionAttrControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 8),
    _SleDhcp6OptionAttrControlType_Type()
)
sleDhcp6OptionAttrControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlType.setStatus("current")


class _SleDhcp6OptionAttrControlLengthHidden_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlLengthHidden based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SleDhcp6OptionAttrControlLengthHidden_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlLengthHidden_Object = MibScalar
sleDhcp6OptionAttrControlLengthHidden = _SleDhcp6OptionAttrControlLengthHidden_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 9),
    _SleDhcp6OptionAttrControlLengthHidden_Type()
)
sleDhcp6OptionAttrControlLengthHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlLengthHidden.setStatus("current")


class _SleDhcp6OptionAttrControlLengthType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlLengthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_SleDhcp6OptionAttrControlLengthType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlLengthType_Object = MibScalar
sleDhcp6OptionAttrControlLengthType = _SleDhcp6OptionAttrControlLengthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 10),
    _SleDhcp6OptionAttrControlLengthType_Type()
)
sleDhcp6OptionAttrControlLengthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlLengthType.setStatus("current")
_SleDhcp6OptionAttrControlLengthValue_Type = OctetString
_SleDhcp6OptionAttrControlLengthValue_Object = MibScalar
sleDhcp6OptionAttrControlLengthValue = _SleDhcp6OptionAttrControlLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 11),
    _SleDhcp6OptionAttrControlLengthValue_Type()
)
sleDhcp6OptionAttrControlLengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlLengthValue.setStatus("current")


class _SleDhcp6OptionAttrControlValueType_Type(Integer32):
    """Custom type sleDhcp6OptionAttrControlValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ifipv6", 2),
          ("index", 3),
          ("ipv6", 4),
          ("string", 5))
    )


_SleDhcp6OptionAttrControlValueType_Type.__name__ = "Integer32"
_SleDhcp6OptionAttrControlValueType_Object = MibScalar
sleDhcp6OptionAttrControlValueType = _SleDhcp6OptionAttrControlValueType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 12),
    _SleDhcp6OptionAttrControlValueType_Type()
)
sleDhcp6OptionAttrControlValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlValueType.setStatus("current")
_SleDhcp6OptionAttrControlValue_Type = OctetString
_SleDhcp6OptionAttrControlValue_Object = MibScalar
sleDhcp6OptionAttrControlValue = _SleDhcp6OptionAttrControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 2, 13),
    _SleDhcp6OptionAttrControlValue_Type()
)
sleDhcp6OptionAttrControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrControlValue.setStatus("current")
_SleDhcp6OptionAttrNotification_ObjectIdentity = ObjectIdentity
sleDhcp6OptionAttrNotification = _SleDhcp6OptionAttrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 3)
)
_SleDhcp6Snooping_ObjectIdentity = ObjectIdentity
sleDhcp6Snooping = _SleDhcp6Snooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9)
)
_SleDhcp6SnoopBase_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBase = _SleDhcp6SnoopBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1)
)
_SleDhcp6SnoopBaseInfo_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBaseInfo = _SleDhcp6SnoopBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 1)
)


class _SleDhcp6SnoopBaseState_Type(Integer32):
    """Custom type sleDhcp6SnoopBaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopBaseState_Type.__name__ = "Integer32"
_SleDhcp6SnoopBaseState_Object = MibScalar
sleDhcp6SnoopBaseState = _SleDhcp6SnoopBaseState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 1, 1),
    _SleDhcp6SnoopBaseState_Type()
)
sleDhcp6SnoopBaseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseState.setStatus("current")


class _SleDhcp6SnoopBaseNdInspTime_Type(Integer32):
    """Custom type sleDhcp6SnoopBaseNdInspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleDhcp6SnoopBaseNdInspTime_Type.__name__ = "Integer32"
_SleDhcp6SnoopBaseNdInspTime_Object = MibScalar
sleDhcp6SnoopBaseNdInspTime = _SleDhcp6SnoopBaseNdInspTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 1, 2),
    _SleDhcp6SnoopBaseNdInspTime_Type()
)
sleDhcp6SnoopBaseNdInspTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseNdInspTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseNdInspTime.setUnits("s")
_SleDhcp6SnoopBaseControl_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBaseControl = _SleDhcp6SnoopBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2)
)


class _SleDhcp6SnoopBaseControlRequest_Type(Integer32):
    """Custom type sleDhcp6SnoopBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setDhcp6SnoopState", 1),
          ("setDhcp6SnoopNdInspTime", 2))
    )


_SleDhcp6SnoopBaseControlRequest_Type.__name__ = "Integer32"
_SleDhcp6SnoopBaseControlRequest_Object = MibScalar
sleDhcp6SnoopBaseControlRequest = _SleDhcp6SnoopBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 1),
    _SleDhcp6SnoopBaseControlRequest_Type()
)
sleDhcp6SnoopBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlRequest.setStatus("current")
_SleDhcp6SnoopBaseControlStatus_Type = SleControlStatusType
_SleDhcp6SnoopBaseControlStatus_Object = MibScalar
sleDhcp6SnoopBaseControlStatus = _SleDhcp6SnoopBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 2),
    _SleDhcp6SnoopBaseControlStatus_Type()
)
sleDhcp6SnoopBaseControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlStatus.setStatus("current")
_SleDhcp6SnoopBaseControlTimer_Type = Gauge32
_SleDhcp6SnoopBaseControlTimer_Object = MibScalar
sleDhcp6SnoopBaseControlTimer = _SleDhcp6SnoopBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 3),
    _SleDhcp6SnoopBaseControlTimer_Type()
)
sleDhcp6SnoopBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlTimer.setStatus("current")
_SleDhcp6SnoopBaseControlTimeStamp_Type = TimeTicks
_SleDhcp6SnoopBaseControlTimeStamp_Object = MibScalar
sleDhcp6SnoopBaseControlTimeStamp = _SleDhcp6SnoopBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 4),
    _SleDhcp6SnoopBaseControlTimeStamp_Type()
)
sleDhcp6SnoopBaseControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlTimeStamp.setStatus("current")
_SleDhcp6SnoopBaseControlReqResult_Type = SleControlRequestResultType
_SleDhcp6SnoopBaseControlReqResult_Object = MibScalar
sleDhcp6SnoopBaseControlReqResult = _SleDhcp6SnoopBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 5),
    _SleDhcp6SnoopBaseControlReqResult_Type()
)
sleDhcp6SnoopBaseControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlReqResult.setStatus("current")


class _SleDhcp6SnoopBaseControlState_Type(Integer32):
    """Custom type sleDhcp6SnoopBaseControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopBaseControlState_Type.__name__ = "Integer32"
_SleDhcp6SnoopBaseControlState_Object = MibScalar
sleDhcp6SnoopBaseControlState = _SleDhcp6SnoopBaseControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 6),
    _SleDhcp6SnoopBaseControlState_Type()
)
sleDhcp6SnoopBaseControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlState.setStatus("current")


class _SleDhcp6SnoopBaseControlNdInspTime_Type(Integer32):
    """Custom type sleDhcp6SnoopBaseControlNdInspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleDhcp6SnoopBaseControlNdInspTime_Type.__name__ = "Integer32"
_SleDhcp6SnoopBaseControlNdInspTime_Object = MibScalar
sleDhcp6SnoopBaseControlNdInspTime = _SleDhcp6SnoopBaseControlNdInspTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 2, 7),
    _SleDhcp6SnoopBaseControlNdInspTime_Type()
)
sleDhcp6SnoopBaseControlNdInspTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlNdInspTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseControlNdInspTime.setUnits("s")
_SleDhcp6SnoopBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBaseNotification = _SleDhcp6SnoopBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 3)
)
_SleDhcp6SnoopVlan_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopVlan = _SleDhcp6SnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2)
)
_SleDhcp6SnoopVlanTable_Object = MibTable
sleDhcp6SnoopVlanTable = _SleDhcp6SnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanTable.setStatus("current")
_SleDhcp6SnoopVlanEntry_Object = MibTableRow
sleDhcp6SnoopVlanEntry = _SleDhcp6SnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 1, 1)
)
sleDhcp6SnoopVlanEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanEntry.setStatus("current")


class _SleDhcp6SnoopVlanIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleDhcp6SnoopVlanIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopVlanIndex_Object = MibTableColumn
sleDhcp6SnoopVlanIndex = _SleDhcp6SnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 1, 1, 1),
    _SleDhcp6SnoopVlanIndex_Type()
)
sleDhcp6SnoopVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanIndex.setStatus("current")


class _SleDhcp6SnoopVlanState_Type(Integer32):
    """Custom type sleDhcp6SnoopVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopVlanState_Type.__name__ = "Integer32"
_SleDhcp6SnoopVlanState_Object = MibTableColumn
sleDhcp6SnoopVlanState = _SleDhcp6SnoopVlanState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 1, 1, 2),
    _SleDhcp6SnoopVlanState_Type()
)
sleDhcp6SnoopVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanState.setStatus("current")
_SleDhcp6SnoopVlanControl_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopVlanControl = _SleDhcp6SnoopVlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2)
)


class _SleDhcp6SnoopVlanControlRequest_Type(Integer32):
    """Custom type sleDhcp6SnoopVlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDhcp6SnoopVlanState", 1)
    )


_SleDhcp6SnoopVlanControlRequest_Type.__name__ = "Integer32"
_SleDhcp6SnoopVlanControlRequest_Object = MibScalar
sleDhcp6SnoopVlanControlRequest = _SleDhcp6SnoopVlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 1),
    _SleDhcp6SnoopVlanControlRequest_Type()
)
sleDhcp6SnoopVlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlRequest.setStatus("current")
_SleDhcp6SnoopVlanControlStatus_Type = SleControlStatusType
_SleDhcp6SnoopVlanControlStatus_Object = MibScalar
sleDhcp6SnoopVlanControlStatus = _SleDhcp6SnoopVlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 2),
    _SleDhcp6SnoopVlanControlStatus_Type()
)
sleDhcp6SnoopVlanControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlStatus.setStatus("current")
_SleDhcp6SnoopVlanControlTimer_Type = Gauge32
_SleDhcp6SnoopVlanControlTimer_Object = MibScalar
sleDhcp6SnoopVlanControlTimer = _SleDhcp6SnoopVlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 3),
    _SleDhcp6SnoopVlanControlTimer_Type()
)
sleDhcp6SnoopVlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlTimer.setStatus("current")
_SleDhcp6SnoopVlanControlTimeStamp_Type = TimeTicks
_SleDhcp6SnoopVlanControlTimeStamp_Object = MibScalar
sleDhcp6SnoopVlanControlTimeStamp = _SleDhcp6SnoopVlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 4),
    _SleDhcp6SnoopVlanControlTimeStamp_Type()
)
sleDhcp6SnoopVlanControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlTimeStamp.setStatus("current")
_SleDhcp6SnoopVlanControlReqResult_Type = SleControlRequestResultType
_SleDhcp6SnoopVlanControlReqResult_Object = MibScalar
sleDhcp6SnoopVlanControlReqResult = _SleDhcp6SnoopVlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 5),
    _SleDhcp6SnoopVlanControlReqResult_Type()
)
sleDhcp6SnoopVlanControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlReqResult.setStatus("current")


class _SleDhcp6SnoopVlanControlIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopVlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleDhcp6SnoopVlanControlIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopVlanControlIndex_Object = MibScalar
sleDhcp6SnoopVlanControlIndex = _SleDhcp6SnoopVlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 6),
    _SleDhcp6SnoopVlanControlIndex_Type()
)
sleDhcp6SnoopVlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlIndex.setStatus("current")


class _SleDhcp6SnoopVlanControlState_Type(Integer32):
    """Custom type sleDhcp6SnoopVlanControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopVlanControlState_Type.__name__ = "Integer32"
_SleDhcp6SnoopVlanControlState_Object = MibScalar
sleDhcp6SnoopVlanControlState = _SleDhcp6SnoopVlanControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 2, 7),
    _SleDhcp6SnoopVlanControlState_Type()
)
sleDhcp6SnoopVlanControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanControlState.setStatus("current")
_SleDhcp6SnoopVlanNotification_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopVlanNotification = _SleDhcp6SnoopVlanNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 3)
)
_SleDhcp6SnoopPort_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopPort = _SleDhcp6SnoopPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3)
)
_SleDhcp6SnoopPortTable_Object = MibTable
sleDhcp6SnoopPortTable = _SleDhcp6SnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortTable.setStatus("current")
_SleDhcp6SnoopPortEntry_Object = MibTableRow
sleDhcp6SnoopPortEntry = _SleDhcp6SnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1, 1)
)
sleDhcp6SnoopPortEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6SnoopPortIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortEntry.setStatus("current")


class _SleDhcp6SnoopPortIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopPortIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortIndex_Object = MibTableColumn
sleDhcp6SnoopPortIndex = _SleDhcp6SnoopPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1, 1, 1),
    _SleDhcp6SnoopPortIndex_Type()
)
sleDhcp6SnoopPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortIndex.setStatus("current")


class _SleDhcp6SnoopPortTrusted_Type(Integer32):
    """Custom type sleDhcp6SnoopPortTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_SleDhcp6SnoopPortTrusted_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortTrusted_Object = MibTableColumn
sleDhcp6SnoopPortTrusted = _SleDhcp6SnoopPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1, 1, 2),
    _SleDhcp6SnoopPortTrusted_Type()
)
sleDhcp6SnoopPortTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortTrusted.setStatus("current")


class _SleDhcp6SnoopPortLimitRate_Type(Integer32):
    """Custom type sleDhcp6SnoopPortLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopPortLimitRate_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortLimitRate_Object = MibTableColumn
sleDhcp6SnoopPortLimitRate = _SleDhcp6SnoopPortLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1, 1, 3),
    _SleDhcp6SnoopPortLimitRate_Type()
)
sleDhcp6SnoopPortLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortLimitRate.setStatus("current")


class _SleDhcp6SnoopPortLimitLease_Type(Integer32):
    """Custom type sleDhcp6SnoopPortLimitLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleDhcp6SnoopPortLimitLease_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortLimitLease_Object = MibTableColumn
sleDhcp6SnoopPortLimitLease = _SleDhcp6SnoopPortLimitLease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 1, 1, 4),
    _SleDhcp6SnoopPortLimitLease_Type()
)
sleDhcp6SnoopPortLimitLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortLimitLease.setStatus("current")
_SleDhcp6SnoopPortControl_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopPortControl = _SleDhcp6SnoopPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2)
)


class _SleDhcp6SnoopPortControlRequest_Type(Integer32):
    """Custom type sleDhcp6SnoopPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setDhcp6SnoopPortTrust", 1),
          ("setDhcp6SnoopPortLimitRate", 2),
          ("setDhcp6SnoopPortLimitLease", 3))
    )


_SleDhcp6SnoopPortControlRequest_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortControlRequest_Object = MibScalar
sleDhcp6SnoopPortControlRequest = _SleDhcp6SnoopPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 1),
    _SleDhcp6SnoopPortControlRequest_Type()
)
sleDhcp6SnoopPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlRequest.setStatus("current")
_SleDhcp6SnoopPortControlStatus_Type = SleControlStatusType
_SleDhcp6SnoopPortControlStatus_Object = MibScalar
sleDhcp6SnoopPortControlStatus = _SleDhcp6SnoopPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 2),
    _SleDhcp6SnoopPortControlStatus_Type()
)
sleDhcp6SnoopPortControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlStatus.setStatus("current")
_SleDhcp6SnoopPortControlTimer_Type = Gauge32
_SleDhcp6SnoopPortControlTimer_Object = MibScalar
sleDhcp6SnoopPortControlTimer = _SleDhcp6SnoopPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 3),
    _SleDhcp6SnoopPortControlTimer_Type()
)
sleDhcp6SnoopPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlTimer.setStatus("current")
_SleDhcp6SnoopPortControlTimeStamp_Type = TimeTicks
_SleDhcp6SnoopPortControlTimeStamp_Object = MibScalar
sleDhcp6SnoopPortControlTimeStamp = _SleDhcp6SnoopPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 4),
    _SleDhcp6SnoopPortControlTimeStamp_Type()
)
sleDhcp6SnoopPortControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlTimeStamp.setStatus("current")
_SleDhcp6SnoopPortControlReqResult_Type = SleControlRequestResultType
_SleDhcp6SnoopPortControlReqResult_Object = MibScalar
sleDhcp6SnoopPortControlReqResult = _SleDhcp6SnoopPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 5),
    _SleDhcp6SnoopPortControlReqResult_Type()
)
sleDhcp6SnoopPortControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlReqResult.setStatus("current")


class _SleDhcp6SnoopPortControlIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopPortControlIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortControlIndex_Object = MibScalar
sleDhcp6SnoopPortControlIndex = _SleDhcp6SnoopPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 6),
    _SleDhcp6SnoopPortControlIndex_Type()
)
sleDhcp6SnoopPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlIndex.setStatus("current")


class _SleDhcp6SnoopPortControlTrusted_Type(Integer32):
    """Custom type sleDhcp6SnoopPortControlTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_SleDhcp6SnoopPortControlTrusted_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortControlTrusted_Object = MibScalar
sleDhcp6SnoopPortControlTrusted = _SleDhcp6SnoopPortControlTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 7),
    _SleDhcp6SnoopPortControlTrusted_Type()
)
sleDhcp6SnoopPortControlTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlTrusted.setStatus("current")


class _SleDhcp6SnoopPortControlLimitRate_Type(Integer32):
    """Custom type sleDhcp6SnoopPortControlLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopPortControlLimitRate_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortControlLimitRate_Object = MibScalar
sleDhcp6SnoopPortControlLimitRate = _SleDhcp6SnoopPortControlLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 8),
    _SleDhcp6SnoopPortControlLimitRate_Type()
)
sleDhcp6SnoopPortControlLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlLimitRate.setStatus("current")


class _SleDhcp6SnoopPortControlLimitLease_Type(Integer32):
    """Custom type sleDhcp6SnoopPortControlLimitLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleDhcp6SnoopPortControlLimitLease_Type.__name__ = "Integer32"
_SleDhcp6SnoopPortControlLimitLease_Object = MibScalar
sleDhcp6SnoopPortControlLimitLease = _SleDhcp6SnoopPortControlLimitLease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 2, 9),
    _SleDhcp6SnoopPortControlLimitLease_Type()
)
sleDhcp6SnoopPortControlLimitLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortControlLimitLease.setStatus("current")
_SleDhcp6SnoopPortNotification_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopPortNotification = _SleDhcp6SnoopPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 3)
)
_SleDhcp6SnoopBind_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBind = _SleDhcp6SnoopBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4)
)
_SleDhcp6SnoopBindTable_Object = MibTable
sleDhcp6SnoopBindTable = _SleDhcp6SnoopBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindTable.setStatus("current")
_SleDhcp6SnoopBindEntry_Object = MibTableRow
sleDhcp6SnoopBindEntry = _SleDhcp6SnoopBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1)
)
sleDhcp6SnoopBindEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6SnoopBindIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindEntry.setStatus("current")


class _SleDhcp6SnoopBindIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleDhcp6SnoopBindIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindIndex_Object = MibTableColumn
sleDhcp6SnoopBindIndex = _SleDhcp6SnoopBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 1),
    _SleDhcp6SnoopBindIndex_Type()
)
sleDhcp6SnoopBindIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindIndex.setStatus("current")


class _SleDhcp6SnoopBindPortIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopBindPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopBindPortIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindPortIndex_Object = MibTableColumn
sleDhcp6SnoopBindPortIndex = _SleDhcp6SnoopBindPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 2),
    _SleDhcp6SnoopBindPortIndex_Type()
)
sleDhcp6SnoopBindPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindPortIndex.setStatus("current")
_SleDhcp6SnoopBindAddress_Type = OctetString
_SleDhcp6SnoopBindAddress_Object = MibTableColumn
sleDhcp6SnoopBindAddress = _SleDhcp6SnoopBindAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 3),
    _SleDhcp6SnoopBindAddress_Type()
)
sleDhcp6SnoopBindAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindAddress.setStatus("current")


class _SleDhcp6SnoopBindVlan_Type(Integer32):
    """Custom type sleDhcp6SnoopBindVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleDhcp6SnoopBindVlan_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindVlan_Object = MibTableColumn
sleDhcp6SnoopBindVlan = _SleDhcp6SnoopBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 4),
    _SleDhcp6SnoopBindVlan_Type()
)
sleDhcp6SnoopBindVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindVlan.setStatus("current")
_SleDhcp6SnoopBindMac_Type = MacAddress
_SleDhcp6SnoopBindMac_Object = MibTableColumn
sleDhcp6SnoopBindMac = _SleDhcp6SnoopBindMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 5),
    _SleDhcp6SnoopBindMac_Type()
)
sleDhcp6SnoopBindMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindMac.setStatus("current")


class _SleDhcp6SnoopBindValTime_Type(Integer32):
    """Custom type sleDhcp6SnoopBindValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcp6SnoopBindValTime_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindValTime_Object = MibTableColumn
sleDhcp6SnoopBindValTime = _SleDhcp6SnoopBindValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 6),
    _SleDhcp6SnoopBindValTime_Type()
)
sleDhcp6SnoopBindValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindValTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindValTime.setUnits("s")


class _SleDhcp6SnoopBindState_Type(Integer32):
    """Custom type sleDhcp6SnoopBindState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopBindState_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindState_Object = MibTableColumn
sleDhcp6SnoopBindState = _SleDhcp6SnoopBindState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 7),
    _SleDhcp6SnoopBindState_Type()
)
sleDhcp6SnoopBindState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindState.setStatus("current")


class _SleDhcp6SnoopBindType_Type(Integer32):
    """Custom type sleDhcp6SnoopBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_SleDhcp6SnoopBindType_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindType_Object = MibTableColumn
sleDhcp6SnoopBindType = _SleDhcp6SnoopBindType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 1, 1, 8),
    _SleDhcp6SnoopBindType_Type()
)
sleDhcp6SnoopBindType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindType.setStatus("current")
_SleDhcp6SnoopBindControl_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBindControl = _SleDhcp6SnoopBindControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2)
)


class _SleDhcp6SnoopBindControlRequest_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6SnoopBind", 1),
          ("destroyDhcp6SnoopBind", 2),
          ("clearDhcp6SnoopBind", 3))
    )


_SleDhcp6SnoopBindControlRequest_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlRequest_Object = MibScalar
sleDhcp6SnoopBindControlRequest = _SleDhcp6SnoopBindControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 1),
    _SleDhcp6SnoopBindControlRequest_Type()
)
sleDhcp6SnoopBindControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlRequest.setStatus("current")
_SleDhcp6SnoopBindControlStatus_Type = SleControlStatusType
_SleDhcp6SnoopBindControlStatus_Object = MibScalar
sleDhcp6SnoopBindControlStatus = _SleDhcp6SnoopBindControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 2),
    _SleDhcp6SnoopBindControlStatus_Type()
)
sleDhcp6SnoopBindControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlStatus.setStatus("current")
_SleDhcp6SnoopBindControlTimer_Type = Gauge32
_SleDhcp6SnoopBindControlTimer_Object = MibScalar
sleDhcp6SnoopBindControlTimer = _SleDhcp6SnoopBindControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 3),
    _SleDhcp6SnoopBindControlTimer_Type()
)
sleDhcp6SnoopBindControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlTimer.setStatus("current")
_SleDhcp6SnoopBindControlTimeStamp_Type = TimeTicks
_SleDhcp6SnoopBindControlTimeStamp_Object = MibScalar
sleDhcp6SnoopBindControlTimeStamp = _SleDhcp6SnoopBindControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 4),
    _SleDhcp6SnoopBindControlTimeStamp_Type()
)
sleDhcp6SnoopBindControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlTimeStamp.setStatus("current")
_SleDhcp6SnoopBindControlReqResult_Type = SleControlRequestResultType
_SleDhcp6SnoopBindControlReqResult_Object = MibScalar
sleDhcp6SnoopBindControlReqResult = _SleDhcp6SnoopBindControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 5),
    _SleDhcp6SnoopBindControlReqResult_Type()
)
sleDhcp6SnoopBindControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlReqResult.setStatus("current")
_SleDhcp6SnoopBindControlIndex_Type = Integer32
_SleDhcp6SnoopBindControlIndex_Object = MibScalar
sleDhcp6SnoopBindControlIndex = _SleDhcp6SnoopBindControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 6),
    _SleDhcp6SnoopBindControlIndex_Type()
)
sleDhcp6SnoopBindControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlIndex.setStatus("current")


class _SleDhcp6SnoopBindControlPortIndex_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDhcp6SnoopBindControlPortIndex_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlPortIndex_Object = MibScalar
sleDhcp6SnoopBindControlPortIndex = _SleDhcp6SnoopBindControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 7),
    _SleDhcp6SnoopBindControlPortIndex_Type()
)
sleDhcp6SnoopBindControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlPortIndex.setStatus("current")
_SleDhcp6SnoopBindControlAddress_Type = InetAddressIPv6
_SleDhcp6SnoopBindControlAddress_Object = MibScalar
sleDhcp6SnoopBindControlAddress = _SleDhcp6SnoopBindControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 8),
    _SleDhcp6SnoopBindControlAddress_Type()
)
sleDhcp6SnoopBindControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlAddress.setStatus("current")


class _SleDhcp6SnoopBindControlVlan_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleDhcp6SnoopBindControlVlan_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlVlan_Object = MibScalar
sleDhcp6SnoopBindControlVlan = _SleDhcp6SnoopBindControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 9),
    _SleDhcp6SnoopBindControlVlan_Type()
)
sleDhcp6SnoopBindControlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlVlan.setStatus("current")
_SleDhcp6SnoopBindControlMac_Type = MacAddress
_SleDhcp6SnoopBindControlMac_Object = MibScalar
sleDhcp6SnoopBindControlMac = _SleDhcp6SnoopBindControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 10),
    _SleDhcp6SnoopBindControlMac_Type()
)
sleDhcp6SnoopBindControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlMac.setStatus("current")


class _SleDhcp6SnoopBindControlValTime_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlValTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcp6SnoopBindControlValTime_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlValTime_Object = MibScalar
sleDhcp6SnoopBindControlValTime = _SleDhcp6SnoopBindControlValTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 11),
    _SleDhcp6SnoopBindControlValTime_Type()
)
sleDhcp6SnoopBindControlValTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlValTime.setStatus("current")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlValTime.setUnits("s")


class _SleDhcp6SnoopBindControlState_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleDhcp6SnoopBindControlState_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlState_Object = MibScalar
sleDhcp6SnoopBindControlState = _SleDhcp6SnoopBindControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 12),
    _SleDhcp6SnoopBindControlState_Type()
)
sleDhcp6SnoopBindControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlState.setStatus("current")


class _SleDhcp6SnoopBindControlType_Type(Integer32):
    """Custom type sleDhcp6SnoopBindControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_SleDhcp6SnoopBindControlType_Type.__name__ = "Integer32"
_SleDhcp6SnoopBindControlType_Object = MibScalar
sleDhcp6SnoopBindControlType = _SleDhcp6SnoopBindControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 2, 13),
    _SleDhcp6SnoopBindControlType_Type()
)
sleDhcp6SnoopBindControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindControlType.setStatus("current")
_SleDhcp6SnoopBindNotification_ObjectIdentity = ObjectIdentity
sleDhcp6SnoopBindNotification = _SleDhcp6SnoopBindNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 3)
)
_SleDhcp6Aaa_ObjectIdentity = ObjectIdentity
sleDhcp6Aaa = _SleDhcp6Aaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10)
)
_SleDhcp6AaaTable_Object = MibTable
sleDhcp6AaaTable = _SleDhcp6AaaTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1)
)
if mibBuilder.loadTexts:
    sleDhcp6AaaTable.setStatus("current")
_SleDhcp6AaaEntry_Object = MibTableRow
sleDhcp6AaaEntry = _SleDhcp6AaaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1)
)
sleDhcp6AaaEntry.setIndexNames(
    (0, "SLE-DHCPV6-MIB", "sleDhcp6AaaIndex"),
)
if mibBuilder.loadTexts:
    sleDhcp6AaaEntry.setStatus("current")


class _SleDhcp6AaaIndex_Type(Integer32):
    """Custom type sleDhcp6AaaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleDhcp6AaaIndex_Type.__name__ = "Integer32"
_SleDhcp6AaaIndex_Object = MibTableColumn
sleDhcp6AaaIndex = _SleDhcp6AaaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 1),
    _SleDhcp6AaaIndex_Type()
)
sleDhcp6AaaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaIndex.setStatus("current")


class _SleDhcp6AaaModelName_Type(OctetString):
    """Custom type sleDhcp6AaaModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6AaaModelName_Type.__name__ = "OctetString"
_SleDhcp6AaaModelName_Object = MibTableColumn
sleDhcp6AaaModelName = _SleDhcp6AaaModelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 2),
    _SleDhcp6AaaModelName_Type()
)
sleDhcp6AaaModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaModelName.setStatus("current")
_SleDhcp6AaaServerType_Type = InetAddressType
_SleDhcp6AaaServerType_Object = MibTableColumn
sleDhcp6AaaServerType = _SleDhcp6AaaServerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 3),
    _SleDhcp6AaaServerType_Type()
)
sleDhcp6AaaServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaServerType.setStatus("current")
_SleDhcp6AaaServerAddr_Type = InetAddress
_SleDhcp6AaaServerAddr_Object = MibTableColumn
sleDhcp6AaaServerAddr = _SleDhcp6AaaServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 4),
    _SleDhcp6AaaServerAddr_Type()
)
sleDhcp6AaaServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaServerAddr.setStatus("current")
_SleDhcp6AaaRadiusKey_Type = OctetString
_SleDhcp6AaaRadiusKey_Object = MibTableColumn
sleDhcp6AaaRadiusKey = _SleDhcp6AaaRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 5),
    _SleDhcp6AaaRadiusKey_Type()
)
sleDhcp6AaaRadiusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusKey.setStatus("current")
_SleDhcp6AaaRadiusUser_Type = OctetString
_SleDhcp6AaaRadiusUser_Object = MibTableColumn
sleDhcp6AaaRadiusUser = _SleDhcp6AaaRadiusUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 6),
    _SleDhcp6AaaRadiusUser_Type()
)
sleDhcp6AaaRadiusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusUser.setStatus("current")
_SleDhcp6AaaRadiusPasswd_Type = OctetString
_SleDhcp6AaaRadiusPasswd_Object = MibTableColumn
sleDhcp6AaaRadiusPasswd = _SleDhcp6AaaRadiusPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 7),
    _SleDhcp6AaaRadiusPasswd_Type()
)
sleDhcp6AaaRadiusPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusPasswd.setStatus("current")


class _SleDhcp6AaaRadiusRetry_Type(Integer32):
    """Custom type sleDhcp6AaaRadiusRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleDhcp6AaaRadiusRetry_Type.__name__ = "Integer32"
_SleDhcp6AaaRadiusRetry_Object = MibTableColumn
sleDhcp6AaaRadiusRetry = _SleDhcp6AaaRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 8),
    _SleDhcp6AaaRadiusRetry_Type()
)
sleDhcp6AaaRadiusRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusRetry.setStatus("current")


class _SleDhcp6AaaRadiusTimeout_Type(Integer32):
    """Custom type sleDhcp6AaaRadiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleDhcp6AaaRadiusTimeout_Type.__name__ = "Integer32"
_SleDhcp6AaaRadiusTimeout_Object = MibTableColumn
sleDhcp6AaaRadiusTimeout = _SleDhcp6AaaRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 9),
    _SleDhcp6AaaRadiusTimeout_Type()
)
sleDhcp6AaaRadiusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusTimeout.setStatus("current")
_SleDhcp6AaaRadiusPort_Type = Integer32
_SleDhcp6AaaRadiusPort_Object = MibTableColumn
sleDhcp6AaaRadiusPort = _SleDhcp6AaaRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 10),
    _SleDhcp6AaaRadiusPort_Type()
)
sleDhcp6AaaRadiusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusPort.setStatus("current")
_SleDhcp6AaaRadiusInterface_Type = OctetString
_SleDhcp6AaaRadiusInterface_Object = MibTableColumn
sleDhcp6AaaRadiusInterface = _SleDhcp6AaaRadiusInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 1, 1, 11),
    _SleDhcp6AaaRadiusInterface_Type()
)
sleDhcp6AaaRadiusInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcp6AaaRadiusInterface.setStatus("current")
_SleDhcp6AaaControl_ObjectIdentity = ObjectIdentity
sleDhcp6AaaControl = _SleDhcp6AaaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2)
)


class _SleDhcp6AaaControlRequest_Type(Integer32):
    """Custom type sleDhcp6AaaControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDhcp6Aaa", 1),
          ("deleteDhcp6Aaa", 2),
          ("changeDhcp6AaaProfile", 3))
    )


_SleDhcp6AaaControlRequest_Type.__name__ = "Integer32"
_SleDhcp6AaaControlRequest_Object = MibScalar
sleDhcp6AaaControlRequest = _SleDhcp6AaaControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 1),
    _SleDhcp6AaaControlRequest_Type()
)
sleDhcp6AaaControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRequest.setStatus("current")
_SleDhcp6AaaControlStatus_Type = SleControlStatusType
_SleDhcp6AaaControlStatus_Object = MibScalar
sleDhcp6AaaControlStatus = _SleDhcp6AaaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 2),
    _SleDhcp6AaaControlStatus_Type()
)
sleDhcp6AaaControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlStatus.setStatus("current")
_SleDhcp6AaaControlTimer_Type = Gauge32
_SleDhcp6AaaControlTimer_Object = MibScalar
sleDhcp6AaaControlTimer = _SleDhcp6AaaControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 3),
    _SleDhcp6AaaControlTimer_Type()
)
sleDhcp6AaaControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlTimer.setStatus("current")
_SleDhcp6AaaControlTimeStamp_Type = TimeTicks
_SleDhcp6AaaControlTimeStamp_Object = MibScalar
sleDhcp6AaaControlTimeStamp = _SleDhcp6AaaControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 4),
    _SleDhcp6AaaControlTimeStamp_Type()
)
sleDhcp6AaaControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlTimeStamp.setStatus("current")
_SleDhcp6AaaControlReqResult_Type = SleControlRequestResultType
_SleDhcp6AaaControlReqResult_Object = MibScalar
sleDhcp6AaaControlReqResult = _SleDhcp6AaaControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 5),
    _SleDhcp6AaaControlReqResult_Type()
)
sleDhcp6AaaControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlReqResult.setStatus("current")
_SleDhcp6AaaControlIndex_Type = Integer32
_SleDhcp6AaaControlIndex_Object = MibScalar
sleDhcp6AaaControlIndex = _SleDhcp6AaaControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 6),
    _SleDhcp6AaaControlIndex_Type()
)
sleDhcp6AaaControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlIndex.setStatus("current")


class _SleDhcp6AaaControlModelName_Type(OctetString):
    """Custom type sleDhcp6AaaControlModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleDhcp6AaaControlModelName_Type.__name__ = "OctetString"
_SleDhcp6AaaControlModelName_Object = MibScalar
sleDhcp6AaaControlModelName = _SleDhcp6AaaControlModelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 7),
    _SleDhcp6AaaControlModelName_Type()
)
sleDhcp6AaaControlModelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlModelName.setStatus("current")
_SleDhcp6AaaControlServerAddr_Type = OctetString
_SleDhcp6AaaControlServerAddr_Object = MibScalar
sleDhcp6AaaControlServerAddr = _SleDhcp6AaaControlServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 8),
    _SleDhcp6AaaControlServerAddr_Type()
)
sleDhcp6AaaControlServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlServerAddr.setStatus("current")
_SleDhcp6AaaControlRadiusKey_Type = OctetString
_SleDhcp6AaaControlRadiusKey_Object = MibScalar
sleDhcp6AaaControlRadiusKey = _SleDhcp6AaaControlRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 9),
    _SleDhcp6AaaControlRadiusKey_Type()
)
sleDhcp6AaaControlRadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusKey.setStatus("current")
_SleDhcp6AaaControlRadiusUser_Type = OctetString
_SleDhcp6AaaControlRadiusUser_Object = MibScalar
sleDhcp6AaaControlRadiusUser = _SleDhcp6AaaControlRadiusUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 10),
    _SleDhcp6AaaControlRadiusUser_Type()
)
sleDhcp6AaaControlRadiusUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusUser.setStatus("current")
_SleDhcp6AaaControlRadiusPasswd_Type = OctetString
_SleDhcp6AaaControlRadiusPasswd_Object = MibScalar
sleDhcp6AaaControlRadiusPasswd = _SleDhcp6AaaControlRadiusPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 11),
    _SleDhcp6AaaControlRadiusPasswd_Type()
)
sleDhcp6AaaControlRadiusPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusPasswd.setStatus("current")


class _SleDhcp6AaaControlRadiusRetry_Type(Integer32):
    """Custom type sleDhcp6AaaControlRadiusRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleDhcp6AaaControlRadiusRetry_Type.__name__ = "Integer32"
_SleDhcp6AaaControlRadiusRetry_Object = MibScalar
sleDhcp6AaaControlRadiusRetry = _SleDhcp6AaaControlRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 12),
    _SleDhcp6AaaControlRadiusRetry_Type()
)
sleDhcp6AaaControlRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusRetry.setStatus("current")


class _SleDhcp6AaaControlRadiusTimeout_Type(Integer32):
    """Custom type sleDhcp6AaaControlRadiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleDhcp6AaaControlRadiusTimeout_Type.__name__ = "Integer32"
_SleDhcp6AaaControlRadiusTimeout_Object = MibScalar
sleDhcp6AaaControlRadiusTimeout = _SleDhcp6AaaControlRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 13),
    _SleDhcp6AaaControlRadiusTimeout_Type()
)
sleDhcp6AaaControlRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusTimeout.setStatus("current")
_SleDhcp6AaaControlRadiusPort_Type = Integer32
_SleDhcp6AaaControlRadiusPort_Object = MibScalar
sleDhcp6AaaControlRadiusPort = _SleDhcp6AaaControlRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 14),
    _SleDhcp6AaaControlRadiusPort_Type()
)
sleDhcp6AaaControlRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusPort.setStatus("current")
_SleDhcp6AaaControlRadiusInterface_Type = OctetString
_SleDhcp6AaaControlRadiusInterface_Object = MibScalar
sleDhcp6AaaControlRadiusInterface = _SleDhcp6AaaControlRadiusInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 2, 15),
    _SleDhcp6AaaControlRadiusInterface_Type()
)
sleDhcp6AaaControlRadiusInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcp6AaaControlRadiusInterface.setStatus("current")
_SleDhcp6AaaNotification_ObjectIdentity = ObjectIdentity
sleDhcp6AaaNotification = _SleDhcp6AaaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 3)
)

# Managed Objects groups

sleDhcp6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 11)
)
sleDhcp6Group.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6Duid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6DatabaseAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6DatabaseInterval"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseInterval"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolStaticEntry"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolDynamicEntry"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportDns"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportDomain"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportInfoRef"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportNisAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportNisDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportNispAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportNispDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportSipAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportSipDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolImportSntpAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolInfoRefTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolAaaValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolAaaPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolPdName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolPdValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolPdPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportDns"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportDomain"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportInfoRef"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportNisAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportNisDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportNispAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportNispDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportSipAdd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportSipDom"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlImportSntpAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlInfoRefTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlAaaValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlAaaPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionCode"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlCode"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeStart"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeEnd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangePreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlStart"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlEnd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlPreTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseLinkLocal"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseIaType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindPdPrefix"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindPdPrefixLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindPdExpireTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindNaAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindNaExpireTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolPrefix"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolPrefixLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolAssignLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolUsedCnt"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolAvailCnt"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlPrefix"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlPrefixLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlAssignLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerPoolName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerPreference"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerRapidCommit"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlPoolName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlPreference"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlRapidCommit"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayDestAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayOutputIfname"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlDestAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlOutputIfname"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaIaid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaT1"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaT2"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaLifeTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaValidTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaExpireTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlStatelessFlag"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlNaFlag"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlPdFlag"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlPdHint"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIanaRapidCommit"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIapdRapidCommit"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRefreshMinimumVal"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientOptionCode"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientOptionType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientOptionValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdIaid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdT1"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdT2"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdPrefix"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdPrefixLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdLifeTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdValidTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdExpireTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrId"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrLengthHidden"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrLengthType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrLengthValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrValueType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlId"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlLengthHidden"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlLengthType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlLengthValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlValueType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseNdInspTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlNdInspTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortTrusted"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortLimitRate"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortLimitLease"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTrusted"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlLimitRate"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlLimitLease"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindPortIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindVlan"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindMac"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlPortIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlVlan"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlMac"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlState"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIapdIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlOptionIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindPdIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindNaIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlPoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlPoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseIaid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseRawDataLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseRawData"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlPoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlPoolIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientServerAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientServerDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientServerPref"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientRapidCommit"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientInfoRefTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaModelName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaServerType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaServerAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusKey"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusUser"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusPasswd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusRetry"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusTimeout"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusPort"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusInterface"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlStatus"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlTimer"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlModelName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlServerAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusKey"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusUser"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusPasswd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusRetry"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusTimeout"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusPort"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRadiusInterface"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientIanaIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientPdname"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlPdname"))
)
if mibBuilder.loadTexts:
    sleDhcp6Group.setStatus("current")


# Notification objects

sleDhcp6DatabaseCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 3, 1)
)
sleDhcp6DatabaseCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6BaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseInterval"))
)
if mibBuilder.loadTexts:
    sleDhcp6DatabaseCreated.setStatus(
        "current"
    )

sleDhcp6DatabaseDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 3, 2)
)
sleDhcp6DatabaseDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6BaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcp6DatabaseDestroyed.setStatus(
        "current"
    )

sleDhcp6DatabaseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 1, 3, 3)
)
sleDhcp6DatabaseChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6BaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BaseControlDatabaseInterval"))
)
if mibBuilder.loadTexts:
    sleDhcp6DatabaseChanged.setStatus(
        "current"
    )

sleDhcp6PoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 1)
)
sleDhcp6PoolCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6PoolCreated.setStatus(
        "current"
    )

sleDhcp6PoolDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 2)
)
sleDhcp6PoolDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6PoolDestroyed.setStatus(
        "current"
    )

sleDhcp6ImportSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 3)
)
sleDhcp6ImportSet.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6ImportSet.setStatus(
        "current"
    )

sleDhcp6PoolAaaTimeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 4)
)
sleDhcp6PoolAaaTimeCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlAaaValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlAaaPreTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6PoolAaaTimeCreated.setStatus(
        "current"
    )

sleDhcp6PoolAaaTimeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 5)
)
sleDhcp6PoolAaaTimeDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcp6PoolAaaTimeDestroyed.setStatus(
        "current"
    )

sleDhcp6PdPoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 6)
)
sleDhcp6PdPoolCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdPreTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6PdPoolCreated.setStatus(
        "current"
    )

sleDhcp6PdPoolDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 1, 3, 7)
)
sleDhcp6PdPoolDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolBaseControlPdName"))
)
if mibBuilder.loadTexts:
    sleDhcp6PdPoolDestroyed.setStatus(
        "current"
    )

sleDhcp6FixedAddrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 3, 1)
)
sleDhcp6FixedAddrCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlDuid"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlPreTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrCreated.setStatus(
        "current"
    )

sleDhcp6FixedAddrDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 2, 3, 2)
)
sleDhcp6FixedAddrDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrControlDuid"))
)
if mibBuilder.loadTexts:
    sleDhcp6FixedAddrDestroyed.setStatus(
        "current"
    )

sleDhcp6ServerOptionCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 3, 1)
)
sleDhcp6ServerOptionCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlCode"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlType"))
)
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionCreated.setStatus(
        "current"
    )

sleDhcp6ServerOptionDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 3, 3, 2)
)
sleDhcp6ServerOptionDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlCode"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionControlValue"))
)
if mibBuilder.loadTexts:
    sleDhcp6ServerOptionDestroyed.setStatus(
        "current"
    )

sleDhcp6RangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 3, 1)
)
sleDhcp6RangeCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6RangeControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlStart"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlEnd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlValTime"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlPreTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6RangeCreated.setStatus(
        "current"
    )

sleDhcp6RangeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 4, 3, 2)
)
sleDhcp6RangeDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6RangeControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlStart"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeControlEnd"))
)
if mibBuilder.loadTexts:
    sleDhcp6RangeDestroyed.setStatus(
        "current"
    )

sleDhcp6FixedPrefixCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 3, 1)
)
sleDhcp6FixedPrefixCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlDuid"))
)
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixCreated.setStatus(
        "current"
    )

sleDhcp6FixedPrefixDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 2, 5, 3, 2)
)
sleDhcp6FixedPrefixDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlValue"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlLen"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixControlDuid"))
)
if mibBuilder.loadTexts:
    sleDhcp6FixedPrefixDestroyed.setStatus(
        "current"
    )

sleDhcp6BindingCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 3, 1, 3, 1)
)
sleDhcp6BindingCleared.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcp6BindingCleared.setStatus(
        "current"
    )

sleDhcp6LocalPoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 3, 1)
)
sleDhcp6LocalPoolCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolCreated.setStatus(
        "current"
    )

sleDhcp6LocalPoolDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 4, 3, 2)
)
sleDhcp6LocalPoolDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6LocalPoolDestroyed.setStatus(
        "current"
    )

sleDhcp6ServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 3, 1)
)
sleDhcp6ServerCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ServerControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlPoolName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlPreference"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlRapidCommit"))
)
if mibBuilder.loadTexts:
    sleDhcp6ServerCreated.setStatus(
        "current"
    )

sleDhcp6ServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 5, 3, 2)
)
sleDhcp6ServerDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ServerControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerControlIfName"))
)
if mibBuilder.loadTexts:
    sleDhcp6ServerDestroyed.setStatus(
        "current"
    )

sleDhcp6RelayCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 3, 1)
)
sleDhcp6RelayCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6RelayControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlDestAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlOutputIfname"))
)
if mibBuilder.loadTexts:
    sleDhcp6RelayCreated.setStatus(
        "current"
    )

sleDhcp6RelayDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 6, 3, 2)
)
sleDhcp6RelayDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6RelayControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayControlDestAddr"))
)
if mibBuilder.loadTexts:
    sleDhcp6RelayDestroyed.setStatus(
        "current"
    )

sleDhcp6ClientStatelessSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3, 1)
)
sleDhcp6ClientStatelessSet.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlStatelessFlag"))
)
if mibBuilder.loadTexts:
    sleDhcp6ClientStatelessSet.setStatus(
        "current"
    )

sleDhcp6ClientNaSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3, 2)
)
sleDhcp6ClientNaSet.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlNaFlag"))
)
if mibBuilder.loadTexts:
    sleDhcp6ClientNaSet.setStatus(
        "current"
    )

sleDhcp6ClientPdSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3, 3)
)
sleDhcp6ClientPdSet.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlPdFlag"))
)
if mibBuilder.loadTexts:
    sleDhcp6ClientPdSet.setStatus(
        "current"
    )

sleDhcp6ClientCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3, 4)
)
sleDhcp6ClientCleared.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"))
)
if mibBuilder.loadTexts:
    sleDhcp6ClientCleared.setStatus(
        "current"
    )

sleDhcp6ClientRefreshMinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 7, 1, 3, 5)
)
sleDhcp6ClientRefreshMinChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlIfName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientBaseControlRefreshMinimumVal"))
)
if mibBuilder.loadTexts:
    sleDhcp6ClientRefreshMinChanged.setStatus(
        "current"
    )

sleDhcp6OptionCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 3, 1)
)
sleDhcp6OptionCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6OptionCreated.setStatus(
        "current"
    )

sleDhcp6OptionDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 1, 3, 2)
)
sleDhcp6OptionDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionBaseControlName"))
)
if mibBuilder.loadTexts:
    sleDhcp6OptionDestroyed.setStatus(
        "current"
    )

sleDhcp6OptionAttrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 3, 1)
)
sleDhcp6OptionAttrCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlOptionName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlId"))
)
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrCreated.setStatus(
        "current"
    )

sleDhcp6OptionAttrDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 3, 2)
)
sleDhcp6OptionAttrDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlOptionName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlId"))
)
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrDestroyed.setStatus(
        "current"
    )

sleDhcp6OptionAttrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 8, 2, 3, 3)
)
sleDhcp6OptionAttrChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlOptionName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrControlId"))
)
if mibBuilder.loadTexts:
    sleDhcp6OptionAttrChanged.setStatus(
        "current"
    )

sleDhcp6SnoopBaseStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 3, 1)
)
sleDhcp6SnoopBaseStateChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlState"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseStateChanged.setStatus(
        "current"
    )

sleDhcp6SnoopBaseNdInspTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 1, 3, 2)
)
sleDhcp6SnoopBaseNdInspTimeChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseControlNdInspTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBaseNdInspTimeChanged.setStatus(
        "current"
    )

sleDhcp6SnoopVlanStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 2, 3, 1)
)
sleDhcp6SnoopVlanStateChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanControlState"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopVlanStateChanged.setStatus(
        "current"
    )

sleDhcp6SnoopPortTrustChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 3, 1)
)
sleDhcp6SnoopPortTrustChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTrusted"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortTrustChanged.setStatus(
        "current"
    )

sleDhcp6SnoopPortLimitRateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 3, 2)
)
sleDhcp6SnoopPortLimitRateChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlLimitRate"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortLimitRateChanged.setStatus(
        "current"
    )

sleDhcp6SnoopPortLimitLeaseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 3, 3, 3)
)
sleDhcp6SnoopPortLimitLeaseChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortControlLimitLease"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopPortLimitLeaseChanged.setStatus(
        "current"
    )

sleDhcp6SnoopBindCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 3, 1)
)
sleDhcp6SnoopBindCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlPortIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlAddress"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlVlan"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlMac"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlValTime"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindCreated.setStatus(
        "current"
    )

sleDhcp6SnoopBindDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 3, 2)
)
sleDhcp6SnoopBindDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlPortIndex"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlAddress"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindDestroyed.setStatus(
        "current"
    )

sleDhcp6SnoopBindCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 9, 4, 3, 3)
)
sleDhcp6SnoopBindCleared.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindControlPortIndex"))
)
if mibBuilder.loadTexts:
    sleDhcp6SnoopBindCleared.setStatus(
        "current"
    )

sleDhcp6AaaCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 3, 1)
)
sleDhcp6AaaCreated.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaModelName"))
)
if mibBuilder.loadTexts:
    sleDhcp6AaaCreated.setStatus(
        "current"
    )

sleDhcp6AaaDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 3, 2)
)
sleDhcp6AaaDestroyed.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlModelName"))
)
if mibBuilder.loadTexts:
    sleDhcp6AaaDestroyed.setStatus(
        "current"
    )

sleDhcp6AaaProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 10, 3, 3)
)
sleDhcp6AaaProfileChanged.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6AaaControlRequest"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlTimeStamp"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaControlReqResult"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaModelName"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaServerType"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaServerAddr"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusKey"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusUser"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusPasswd"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusRetry"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusTimeout"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusPort"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaRadiusInterface"))
)
if mibBuilder.loadTexts:
    sleDhcp6AaaProfileChanged.setStatus(
        "current"
    )


# Notifications groups

sleDhcp6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 27, 12)
)
sleDhcp6NotificationGroup.setObjects(
      *(("SLE-DHCPV6-MIB", "sleDhcp6DatabaseCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6DatabaseDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6DatabaseChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolAaaTimeCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PoolAaaTimeDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PdPoolCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6PdPoolDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedAddrDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerOptionDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RangeDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6FixedPrefixDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6BindingCleared"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6LocalPoolDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ServerDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6RelayDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientStatelessSet"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientNaSet"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientPdSet"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientCleared"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ClientRefreshMinChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6OptionAttrChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseStateChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBaseNdInspTimeChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopVlanStateChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortTrustChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortLimitRateChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopPortLimitLeaseChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaCreated"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaDestroyed"),
        ("SLE-DHCPV6-MIB", "sleDhcp6AaaProfileChanged"),
        ("SLE-DHCPV6-MIB", "sleDhcp6SnoopBindCleared"),
        ("SLE-DHCPV6-MIB", "sleDhcp6ImportSet"))
)
if mibBuilder.loadTexts:
    sleDhcp6NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DHCPV6-MIB",
    **{"sleDhcp6": sleDhcp6,
       "sleDhcp6Base": sleDhcp6Base,
       "sleDhcp6BaseInfo": sleDhcp6BaseInfo,
       "sleDhcp6Duid": sleDhcp6Duid,
       "sleDhcp6DatabaseAddr": sleDhcp6DatabaseAddr,
       "sleDhcp6DatabaseInterval": sleDhcp6DatabaseInterval,
       "sleDhcp6BaseControl": sleDhcp6BaseControl,
       "sleDhcp6BaseControlRequest": sleDhcp6BaseControlRequest,
       "sleDhcp6BaseControlStatus": sleDhcp6BaseControlStatus,
       "sleDhcp6BaseControlTimer": sleDhcp6BaseControlTimer,
       "sleDhcp6BaseControlTimeStamp": sleDhcp6BaseControlTimeStamp,
       "sleDhcp6BaseControlReqResult": sleDhcp6BaseControlReqResult,
       "sleDhcp6BaseControlDatabaseAddr": sleDhcp6BaseControlDatabaseAddr,
       "sleDhcp6BaseControlDatabaseInterval": sleDhcp6BaseControlDatabaseInterval,
       "sleDhcp6BaseNotification": sleDhcp6BaseNotification,
       "sleDhcp6DatabaseCreated": sleDhcp6DatabaseCreated,
       "sleDhcp6DatabaseDestroyed": sleDhcp6DatabaseDestroyed,
       "sleDhcp6DatabaseChanged": sleDhcp6DatabaseChanged,
       "sleDhcp6Pool": sleDhcp6Pool,
       "sleDhcp6PoolBase": sleDhcp6PoolBase,
       "sleDhcp6PoolTable": sleDhcp6PoolTable,
       "sleDhcp6PoolEntry": sleDhcp6PoolEntry,
       "sleDhcp6PoolIndex": sleDhcp6PoolIndex,
       "sleDhcp6PoolName": sleDhcp6PoolName,
       "sleDhcp6PoolStaticEntry": sleDhcp6PoolStaticEntry,
       "sleDhcp6PoolDynamicEntry": sleDhcp6PoolDynamicEntry,
       "sleDhcp6PoolImportDns": sleDhcp6PoolImportDns,
       "sleDhcp6PoolImportDomain": sleDhcp6PoolImportDomain,
       "sleDhcp6PoolImportInfoRef": sleDhcp6PoolImportInfoRef,
       "sleDhcp6PoolImportNisAdd": sleDhcp6PoolImportNisAdd,
       "sleDhcp6PoolImportNisDom": sleDhcp6PoolImportNisDom,
       "sleDhcp6PoolImportNispAdd": sleDhcp6PoolImportNispAdd,
       "sleDhcp6PoolImportNispDom": sleDhcp6PoolImportNispDom,
       "sleDhcp6PoolImportSipAdd": sleDhcp6PoolImportSipAdd,
       "sleDhcp6PoolImportSipDom": sleDhcp6PoolImportSipDom,
       "sleDhcp6PoolImportSntpAdd": sleDhcp6PoolImportSntpAdd,
       "sleDhcp6PoolInfoRefTime": sleDhcp6PoolInfoRefTime,
       "sleDhcp6PoolAaaValTime": sleDhcp6PoolAaaValTime,
       "sleDhcp6PoolAaaPreTime": sleDhcp6PoolAaaPreTime,
       "sleDhcp6PoolPdName": sleDhcp6PoolPdName,
       "sleDhcp6PoolPdValTime": sleDhcp6PoolPdValTime,
       "sleDhcp6PoolPdPreTime": sleDhcp6PoolPdPreTime,
       "sleDhcp6PoolBaseControl": sleDhcp6PoolBaseControl,
       "sleDhcp6PoolBaseControlRequest": sleDhcp6PoolBaseControlRequest,
       "sleDhcp6PoolBaseControlStatus": sleDhcp6PoolBaseControlStatus,
       "sleDhcp6PoolBaseControlTimer": sleDhcp6PoolBaseControlTimer,
       "sleDhcp6PoolBaseControlTimeStamp": sleDhcp6PoolBaseControlTimeStamp,
       "sleDhcp6PoolBaseControlReqResult": sleDhcp6PoolBaseControlReqResult,
       "sleDhcp6PoolBaseControlIndex": sleDhcp6PoolBaseControlIndex,
       "sleDhcp6PoolBaseControlName": sleDhcp6PoolBaseControlName,
       "sleDhcp6PoolBaseControlImportDns": sleDhcp6PoolBaseControlImportDns,
       "sleDhcp6PoolBaseControlImportDomain": sleDhcp6PoolBaseControlImportDomain,
       "sleDhcp6PoolBaseControlImportInfoRef": sleDhcp6PoolBaseControlImportInfoRef,
       "sleDhcp6PoolBaseControlImportNisAdd": sleDhcp6PoolBaseControlImportNisAdd,
       "sleDhcp6PoolBaseControlImportNisDom": sleDhcp6PoolBaseControlImportNisDom,
       "sleDhcp6PoolBaseControlImportNispAdd": sleDhcp6PoolBaseControlImportNispAdd,
       "sleDhcp6PoolBaseControlImportNispDom": sleDhcp6PoolBaseControlImportNispDom,
       "sleDhcp6PoolBaseControlImportSipAdd": sleDhcp6PoolBaseControlImportSipAdd,
       "sleDhcp6PoolBaseControlImportSipDom": sleDhcp6PoolBaseControlImportSipDom,
       "sleDhcp6PoolBaseControlImportSntpAddr": sleDhcp6PoolBaseControlImportSntpAddr,
       "sleDhcp6PoolBaseControlInfoRefTime": sleDhcp6PoolBaseControlInfoRefTime,
       "sleDhcp6PoolBaseControlAaaValTime": sleDhcp6PoolBaseControlAaaValTime,
       "sleDhcp6PoolBaseControlAaaPreTime": sleDhcp6PoolBaseControlAaaPreTime,
       "sleDhcp6PoolBaseControlPdName": sleDhcp6PoolBaseControlPdName,
       "sleDhcp6PoolBaseControlPdValTime": sleDhcp6PoolBaseControlPdValTime,
       "sleDhcp6PoolBaseControlPdPreTime": sleDhcp6PoolBaseControlPdPreTime,
       "sleDhcp6PoolBaseNotification": sleDhcp6PoolBaseNotification,
       "sleDhcp6PoolCreated": sleDhcp6PoolCreated,
       "sleDhcp6PoolDestroyed": sleDhcp6PoolDestroyed,
       "sleDhcp6ImportSet": sleDhcp6ImportSet,
       "sleDhcp6PoolAaaTimeCreated": sleDhcp6PoolAaaTimeCreated,
       "sleDhcp6PoolAaaTimeDestroyed": sleDhcp6PoolAaaTimeDestroyed,
       "sleDhcp6PdPoolCreated": sleDhcp6PdPoolCreated,
       "sleDhcp6PdPoolDestroyed": sleDhcp6PdPoolDestroyed,
       "sleDhcp6FixedAddr": sleDhcp6FixedAddr,
       "sleDhcp6FixedAddrTable": sleDhcp6FixedAddrTable,
       "sleDhcp6FixedAddrEntry": sleDhcp6FixedAddrEntry,
       "sleDhcp6FixedAddrIndex": sleDhcp6FixedAddrIndex,
       "sleDhcp6FixedAddrAddress": sleDhcp6FixedAddrAddress,
       "sleDhcp6FixedAddrDuid": sleDhcp6FixedAddrDuid,
       "sleDhcp6FixedAddrValTime": sleDhcp6FixedAddrValTime,
       "sleDhcp6FixedAddrPreTime": sleDhcp6FixedAddrPreTime,
       "sleDhcp6FixedAddrControl": sleDhcp6FixedAddrControl,
       "sleDhcp6FixedAddrControlRequest": sleDhcp6FixedAddrControlRequest,
       "sleDhcp6FixedAddrControlStatus": sleDhcp6FixedAddrControlStatus,
       "sleDhcp6FixedAddrControlTimer": sleDhcp6FixedAddrControlTimer,
       "sleDhcp6FixedAddrControlTimeStamp": sleDhcp6FixedAddrControlTimeStamp,
       "sleDhcp6FixedAddrControlReqResult": sleDhcp6FixedAddrControlReqResult,
       "sleDhcp6FixedAddrControlPoolIndex": sleDhcp6FixedAddrControlPoolIndex,
       "sleDhcp6FixedAddrControlIndex": sleDhcp6FixedAddrControlIndex,
       "sleDhcp6FixedAddrControlAddress": sleDhcp6FixedAddrControlAddress,
       "sleDhcp6FixedAddrControlDuid": sleDhcp6FixedAddrControlDuid,
       "sleDhcp6FixedAddrControlValTime": sleDhcp6FixedAddrControlValTime,
       "sleDhcp6FixedAddrControlPreTime": sleDhcp6FixedAddrControlPreTime,
       "sleDhcp6FixedAddrNotification": sleDhcp6FixedAddrNotification,
       "sleDhcp6FixedAddrCreated": sleDhcp6FixedAddrCreated,
       "sleDhcp6FixedAddrDestroyed": sleDhcp6FixedAddrDestroyed,
       "sleDhcp6ServerOption": sleDhcp6ServerOption,
       "sleDhcp6ServerOptionTable": sleDhcp6ServerOptionTable,
       "sleDhcp6ServerOptionEntry": sleDhcp6ServerOptionEntry,
       "sleDhcp6ServerOptionCode": sleDhcp6ServerOptionCode,
       "sleDhcp6ServerOptionIndex": sleDhcp6ServerOptionIndex,
       "sleDhcp6ServerOptionType": sleDhcp6ServerOptionType,
       "sleDhcp6ServerOptionValue": sleDhcp6ServerOptionValue,
       "sleDhcp6ServerOptionControl": sleDhcp6ServerOptionControl,
       "sleDhcp6ServerOptionControlRequest": sleDhcp6ServerOptionControlRequest,
       "sleDhcp6ServerOptionControlStatus": sleDhcp6ServerOptionControlStatus,
       "sleDhcp6ServerOptionControlTimer": sleDhcp6ServerOptionControlTimer,
       "sleDhcp6ServerOptionControlTimeStamp": sleDhcp6ServerOptionControlTimeStamp,
       "sleDhcp6ServerOptionControlReqResult": sleDhcp6ServerOptionControlReqResult,
       "sleDhcp6ServerOptionControlPoolIndex": sleDhcp6ServerOptionControlPoolIndex,
       "sleDhcp6ServerOptionControlCode": sleDhcp6ServerOptionControlCode,
       "sleDhcp6ServerOptionControlIndex": sleDhcp6ServerOptionControlIndex,
       "sleDhcp6ServerOptionControlType": sleDhcp6ServerOptionControlType,
       "sleDhcp6ServerOptionControlValue": sleDhcp6ServerOptionControlValue,
       "sleDhcp6ServerOptionNotification": sleDhcp6ServerOptionNotification,
       "sleDhcp6ServerOptionCreated": sleDhcp6ServerOptionCreated,
       "sleDhcp6ServerOptionDestroyed": sleDhcp6ServerOptionDestroyed,
       "sleDhcp6Range": sleDhcp6Range,
       "sleDhcp6RangeTable": sleDhcp6RangeTable,
       "sleDhcp6RangeEntry": sleDhcp6RangeEntry,
       "sleDhcp6RangeIndex": sleDhcp6RangeIndex,
       "sleDhcp6RangeStart": sleDhcp6RangeStart,
       "sleDhcp6RangeEnd": sleDhcp6RangeEnd,
       "sleDhcp6RangeValTime": sleDhcp6RangeValTime,
       "sleDhcp6RangePreTime": sleDhcp6RangePreTime,
       "sleDhcp6RangeControl": sleDhcp6RangeControl,
       "sleDhcp6RangeControlRequest": sleDhcp6RangeControlRequest,
       "sleDhcp6RangeControlStatus": sleDhcp6RangeControlStatus,
       "sleDhcp6RangeControlTimer": sleDhcp6RangeControlTimer,
       "sleDhcp6RangeControlTimeStamp": sleDhcp6RangeControlTimeStamp,
       "sleDhcp6RangeControlReqResult": sleDhcp6RangeControlReqResult,
       "sleDhcp6RangeControlPoolIndex": sleDhcp6RangeControlPoolIndex,
       "sleDhcp6RangeControlIndex": sleDhcp6RangeControlIndex,
       "sleDhcp6RangeControlStart": sleDhcp6RangeControlStart,
       "sleDhcp6RangeControlEnd": sleDhcp6RangeControlEnd,
       "sleDhcp6RangeControlValTime": sleDhcp6RangeControlValTime,
       "sleDhcp6RangeControlPreTime": sleDhcp6RangeControlPreTime,
       "sleDhcp6RangeNotification": sleDhcp6RangeNotification,
       "sleDhcp6RangeCreated": sleDhcp6RangeCreated,
       "sleDhcp6RangeDestroyed": sleDhcp6RangeDestroyed,
       "sleDhcp6FixedPrefix": sleDhcp6FixedPrefix,
       "sleDhcp6FixedPrefixTable": sleDhcp6FixedPrefixTable,
       "sleDhcp6FixedPrefixEntry": sleDhcp6FixedPrefixEntry,
       "sleDhcp6FixedPrefixIndex": sleDhcp6FixedPrefixIndex,
       "sleDhcp6FixedPrefixValue": sleDhcp6FixedPrefixValue,
       "sleDhcp6FixedPrefixLen": sleDhcp6FixedPrefixLen,
       "sleDhcp6FixedPrefixDuid": sleDhcp6FixedPrefixDuid,
       "sleDhcp6FixedPrefixValTime": sleDhcp6FixedPrefixValTime,
       "sleDhcp6FixedPrefixPreTime": sleDhcp6FixedPrefixPreTime,
       "sleDhcp6FixedPrefixControl": sleDhcp6FixedPrefixControl,
       "sleDhcp6FixedPrefixControlRequest": sleDhcp6FixedPrefixControlRequest,
       "sleDhcp6FixedPrefixControlStatus": sleDhcp6FixedPrefixControlStatus,
       "sleDhcp6FixedPrefixControlTimer": sleDhcp6FixedPrefixControlTimer,
       "sleDhcp6FixedPrefixControlTimeStamp": sleDhcp6FixedPrefixControlTimeStamp,
       "sleDhcp6FixedPrefixControlReqResult": sleDhcp6FixedPrefixControlReqResult,
       "sleDhcp6FixedPrefixControlPoolIndex": sleDhcp6FixedPrefixControlPoolIndex,
       "sleDhcp6FixedPrefixControlIndex": sleDhcp6FixedPrefixControlIndex,
       "sleDhcp6FixedPrefixControlValue": sleDhcp6FixedPrefixControlValue,
       "sleDhcp6FixedPrefixControlLen": sleDhcp6FixedPrefixControlLen,
       "sleDhcp6FixedPrefixControlDuid": sleDhcp6FixedPrefixControlDuid,
       "sleDhcp6FixedPrefixControlValTime": sleDhcp6FixedPrefixControlValTime,
       "sleDhcp6FixedPrefixControlPreTime": sleDhcp6FixedPrefixControlPreTime,
       "sleDhcp6FixedPrefixNotification": sleDhcp6FixedPrefixNotification,
       "sleDhcp6FixedPrefixCreated": sleDhcp6FixedPrefixCreated,
       "sleDhcp6FixedPrefixDestroyed": sleDhcp6FixedPrefixDestroyed,
       "sleDhcp6Binding": sleDhcp6Binding,
       "sleDhcp6BindBase": sleDhcp6BindBase,
       "sleDhcp6BindBaseTable": sleDhcp6BindBaseTable,
       "sleDhcp6BindBaseEntry": sleDhcp6BindBaseEntry,
       "sleDhcp6BindBaseIndex": sleDhcp6BindBaseIndex,
       "sleDhcp6BindBaseLinkLocal": sleDhcp6BindBaseLinkLocal,
       "sleDhcp6BindBaseDuid": sleDhcp6BindBaseDuid,
       "sleDhcp6BindBaseIaType": sleDhcp6BindBaseIaType,
       "sleDhcp6BindBaseIaid": sleDhcp6BindBaseIaid,
       "sleDhcp6BindBaseControl": sleDhcp6BindBaseControl,
       "sleDhcp6BindBaseControlRequest": sleDhcp6BindBaseControlRequest,
       "sleDhcp6BindBaseControlStatus": sleDhcp6BindBaseControlStatus,
       "sleDhcp6BindBaseControlTimer": sleDhcp6BindBaseControlTimer,
       "sleDhcp6BindBaseControlTimeStamp": sleDhcp6BindBaseControlTimeStamp,
       "sleDhcp6BindBaseControlReqResult": sleDhcp6BindBaseControlReqResult,
       "sleDhcp6BindBaseNotification": sleDhcp6BindBaseNotification,
       "sleDhcp6BindingCleared": sleDhcp6BindingCleared,
       "sleDhcp6BindPd": sleDhcp6BindPd,
       "sleDhcp6BindPdTable": sleDhcp6BindPdTable,
       "sleDhcp6BindPdEntry": sleDhcp6BindPdEntry,
       "sleDhcp6BindPdIndex": sleDhcp6BindPdIndex,
       "sleDhcp6BindPdPrefix": sleDhcp6BindPdPrefix,
       "sleDhcp6BindPdPrefixLen": sleDhcp6BindPdPrefixLen,
       "sleDhcp6BindPdExpireTime": sleDhcp6BindPdExpireTime,
       "sleDhcp6BindNa": sleDhcp6BindNa,
       "sleDhcp6BindNaTable": sleDhcp6BindNaTable,
       "sleDhcp6BindNaEntry": sleDhcp6BindNaEntry,
       "sleDhcp6BindNaIndex": sleDhcp6BindNaIndex,
       "sleDhcp6BindNaAddress": sleDhcp6BindNaAddress,
       "sleDhcp6BindNaExpireTime": sleDhcp6BindNaExpireTime,
       "sleDhcp6LocalPool": sleDhcp6LocalPool,
       "sleDhcp6LocalPoolTable": sleDhcp6LocalPoolTable,
       "sleDhcp6LocalPoolEntry": sleDhcp6LocalPoolEntry,
       "sleDhcp6LocalPoolIndex": sleDhcp6LocalPoolIndex,
       "sleDhcp6LocalPoolName": sleDhcp6LocalPoolName,
       "sleDhcp6LocalPoolPrefix": sleDhcp6LocalPoolPrefix,
       "sleDhcp6LocalPoolPrefixLen": sleDhcp6LocalPoolPrefixLen,
       "sleDhcp6LocalPoolAssignLen": sleDhcp6LocalPoolAssignLen,
       "sleDhcp6LocalPoolUsedCnt": sleDhcp6LocalPoolUsedCnt,
       "sleDhcp6LocalPoolAvailCnt": sleDhcp6LocalPoolAvailCnt,
       "sleDhcp6LocalPoolControl": sleDhcp6LocalPoolControl,
       "sleDhcp6LocalPoolControlRequest": sleDhcp6LocalPoolControlRequest,
       "sleDhcp6LocalPoolControlStatus": sleDhcp6LocalPoolControlStatus,
       "sleDhcp6LocalPoolControlTimer": sleDhcp6LocalPoolControlTimer,
       "sleDhcp6LocalPoolControlTimeStamp": sleDhcp6LocalPoolControlTimeStamp,
       "sleDhcp6LocalPoolControlReqResult": sleDhcp6LocalPoolControlReqResult,
       "sleDhcp6LocalPoolControlIndex": sleDhcp6LocalPoolControlIndex,
       "sleDhcp6LocalPoolControlName": sleDhcp6LocalPoolControlName,
       "sleDhcp6LocalPoolControlPrefix": sleDhcp6LocalPoolControlPrefix,
       "sleDhcp6LocalPoolControlPrefixLen": sleDhcp6LocalPoolControlPrefixLen,
       "sleDhcp6LocalPoolControlAssignLen": sleDhcp6LocalPoolControlAssignLen,
       "sleDhcp6LocalPoolNotification": sleDhcp6LocalPoolNotification,
       "sleDhcp6LocalPoolCreated": sleDhcp6LocalPoolCreated,
       "sleDhcp6LocalPoolDestroyed": sleDhcp6LocalPoolDestroyed,
       "sleDhcp6Server": sleDhcp6Server,
       "sleDhcp6ServerTable": sleDhcp6ServerTable,
       "sleDhcp6ServerEntry": sleDhcp6ServerEntry,
       "sleDhcp6ServerIndex": sleDhcp6ServerIndex,
       "sleDhcp6ServerIfName": sleDhcp6ServerIfName,
       "sleDhcp6ServerPoolName": sleDhcp6ServerPoolName,
       "sleDhcp6ServerPreference": sleDhcp6ServerPreference,
       "sleDhcp6ServerRapidCommit": sleDhcp6ServerRapidCommit,
       "sleDhcp6ServerControl": sleDhcp6ServerControl,
       "sleDhcp6ServerControlRequest": sleDhcp6ServerControlRequest,
       "sleDhcp6ServerControlStatus": sleDhcp6ServerControlStatus,
       "sleDhcp6ServerControlTimer": sleDhcp6ServerControlTimer,
       "sleDhcp6ServerControlTimeStamp": sleDhcp6ServerControlTimeStamp,
       "sleDhcp6ServerControlReqResult": sleDhcp6ServerControlReqResult,
       "sleDhcp6ServerControlIndex": sleDhcp6ServerControlIndex,
       "sleDhcp6ServerControlIfName": sleDhcp6ServerControlIfName,
       "sleDhcp6ServerControlPoolName": sleDhcp6ServerControlPoolName,
       "sleDhcp6ServerControlPreference": sleDhcp6ServerControlPreference,
       "sleDhcp6ServerControlRapidCommit": sleDhcp6ServerControlRapidCommit,
       "sleDhcp6ServerNotification": sleDhcp6ServerNotification,
       "sleDhcp6ServerCreated": sleDhcp6ServerCreated,
       "sleDhcp6ServerDestroyed": sleDhcp6ServerDestroyed,
       "sleDhcp6Relay": sleDhcp6Relay,
       "sleDhcp6RelayTable": sleDhcp6RelayTable,
       "sleDhcp6RelayEntry": sleDhcp6RelayEntry,
       "sleDhcp6RelayIndex": sleDhcp6RelayIndex,
       "sleDhcp6RelayIfName": sleDhcp6RelayIfName,
       "sleDhcp6RelayDestAddr": sleDhcp6RelayDestAddr,
       "sleDhcp6RelayOutputIfname": sleDhcp6RelayOutputIfname,
       "sleDhcp6RelayControl": sleDhcp6RelayControl,
       "sleDhcp6RelayControlRequest": sleDhcp6RelayControlRequest,
       "sleDhcp6RelayControlStatus": sleDhcp6RelayControlStatus,
       "sleDhcp6RelayControlTimer": sleDhcp6RelayControlTimer,
       "sleDhcp6RelayControlTimeStamp": sleDhcp6RelayControlTimeStamp,
       "sleDhcp6RelayControlReqResult": sleDhcp6RelayControlReqResult,
       "sleDhcp6RelayControlIndex": sleDhcp6RelayControlIndex,
       "sleDhcp6RelayControlIfName": sleDhcp6RelayControlIfName,
       "sleDhcp6RelayControlDestAddr": sleDhcp6RelayControlDestAddr,
       "sleDhcp6RelayControlOutputIfname": sleDhcp6RelayControlOutputIfname,
       "sleDhcp6RelayNotification": sleDhcp6RelayNotification,
       "sleDhcp6RelayCreated": sleDhcp6RelayCreated,
       "sleDhcp6RelayDestroyed": sleDhcp6RelayDestroyed,
       "sleDhcp6Client": sleDhcp6Client,
       "sleDhcp6ClientBase": sleDhcp6ClientBase,
       "sleDhcp6ClientTable": sleDhcp6ClientTable,
       "sleDhcp6ClientEntry": sleDhcp6ClientEntry,
       "sleDhcp6ClientIndex": sleDhcp6ClientIndex,
       "sleDhcp6ClientIfName": sleDhcp6ClientIfName,
       "sleDhcp6ClientState": sleDhcp6ClientState,
       "sleDhcp6ClientServerAddr": sleDhcp6ClientServerAddr,
       "sleDhcp6ClientServerDuid": sleDhcp6ClientServerDuid,
       "sleDhcp6ClientServerPref": sleDhcp6ClientServerPref,
       "sleDhcp6ClientRapidCommit": sleDhcp6ClientRapidCommit,
       "sleDhcp6ClientPdname": sleDhcp6ClientPdname,
       "sleDhcp6ClientInfoRefTime": sleDhcp6ClientInfoRefTime,
       "sleDhcp6ClientBaseControl": sleDhcp6ClientBaseControl,
       "sleDhcp6ClientBaseControlRequest": sleDhcp6ClientBaseControlRequest,
       "sleDhcp6ClientBaseControlStatus": sleDhcp6ClientBaseControlStatus,
       "sleDhcp6ClientBaseControlTimer": sleDhcp6ClientBaseControlTimer,
       "sleDhcp6ClientBaseControlTimeStamp": sleDhcp6ClientBaseControlTimeStamp,
       "sleDhcp6ClientBaseControlReqResult": sleDhcp6ClientBaseControlReqResult,
       "sleDhcp6ClientBaseControlIndex": sleDhcp6ClientBaseControlIndex,
       "sleDhcp6ClientBaseControlIfName": sleDhcp6ClientBaseControlIfName,
       "sleDhcp6ClientBaseControlStatelessFlag": sleDhcp6ClientBaseControlStatelessFlag,
       "sleDhcp6ClientBaseControlNaFlag": sleDhcp6ClientBaseControlNaFlag,
       "sleDhcp6ClientBaseControlPdFlag": sleDhcp6ClientBaseControlPdFlag,
       "sleDhcp6ClientBaseControlPdHint": sleDhcp6ClientBaseControlPdHint,
       "sleDhcp6ClientBaseControlIanaRapidCommit": sleDhcp6ClientBaseControlIanaRapidCommit,
       "sleDhcp6ClientBaseControlIapdRapidCommit": sleDhcp6ClientBaseControlIapdRapidCommit,
       "sleDhcp6ClientBaseControlRefreshMinimumVal": sleDhcp6ClientBaseControlRefreshMinimumVal,
       "sleDhcp6ClientBaseControlPdname": sleDhcp6ClientBaseControlPdname,
       "sleDhcp6ClientBaseNotification": sleDhcp6ClientBaseNotification,
       "sleDhcp6ClientStatelessSet": sleDhcp6ClientStatelessSet,
       "sleDhcp6ClientNaSet": sleDhcp6ClientNaSet,
       "sleDhcp6ClientPdSet": sleDhcp6ClientPdSet,
       "sleDhcp6ClientCleared": sleDhcp6ClientCleared,
       "sleDhcp6ClientRefreshMinChanged": sleDhcp6ClientRefreshMinChanged,
       "sleDhcp6ClientOption": sleDhcp6ClientOption,
       "sleDhcp6ClientOptionTable": sleDhcp6ClientOptionTable,
       "sleDhcp6ClientOptionEntry": sleDhcp6ClientOptionEntry,
       "sleDhcp6ClientOptionCode": sleDhcp6ClientOptionCode,
       "sleDhcp6ClientOptionType": sleDhcp6ClientOptionType,
       "sleDhcp6ClientOptionValue": sleDhcp6ClientOptionValue,
       "sleDhcp6ClientIapd": sleDhcp6ClientIapd,
       "sleDhcp6ClientIapdTable": sleDhcp6ClientIapdTable,
       "sleDhcp6ClientIapdEntry": sleDhcp6ClientIapdEntry,
       "sleDhcp6ClientIapdIndex": sleDhcp6ClientIapdIndex,
       "sleDhcp6ClientIapdIaid": sleDhcp6ClientIapdIaid,
       "sleDhcp6ClientIapdT1": sleDhcp6ClientIapdT1,
       "sleDhcp6ClientIapdT2": sleDhcp6ClientIapdT2,
       "sleDhcp6ClientIapdPrefix": sleDhcp6ClientIapdPrefix,
       "sleDhcp6ClientIapdPrefixLen": sleDhcp6ClientIapdPrefixLen,
       "sleDhcp6ClientIapdLifeTime": sleDhcp6ClientIapdLifeTime,
       "sleDhcp6ClientIapdValidTime": sleDhcp6ClientIapdValidTime,
       "sleDhcp6ClientIapdExpireTime": sleDhcp6ClientIapdExpireTime,
       "sleDhcp6ClientIana": sleDhcp6ClientIana,
       "sleDhcp6ClientIanaTable": sleDhcp6ClientIanaTable,
       "sleDhcp6ClientIanaEntry": sleDhcp6ClientIanaEntry,
       "sleDhcp6ClientIanaIndex": sleDhcp6ClientIanaIndex,
       "sleDhcp6ClientIanaIaid": sleDhcp6ClientIanaIaid,
       "sleDhcp6ClientIanaT1": sleDhcp6ClientIanaT1,
       "sleDhcp6ClientIanaT2": sleDhcp6ClientIanaT2,
       "sleDhcp6ClientIanaAddress": sleDhcp6ClientIanaAddress,
       "sleDhcp6ClientIanaLifeTime": sleDhcp6ClientIanaLifeTime,
       "sleDhcp6ClientIanaValidTime": sleDhcp6ClientIanaValidTime,
       "sleDhcp6ClientIanaExpireTime": sleDhcp6ClientIanaExpireTime,
       "sleDhcp6Option": sleDhcp6Option,
       "sleDhcp6OptionBase": sleDhcp6OptionBase,
       "sleDhcp6OptionBaseTable": sleDhcp6OptionBaseTable,
       "sleDhcp6OptionBaseEntry": sleDhcp6OptionBaseEntry,
       "sleDhcp6OptionBaseIndex": sleDhcp6OptionBaseIndex,
       "sleDhcp6OptionBaseName": sleDhcp6OptionBaseName,
       "sleDhcp6OptionBaseRawDataLen": sleDhcp6OptionBaseRawDataLen,
       "sleDhcp6OptionBaseRawData": sleDhcp6OptionBaseRawData,
       "sleDhcp6OptionBaseControl": sleDhcp6OptionBaseControl,
       "sleDhcp6OptionBaseControlRequest": sleDhcp6OptionBaseControlRequest,
       "sleDhcp6OptionBaseControlStatus": sleDhcp6OptionBaseControlStatus,
       "sleDhcp6OptionBaseControlTimer": sleDhcp6OptionBaseControlTimer,
       "sleDhcp6OptionBaseControlTimeStamp": sleDhcp6OptionBaseControlTimeStamp,
       "sleDhcp6OptionBaseControlReqResult": sleDhcp6OptionBaseControlReqResult,
       "sleDhcp6OptionBaseControlIndex": sleDhcp6OptionBaseControlIndex,
       "sleDhcp6OptionBaseControlName": sleDhcp6OptionBaseControlName,
       "sleDhcp6OptionBaseNotification": sleDhcp6OptionBaseNotification,
       "sleDhcp6OptionCreated": sleDhcp6OptionCreated,
       "sleDhcp6OptionDestroyed": sleDhcp6OptionDestroyed,
       "sleDhcp6OptionAttr": sleDhcp6OptionAttr,
       "sleDhcp6OptionAttrTable": sleDhcp6OptionAttrTable,
       "sleDhcp6OptionAttrEntry": sleDhcp6OptionAttrEntry,
       "sleDhcp6OptionAttrId": sleDhcp6OptionAttrId,
       "sleDhcp6OptionAttrType": sleDhcp6OptionAttrType,
       "sleDhcp6OptionAttrLengthHidden": sleDhcp6OptionAttrLengthHidden,
       "sleDhcp6OptionAttrLengthType": sleDhcp6OptionAttrLengthType,
       "sleDhcp6OptionAttrLengthValue": sleDhcp6OptionAttrLengthValue,
       "sleDhcp6OptionAttrValueType": sleDhcp6OptionAttrValueType,
       "sleDhcp6OptionAttrValue": sleDhcp6OptionAttrValue,
       "sleDhcp6OptionAttrControl": sleDhcp6OptionAttrControl,
       "sleDhcp6OptionAttrControlRequest": sleDhcp6OptionAttrControlRequest,
       "sleDhcp6OptionAttrControlStatus": sleDhcp6OptionAttrControlStatus,
       "sleDhcp6OptionAttrControlTimer": sleDhcp6OptionAttrControlTimer,
       "sleDhcp6OptionAttrControlTimeStamp": sleDhcp6OptionAttrControlTimeStamp,
       "sleDhcp6OptionAttrControlReqResult": sleDhcp6OptionAttrControlReqResult,
       "sleDhcp6OptionAttrControlOptionIndex": sleDhcp6OptionAttrControlOptionIndex,
       "sleDhcp6OptionAttrControlId": sleDhcp6OptionAttrControlId,
       "sleDhcp6OptionAttrControlType": sleDhcp6OptionAttrControlType,
       "sleDhcp6OptionAttrControlLengthHidden": sleDhcp6OptionAttrControlLengthHidden,
       "sleDhcp6OptionAttrControlLengthType": sleDhcp6OptionAttrControlLengthType,
       "sleDhcp6OptionAttrControlLengthValue": sleDhcp6OptionAttrControlLengthValue,
       "sleDhcp6OptionAttrControlValueType": sleDhcp6OptionAttrControlValueType,
       "sleDhcp6OptionAttrControlValue": sleDhcp6OptionAttrControlValue,
       "sleDhcp6OptionAttrNotification": sleDhcp6OptionAttrNotification,
       "sleDhcp6OptionAttrCreated": sleDhcp6OptionAttrCreated,
       "sleDhcp6OptionAttrDestroyed": sleDhcp6OptionAttrDestroyed,
       "sleDhcp6OptionAttrChanged": sleDhcp6OptionAttrChanged,
       "sleDhcp6Snooping": sleDhcp6Snooping,
       "sleDhcp6SnoopBase": sleDhcp6SnoopBase,
       "sleDhcp6SnoopBaseInfo": sleDhcp6SnoopBaseInfo,
       "sleDhcp6SnoopBaseState": sleDhcp6SnoopBaseState,
       "sleDhcp6SnoopBaseNdInspTime": sleDhcp6SnoopBaseNdInspTime,
       "sleDhcp6SnoopBaseControl": sleDhcp6SnoopBaseControl,
       "sleDhcp6SnoopBaseControlRequest": sleDhcp6SnoopBaseControlRequest,
       "sleDhcp6SnoopBaseControlStatus": sleDhcp6SnoopBaseControlStatus,
       "sleDhcp6SnoopBaseControlTimer": sleDhcp6SnoopBaseControlTimer,
       "sleDhcp6SnoopBaseControlTimeStamp": sleDhcp6SnoopBaseControlTimeStamp,
       "sleDhcp6SnoopBaseControlReqResult": sleDhcp6SnoopBaseControlReqResult,
       "sleDhcp6SnoopBaseControlState": sleDhcp6SnoopBaseControlState,
       "sleDhcp6SnoopBaseControlNdInspTime": sleDhcp6SnoopBaseControlNdInspTime,
       "sleDhcp6SnoopBaseNotification": sleDhcp6SnoopBaseNotification,
       "sleDhcp6SnoopBaseStateChanged": sleDhcp6SnoopBaseStateChanged,
       "sleDhcp6SnoopBaseNdInspTimeChanged": sleDhcp6SnoopBaseNdInspTimeChanged,
       "sleDhcp6SnoopVlan": sleDhcp6SnoopVlan,
       "sleDhcp6SnoopVlanTable": sleDhcp6SnoopVlanTable,
       "sleDhcp6SnoopVlanEntry": sleDhcp6SnoopVlanEntry,
       "sleDhcp6SnoopVlanIndex": sleDhcp6SnoopVlanIndex,
       "sleDhcp6SnoopVlanState": sleDhcp6SnoopVlanState,
       "sleDhcp6SnoopVlanControl": sleDhcp6SnoopVlanControl,
       "sleDhcp6SnoopVlanControlRequest": sleDhcp6SnoopVlanControlRequest,
       "sleDhcp6SnoopVlanControlStatus": sleDhcp6SnoopVlanControlStatus,
       "sleDhcp6SnoopVlanControlTimer": sleDhcp6SnoopVlanControlTimer,
       "sleDhcp6SnoopVlanControlTimeStamp": sleDhcp6SnoopVlanControlTimeStamp,
       "sleDhcp6SnoopVlanControlReqResult": sleDhcp6SnoopVlanControlReqResult,
       "sleDhcp6SnoopVlanControlIndex": sleDhcp6SnoopVlanControlIndex,
       "sleDhcp6SnoopVlanControlState": sleDhcp6SnoopVlanControlState,
       "sleDhcp6SnoopVlanNotification": sleDhcp6SnoopVlanNotification,
       "sleDhcp6SnoopVlanStateChanged": sleDhcp6SnoopVlanStateChanged,
       "sleDhcp6SnoopPort": sleDhcp6SnoopPort,
       "sleDhcp6SnoopPortTable": sleDhcp6SnoopPortTable,
       "sleDhcp6SnoopPortEntry": sleDhcp6SnoopPortEntry,
       "sleDhcp6SnoopPortIndex": sleDhcp6SnoopPortIndex,
       "sleDhcp6SnoopPortTrusted": sleDhcp6SnoopPortTrusted,
       "sleDhcp6SnoopPortLimitRate": sleDhcp6SnoopPortLimitRate,
       "sleDhcp6SnoopPortLimitLease": sleDhcp6SnoopPortLimitLease,
       "sleDhcp6SnoopPortControl": sleDhcp6SnoopPortControl,
       "sleDhcp6SnoopPortControlRequest": sleDhcp6SnoopPortControlRequest,
       "sleDhcp6SnoopPortControlStatus": sleDhcp6SnoopPortControlStatus,
       "sleDhcp6SnoopPortControlTimer": sleDhcp6SnoopPortControlTimer,
       "sleDhcp6SnoopPortControlTimeStamp": sleDhcp6SnoopPortControlTimeStamp,
       "sleDhcp6SnoopPortControlReqResult": sleDhcp6SnoopPortControlReqResult,
       "sleDhcp6SnoopPortControlIndex": sleDhcp6SnoopPortControlIndex,
       "sleDhcp6SnoopPortControlTrusted": sleDhcp6SnoopPortControlTrusted,
       "sleDhcp6SnoopPortControlLimitRate": sleDhcp6SnoopPortControlLimitRate,
       "sleDhcp6SnoopPortControlLimitLease": sleDhcp6SnoopPortControlLimitLease,
       "sleDhcp6SnoopPortNotification": sleDhcp6SnoopPortNotification,
       "sleDhcp6SnoopPortTrustChanged": sleDhcp6SnoopPortTrustChanged,
       "sleDhcp6SnoopPortLimitRateChanged": sleDhcp6SnoopPortLimitRateChanged,
       "sleDhcp6SnoopPortLimitLeaseChanged": sleDhcp6SnoopPortLimitLeaseChanged,
       "sleDhcp6SnoopBind": sleDhcp6SnoopBind,
       "sleDhcp6SnoopBindTable": sleDhcp6SnoopBindTable,
       "sleDhcp6SnoopBindEntry": sleDhcp6SnoopBindEntry,
       "sleDhcp6SnoopBindIndex": sleDhcp6SnoopBindIndex,
       "sleDhcp6SnoopBindPortIndex": sleDhcp6SnoopBindPortIndex,
       "sleDhcp6SnoopBindAddress": sleDhcp6SnoopBindAddress,
       "sleDhcp6SnoopBindVlan": sleDhcp6SnoopBindVlan,
       "sleDhcp6SnoopBindMac": sleDhcp6SnoopBindMac,
       "sleDhcp6SnoopBindValTime": sleDhcp6SnoopBindValTime,
       "sleDhcp6SnoopBindState": sleDhcp6SnoopBindState,
       "sleDhcp6SnoopBindType": sleDhcp6SnoopBindType,
       "sleDhcp6SnoopBindControl": sleDhcp6SnoopBindControl,
       "sleDhcp6SnoopBindControlRequest": sleDhcp6SnoopBindControlRequest,
       "sleDhcp6SnoopBindControlStatus": sleDhcp6SnoopBindControlStatus,
       "sleDhcp6SnoopBindControlTimer": sleDhcp6SnoopBindControlTimer,
       "sleDhcp6SnoopBindControlTimeStamp": sleDhcp6SnoopBindControlTimeStamp,
       "sleDhcp6SnoopBindControlReqResult": sleDhcp6SnoopBindControlReqResult,
       "sleDhcp6SnoopBindControlIndex": sleDhcp6SnoopBindControlIndex,
       "sleDhcp6SnoopBindControlPortIndex": sleDhcp6SnoopBindControlPortIndex,
       "sleDhcp6SnoopBindControlAddress": sleDhcp6SnoopBindControlAddress,
       "sleDhcp6SnoopBindControlVlan": sleDhcp6SnoopBindControlVlan,
       "sleDhcp6SnoopBindControlMac": sleDhcp6SnoopBindControlMac,
       "sleDhcp6SnoopBindControlValTime": sleDhcp6SnoopBindControlValTime,
       "sleDhcp6SnoopBindControlState": sleDhcp6SnoopBindControlState,
       "sleDhcp6SnoopBindControlType": sleDhcp6SnoopBindControlType,
       "sleDhcp6SnoopBindNotification": sleDhcp6SnoopBindNotification,
       "sleDhcp6SnoopBindCreated": sleDhcp6SnoopBindCreated,
       "sleDhcp6SnoopBindDestroyed": sleDhcp6SnoopBindDestroyed,
       "sleDhcp6SnoopBindCleared": sleDhcp6SnoopBindCleared,
       "sleDhcp6Aaa": sleDhcp6Aaa,
       "sleDhcp6AaaTable": sleDhcp6AaaTable,
       "sleDhcp6AaaEntry": sleDhcp6AaaEntry,
       "sleDhcp6AaaIndex": sleDhcp6AaaIndex,
       "sleDhcp6AaaModelName": sleDhcp6AaaModelName,
       "sleDhcp6AaaServerType": sleDhcp6AaaServerType,
       "sleDhcp6AaaServerAddr": sleDhcp6AaaServerAddr,
       "sleDhcp6AaaRadiusKey": sleDhcp6AaaRadiusKey,
       "sleDhcp6AaaRadiusUser": sleDhcp6AaaRadiusUser,
       "sleDhcp6AaaRadiusPasswd": sleDhcp6AaaRadiusPasswd,
       "sleDhcp6AaaRadiusRetry": sleDhcp6AaaRadiusRetry,
       "sleDhcp6AaaRadiusTimeout": sleDhcp6AaaRadiusTimeout,
       "sleDhcp6AaaRadiusPort": sleDhcp6AaaRadiusPort,
       "sleDhcp6AaaRadiusInterface": sleDhcp6AaaRadiusInterface,
       "sleDhcp6AaaControl": sleDhcp6AaaControl,
       "sleDhcp6AaaControlRequest": sleDhcp6AaaControlRequest,
       "sleDhcp6AaaControlStatus": sleDhcp6AaaControlStatus,
       "sleDhcp6AaaControlTimer": sleDhcp6AaaControlTimer,
       "sleDhcp6AaaControlTimeStamp": sleDhcp6AaaControlTimeStamp,
       "sleDhcp6AaaControlReqResult": sleDhcp6AaaControlReqResult,
       "sleDhcp6AaaControlIndex": sleDhcp6AaaControlIndex,
       "sleDhcp6AaaControlModelName": sleDhcp6AaaControlModelName,
       "sleDhcp6AaaControlServerAddr": sleDhcp6AaaControlServerAddr,
       "sleDhcp6AaaControlRadiusKey": sleDhcp6AaaControlRadiusKey,
       "sleDhcp6AaaControlRadiusUser": sleDhcp6AaaControlRadiusUser,
       "sleDhcp6AaaControlRadiusPasswd": sleDhcp6AaaControlRadiusPasswd,
       "sleDhcp6AaaControlRadiusRetry": sleDhcp6AaaControlRadiusRetry,
       "sleDhcp6AaaControlRadiusTimeout": sleDhcp6AaaControlRadiusTimeout,
       "sleDhcp6AaaControlRadiusPort": sleDhcp6AaaControlRadiusPort,
       "sleDhcp6AaaControlRadiusInterface": sleDhcp6AaaControlRadiusInterface,
       "sleDhcp6AaaNotification": sleDhcp6AaaNotification,
       "sleDhcp6AaaCreated": sleDhcp6AaaCreated,
       "sleDhcp6AaaDestroyed": sleDhcp6AaaDestroyed,
       "sleDhcp6AaaProfileChanged": sleDhcp6AaaProfileChanged,
       "sleDhcp6Group": sleDhcp6Group,
       "sleDhcp6NotificationGroup": sleDhcp6NotificationGroup}
)
