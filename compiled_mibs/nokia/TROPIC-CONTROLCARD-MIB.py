# SNMP MIB module (TROPIC-CONTROLCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-CONTROLCARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:26 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnCardModules,
 tnControlCardMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardModules",
    "tnControlCardMIB")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")


# MODULE-IDENTITY

tnControlCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tnControlCardMibModule.setRevisions(
        ("2018-02-23 12:00",
         "2017-07-07 12:00",
         "2016-11-16 12:00",
         "2014-09-04 12:00",
         "2013-05-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnControlCardConf_ObjectIdentity = ObjectIdentity
tnControlCardConf = _TnControlCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1)
)
_TnControlCardGroups_ObjectIdentity = ObjectIdentity
tnControlCardGroups = _TnControlCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1)
)
_TnControlCardCompliances_ObjectIdentity = ObjectIdentity
tnControlCardCompliances = _TnControlCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 2)
)
_TnControlCardObjs_ObjectIdentity = ObjectIdentity
tnControlCardObjs = _TnControlCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2)
)
_TnControlCardTotal_Type = Integer32
_TnControlCardTotal_Object = MibScalar
tnControlCardTotal = _TnControlCardTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 1),
    _TnControlCardTotal_Type()
)
tnControlCardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnControlCardTotal.setStatus("current")
_TnControlCardTable_Object = MibTable
tnControlCardTable = _TnControlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tnControlCardTable.setStatus("current")
_TnControlCardEntry_Object = MibTableRow
tnControlCardEntry = _TnControlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 2, 1)
)
tnControlCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnControlCardEntry.setStatus("current")


class _TnControlCardActivityState_Type(Integer32):
    """Custom type tnControlCardActivityState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3),
          ("unequipped", 4))
    )


_TnControlCardActivityState_Type.__name__ = "Integer32"
_TnControlCardActivityState_Object = MibTableColumn
tnControlCardActivityState = _TnControlCardActivityState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 2, 1, 1),
    _TnControlCardActivityState_Type()
)
tnControlCardActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnControlCardActivityState.setStatus("current")
_TnRedundancyDemeritTable_Object = MibTable
tnRedundancyDemeritTable = _TnRedundancyDemeritTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    tnRedundancyDemeritTable.setStatus("current")
_TnRedundancyDemeritEntry_Object = MibTableRow
tnRedundancyDemeritEntry = _TnRedundancyDemeritEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3, 1)
)
tnRedundancyDemeritEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-CONTROLCARD-MIB", "tnRedundancyDemeritId"),
)
if mibBuilder.loadTexts:
    tnRedundancyDemeritEntry.setStatus("current")
_TnRedundancyDemeritId_Type = Unsigned32
_TnRedundancyDemeritId_Object = MibTableColumn
tnRedundancyDemeritId = _TnRedundancyDemeritId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3, 1, 1),
    _TnRedundancyDemeritId_Type()
)
tnRedundancyDemeritId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRedundancyDemeritId.setStatus("current")


class _TnRedundancyDemeritName_Type(SnmpAdminString):
    """Custom type tnRedundancyDemeritName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnRedundancyDemeritName_Type.__name__ = "SnmpAdminString"
_TnRedundancyDemeritName_Object = MibTableColumn
tnRedundancyDemeritName = _TnRedundancyDemeritName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3, 1, 2),
    _TnRedundancyDemeritName_Type()
)
tnRedundancyDemeritName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRedundancyDemeritName.setStatus("current")
_TnRedundancyDemeritRaised_Type = TruthValue
_TnRedundancyDemeritRaised_Object = MibTableColumn
tnRedundancyDemeritRaised = _TnRedundancyDemeritRaised_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3, 1, 3),
    _TnRedundancyDemeritRaised_Type()
)
tnRedundancyDemeritRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRedundancyDemeritRaised.setStatus("current")
_TnRedundancyDemeritValue_Type = Unsigned32
_TnRedundancyDemeritValue_Object = MibTableColumn
tnRedundancyDemeritValue = _TnRedundancyDemeritValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 3, 1, 4),
    _TnRedundancyDemeritValue_Type()
)
tnRedundancyDemeritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRedundancyDemeritValue.setStatus("current")
_TnVwmEcCardAttributeTotal_Type = Integer32
_TnVwmEcCardAttributeTotal_Object = MibScalar
tnVwmEcCardAttributeTotal = _TnVwmEcCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 4),
    _TnVwmEcCardAttributeTotal_Type()
)
tnVwmEcCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmEcCardAttributeTotal.setStatus("current")
_TnVwmEcCardTable_Object = MibTable
tnVwmEcCardTable = _TnVwmEcCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    tnVwmEcCardTable.setStatus("current")
_TnVwmEcCardEntry_Object = MibTableRow
tnVwmEcCardEntry = _TnVwmEcCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 5, 1)
)
tnVwmEcCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmEcCardEntry.setStatus("current")


class _TnVwmEcCardConnectTo_Type(InterfaceIndexOrZero):
    """Custom type tnVwmEcCardConnectTo based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnVwmEcCardConnectTo_Type.__name__ = "InterfaceIndexOrZero"
_TnVwmEcCardConnectTo_Object = MibTableColumn
tnVwmEcCardConnectTo = _TnVwmEcCardConnectTo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 5, 1, 1),
    _TnVwmEcCardConnectTo_Type()
)
tnVwmEcCardConnectTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmEcCardConnectTo.setStatus("current")


class _TnVwmEcCardClipOnId_Type(Unsigned32):
    """Custom type tnVwmEcCardClipOnId based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnVwmEcCardClipOnId_Type.__name__ = "Unsigned32"
_TnVwmEcCardClipOnId_Object = MibTableColumn
tnVwmEcCardClipOnId = _TnVwmEcCardClipOnId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 2, 5, 1, 2),
    _TnVwmEcCardClipOnId_Type()
)
tnVwmEcCardClipOnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmEcCardClipOnId.setStatus("current")

# Managed Objects groups

tnControlCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1, 1)
)
tnControlCardScalarsGroup.setObjects(
    ("TROPIC-CONTROLCARD-MIB", "tnControlCardTotal")
)
if mibBuilder.loadTexts:
    tnControlCardScalarsGroup.setStatus("current")

tnControlCardTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1, 2)
)
tnControlCardTableGroup.setObjects(
    ("TROPIC-CONTROLCARD-MIB", "tnControlCardActivityState")
)
if mibBuilder.loadTexts:
    tnControlCardTableGroup.setStatus("current")

tnRedundancyDemeritTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1, 3)
)
tnRedundancyDemeritTableGroup.setObjects(
      *(("TROPIC-CONTROLCARD-MIB", "tnRedundancyDemeritName"),
        ("TROPIC-CONTROLCARD-MIB", "tnRedundancyDemeritRaised"),
        ("TROPIC-CONTROLCARD-MIB", "tnRedundancyDemeritValue"))
)
if mibBuilder.loadTexts:
    tnRedundancyDemeritTableGroup.setStatus("current")

tnVwmEcCardTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1, 4)
)
tnVwmEcCardTableGroup.setObjects(
      *(("TROPIC-CONTROLCARD-MIB", "tnVwmEcCardConnectTo"),
        ("TROPIC-CONTROLCARD-MIB", "tnVwmEcCardClipOnId"))
)
if mibBuilder.loadTexts:
    tnVwmEcCardTableGroup.setStatus("current")

tnVwmEcCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 1, 5)
)
tnVwmEcCardScalarsGroup.setObjects(
    ("TROPIC-CONTROLCARD-MIB", "tnVwmEcCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnVwmEcCardScalarsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnControlCardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3, 1, 2, 1)
)
tnControlCardCompliance.setObjects(
      *(("TROPIC-CONTROLCARD-MIB", "tnControlCardScalarsGroup"),
        ("TROPIC-CONTROLCARD-MIB", "tnControlCardTableGroup"),
        ("TROPIC-CONTROLCARD-MIB", "tnRedundancyDemeritTableGroup"),
        ("TROPIC-CONTROLCARD-MIB", "tnVwmEcCardTableGroup"),
        ("TROPIC-CONTROLCARD-MIB", "tnVwmEcCardScalarsGroup"))
)
if mibBuilder.loadTexts:
    tnControlCardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-CONTROLCARD-MIB",
    **{"tnControlCardMibModule": tnControlCardMibModule,
       "tnControlCardConf": tnControlCardConf,
       "tnControlCardGroups": tnControlCardGroups,
       "tnControlCardScalarsGroup": tnControlCardScalarsGroup,
       "tnControlCardTableGroup": tnControlCardTableGroup,
       "tnRedundancyDemeritTableGroup": tnRedundancyDemeritTableGroup,
       "tnVwmEcCardTableGroup": tnVwmEcCardTableGroup,
       "tnVwmEcCardScalarsGroup": tnVwmEcCardScalarsGroup,
       "tnControlCardCompliances": tnControlCardCompliances,
       "tnControlCardCompliance": tnControlCardCompliance,
       "tnControlCardObjs": tnControlCardObjs,
       "tnControlCardTotal": tnControlCardTotal,
       "tnControlCardTable": tnControlCardTable,
       "tnControlCardEntry": tnControlCardEntry,
       "tnControlCardActivityState": tnControlCardActivityState,
       "tnRedundancyDemeritTable": tnRedundancyDemeritTable,
       "tnRedundancyDemeritEntry": tnRedundancyDemeritEntry,
       "tnRedundancyDemeritId": tnRedundancyDemeritId,
       "tnRedundancyDemeritName": tnRedundancyDemeritName,
       "tnRedundancyDemeritRaised": tnRedundancyDemeritRaised,
       "tnRedundancyDemeritValue": tnRedundancyDemeritValue,
       "tnVwmEcCardAttributeTotal": tnVwmEcCardAttributeTotal,
       "tnVwmEcCardTable": tnVwmEcCardTable,
       "tnVwmEcCardEntry": tnVwmEcCardEntry,
       "tnVwmEcCardConnectTo": tnVwmEcCardConnectTo,
       "tnVwmEcCardClipOnId": tnVwmEcCardClipOnId}
)
