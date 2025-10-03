# SNMP MIB module (HH3C-UNICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-UNICAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:10 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cUnicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44)
)
if mibBuilder.loadTexts:
    hh3cUnicast.setRevisions(
        ("2005-03-24 14:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cURPFTable_Object = MibTable
hh3cURPFTable = _Hh3cURPFTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1)
)
if mibBuilder.loadTexts:
    hh3cURPFTable.setStatus("current")
_Hh3cURPFEntry_Object = MibTableRow
hh3cURPFEntry = _Hh3cURPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1)
)
hh3cURPFEntry.setIndexNames(
    (0, "HH3C-UNICAST-MIB", "hh3cURPFIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cURPFEntry.setStatus("current")
_Hh3cURPFIfIndex_Type = Integer32
_Hh3cURPFIfIndex_Object = MibTableColumn
hh3cURPFIfIndex = _Hh3cURPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 1),
    _Hh3cURPFIfIndex_Type()
)
hh3cURPFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cURPFIfIndex.setStatus("current")


class _Hh3cURPFEnabled_Type(TruthValue):
    """Custom type hh3cURPFEnabled based on TruthValue"""
    defaultValue = 2


_Hh3cURPFEnabled_Type.__name__ = "TruthValue"
_Hh3cURPFEnabled_Object = MibTableColumn
hh3cURPFEnabled = _Hh3cURPFEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 2),
    _Hh3cURPFEnabled_Type()
)
hh3cURPFEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cURPFEnabled.setStatus("current")
_Hh3cURPFSlotID_Type = Integer32
_Hh3cURPFSlotID_Object = MibTableColumn
hh3cURPFSlotID = _Hh3cURPFSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 3),
    _Hh3cURPFSlotID_Type()
)
hh3cURPFSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cURPFSlotID.setStatus("current")
_Hh3cURPFTotalReceivedPacket_Type = Counter64
_Hh3cURPFTotalReceivedPacket_Object = MibTableColumn
hh3cURPFTotalReceivedPacket = _Hh3cURPFTotalReceivedPacket_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 4),
    _Hh3cURPFTotalReceivedPacket_Type()
)
hh3cURPFTotalReceivedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cURPFTotalReceivedPacket.setStatus("current")
_Hh3cURPFDroppedPacket_Type = Counter64
_Hh3cURPFDroppedPacket_Object = MibTableColumn
hh3cURPFDroppedPacket = _Hh3cURPFDroppedPacket_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 5),
    _Hh3cURPFDroppedPacket_Type()
)
hh3cURPFDroppedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cURPFDroppedPacket.setStatus("current")


class _Hh3cURPFClearStat_Type(Integer32):
    """Custom type hh3cURPFClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("reset", 1))
    )


_Hh3cURPFClearStat_Type.__name__ = "Integer32"
_Hh3cURPFClearStat_Object = MibTableColumn
hh3cURPFClearStat = _Hh3cURPFClearStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44, 1, 1, 6),
    _Hh3cURPFClearStat_Type()
)
hh3cURPFClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cURPFClearStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-UNICAST-MIB",
    **{"hh3cUnicast": hh3cUnicast,
       "hh3cURPFTable": hh3cURPFTable,
       "hh3cURPFEntry": hh3cURPFEntry,
       "hh3cURPFIfIndex": hh3cURPFIfIndex,
       "hh3cURPFEnabled": hh3cURPFEnabled,
       "hh3cURPFSlotID": hh3cURPFSlotID,
       "hh3cURPFTotalReceivedPacket": hh3cURPFTotalReceivedPacket,
       "hh3cURPFDroppedPacket": hh3cURPFDroppedPacket,
       "hh3cURPFClearStat": hh3cURPFClearStat}
)
