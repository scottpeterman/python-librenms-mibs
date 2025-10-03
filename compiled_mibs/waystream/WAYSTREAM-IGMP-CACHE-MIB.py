# SNMP MIB module (WAYSTREAM-IGMP-CACHE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-IGMP-CACHE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:59 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(wsMgmt,) = mibBuilder.importSymbols(
    "WAYSTREAM-SMI",
    "wsMgmt")


# MODULE-IDENTITY

wsIgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13)
)
if mibBuilder.loadTexts:
    wsIgmp.setRevisions(
        ("2017-02-10 11:00",
         "2011-01-11 17:54",
         "2009-04-29 13:49",
         "2009-03-23 11:25",
         "2008-04-30 13:48",
         "2007-06-13 14:37")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsIgmpCacheTable_Object = MibTable
wsIgmpCacheTable = _WsIgmpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2)
)
if mibBuilder.loadTexts:
    wsIgmpCacheTable.setStatus("current")
_WsIgmpCacheEntry_Object = MibTableRow
wsIgmpCacheEntry = _WsIgmpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1)
)
wsIgmpCacheEntry.setIndexNames(
    (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheAddress"),
    (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheIfIndex"),
    (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheReporter"),
)
if mibBuilder.loadTexts:
    wsIgmpCacheEntry.setStatus("current")
_WsIgmpCacheAddress_Type = IpAddress
_WsIgmpCacheAddress_Object = MibTableColumn
wsIgmpCacheAddress = _WsIgmpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 1),
    _WsIgmpCacheAddress_Type()
)
wsIgmpCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsIgmpCacheAddress.setStatus("current")
_WsIgmpCacheIfIndex_Type = InterfaceIndex
_WsIgmpCacheIfIndex_Object = MibTableColumn
wsIgmpCacheIfIndex = _WsIgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 2),
    _WsIgmpCacheIfIndex_Type()
)
wsIgmpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsIgmpCacheIfIndex.setStatus("current")
_WsIgmpCacheReporter_Type = IpAddress
_WsIgmpCacheReporter_Object = MibTableColumn
wsIgmpCacheReporter = _WsIgmpCacheReporter_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 3),
    _WsIgmpCacheReporter_Type()
)
wsIgmpCacheReporter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsIgmpCacheReporter.setStatus("current")
_WsIgmpCacheUpTime_Type = TimeTicks
_WsIgmpCacheUpTime_Object = MibTableColumn
wsIgmpCacheUpTime = _WsIgmpCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 4),
    _WsIgmpCacheUpTime_Type()
)
wsIgmpCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIgmpCacheUpTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-IGMP-CACHE-MIB",
    **{"wsIgmp": wsIgmp,
       "wsIgmpCacheTable": wsIgmpCacheTable,
       "wsIgmpCacheEntry": wsIgmpCacheEntry,
       "wsIgmpCacheAddress": wsIgmpCacheAddress,
       "wsIgmpCacheIfIndex": wsIgmpCacheIfIndex,
       "wsIgmpCacheReporter": wsIgmpCacheReporter,
       "wsIgmpCacheUpTime": wsIgmpCacheUpTime}
)
