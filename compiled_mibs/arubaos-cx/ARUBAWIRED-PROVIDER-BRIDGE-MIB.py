# SNMP MIB module (ARUBAWIRED-PROVIDER-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-PROVIDER-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:25 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

arubaWiredProviderBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23)
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeMIB.setRevisions(
        ("2021-11-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredProviderBridgeNotifications_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeNotifications = _ArubaWiredProviderBridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 0)
)
_ArubaWiredProviderBridgeObjects_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeObjects = _ArubaWiredProviderBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1)
)
_ArubaWiredProviderBridgeBase_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeBase = _ArubaWiredProviderBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0)
)


class _ArubaWiredProviderBridgeType_Type(Integer32):
    """Custom type arubaWiredProviderBridgeType based on Integer32"""
    defaultValue = 1

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
        *(("vlanBridge", 1),
          ("svlanBridge", 2),
          ("providerEdgeBridge", 3),
          ("vlanSvlanBridge", 4))
    )


_ArubaWiredProviderBridgeType_Type.__name__ = "Integer32"
_ArubaWiredProviderBridgeType_Object = MibScalar
arubaWiredProviderBridgeType = _ArubaWiredProviderBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 1),
    _ArubaWiredProviderBridgeType_Type()
)
arubaWiredProviderBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeType.setStatus("current")


class _ArubaWiredProviderBridgeEtherType_Type(Integer32):
    """Custom type arubaWiredProviderBridgeEtherType based on Integer32"""
    defaultValue = 34984

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_ArubaWiredProviderBridgeEtherType_Type.__name__ = "Integer32"
_ArubaWiredProviderBridgeEtherType_Object = MibScalar
arubaWiredProviderBridgeEtherType = _ArubaWiredProviderBridgeEtherType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 2),
    _ArubaWiredProviderBridgeEtherType_Type()
)
arubaWiredProviderBridgeEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeEtherType.setStatus("current")
_ArubaWiredProviderBridgeVlanTypeTable_Object = MibTable
arubaWiredProviderBridgeVlanTypeTable = _ArubaWiredProviderBridgeVlanTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 3)
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeVlanTypeTable.setStatus("current")
_ArubaWiredProviderBridgeVlanTypeEntry_Object = MibTableRow
arubaWiredProviderBridgeVlanTypeEntry = _ArubaWiredProviderBridgeVlanTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 3, 1)
)
arubaWiredProviderBridgeVlanTypeEntry.setIndexNames(
    (0, "ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgeVlanTypeVlanID"),
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeVlanTypeEntry.setStatus("current")
_ArubaWiredProviderBridgeVlanTypeVlanID_Type = VlanId
_ArubaWiredProviderBridgeVlanTypeVlanID_Object = MibTableColumn
arubaWiredProviderBridgeVlanTypeVlanID = _ArubaWiredProviderBridgeVlanTypeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 3, 1, 1),
    _ArubaWiredProviderBridgeVlanTypeVlanID_Type()
)
arubaWiredProviderBridgeVlanTypeVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeVlanTypeVlanID.setStatus("current")


class _ArubaWiredProviderBridgeVlanType_Type(Integer32):
    """Custom type arubaWiredProviderBridgeVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )


_ArubaWiredProviderBridgeVlanType_Type.__name__ = "Integer32"
_ArubaWiredProviderBridgeVlanType_Object = MibTableColumn
arubaWiredProviderBridgeVlanType = _ArubaWiredProviderBridgeVlanType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 3, 1, 2),
    _ArubaWiredProviderBridgeVlanType_Type()
)
arubaWiredProviderBridgeVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeVlanType.setStatus("current")
_ArubaWiredProviderBridgePortTable_Object = MibTable
arubaWiredProviderBridgePortTable = _ArubaWiredProviderBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 4)
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgePortTable.setStatus("current")
_ArubaWiredProviderBridgePortEntry_Object = MibTableRow
arubaWiredProviderBridgePortEntry = _ArubaWiredProviderBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 4, 1)
)
arubaWiredProviderBridgePortEntry.setIndexNames(
    (0, "ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgePortifIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgePortEntry.setStatus("current")
_ArubaWiredProviderBridgePortifIndex_Type = InterfaceIndex
_ArubaWiredProviderBridgePortifIndex_Object = MibTableColumn
arubaWiredProviderBridgePortifIndex = _ArubaWiredProviderBridgePortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 4, 1, 1),
    _ArubaWiredProviderBridgePortifIndex_Type()
)
arubaWiredProviderBridgePortifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgePortifIndex.setStatus("current")


class _ArubaWiredProviderBridgePortType_Type(Integer32):
    """Custom type arubaWiredProviderBridgePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customerEdge", 1),
          ("customerNetwork", 2),
          ("providerNetwork", 3))
    )


_ArubaWiredProviderBridgePortType_Type.__name__ = "Integer32"
_ArubaWiredProviderBridgePortType_Object = MibTableColumn
arubaWiredProviderBridgePortType = _ArubaWiredProviderBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 1, 0, 4, 1, 2),
    _ArubaWiredProviderBridgePortType_Type()
)
arubaWiredProviderBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredProviderBridgePortType.setStatus("current")
_ArubaWiredProviderBridgeConformance_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeConformance = _ArubaWiredProviderBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 2)
)
_ArubaWiredProviderBridgeCompliances_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeCompliances = _ArubaWiredProviderBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 2, 1)
)
_ArubaWiredProviderBridgeGroups_ObjectIdentity = ObjectIdentity
arubaWiredProviderBridgeGroups = _ArubaWiredProviderBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 2, 2)
)

# Managed Objects groups

arubaWiredProviderBridgeBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 2, 2, 1)
)
arubaWiredProviderBridgeBaseGroup.setObjects(
      *(("ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgeType"),
        ("ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgeEtherType"),
        ("ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgePortType"),
        ("ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgeVlanType"))
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredProviderBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23, 2, 1, 1)
)
arubaWiredProviderBridgeCompliance.setObjects(
    ("ARUBAWIRED-PROVIDER-BRIDGE-MIB", "arubaWiredProviderBridgeBaseGroup")
)
if mibBuilder.loadTexts:
    arubaWiredProviderBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-PROVIDER-BRIDGE-MIB",
    **{"arubaWiredProviderBridgeMIB": arubaWiredProviderBridgeMIB,
       "arubaWiredProviderBridgeNotifications": arubaWiredProviderBridgeNotifications,
       "arubaWiredProviderBridgeObjects": arubaWiredProviderBridgeObjects,
       "arubaWiredProviderBridgeBase": arubaWiredProviderBridgeBase,
       "arubaWiredProviderBridgeType": arubaWiredProviderBridgeType,
       "arubaWiredProviderBridgeEtherType": arubaWiredProviderBridgeEtherType,
       "arubaWiredProviderBridgeVlanTypeTable": arubaWiredProviderBridgeVlanTypeTable,
       "arubaWiredProviderBridgeVlanTypeEntry": arubaWiredProviderBridgeVlanTypeEntry,
       "arubaWiredProviderBridgeVlanTypeVlanID": arubaWiredProviderBridgeVlanTypeVlanID,
       "arubaWiredProviderBridgeVlanType": arubaWiredProviderBridgeVlanType,
       "arubaWiredProviderBridgePortTable": arubaWiredProviderBridgePortTable,
       "arubaWiredProviderBridgePortEntry": arubaWiredProviderBridgePortEntry,
       "arubaWiredProviderBridgePortifIndex": arubaWiredProviderBridgePortifIndex,
       "arubaWiredProviderBridgePortType": arubaWiredProviderBridgePortType,
       "arubaWiredProviderBridgeConformance": arubaWiredProviderBridgeConformance,
       "arubaWiredProviderBridgeCompliances": arubaWiredProviderBridgeCompliances,
       "arubaWiredProviderBridgeCompliance": arubaWiredProviderBridgeCompliance,
       "arubaWiredProviderBridgeGroups": arubaWiredProviderBridgeGroups,
       "arubaWiredProviderBridgeBaseGroup": arubaWiredProviderBridgeBaseGroup}
)
