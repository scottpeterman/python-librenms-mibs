# SNMP MIB module (PT-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\PT-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:38 2025
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

(pt,) = mibBuilder.importSymbols(
    "PT-MIB",
    "pt")

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

ptPM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5)
)
if mibBuilder.loadTexts:
    ptPM.setRevisions(
        ("2018-08-29 12:30",
         "2016-03-09 12:30",
         "2016-02-10 12:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PtPMTable_Object = MibTable
ptPMTable = _PtPMTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ptPMTable.setStatus("current")
_PtPMEntry_Object = MibTableRow
ptPMEntry = _PtPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1)
)
ptPMEntry.setIndexNames(
    (0, "PT-PM-MIB", "queueIndex"),
)
if mibBuilder.loadTexts:
    ptPMEntry.setStatus("current")


class _QueueIndex_Type(Integer32):
    """Custom type queueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QueueIndex_Type.__name__ = "Integer32"
_QueueIndex_Object = MibTableColumn
queueIndex = _QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 1),
    _QueueIndex_Type()
)
queueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueIndex.setStatus("current")
_ForwardingPacket_Type = Counter64
_ForwardingPacket_Object = MibTableColumn
forwardingPacket = _ForwardingPacket_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 2),
    _ForwardingPacket_Type()
)
forwardingPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardingPacket.setStatus("current")
_ForwardingOctets_Type = Counter64
_ForwardingOctets_Object = MibTableColumn
forwardingOctets = _ForwardingOctets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 3),
    _ForwardingOctets_Type()
)
forwardingOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardingOctets.setStatus("current")
_DiscardPackets_Type = Counter64
_DiscardPackets_Object = MibTableColumn
discardPackets = _DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 4),
    _DiscardPackets_Type()
)
discardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discardPackets.setStatus("current")
_DiscardOctets_Type = Counter64
_DiscardOctets_Object = MibTableColumn
discardOctets = _DiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 5),
    _DiscardOctets_Type()
)
discardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discardOctets.setStatus("current")
_InputPackets_Type = Counter64
_InputPackets_Object = MibTableColumn
inputPackets = _InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 6),
    _InputPackets_Type()
)
inputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPackets.setStatus("current")
_InputOctets_Type = Counter64
_InputOctets_Object = MibTableColumn
inputOctets = _InputOctets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 7),
    _InputOctets_Type()
)
inputOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputOctets.setStatus("current")
_PtPMConformance_ObjectIdentity = ObjectIdentity
ptPMConformance = _PtPMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2)
)
_PtPMCompliances_ObjectIdentity = ObjectIdentity
ptPMCompliances = _PtPMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1)
)
_PtPMGroups_ObjectIdentity = ObjectIdentity
ptPMGroups = _PtPMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2)
)

# Managed Objects groups

ptPMCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2, 1)
)
ptPMCompleteGroup.setObjects(
      *(("PT-PM-MIB", "forwardingPacket"),
        ("PT-PM-MIB", "forwardingOctets"),
        ("PT-PM-MIB", "discardPackets"),
        ("PT-PM-MIB", "discardOctets"),
        ("PT-PM-MIB", "inputPackets"),
        ("PT-PM-MIB", "inputOctets"))
)
if mibBuilder.loadTexts:
    ptPMCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptPMFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1, 1)
)
ptPMFullCompliance.setObjects(
    ("PT-PM-MIB", "ptPMCompleteGroup")
)
if mibBuilder.loadTexts:
    ptPMFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PT-PM-MIB",
    **{"ptPM": ptPM,
       "ptPMTable": ptPMTable,
       "ptPMEntry": ptPMEntry,
       "queueIndex": queueIndex,
       "forwardingPacket": forwardingPacket,
       "forwardingOctets": forwardingOctets,
       "discardPackets": discardPackets,
       "discardOctets": discardOctets,
       "inputPackets": inputPackets,
       "inputOctets": inputOctets,
       "ptPMConformance": ptPMConformance,
       "ptPMCompliances": ptPMCompliances,
       "ptPMFullCompliance": ptPMFullCompliance,
       "ptPMGroups": ptPMGroups,
       "ptPMCompleteGroup": ptPMCompleteGroup}
)
