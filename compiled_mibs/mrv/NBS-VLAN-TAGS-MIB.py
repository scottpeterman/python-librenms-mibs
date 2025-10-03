# SNMP MIB module (NBS-VLAN-TAGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-VLAN-TAGS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:40 2025
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

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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


# MODULE-IDENTITY

nbsVlanTagsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 219)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsVlanTagsPortGrp_ObjectIdentity = ObjectIdentity
nbsVlanTagsPortGrp = _NbsVlanTagsPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 219, 1)
)
if mibBuilder.loadTexts:
    nbsVlanTagsPortGrp.setStatus("current")
_NbsVlanTagsPortTableSize_Type = Unsigned32
_NbsVlanTagsPortTableSize_Object = MibScalar
nbsVlanTagsPortTableSize = _NbsVlanTagsPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 1),
    _NbsVlanTagsPortTableSize_Type()
)
nbsVlanTagsPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanTagsPortTableSize.setStatus("current")
_NbsVlanTagsPortTable_Object = MibTable
nbsVlanTagsPortTable = _NbsVlanTagsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2)
)
if mibBuilder.loadTexts:
    nbsVlanTagsPortTable.setStatus("current")
_NbsVlanTagsPortEntry_Object = MibTableRow
nbsVlanTagsPortEntry = _NbsVlanTagsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1)
)
nbsVlanTagsPortEntry.setIndexNames(
    (0, "NBS-VLAN-TAGS-MIB", "nbsVlanTagsPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsVlanTagsPortEntry.setStatus("current")
_NbsVlanTagsPortIfIndex_Type = InterfaceIndex
_NbsVlanTagsPortIfIndex_Object = MibTableColumn
nbsVlanTagsPortIfIndex = _NbsVlanTagsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 1),
    _NbsVlanTagsPortIfIndex_Type()
)
nbsVlanTagsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanTagsPortIfIndex.setStatus("current")


class _NbsVlanTagsPortAction_Type(Integer32):
    """Custom type nbsVlanTagsPortAction based on Integer32"""
    defaultValue = 4

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
        *(("notSupported", 1),
          ("add", 2),
          ("strip", 3),
          ("ignore", 4))
    )


_NbsVlanTagsPortAction_Type.__name__ = "Integer32"
_NbsVlanTagsPortAction_Object = MibTableColumn
nbsVlanTagsPortAction = _NbsVlanTagsPortAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 2),
    _NbsVlanTagsPortAction_Type()
)
nbsVlanTagsPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanTagsPortAction.setStatus("current")


class _NbsVlanTagsPortVid_Type(Integer32):
    """Custom type nbsVlanTagsPortVid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_NbsVlanTagsPortVid_Type.__name__ = "Integer32"
_NbsVlanTagsPortVid_Object = MibTableColumn
nbsVlanTagsPortVid = _NbsVlanTagsPortVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 3),
    _NbsVlanTagsPortVid_Type()
)
nbsVlanTagsPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanTagsPortVid.setStatus("current")


class _NbsVlanTagsPortPriority_Type(Integer32):
    """Custom type nbsVlanTagsPortPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbsVlanTagsPortPriority_Type.__name__ = "Integer32"
_NbsVlanTagsPortPriority_Object = MibTableColumn
nbsVlanTagsPortPriority = _NbsVlanTagsPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 219, 1, 2, 1, 4),
    _NbsVlanTagsPortPriority_Type()
)
nbsVlanTagsPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanTagsPortPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-VLAN-TAGS-MIB",
    **{"nbsVlanTagsMib": nbsVlanTagsMib,
       "nbsVlanTagsPortGrp": nbsVlanTagsPortGrp,
       "nbsVlanTagsPortTableSize": nbsVlanTagsPortTableSize,
       "nbsVlanTagsPortTable": nbsVlanTagsPortTable,
       "nbsVlanTagsPortEntry": nbsVlanTagsPortEntry,
       "nbsVlanTagsPortIfIndex": nbsVlanTagsPortIfIndex,
       "nbsVlanTagsPortAction": nbsVlanTagsPortAction,
       "nbsVlanTagsPortVid": nbsVlanTagsPortVid,
       "nbsVlanTagsPortPriority": nbsVlanTagsPortPriority}
)
