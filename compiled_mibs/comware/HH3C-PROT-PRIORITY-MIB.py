# SNMP MIB module (HH3C-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PROT-PRIORITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:33 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37)
)
if mibBuilder.loadTexts:
    hh3cProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
hh3cProtocolPriorityObjects = _Hh3cProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1)
)
_Hh3cPPri_ObjectIdentity = ObjectIdentity
hh3cPPri = _Hh3cPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1)
)
_Hh3cProtocolPriorityTable_Object = MibTable
hh3cProtocolPriorityTable = _Hh3cProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cProtocolPriorityTable.setStatus("current")
_Hh3cProtocolPriorityEntry_Object = MibTableRow
hh3cProtocolPriorityEntry = _Hh3cProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1)
)
hh3cProtocolPriorityEntry.setIndexNames(
    (0, "HH3C-PROT-PRIORITY-MIB", "hh3cPPriProtocolType"),
)
if mibBuilder.loadTexts:
    hh3cProtocolPriorityEntry.setStatus("current")


class _Hh3cPPriProtocolType_Type(Integer32):
    """Custom type hh3cPPriProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ospf", 1),
          ("telnet", 2),
          ("snmp", 3),
          ("icmp", 4),
          ("bgp", 5),
          ("ldp", 6))
    )


_Hh3cPPriProtocolType_Type.__name__ = "Integer32"
_Hh3cPPriProtocolType_Object = MibTableColumn
hh3cPPriProtocolType = _Hh3cPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 1),
    _Hh3cPPriProtocolType_Type()
)
hh3cPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPPriProtocolType.setStatus("current")


class _Hh3cPPriPriorityType_Type(Integer32):
    """Custom type hh3cPPriPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("dscp", 2))
    )


_Hh3cPPriPriorityType_Type.__name__ = "Integer32"
_Hh3cPPriPriorityType_Object = MibTableColumn
hh3cPPriPriorityType = _Hh3cPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 2),
    _Hh3cPPriPriorityType_Type()
)
hh3cPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriPriorityType.setStatus("current")


class _Hh3cPPriPriorityVlaue_Type(Integer32):
    """Custom type hh3cPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cPPriPriorityVlaue_Type.__name__ = "Integer32"
_Hh3cPPriPriorityVlaue_Object = MibTableColumn
hh3cPPriPriorityVlaue = _Hh3cPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 3),
    _Hh3cPPriPriorityVlaue_Type()
)
hh3cPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriPriorityVlaue.setStatus("current")
_Hh3cPPriRowStatus_Type = RowStatus
_Hh3cPPriRowStatus_Object = MibTableColumn
hh3cPPriRowStatus = _Hh3cPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 4),
    _Hh3cPPriRowStatus_Type()
)
hh3cPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PROT-PRIORITY-MIB",
    **{"hh3cProtocolPriority": hh3cProtocolPriority,
       "hh3cProtocolPriorityObjects": hh3cProtocolPriorityObjects,
       "hh3cPPri": hh3cPPri,
       "hh3cProtocolPriorityTable": hh3cProtocolPriorityTable,
       "hh3cProtocolPriorityEntry": hh3cProtocolPriorityEntry,
       "hh3cPPriProtocolType": hh3cPPriProtocolType,
       "hh3cPPriPriorityType": hh3cPPriPriorityType,
       "hh3cPPriPriorityVlaue": hh3cPPriPriorityVlaue,
       "hh3cPPriRowStatus": hh3cPPriRowStatus}
)
