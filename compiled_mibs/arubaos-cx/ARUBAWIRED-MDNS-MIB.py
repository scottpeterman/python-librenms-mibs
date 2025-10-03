# SNMP MIB module (ARUBAWIRED-MDNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MDNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:15 2025
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

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

arubaWiredMdnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsMIB.setRevisions(
        ("2020-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(TextualConvention, OctetString):
    status = "current"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMdnsNotifications_ObjectIdentity = ObjectIdentity
arubaWiredMdnsNotifications = _ArubaWiredMdnsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 0)
)
_ArubaWiredMdnsObjects_ObjectIdentity = ObjectIdentity
arubaWiredMdnsObjects = _ArubaWiredMdnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1)
)


class _ArubaWiredMdnsAdminState_Type(Integer32):
    """Custom type arubaWiredMdnsAdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArubaWiredMdnsAdminState_Type.__name__ = "Integer32"
_ArubaWiredMdnsAdminState_Object = MibScalar
arubaWiredMdnsAdminState = _ArubaWiredMdnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 1),
    _ArubaWiredMdnsAdminState_Type()
)
arubaWiredMdnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsAdminState.setStatus("current")
_ArubaWiredMdnsServiceTable_Object = MibTable
arubaWiredMdnsServiceTable = _ArubaWiredMdnsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceTable.setStatus("current")
_ArubaWiredMdnsServiceEntry_Object = MibTableRow
arubaWiredMdnsServiceEntry = _ArubaWiredMdnsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 2, 1)
)
arubaWiredMdnsServiceEntry.setIndexNames(
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceName"),
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceIdIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceEntry.setStatus("current")


class _ArubaWiredMdnsServiceName_Type(DisplayString):
    """Custom type arubaWiredMdnsServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArubaWiredMdnsServiceName_Type.__name__ = "DisplayString"
_ArubaWiredMdnsServiceName_Object = MibTableColumn
arubaWiredMdnsServiceName = _ArubaWiredMdnsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 2, 1, 1),
    _ArubaWiredMdnsServiceName_Type()
)
arubaWiredMdnsServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceName.setStatus("current")
_ArubaWiredMdnsServiceIdIndex_Type = Unsigned32
_ArubaWiredMdnsServiceIdIndex_Object = MibTableColumn
arubaWiredMdnsServiceIdIndex = _ArubaWiredMdnsServiceIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 2, 1, 2),
    _ArubaWiredMdnsServiceIdIndex_Type()
)
arubaWiredMdnsServiceIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceIdIndex.setStatus("current")
_ArubaWiredMdnsServiceId_Type = DisplayString
_ArubaWiredMdnsServiceId_Object = MibTableColumn
arubaWiredMdnsServiceId = _ArubaWiredMdnsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 2, 1, 3),
    _ArubaWiredMdnsServiceId_Type()
)
arubaWiredMdnsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceId.setStatus("current")
_ArubaWiredMdnsProfileTable_Object = MibTable
arubaWiredMdnsProfileTable = _ArubaWiredMdnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileTable.setStatus("current")
_ArubaWiredMdnsProfileEntry_Object = MibTableRow
arubaWiredMdnsProfileEntry = _ArubaWiredMdnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3, 1)
)
arubaWiredMdnsProfileEntry.setIndexNames(
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileName"),
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileEntry.setStatus("current")


class _ArubaWiredMdnsProfileName_Type(DisplayString):
    """Custom type arubaWiredMdnsProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArubaWiredMdnsProfileName_Type.__name__ = "DisplayString"
_ArubaWiredMdnsProfileName_Object = MibTableColumn
arubaWiredMdnsProfileName = _ArubaWiredMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3, 1, 1),
    _ArubaWiredMdnsProfileName_Type()
)
arubaWiredMdnsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileName.setStatus("current")
_ArubaWiredMdnsProfileVIDList_Type = VidList
_ArubaWiredMdnsProfileVIDList_Object = MibTableColumn
arubaWiredMdnsProfileVIDList = _ArubaWiredMdnsProfileVIDList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3, 1, 2),
    _ArubaWiredMdnsProfileVIDList_Type()
)
arubaWiredMdnsProfileVIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileVIDList.setStatus("current")


class _ArubaWiredMdnsProfilePermitCount_Type(Unsigned32):
    """Custom type arubaWiredMdnsProfilePermitCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ArubaWiredMdnsProfilePermitCount_Type.__name__ = "Unsigned32"
_ArubaWiredMdnsProfilePermitCount_Object = MibTableColumn
arubaWiredMdnsProfilePermitCount = _ArubaWiredMdnsProfilePermitCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3, 1, 3),
    _ArubaWiredMdnsProfilePermitCount_Type()
)
arubaWiredMdnsProfilePermitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfilePermitCount.setStatus("current")


class _ArubaWiredMdnsProfileDenyCount_Type(Unsigned32):
    """Custom type arubaWiredMdnsProfileDenyCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ArubaWiredMdnsProfileDenyCount_Type.__name__ = "Unsigned32"
_ArubaWiredMdnsProfileDenyCount_Object = MibTableColumn
arubaWiredMdnsProfileDenyCount = _ArubaWiredMdnsProfileDenyCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 3, 1, 4),
    _ArubaWiredMdnsProfileDenyCount_Type()
)
arubaWiredMdnsProfileDenyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileDenyCount.setStatus("current")
_ArubaWiredMdnsProfileFilterRuleTable_Object = MibTable
arubaWiredMdnsProfileFilterRuleTable = _ArubaWiredMdnsProfileFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleTable.setStatus("current")
_ArubaWiredMdnsProfileFilterRuleEntry_Object = MibTableRow
arubaWiredMdnsProfileFilterRuleEntry = _ArubaWiredMdnsProfileFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1)
)
arubaWiredMdnsProfileFilterRuleEntry.setIndexNames(
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleProfileName"),
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleEntry.setStatus("current")


class _ArubaWiredMdnsProfileFilterRuleProfileName_Type(DisplayString):
    """Custom type arubaWiredMdnsProfileFilterRuleProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArubaWiredMdnsProfileFilterRuleProfileName_Type.__name__ = "DisplayString"
_ArubaWiredMdnsProfileFilterRuleProfileName_Object = MibTableColumn
arubaWiredMdnsProfileFilterRuleProfileName = _ArubaWiredMdnsProfileFilterRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1, 1),
    _ArubaWiredMdnsProfileFilterRuleProfileName_Type()
)
arubaWiredMdnsProfileFilterRuleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleProfileName.setStatus("current")


class _ArubaWiredMdnsProfileFilterRuleIndex_Type(Integer32):
    """Custom type arubaWiredMdnsProfileFilterRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ArubaWiredMdnsProfileFilterRuleIndex_Type.__name__ = "Integer32"
_ArubaWiredMdnsProfileFilterRuleIndex_Object = MibTableColumn
arubaWiredMdnsProfileFilterRuleIndex = _ArubaWiredMdnsProfileFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1, 2),
    _ArubaWiredMdnsProfileFilterRuleIndex_Type()
)
arubaWiredMdnsProfileFilterRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleIndex.setStatus("current")


class _ArubaWiredMdnsProfileFilterRuleServiceName_Type(OctetString):
    """Custom type arubaWiredMdnsProfileFilterRuleServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredMdnsProfileFilterRuleServiceName_Type.__name__ = "OctetString"
_ArubaWiredMdnsProfileFilterRuleServiceName_Object = MibTableColumn
arubaWiredMdnsProfileFilterRuleServiceName = _ArubaWiredMdnsProfileFilterRuleServiceName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1, 3),
    _ArubaWiredMdnsProfileFilterRuleServiceName_Type()
)
arubaWiredMdnsProfileFilterRuleServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleServiceName.setStatus("current")


class _ArubaWiredMdnsProfileFilterRuleInstanceName_Type(OctetString):
    """Custom type arubaWiredMdnsProfileFilterRuleInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredMdnsProfileFilterRuleInstanceName_Type.__name__ = "OctetString"
_ArubaWiredMdnsProfileFilterRuleInstanceName_Object = MibTableColumn
arubaWiredMdnsProfileFilterRuleInstanceName = _ArubaWiredMdnsProfileFilterRuleInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1, 4),
    _ArubaWiredMdnsProfileFilterRuleInstanceName_Type()
)
arubaWiredMdnsProfileFilterRuleInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleInstanceName.setStatus("current")


class _ArubaWiredMdnsProfileFilterRuleAction_Type(Integer32):
    """Custom type arubaWiredMdnsProfileFilterRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_ArubaWiredMdnsProfileFilterRuleAction_Type.__name__ = "Integer32"
_ArubaWiredMdnsProfileFilterRuleAction_Object = MibTableColumn
arubaWiredMdnsProfileFilterRuleAction = _ArubaWiredMdnsProfileFilterRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 4, 1, 5),
    _ArubaWiredMdnsProfileFilterRuleAction_Type()
)
arubaWiredMdnsProfileFilterRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleAction.setStatus("current")
_ArubaWiredMdnsPortTable_Object = MibTable
arubaWiredMdnsPortTable = _ArubaWiredMdnsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsPortTable.setStatus("current")
_ArubaWiredMdnsPortEntry_Object = MibTableRow
arubaWiredMdnsPortEntry = _ArubaWiredMdnsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5, 1)
)
arubaWiredMdnsPortEntry.setIndexNames(
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsPortVlanId"),
)
if mibBuilder.loadTexts:
    arubaWiredMdnsPortEntry.setStatus("current")
_ArubaWiredMdnsPortVlanId_Type = VlanIndex
_ArubaWiredMdnsPortVlanId_Object = MibTableColumn
arubaWiredMdnsPortVlanId = _ArubaWiredMdnsPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5, 1, 1),
    _ArubaWiredMdnsPortVlanId_Type()
)
arubaWiredMdnsPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsPortVlanId.setStatus("current")


class _ArubaWiredMdnsPortMdnsEnabled_Type(Integer32):
    """Custom type arubaWiredMdnsPortMdnsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArubaWiredMdnsPortMdnsEnabled_Type.__name__ = "Integer32"
_ArubaWiredMdnsPortMdnsEnabled_Object = MibTableColumn
arubaWiredMdnsPortMdnsEnabled = _ArubaWiredMdnsPortMdnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5, 1, 2),
    _ArubaWiredMdnsPortMdnsEnabled_Type()
)
arubaWiredMdnsPortMdnsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsPortMdnsEnabled.setStatus("current")


class _ArubaWiredMdnsPortTxProfileName_Type(DisplayString):
    """Custom type arubaWiredMdnsPortTxProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArubaWiredMdnsPortTxProfileName_Type.__name__ = "DisplayString"
_ArubaWiredMdnsPortTxProfileName_Object = MibTableColumn
arubaWiredMdnsPortTxProfileName = _ArubaWiredMdnsPortTxProfileName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5, 1, 3),
    _ArubaWiredMdnsPortTxProfileName_Type()
)
arubaWiredMdnsPortTxProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsPortTxProfileName.setStatus("current")


class _ArubaWiredMdnsPortRxProfileName_Type(DisplayString):
    """Custom type arubaWiredMdnsPortRxProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArubaWiredMdnsPortRxProfileName_Type.__name__ = "DisplayString"
_ArubaWiredMdnsPortRxProfileName_Object = MibTableColumn
arubaWiredMdnsPortRxProfileName = _ArubaWiredMdnsPortRxProfileName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 5, 1, 4),
    _ArubaWiredMdnsPortRxProfileName_Type()
)
arubaWiredMdnsPortRxProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsPortRxProfileName.setStatus("current")
_ArubaWiredMdnsServiceProviderTable_Object = MibTable
arubaWiredMdnsServiceProviderTable = _ArubaWiredMdnsServiceProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6)
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderTable.setStatus("current")
_ArubaWiredMdnsServiceProviderEntry_Object = MibTableRow
arubaWiredMdnsServiceProviderEntry = _ArubaWiredMdnsServiceProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1)
)
arubaWiredMdnsServiceProviderEntry.setIndexNames(
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderServiceId"),
    (0, "ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderServiceIdIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderEntry.setStatus("current")


class _ArubaWiredMdnsServiceProviderServiceId_Type(DisplayString):
    """Custom type arubaWiredMdnsServiceProviderServiceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_ArubaWiredMdnsServiceProviderServiceId_Type.__name__ = "DisplayString"
_ArubaWiredMdnsServiceProviderServiceId_Object = MibTableColumn
arubaWiredMdnsServiceProviderServiceId = _ArubaWiredMdnsServiceProviderServiceId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 1),
    _ArubaWiredMdnsServiceProviderServiceId_Type()
)
arubaWiredMdnsServiceProviderServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderServiceId.setStatus("current")
_ArubaWiredMdnsServiceProviderServiceIdIndex_Type = Unsigned32
_ArubaWiredMdnsServiceProviderServiceIdIndex_Object = MibTableColumn
arubaWiredMdnsServiceProviderServiceIdIndex = _ArubaWiredMdnsServiceProviderServiceIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 2),
    _ArubaWiredMdnsServiceProviderServiceIdIndex_Type()
)
arubaWiredMdnsServiceProviderServiceIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderServiceIdIndex.setStatus("current")
_ArubaWiredMdnsServiceProviderServiceInstanceName_Type = DisplayString
_ArubaWiredMdnsServiceProviderServiceInstanceName_Object = MibTableColumn
arubaWiredMdnsServiceProviderServiceInstanceName = _ArubaWiredMdnsServiceProviderServiceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 3),
    _ArubaWiredMdnsServiceProviderServiceInstanceName_Type()
)
arubaWiredMdnsServiceProviderServiceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderServiceInstanceName.setStatus("current")
_ArubaWiredMdnsServiceProviderVlanId_Type = VlanIndex
_ArubaWiredMdnsServiceProviderVlanId_Object = MibTableColumn
arubaWiredMdnsServiceProviderVlanId = _ArubaWiredMdnsServiceProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 4),
    _ArubaWiredMdnsServiceProviderVlanId_Type()
)
arubaWiredMdnsServiceProviderVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderVlanId.setStatus("current")
_ArubaWiredMdnsServiceProviderMacAddress_Type = MacAddress
_ArubaWiredMdnsServiceProviderMacAddress_Object = MibTableColumn
arubaWiredMdnsServiceProviderMacAddress = _ArubaWiredMdnsServiceProviderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 5),
    _ArubaWiredMdnsServiceProviderMacAddress_Type()
)
arubaWiredMdnsServiceProviderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderMacAddress.setStatus("current")
_ArubaWiredMdnsServiceProviderHostname_Type = DisplayString
_ArubaWiredMdnsServiceProviderHostname_Object = MibTableColumn
arubaWiredMdnsServiceProviderHostname = _ArubaWiredMdnsServiceProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 6),
    _ArubaWiredMdnsServiceProviderHostname_Type()
)
arubaWiredMdnsServiceProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderHostname.setStatus("current")
_ArubaWiredMdnsServiceProviderIpAddress_Type = IpAddress
_ArubaWiredMdnsServiceProviderIpAddress_Object = MibTableColumn
arubaWiredMdnsServiceProviderIpAddress = _ArubaWiredMdnsServiceProviderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 7),
    _ArubaWiredMdnsServiceProviderIpAddress_Type()
)
arubaWiredMdnsServiceProviderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderIpAddress.setStatus("current")
_ArubaWiredMdnsServiceProviderTtl_Type = Unsigned32
_ArubaWiredMdnsServiceProviderTtl_Object = MibTableColumn
arubaWiredMdnsServiceProviderTtl = _ArubaWiredMdnsServiceProviderTtl_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 8),
    _ArubaWiredMdnsServiceProviderTtl_Type()
)
arubaWiredMdnsServiceProviderTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderTtl.setStatus("current")
_ArubaWiredMdnsServiceProviderExpireTime_Type = Unsigned32
_ArubaWiredMdnsServiceProviderExpireTime_Object = MibTableColumn
arubaWiredMdnsServiceProviderExpireTime = _ArubaWiredMdnsServiceProviderExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 1, 6, 1, 9),
    _ArubaWiredMdnsServiceProviderExpireTime_Type()
)
arubaWiredMdnsServiceProviderExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderExpireTime.setStatus("current")
_ArubaWiredMdnsConformance_ObjectIdentity = ObjectIdentity
arubaWiredMdnsConformance = _ArubaWiredMdnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2)
)
_ArubaWiredMdnsCompliances_ObjectIdentity = ObjectIdentity
arubaWiredMdnsCompliances = _ArubaWiredMdnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 1)
)
_ArubaWiredMdnsGroups_ObjectIdentity = ObjectIdentity
arubaWiredMdnsGroups = _ArubaWiredMdnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2)
)

# Managed Objects groups

arubaWiredMdnsScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 1)
)
arubaWiredMdnsScalarGroup.setObjects(
    ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsAdminState")
)
if mibBuilder.loadTexts:
    arubaWiredMdnsScalarGroup.setStatus("current")

arubaWiredMdnsServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 2)
)
arubaWiredMdnsServiceGroup.setObjects(
    ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceId")
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceGroup.setStatus("current")

arubaWiredMdnsProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 3)
)
arubaWiredMdnsProfileGroup.setObjects(
      *(("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileVIDList"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfilePermitCount"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileDenyCount"))
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileGroup.setStatus("current")

arubaWiredMdnsProfileFilterRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 4)
)
arubaWiredMdnsProfileFilterRuleGroup.setObjects(
      *(("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleServiceName"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleInstanceName"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleAction"))
)
if mibBuilder.loadTexts:
    arubaWiredMdnsProfileFilterRuleGroup.setStatus("current")

arubaWiredMdnsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 5)
)
arubaWiredMdnsPortGroup.setObjects(
      *(("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsPortMdnsEnabled"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsPortTxProfileName"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsPortRxProfileName"))
)
if mibBuilder.loadTexts:
    arubaWiredMdnsPortGroup.setStatus("current")

arubaWiredMdnsServiceProviderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 2, 6)
)
arubaWiredMdnsServiceProviderGroup.setObjects(
      *(("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderServiceInstanceName"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderVlanId"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderMacAddress"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderHostname"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderIpAddress"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderTtl"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderExpireTime"))
)
if mibBuilder.loadTexts:
    arubaWiredMdnsServiceProviderGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredMdnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14, 2, 1, 1)
)
arubaWiredMdnsCompliance.setObjects(
      *(("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsScalarGroup"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceGroup"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileGroup"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsProfileFilterRuleGroup"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsPortGroup"),
        ("ARUBAWIRED-MDNS-MIB", "arubaWiredMdnsServiceProviderGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredMdnsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MDNS-MIB",
    **{"VidList": VidList,
       "arubaWiredMdnsMIB": arubaWiredMdnsMIB,
       "arubaWiredMdnsNotifications": arubaWiredMdnsNotifications,
       "arubaWiredMdnsObjects": arubaWiredMdnsObjects,
       "arubaWiredMdnsAdminState": arubaWiredMdnsAdminState,
       "arubaWiredMdnsServiceTable": arubaWiredMdnsServiceTable,
       "arubaWiredMdnsServiceEntry": arubaWiredMdnsServiceEntry,
       "arubaWiredMdnsServiceName": arubaWiredMdnsServiceName,
       "arubaWiredMdnsServiceIdIndex": arubaWiredMdnsServiceIdIndex,
       "arubaWiredMdnsServiceId": arubaWiredMdnsServiceId,
       "arubaWiredMdnsProfileTable": arubaWiredMdnsProfileTable,
       "arubaWiredMdnsProfileEntry": arubaWiredMdnsProfileEntry,
       "arubaWiredMdnsProfileName": arubaWiredMdnsProfileName,
       "arubaWiredMdnsProfileVIDList": arubaWiredMdnsProfileVIDList,
       "arubaWiredMdnsProfilePermitCount": arubaWiredMdnsProfilePermitCount,
       "arubaWiredMdnsProfileDenyCount": arubaWiredMdnsProfileDenyCount,
       "arubaWiredMdnsProfileFilterRuleTable": arubaWiredMdnsProfileFilterRuleTable,
       "arubaWiredMdnsProfileFilterRuleEntry": arubaWiredMdnsProfileFilterRuleEntry,
       "arubaWiredMdnsProfileFilterRuleProfileName": arubaWiredMdnsProfileFilterRuleProfileName,
       "arubaWiredMdnsProfileFilterRuleIndex": arubaWiredMdnsProfileFilterRuleIndex,
       "arubaWiredMdnsProfileFilterRuleServiceName": arubaWiredMdnsProfileFilterRuleServiceName,
       "arubaWiredMdnsProfileFilterRuleInstanceName": arubaWiredMdnsProfileFilterRuleInstanceName,
       "arubaWiredMdnsProfileFilterRuleAction": arubaWiredMdnsProfileFilterRuleAction,
       "arubaWiredMdnsPortTable": arubaWiredMdnsPortTable,
       "arubaWiredMdnsPortEntry": arubaWiredMdnsPortEntry,
       "arubaWiredMdnsPortVlanId": arubaWiredMdnsPortVlanId,
       "arubaWiredMdnsPortMdnsEnabled": arubaWiredMdnsPortMdnsEnabled,
       "arubaWiredMdnsPortTxProfileName": arubaWiredMdnsPortTxProfileName,
       "arubaWiredMdnsPortRxProfileName": arubaWiredMdnsPortRxProfileName,
       "arubaWiredMdnsServiceProviderTable": arubaWiredMdnsServiceProviderTable,
       "arubaWiredMdnsServiceProviderEntry": arubaWiredMdnsServiceProviderEntry,
       "arubaWiredMdnsServiceProviderServiceId": arubaWiredMdnsServiceProviderServiceId,
       "arubaWiredMdnsServiceProviderServiceIdIndex": arubaWiredMdnsServiceProviderServiceIdIndex,
       "arubaWiredMdnsServiceProviderServiceInstanceName": arubaWiredMdnsServiceProviderServiceInstanceName,
       "arubaWiredMdnsServiceProviderVlanId": arubaWiredMdnsServiceProviderVlanId,
       "arubaWiredMdnsServiceProviderMacAddress": arubaWiredMdnsServiceProviderMacAddress,
       "arubaWiredMdnsServiceProviderHostname": arubaWiredMdnsServiceProviderHostname,
       "arubaWiredMdnsServiceProviderIpAddress": arubaWiredMdnsServiceProviderIpAddress,
       "arubaWiredMdnsServiceProviderTtl": arubaWiredMdnsServiceProviderTtl,
       "arubaWiredMdnsServiceProviderExpireTime": arubaWiredMdnsServiceProviderExpireTime,
       "arubaWiredMdnsConformance": arubaWiredMdnsConformance,
       "arubaWiredMdnsCompliances": arubaWiredMdnsCompliances,
       "arubaWiredMdnsCompliance": arubaWiredMdnsCompliance,
       "arubaWiredMdnsGroups": arubaWiredMdnsGroups,
       "arubaWiredMdnsScalarGroup": arubaWiredMdnsScalarGroup,
       "arubaWiredMdnsServiceGroup": arubaWiredMdnsServiceGroup,
       "arubaWiredMdnsProfileGroup": arubaWiredMdnsProfileGroup,
       "arubaWiredMdnsProfileFilterRuleGroup": arubaWiredMdnsProfileFilterRuleGroup,
       "arubaWiredMdnsPortGroup": arubaWiredMdnsPortGroup,
       "arubaWiredMdnsServiceProviderGroup": arubaWiredMdnsServiceProviderGroup}
)
