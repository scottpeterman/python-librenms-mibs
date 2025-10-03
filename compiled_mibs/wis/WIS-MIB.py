# SNMP MIB module (WIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wis\WIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:15 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1)
)
if mibBuilder.loadTexts:
    wisMIB.setRevisions(
        ("2024-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wis_ObjectIdentity = ObjectIdentity
wis = _Wis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 62821)
)
_WisORTable_Object = MibTable
wisORTable = _WisORTable_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 1)
)
if mibBuilder.loadTexts:
    wisORTable.setStatus("current")
_WisOREntry_Object = MibTableRow
wisOREntry = _WisOREntry_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 1, 1)
)
wisOREntry.setIndexNames(
    (0, "WIS-MIB", "wisORIndex"),
)
if mibBuilder.loadTexts:
    wisOREntry.setStatus("current")


class _WisORIndex_Type(Integer32):
    """Custom type wisORIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WisORIndex_Type.__name__ = "Integer32"
_WisORIndex_Object = MibTableColumn
wisORIndex = _WisORIndex_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 1, 1, 1),
    _WisORIndex_Type()
)
wisORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wisORIndex.setStatus("current")
_WisORID_Type = ObjectIdentifier
_WisORID_Object = MibTableColumn
wisORID = _WisORID_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 1, 1, 2),
    _WisORID_Type()
)
wisORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisORID.setStatus("current")
_WisORDescr_Type = DisplayString
_WisORDescr_Object = MibTableColumn
wisORDescr = _WisORDescr_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 1, 1, 3),
    _WisORDescr_Type()
)
wisORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisORDescr.setStatus("current")
_WisSnmpInfo_ObjectIdentity = ObjectIdentity
wisSnmpInfo = _WisSnmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2)
)
_WisSnmpGroups_ObjectIdentity = ObjectIdentity
wisSnmpGroups = _WisSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 1)
)
_WisBridgeGroups_ObjectIdentity = ObjectIdentity
wisBridgeGroups = _WisBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 2)
)

# Managed Objects groups

wisORInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 1, 1)
)
wisORInfoGroup.setObjects(
      *(("WIS-MIB", "wisORID"),
        ("WIS-MIB", "wisORDescr"))
)
if mibBuilder.loadTexts:
    wisORInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wisORCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 1, 2)
)
wisORCompliance.setObjects(
    ("WIS-MIB", "wisORInfoGroup")
)
if mibBuilder.loadTexts:
    wisORCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WIS-MIB",
    **{"wis": wis,
       "wisMIB": wisMIB,
       "wisORTable": wisORTable,
       "wisOREntry": wisOREntry,
       "wisORIndex": wisORIndex,
       "wisORID": wisORID,
       "wisORDescr": wisORDescr,
       "wisSnmpInfo": wisSnmpInfo,
       "wisSnmpGroups": wisSnmpGroups,
       "wisORInfoGroup": wisORInfoGroup,
       "wisORCompliance": wisORCompliance,
       "wisBridgeGroups": wisBridgeGroups}
)
