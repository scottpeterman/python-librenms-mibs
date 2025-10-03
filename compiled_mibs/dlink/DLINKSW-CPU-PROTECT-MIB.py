# SNMP MIB module (DLINKSW-CPU-PROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-CPU-PROTECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:43 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwCpuProtectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19)
)
if mibBuilder.loadTexts:
    dlinkSwCpuProtectMIB.setRevisions(
        ("2012-08-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CpuProtectProtocolType(TextualConvention, Integer32):
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bgp", 2),
          ("dhcp", 3),
          ("dhcpv6", 4),
          ("dns", 5),
          ("dot1x", 6),
          ("dvmrp", 7),
          ("gvrp", 8),
          ("icmp", 9),
          ("icmpv6Ndp", 10),
          ("icmpv6Other", 11),
          ("igmp", 12),
          ("lacp", 13),
          ("ntp", 14),
          ("ospf", 15),
          ("ospfv3", 16),
          ("pim", 17),
          ("pppoe", 18),
          ("rip", 19),
          ("ripng", 20),
          ("snmp", 21),
          ("ssh", 22),
          ("stp", 23),
          ("telnet", 24),
          ("tftp", 25),
          ("vrrp", 26),
          ("web", 27))
    )



class MaxRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )



class UnitID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_DCpuProtectMIBNotifications_ObjectIdentity = ObjectIdentity
dCpuProtectMIBNotifications = _DCpuProtectMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 0)
)
_DCpuProtectMIBObjects_ObjectIdentity = ObjectIdentity
dCpuProtectMIBObjects = _DCpuProtectMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1)
)
_DCpuProtectMIBObjectsCtrl_ObjectIdentity = ObjectIdentity
dCpuProtectMIBObjectsCtrl = _DCpuProtectMIBObjectsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2)
)
_DCpuProtectProtoRateLimitTable_Object = MibTable
dCpuProtectProtoRateLimitTable = _DCpuProtectProtoRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dCpuProtectProtoRateLimitTable.setStatus("current")
_DCpuProtectProtoRateLimitEntry_Object = MibTableRow
dCpuProtectProtoRateLimitEntry = _DCpuProtectProtoRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 1, 1)
)
dCpuProtectProtoRateLimitEntry.setIndexNames(
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLType"),
)
if mibBuilder.loadTexts:
    dCpuProtectProtoRateLimitEntry.setStatus("current")
_DCpuProtectProtoRLType_Type = CpuProtectProtocolType
_DCpuProtectProtoRLType_Object = MibTableColumn
dCpuProtectProtoRLType = _DCpuProtectProtoRLType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 1, 1, 1),
    _DCpuProtectProtoRLType_Type()
)
dCpuProtectProtoRLType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLType.setStatus("current")


class _DCpuProtectProtoRLRate_Type(MaxRate):
    """Custom type dCpuProtectProtoRLRate based on MaxRate"""
    defaultValue = -1


_DCpuProtectProtoRLRate_Type.__name__ = "MaxRate"
_DCpuProtectProtoRLRate_Object = MibTableColumn
dCpuProtectProtoRLRate = _DCpuProtectProtoRLRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 1, 1, 2),
    _DCpuProtectProtoRLRate_Type()
)
dCpuProtectProtoRLRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLRate.setStatus("current")


class _DCpuProtectProtoRLClearCounter_Type(Integer32):
    """Custom type dCpuProtectProtoRLClearCounter based on Integer32"""
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


_DCpuProtectProtoRLClearCounter_Type.__name__ = "Integer32"
_DCpuProtectProtoRLClearCounter_Object = MibTableColumn
dCpuProtectProtoRLClearCounter = _DCpuProtectProtoRLClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 1, 1, 3),
    _DCpuProtectProtoRLClearCounter_Type()
)
dCpuProtectProtoRLClearCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLClearCounter.setStatus("current")
_DCpuProtectSubIntfRLTable_Object = MibTable
dCpuProtectSubIntfRLTable = _DCpuProtectSubIntfRLTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLTable.setStatus("current")
_DCpuProtectSubIntfRLEntry_Object = MibTableRow
dCpuProtectSubIntfRLEntry = _DCpuProtectSubIntfRLEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 2, 1)
)
dCpuProtectSubIntfRLEntry.setIndexNames(
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLType"),
)
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLEntry.setStatus("current")


class _DCpuProtectSubIntfRLType_Type(Integer32):
    """Custom type dCpuProtectSubIntfRLType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manage", 1),
          ("protocol", 2),
          ("route", 3))
    )


_DCpuProtectSubIntfRLType_Type.__name__ = "Integer32"
_DCpuProtectSubIntfRLType_Object = MibTableColumn
dCpuProtectSubIntfRLType = _DCpuProtectSubIntfRLType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 2, 1, 1),
    _DCpuProtectSubIntfRLType_Type()
)
dCpuProtectSubIntfRLType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLType.setStatus("current")


class _DCpuProtectSubIntfRLRate_Type(MaxRate):
    """Custom type dCpuProtectSubIntfRLRate based on MaxRate"""
    defaultValue = -1


_DCpuProtectSubIntfRLRate_Type.__name__ = "MaxRate"
_DCpuProtectSubIntfRLRate_Object = MibTableColumn
dCpuProtectSubIntfRLRate = _DCpuProtectSubIntfRLRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 2, 1, 2),
    _DCpuProtectSubIntfRLRate_Type()
)
dCpuProtectSubIntfRLRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLRate.setStatus("current")


class _DCpuProtectSubIntfRLClearCounter_Type(Integer32):
    """Custom type dCpuProtectSubIntfRLClearCounter based on Integer32"""
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


_DCpuProtectSubIntfRLClearCounter_Type.__name__ = "Integer32"
_DCpuProtectSubIntfRLClearCounter_Object = MibTableColumn
dCpuProtectSubIntfRLClearCounter = _DCpuProtectSubIntfRLClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 2, 2, 1, 3),
    _DCpuProtectSubIntfRLClearCounter_Type()
)
dCpuProtectSubIntfRLClearCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLClearCounter.setStatus("current")
_DCpuProtectMIBObjectsCounters_ObjectIdentity = ObjectIdentity
dCpuProtectMIBObjectsCounters = _DCpuProtectMIBObjectsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3)
)
_DCpuProtectProtoRLCntTable_Object = MibTable
dCpuProtectProtoRLCntTable = _DCpuProtectProtoRLCntTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntTable.setStatus("current")
_DCpuProtectProtoRLCntEntry_Object = MibTableRow
dCpuProtectProtoRLCntEntry = _DCpuProtectProtoRLCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1, 1)
)
dCpuProtectProtoRLCntEntry.setIndexNames(
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLCntType"),
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLCntUnitID"),
)
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntEntry.setStatus("current")
_DCpuProtectProtoRLCntType_Type = CpuProtectProtocolType
_DCpuProtectProtoRLCntType_Object = MibTableColumn
dCpuProtectProtoRLCntType = _DCpuProtectProtoRLCntType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1, 1, 1),
    _DCpuProtectProtoRLCntType_Type()
)
dCpuProtectProtoRLCntType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntType.setStatus("current")
_DCpuProtectProtoRLCntUnitID_Type = UnitID
_DCpuProtectProtoRLCntUnitID_Object = MibTableColumn
dCpuProtectProtoRLCntUnitID = _DCpuProtectProtoRLCntUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1, 1, 2),
    _DCpuProtectProtoRLCntUnitID_Type()
)
dCpuProtectProtoRLCntUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntUnitID.setStatus("current")
_DCpuProtectProtoRLCntTotalCnt_Type = Counter64
_DCpuProtectProtoRLCntTotalCnt_Object = MibTableColumn
dCpuProtectProtoRLCntTotalCnt = _DCpuProtectProtoRLCntTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1, 1, 3),
    _DCpuProtectProtoRLCntTotalCnt_Type()
)
dCpuProtectProtoRLCntTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntTotalCnt.setStatus("current")
_DCpuProtectProtoRLCntDropCnt_Type = Counter64
_DCpuProtectProtoRLCntDropCnt_Object = MibTableColumn
dCpuProtectProtoRLCntDropCnt = _DCpuProtectProtoRLCntDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 1, 1, 4),
    _DCpuProtectProtoRLCntDropCnt_Type()
)
dCpuProtectProtoRLCntDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCpuProtectProtoRLCntDropCnt.setStatus("current")
_DCpuProtectSubIntfRLCounterTable_Object = MibTable
dCpuProtectSubIntfRLCounterTable = _DCpuProtectSubIntfRLCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCounterTable.setStatus("current")
_DCpuProtectSubIntfRLCounterEntry_Object = MibTableRow
dCpuProtectSubIntfRLCounterEntry = _DCpuProtectSubIntfRLCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2, 1)
)
dCpuProtectSubIntfRLCounterEntry.setIndexNames(
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLCntType"),
    (0, "DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLCntUnitID"),
)
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCounterEntry.setStatus("current")


class _DCpuProtectSubIntfRLCntType_Type(Integer32):
    """Custom type dCpuProtectSubIntfRLCntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manage", 1),
          ("protocol", 2),
          ("route", 3))
    )


_DCpuProtectSubIntfRLCntType_Type.__name__ = "Integer32"
_DCpuProtectSubIntfRLCntType_Object = MibTableColumn
dCpuProtectSubIntfRLCntType = _DCpuProtectSubIntfRLCntType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2, 1, 1),
    _DCpuProtectSubIntfRLCntType_Type()
)
dCpuProtectSubIntfRLCntType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCntType.setStatus("current")
_DCpuProtectSubIntfRLCntUnitID_Type = UnitID
_DCpuProtectSubIntfRLCntUnitID_Object = MibTableColumn
dCpuProtectSubIntfRLCntUnitID = _DCpuProtectSubIntfRLCntUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2, 1, 2),
    _DCpuProtectSubIntfRLCntUnitID_Type()
)
dCpuProtectSubIntfRLCntUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCntUnitID.setStatus("current")
_DCpuProtectSubIntfRLCntTotalCnt_Type = Counter64
_DCpuProtectSubIntfRLCntTotalCnt_Object = MibTableColumn
dCpuProtectSubIntfRLCntTotalCnt = _DCpuProtectSubIntfRLCntTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2, 1, 3),
    _DCpuProtectSubIntfRLCntTotalCnt_Type()
)
dCpuProtectSubIntfRLCntTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCntTotalCnt.setStatus("current")
_DCpuProtectSubIntfRLCntDropCnt_Type = Counter64
_DCpuProtectSubIntfRLCntDropCnt_Object = MibTableColumn
dCpuProtectSubIntfRLCntDropCnt = _DCpuProtectSubIntfRLCntDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 3, 2, 1, 4),
    _DCpuProtectSubIntfRLCntDropCnt_Type()
)
dCpuProtectSubIntfRLCntDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCpuProtectSubIntfRLCntDropCnt.setStatus("current")
_DCpuProtectMIBConformance_ObjectIdentity = ObjectIdentity
dCpuProtectMIBConformance = _DCpuProtectMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2)
)
_DCpuProtectMIBCompliances_ObjectIdentity = ObjectIdentity
dCpuProtectMIBCompliances = _DCpuProtectMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2, 1)
)
_DCpuProtectMIBGroups_ObjectIdentity = ObjectIdentity
dCpuProtectMIBGroups = _DCpuProtectMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2, 2)
)

# Managed Objects groups

dCpuProtectProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2, 2, 1)
)
dCpuProtectProtoGroup.setObjects(
      *(("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLRate"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLClearCounter"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLCntTotalCnt"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoRLCntDropCnt"))
)
if mibBuilder.loadTexts:
    dCpuProtectProtoGroup.setStatus("current")

dCpuProtectSubIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2, 2, 2)
)
dCpuProtectSubIntfGroup.setObjects(
      *(("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLRate"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLClearCounter"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLCntTotalCnt"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfRLCntDropCnt"))
)
if mibBuilder.loadTexts:
    dCpuProtectSubIntfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dCpuProtectMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 2, 1, 1)
)
dCpuProtectMIBCompliance.setObjects(
      *(("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectProtoGroup"),
        ("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectSubIntfGroup"))
)
if mibBuilder.loadTexts:
    dCpuProtectMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-CPU-PROTECT-MIB",
    **{"CpuProtectProtocolType": CpuProtectProtocolType,
       "MaxRate": MaxRate,
       "UnitID": UnitID,
       "dlinkSwCpuProtectMIB": dlinkSwCpuProtectMIB,
       "dCpuProtectMIBNotifications": dCpuProtectMIBNotifications,
       "dCpuProtectMIBObjects": dCpuProtectMIBObjects,
       "dCpuProtectMIBObjectsCtrl": dCpuProtectMIBObjectsCtrl,
       "dCpuProtectProtoRateLimitTable": dCpuProtectProtoRateLimitTable,
       "dCpuProtectProtoRateLimitEntry": dCpuProtectProtoRateLimitEntry,
       "dCpuProtectProtoRLType": dCpuProtectProtoRLType,
       "dCpuProtectProtoRLRate": dCpuProtectProtoRLRate,
       "dCpuProtectProtoRLClearCounter": dCpuProtectProtoRLClearCounter,
       "dCpuProtectSubIntfRLTable": dCpuProtectSubIntfRLTable,
       "dCpuProtectSubIntfRLEntry": dCpuProtectSubIntfRLEntry,
       "dCpuProtectSubIntfRLType": dCpuProtectSubIntfRLType,
       "dCpuProtectSubIntfRLRate": dCpuProtectSubIntfRLRate,
       "dCpuProtectSubIntfRLClearCounter": dCpuProtectSubIntfRLClearCounter,
       "dCpuProtectMIBObjectsCounters": dCpuProtectMIBObjectsCounters,
       "dCpuProtectProtoRLCntTable": dCpuProtectProtoRLCntTable,
       "dCpuProtectProtoRLCntEntry": dCpuProtectProtoRLCntEntry,
       "dCpuProtectProtoRLCntType": dCpuProtectProtoRLCntType,
       "dCpuProtectProtoRLCntUnitID": dCpuProtectProtoRLCntUnitID,
       "dCpuProtectProtoRLCntTotalCnt": dCpuProtectProtoRLCntTotalCnt,
       "dCpuProtectProtoRLCntDropCnt": dCpuProtectProtoRLCntDropCnt,
       "dCpuProtectSubIntfRLCounterTable": dCpuProtectSubIntfRLCounterTable,
       "dCpuProtectSubIntfRLCounterEntry": dCpuProtectSubIntfRLCounterEntry,
       "dCpuProtectSubIntfRLCntType": dCpuProtectSubIntfRLCntType,
       "dCpuProtectSubIntfRLCntUnitID": dCpuProtectSubIntfRLCntUnitID,
       "dCpuProtectSubIntfRLCntTotalCnt": dCpuProtectSubIntfRLCntTotalCnt,
       "dCpuProtectSubIntfRLCntDropCnt": dCpuProtectSubIntfRLCntDropCnt,
       "dCpuProtectMIBConformance": dCpuProtectMIBConformance,
       "dCpuProtectMIBCompliances": dCpuProtectMIBCompliances,
       "dCpuProtectMIBCompliance": dCpuProtectMIBCompliance,
       "dCpuProtectMIBGroups": dCpuProtectMIBGroups,
       "dCpuProtectProtoGroup": dCpuProtectProtoGroup,
       "dCpuProtectSubIntfGroup": dCpuProtectSubIntfGroup}
)
