# SNMP MIB module (EdgeSwitch-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\edgeswitch\EdgeSwitch-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:03 2025
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathInventory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fastPathInventory.setRevisions(
        ("2013-10-15 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2004-10-28 20:37",
         "2003-05-26 19:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("unsassigned", 1),
          ("assigned", 2))
    )



class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_AgentInventoryTraps_ObjectIdentity = ObjectIdentity
agentInventoryTraps = _AgentInventoryTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0)
)
_AgentInventoryStackGroup_ObjectIdentity = ObjectIdentity
agentInventoryStackGroup = _AgentInventoryStackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1)
)


class _AgentInventoryStackReplicateSTK_Type(Integer32):
    """Custom type agentInventoryStackReplicateSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackReplicateSTK_Type.__name__ = "Integer32"
_AgentInventoryStackReplicateSTK_Object = MibScalar
agentInventoryStackReplicateSTK = _AgentInventoryStackReplicateSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 1),
    _AgentInventoryStackReplicateSTK_Type()
)
agentInventoryStackReplicateSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackReplicateSTK.setStatus("current")


class _AgentInventoryStackReload_Type(Integer32):
    """Custom type agentInventoryStackReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackReload_Type.__name__ = "Integer32"
_AgentInventoryStackReload_Object = MibScalar
agentInventoryStackReload = _AgentInventoryStackReload_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 2),
    _AgentInventoryStackReload_Type()
)
agentInventoryStackReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackReload.setStatus("current")
_AgentInventoryStackMaxUnitNumber_Type = Unsigned32
_AgentInventoryStackMaxUnitNumber_Object = MibScalar
agentInventoryStackMaxUnitNumber = _AgentInventoryStackMaxUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 3),
    _AgentInventoryStackMaxUnitNumber_Type()
)
agentInventoryStackMaxUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackMaxUnitNumber.setStatus("current")


class _AgentInventoryStackReplicateSTKStatus_Type(Integer32):
    """Custom type agentInventoryStackReplicateSTKStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("notInProgress", 2),
          ("finishedWithSuccess", 3),
          ("finishedWithError", 4))
    )


_AgentInventoryStackReplicateSTKStatus_Type.__name__ = "Integer32"
_AgentInventoryStackReplicateSTKStatus_Object = MibScalar
agentInventoryStackReplicateSTKStatus = _AgentInventoryStackReplicateSTKStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 4),
    _AgentInventoryStackReplicateSTKStatus_Type()
)
agentInventoryStackReplicateSTKStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackReplicateSTKStatus.setStatus("current")


class _AgentInventoryStackSTKname_Type(Integer32):
    """Custom type agentInventoryStackSTKname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 1),
          ("image1", 2),
          ("image2", 3))
    )


_AgentInventoryStackSTKname_Type.__name__ = "Integer32"
_AgentInventoryStackSTKname_Object = MibScalar
agentInventoryStackSTKname = _AgentInventoryStackSTKname_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 5),
    _AgentInventoryStackSTKname_Type()
)
agentInventoryStackSTKname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackSTKname.setStatus("current")


class _AgentInventoryStackActivateSTK_Type(Integer32):
    """Custom type agentInventoryStackActivateSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackActivateSTK_Type.__name__ = "Integer32"
_AgentInventoryStackActivateSTK_Object = MibScalar
agentInventoryStackActivateSTK = _AgentInventoryStackActivateSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 6),
    _AgentInventoryStackActivateSTK_Type()
)
agentInventoryStackActivateSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackActivateSTK.setStatus("current")


class _AgentInventoryStackDeleteSTK_Type(Integer32):
    """Custom type agentInventoryStackDeleteSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackDeleteSTK_Type.__name__ = "Integer32"
_AgentInventoryStackDeleteSTK_Object = MibScalar
agentInventoryStackDeleteSTK = _AgentInventoryStackDeleteSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 7),
    _AgentInventoryStackDeleteSTK_Type()
)
agentInventoryStackDeleteSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackDeleteSTK.setStatus("current")
_AgentInventoryStackTemplateId_Type = Unsigned32
_AgentInventoryStackTemplateId_Object = MibScalar
agentInventoryStackTemplateId = _AgentInventoryStackTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 8),
    _AgentInventoryStackTemplateId_Type()
)
agentInventoryStackTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackTemplateId.setStatus("current")
_AgentInventoryUnitGroup_ObjectIdentity = ObjectIdentity
agentInventoryUnitGroup = _AgentInventoryUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2)
)
_AgentInventorySupportedUnitTable_Object = MibTable
agentInventorySupportedUnitTable = _AgentInventorySupportedUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    agentInventorySupportedUnitTable.setStatus("current")
_AgentInventorySupportedUnitEntry_Object = MibTableRow
agentInventorySupportedUnitEntry = _AgentInventorySupportedUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1)
)
agentInventorySupportedUnitEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitIndex"),
)
if mibBuilder.loadTexts:
    agentInventorySupportedUnitEntry.setStatus("current")


class _AgentInventorySupportedUnitIndex_Type(Unsigned32):
    """Custom type agentInventorySupportedUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgentInventorySupportedUnitIndex_Type.__name__ = "Unsigned32"
_AgentInventorySupportedUnitIndex_Object = MibTableColumn
agentInventorySupportedUnitIndex = _AgentInventorySupportedUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 1),
    _AgentInventorySupportedUnitIndex_Type()
)
agentInventorySupportedUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventorySupportedUnitIndex.setStatus("current")
_AgentInventorySupportedUnitModelIdentifier_Type = DisplayString
_AgentInventorySupportedUnitModelIdentifier_Object = MibTableColumn
agentInventorySupportedUnitModelIdentifier = _AgentInventorySupportedUnitModelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 4),
    _AgentInventorySupportedUnitModelIdentifier_Type()
)
agentInventorySupportedUnitModelIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySupportedUnitModelIdentifier.setStatus("current")


class _AgentInventorySupportedUnitDescription_Type(DisplayString):
    """Custom type agentInventorySupportedUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AgentInventorySupportedUnitDescription_Type.__name__ = "DisplayString"
_AgentInventorySupportedUnitDescription_Object = MibTableColumn
agentInventorySupportedUnitDescription = _AgentInventorySupportedUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 5),
    _AgentInventorySupportedUnitDescription_Type()
)
agentInventorySupportedUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySupportedUnitDescription.setStatus("current")
_AgentInventorySupportedUnitExpectedCodeVer_Type = DisplayString
_AgentInventorySupportedUnitExpectedCodeVer_Object = MibTableColumn
agentInventorySupportedUnitExpectedCodeVer = _AgentInventorySupportedUnitExpectedCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 6),
    _AgentInventorySupportedUnitExpectedCodeVer_Type()
)
agentInventorySupportedUnitExpectedCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySupportedUnitExpectedCodeVer.setStatus("obsolete")
_AgentInventoryUnitTable_Object = MibTable
agentInventoryUnitTable = _AgentInventoryUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2)
)
if mibBuilder.loadTexts:
    agentInventoryUnitTable.setStatus("current")
_AgentInventoryUnitEntry_Object = MibTableRow
agentInventoryUnitEntry = _AgentInventoryUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1)
)
agentInventoryUnitEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"),
)
if mibBuilder.loadTexts:
    agentInventoryUnitEntry.setStatus("current")
_AgentInventoryUnitNumber_Type = Unsigned32
_AgentInventoryUnitNumber_Object = MibTableColumn
agentInventoryUnitNumber = _AgentInventoryUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 1),
    _AgentInventoryUnitNumber_Type()
)
agentInventoryUnitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryUnitNumber.setStatus("current")
_AgentInventoryUnitAssignNumber_Type = Unsigned32
_AgentInventoryUnitAssignNumber_Object = MibTableColumn
agentInventoryUnitAssignNumber = _AgentInventoryUnitAssignNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 2),
    _AgentInventoryUnitAssignNumber_Type()
)
agentInventoryUnitAssignNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitAssignNumber.setStatus("current")
_AgentInventoryUnitType_Type = AgentInventoryUnitType
_AgentInventoryUnitType_Object = MibTableColumn
agentInventoryUnitType = _AgentInventoryUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 3),
    _AgentInventoryUnitType_Type()
)
agentInventoryUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitType.setStatus("current")
_AgentInventoryUnitSupportedUnitIndex_Type = Unsigned32
_AgentInventoryUnitSupportedUnitIndex_Object = MibTableColumn
agentInventoryUnitSupportedUnitIndex = _AgentInventoryUnitSupportedUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 4),
    _AgentInventoryUnitSupportedUnitIndex_Type()
)
agentInventoryUnitSupportedUnitIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitSupportedUnitIndex.setStatus("current")


class _AgentInventoryUnitMgmtAdmin_Type(Integer32):
    """Custom type agentInventoryUnitMgmtAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmtUnit", 1),
          ("stackUnit", 2),
          ("mgmtUnassigned", 3))
    )


_AgentInventoryUnitMgmtAdmin_Type.__name__ = "Integer32"
_AgentInventoryUnitMgmtAdmin_Object = MibTableColumn
agentInventoryUnitMgmtAdmin = _AgentInventoryUnitMgmtAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 6),
    _AgentInventoryUnitMgmtAdmin_Type()
)
agentInventoryUnitMgmtAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitMgmtAdmin.setStatus("current")
_AgentInventoryUnitHWMgmtPref_Type = AgentInventoryUnitPreference
_AgentInventoryUnitHWMgmtPref_Object = MibTableColumn
agentInventoryUnitHWMgmtPref = _AgentInventoryUnitHWMgmtPref_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 7),
    _AgentInventoryUnitHWMgmtPref_Type()
)
agentInventoryUnitHWMgmtPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitHWMgmtPref.setStatus("obsolete")


class _AgentInventoryUnitHWMgmtPrefValue_Type(Unsigned32):
    """Custom type agentInventoryUnitHWMgmtPrefValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_AgentInventoryUnitHWMgmtPrefValue_Type.__name__ = "Unsigned32"
_AgentInventoryUnitHWMgmtPrefValue_Object = MibTableColumn
agentInventoryUnitHWMgmtPrefValue = _AgentInventoryUnitHWMgmtPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 8),
    _AgentInventoryUnitHWMgmtPrefValue_Type()
)
agentInventoryUnitHWMgmtPrefValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitHWMgmtPrefValue.setStatus("obsolete")
_AgentInventoryUnitAdminMgmtPref_Type = AgentInventoryUnitPreference
_AgentInventoryUnitAdminMgmtPref_Object = MibTableColumn
agentInventoryUnitAdminMgmtPref = _AgentInventoryUnitAdminMgmtPref_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 9),
    _AgentInventoryUnitAdminMgmtPref_Type()
)
agentInventoryUnitAdminMgmtPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitAdminMgmtPref.setStatus("obsolete")


class _AgentInventoryUnitAdminMgmtPrefValue_Type(Unsigned32):
    """Custom type agentInventoryUnitAdminMgmtPrefValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_AgentInventoryUnitAdminMgmtPrefValue_Type.__name__ = "Unsigned32"
_AgentInventoryUnitAdminMgmtPrefValue_Object = MibTableColumn
agentInventoryUnitAdminMgmtPrefValue = _AgentInventoryUnitAdminMgmtPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 10),
    _AgentInventoryUnitAdminMgmtPrefValue_Type()
)
agentInventoryUnitAdminMgmtPrefValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitAdminMgmtPrefValue.setStatus("obsolete")


class _AgentInventoryUnitStatus_Type(Integer32):
    """Custom type agentInventoryUnitStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unsupported", 2),
          ("codeMismatch", 3),
          ("configMismatch", 4),
          ("sdmMismatch", 5),
          ("notPresent", 6),
          ("codeUpdate", 7),
          ("stmMismatch", 8))
    )


_AgentInventoryUnitStatus_Type.__name__ = "Integer32"
_AgentInventoryUnitStatus_Object = MibTableColumn
agentInventoryUnitStatus = _AgentInventoryUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 11),
    _AgentInventoryUnitStatus_Type()
)
agentInventoryUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitStatus.setStatus("current")
_AgentInventoryUnitDetectedCodeVer_Type = DisplayString
_AgentInventoryUnitDetectedCodeVer_Object = MibTableColumn
agentInventoryUnitDetectedCodeVer = _AgentInventoryUnitDetectedCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 12),
    _AgentInventoryUnitDetectedCodeVer_Type()
)
agentInventoryUnitDetectedCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitDetectedCodeVer.setStatus("current")
_AgentInventoryUnitDetectedCodeInFlashVer_Type = DisplayString
_AgentInventoryUnitDetectedCodeInFlashVer_Object = MibTableColumn
agentInventoryUnitDetectedCodeInFlashVer = _AgentInventoryUnitDetectedCodeInFlashVer_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 13),
    _AgentInventoryUnitDetectedCodeInFlashVer_Type()
)
agentInventoryUnitDetectedCodeInFlashVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitDetectedCodeInFlashVer.setStatus("current")
_AgentInventoryUnitUpTime_Type = TimeTicks
_AgentInventoryUnitUpTime_Object = MibTableColumn
agentInventoryUnitUpTime = _AgentInventoryUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 14),
    _AgentInventoryUnitUpTime_Type()
)
agentInventoryUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitUpTime.setStatus("current")


class _AgentInventoryUnitDescription_Type(DisplayString):
    """Custom type agentInventoryUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AgentInventoryUnitDescription_Type.__name__ = "DisplayString"
_AgentInventoryUnitDescription_Object = MibTableColumn
agentInventoryUnitDescription = _AgentInventoryUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 15),
    _AgentInventoryUnitDescription_Type()
)
agentInventoryUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitDescription.setStatus("current")


class _AgentInventoryUnitReplicateSTK_Type(Integer32):
    """Custom type agentInventoryUnitReplicateSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryUnitReplicateSTK_Type.__name__ = "Integer32"
_AgentInventoryUnitReplicateSTK_Object = MibTableColumn
agentInventoryUnitReplicateSTK = _AgentInventoryUnitReplicateSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 16),
    _AgentInventoryUnitReplicateSTK_Type()
)
agentInventoryUnitReplicateSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitReplicateSTK.setStatus("current")


class _AgentInventoryUnitReload_Type(Integer32):
    """Custom type agentInventoryUnitReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryUnitReload_Type.__name__ = "Integer32"
_AgentInventoryUnitReload_Object = MibTableColumn
agentInventoryUnitReload = _AgentInventoryUnitReload_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 17),
    _AgentInventoryUnitReload_Type()
)
agentInventoryUnitReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitReload.setStatus("current")
_AgentInventoryUnitRowStatus_Type = RowStatus
_AgentInventoryUnitRowStatus_Object = MibTableColumn
agentInventoryUnitRowStatus = _AgentInventoryUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 18),
    _AgentInventoryUnitRowStatus_Type()
)
agentInventoryUnitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInventoryUnitRowStatus.setStatus("current")
_AgentInventoryUnitSerialNumber_Type = DisplayString
_AgentInventoryUnitSerialNumber_Object = MibTableColumn
agentInventoryUnitSerialNumber = _AgentInventoryUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 19),
    _AgentInventoryUnitSerialNumber_Type()
)
agentInventoryUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitSerialNumber.setStatus("current")


class _AgentInventoryUnitImage1Version_Type(DisplayString):
    """Custom type agentInventoryUnitImage1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AgentInventoryUnitImage1Version_Type.__name__ = "DisplayString"
_AgentInventoryUnitImage1Version_Object = MibTableColumn
agentInventoryUnitImage1Version = _AgentInventoryUnitImage1Version_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 20),
    _AgentInventoryUnitImage1Version_Type()
)
agentInventoryUnitImage1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitImage1Version.setStatus("current")


class _AgentInventoryUnitImage2Version_Type(DisplayString):
    """Custom type agentInventoryUnitImage2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AgentInventoryUnitImage2Version_Type.__name__ = "DisplayString"
_AgentInventoryUnitImage2Version_Object = MibTableColumn
agentInventoryUnitImage2Version = _AgentInventoryUnitImage2Version_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 21),
    _AgentInventoryUnitImage2Version_Type()
)
agentInventoryUnitImage2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitImage2Version.setStatus("current")


class _AgentInventoryUnitSTKname_Type(Integer32):
    """Custom type agentInventoryUnitSTKname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3))
    )


_AgentInventoryUnitSTKname_Type.__name__ = "Integer32"
_AgentInventoryUnitSTKname_Object = MibTableColumn
agentInventoryUnitSTKname = _AgentInventoryUnitSTKname_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 22),
    _AgentInventoryUnitSTKname_Type()
)
agentInventoryUnitSTKname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitSTKname.setStatus("current")


class _AgentInventoryUnitActivateSTK_Type(Integer32):
    """Custom type agentInventoryUnitActivateSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryUnitActivateSTK_Type.__name__ = "Integer32"
_AgentInventoryUnitActivateSTK_Object = MibTableColumn
agentInventoryUnitActivateSTK = _AgentInventoryUnitActivateSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 23),
    _AgentInventoryUnitActivateSTK_Type()
)
agentInventoryUnitActivateSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitActivateSTK.setStatus("current")


class _AgentInventoryUnitDeleteSTK_Type(Integer32):
    """Custom type agentInventoryUnitDeleteSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryUnitDeleteSTK_Type.__name__ = "Integer32"
_AgentInventoryUnitDeleteSTK_Object = MibTableColumn
agentInventoryUnitDeleteSTK = _AgentInventoryUnitDeleteSTK_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 24),
    _AgentInventoryUnitDeleteSTK_Type()
)
agentInventoryUnitDeleteSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitDeleteSTK.setStatus("current")


class _AgentInventoryUnitReplicateSTKStatus_Type(Integer32):
    """Custom type agentInventoryUnitReplicateSTKStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("notInProgress", 2),
          ("finishedWithSuccess", 3),
          ("finishedWithError", 4))
    )


_AgentInventoryUnitReplicateSTKStatus_Type.__name__ = "Integer32"
_AgentInventoryUnitReplicateSTKStatus_Object = MibTableColumn
agentInventoryUnitReplicateSTKStatus = _AgentInventoryUnitReplicateSTKStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 25),
    _AgentInventoryUnitReplicateSTKStatus_Type()
)
agentInventoryUnitReplicateSTKStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitReplicateSTKStatus.setStatus("current")


class _AgentInventoryUnitStandby_Type(Integer32):
    """Custom type agentInventoryUnitStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 1),
          ("standby-opr", 2),
          ("standby-cfg", 3))
    )


_AgentInventoryUnitStandby_Type.__name__ = "Integer32"
_AgentInventoryUnitStandby_Object = MibTableColumn
agentInventoryUnitStandby = _AgentInventoryUnitStandby_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 26),
    _AgentInventoryUnitStandby_Type()
)
agentInventoryUnitStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryUnitStandby.setStatus("current")


class _AgentInventoryUnitSFSTransferStatus_Type(Integer32):
    """Custom type agentInventoryUnitSFSTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("inProgress", 2))
    )


_AgentInventoryUnitSFSTransferStatus_Type.__name__ = "Integer32"
_AgentInventoryUnitSFSTransferStatus_Object = MibTableColumn
agentInventoryUnitSFSTransferStatus = _AgentInventoryUnitSFSTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 27),
    _AgentInventoryUnitSFSTransferStatus_Type()
)
agentInventoryUnitSFSTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitSFSTransferStatus.setStatus("current")


class _AgentInventoryUnitSFSLastAttemptStatus_Type(Integer32):
    """Custom type agentInventoryUnitSFSLastAttemptStatus based on Integer32"""
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
        *(("none", 1),
          ("success", 2),
          ("failure", 3),
          ("min-bootcode-version-not-present", 4))
    )


_AgentInventoryUnitSFSLastAttemptStatus_Type.__name__ = "Integer32"
_AgentInventoryUnitSFSLastAttemptStatus_Object = MibTableColumn
agentInventoryUnitSFSLastAttemptStatus = _AgentInventoryUnitSFSLastAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 28),
    _AgentInventoryUnitSFSLastAttemptStatus_Type()
)
agentInventoryUnitSFSLastAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryUnitSFSLastAttemptStatus.setStatus("current")
_AgentInventorySlotGroup_ObjectIdentity = ObjectIdentity
agentInventorySlotGroup = _AgentInventorySlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3)
)
_AgentInventorySlotTable_Object = MibTable
agentInventorySlotTable = _AgentInventorySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    agentInventorySlotTable.setStatus("current")
_AgentInventorySlotEntry_Object = MibTableRow
agentInventorySlotEntry = _AgentInventorySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1)
)
agentInventorySlotEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"),
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"),
)
if mibBuilder.loadTexts:
    agentInventorySlotEntry.setStatus("current")
_AgentInventorySlotNumber_Type = Unsigned32
_AgentInventorySlotNumber_Object = MibTableColumn
agentInventorySlotNumber = _AgentInventorySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 1),
    _AgentInventorySlotNumber_Type()
)
agentInventorySlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventorySlotNumber.setStatus("current")


class _AgentInventorySlotStatus_Type(Integer32):
    """Custom type agentInventorySlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("full", 2),
          ("error", 3))
    )


_AgentInventorySlotStatus_Type.__name__ = "Integer32"
_AgentInventorySlotStatus_Object = MibTableColumn
agentInventorySlotStatus = _AgentInventorySlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 3),
    _AgentInventorySlotStatus_Type()
)
agentInventorySlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySlotStatus.setStatus("current")


class _AgentInventorySlotPowerMode_Type(Integer32):
    """Custom type agentInventorySlotPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventorySlotPowerMode_Type.__name__ = "Integer32"
_AgentInventorySlotPowerMode_Object = MibTableColumn
agentInventorySlotPowerMode = _AgentInventorySlotPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 4),
    _AgentInventorySlotPowerMode_Type()
)
agentInventorySlotPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySlotPowerMode.setStatus("current")


class _AgentInventorySlotAdminMode_Type(Integer32):
    """Custom type agentInventorySlotAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventorySlotAdminMode_Type.__name__ = "Integer32"
_AgentInventorySlotAdminMode_Object = MibTableColumn
agentInventorySlotAdminMode = _AgentInventorySlotAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 5),
    _AgentInventorySlotAdminMode_Type()
)
agentInventorySlotAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySlotAdminMode.setStatus("current")
_AgentInventorySlotInsertedCardType_Type = AgentInventoryCardType
_AgentInventorySlotInsertedCardType_Object = MibTableColumn
agentInventorySlotInsertedCardType = _AgentInventorySlotInsertedCardType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 6),
    _AgentInventorySlotInsertedCardType_Type()
)
agentInventorySlotInsertedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySlotInsertedCardType.setStatus("current")
_AgentInventorySlotConfiguredCardType_Type = AgentInventoryCardType
_AgentInventorySlotConfiguredCardType_Object = MibTableColumn
agentInventorySlotConfiguredCardType = _AgentInventorySlotConfiguredCardType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 7),
    _AgentInventorySlotConfiguredCardType_Type()
)
agentInventorySlotConfiguredCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySlotConfiguredCardType.setStatus("current")


class _AgentInventorySlotCapabilities_Type(Bits):
    """Custom type agentInventorySlotCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("pluggable", 0),
          ("power-down", 1))
    )

_AgentInventorySlotCapabilities_Type.__name__ = "Bits"
_AgentInventorySlotCapabilities_Object = MibTableColumn
agentInventorySlotCapabilities = _AgentInventorySlotCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 8),
    _AgentInventorySlotCapabilities_Type()
)
agentInventorySlotCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySlotCapabilities.setStatus("current")
_AgentInventoryCardGroup_ObjectIdentity = ObjectIdentity
agentInventoryCardGroup = _AgentInventoryCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4)
)
_AgentInventoryCardTypeTable_Object = MibTable
agentInventoryCardTypeTable = _AgentInventoryCardTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    agentInventoryCardTypeTable.setStatus("current")
_AgentInventoryCardTypeEntry_Object = MibTableRow
agentInventoryCardTypeEntry = _AgentInventoryCardTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1)
)
agentInventoryCardTypeEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryCardIndex"),
)
if mibBuilder.loadTexts:
    agentInventoryCardTypeEntry.setStatus("current")
_AgentInventoryCardIndex_Type = Unsigned32
_AgentInventoryCardIndex_Object = MibTableColumn
agentInventoryCardIndex = _AgentInventoryCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 1),
    _AgentInventoryCardIndex_Type()
)
agentInventoryCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryCardIndex.setStatus("current")
_AgentInventoryCardType_Type = AgentInventoryCardType
_AgentInventoryCardType_Object = MibTableColumn
agentInventoryCardType = _AgentInventoryCardType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 2),
    _AgentInventoryCardType_Type()
)
agentInventoryCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardType.setStatus("current")
_AgentInventoryCardModelIdentifier_Type = DisplayString
_AgentInventoryCardModelIdentifier_Object = MibTableColumn
agentInventoryCardModelIdentifier = _AgentInventoryCardModelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 3),
    _AgentInventoryCardModelIdentifier_Type()
)
agentInventoryCardModelIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardModelIdentifier.setStatus("current")
_AgentInventoryCardDescription_Type = DisplayString
_AgentInventoryCardDescription_Object = MibTableColumn
agentInventoryCardDescription = _AgentInventoryCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 4),
    _AgentInventoryCardDescription_Type()
)
agentInventoryCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardDescription.setStatus("current")
_AgentInventoryComponentGroup_ObjectIdentity = ObjectIdentity
agentInventoryComponentGroup = _AgentInventoryComponentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5)
)
_AgentInventoryComponentTable_Object = MibTable
agentInventoryComponentTable = _AgentInventoryComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    agentInventoryComponentTable.setStatus("current")
_AgentInventoryComponentEntry_Object = MibTableRow
agentInventoryComponentEntry = _AgentInventoryComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1)
)
agentInventoryComponentEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryComponentIndex"),
)
if mibBuilder.loadTexts:
    agentInventoryComponentEntry.setStatus("current")
_AgentInventoryComponentIndex_Type = Unsigned32
_AgentInventoryComponentIndex_Object = MibTableColumn
agentInventoryComponentIndex = _AgentInventoryComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 1),
    _AgentInventoryComponentIndex_Type()
)
agentInventoryComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryComponentIndex.setStatus("current")
_AgentInventoryComponentMnemonic_Type = DisplayString
_AgentInventoryComponentMnemonic_Object = MibTableColumn
agentInventoryComponentMnemonic = _AgentInventoryComponentMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 2),
    _AgentInventoryComponentMnemonic_Type()
)
agentInventoryComponentMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryComponentMnemonic.setStatus("current")
_AgentInventoryComponentName_Type = DisplayString
_AgentInventoryComponentName_Object = MibTableColumn
agentInventoryComponentName = _AgentInventoryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 3),
    _AgentInventoryComponentName_Type()
)
agentInventoryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryComponentName.setStatus("current")
_FastPathInventoryConformance_ObjectIdentity = ObjectIdentity
fastPathInventoryConformance = _FastPathInventoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6)
)
_FastPathInventoryCompliances_ObjectIdentity = ObjectIdentity
fastPathInventoryCompliances = _FastPathInventoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1)
)
_FastPathInventoryGroups_ObjectIdentity = ObjectIdentity
fastPathInventoryGroups = _FastPathInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2)
)
_AgentInventoryStackPortGroup_ObjectIdentity = ObjectIdentity
agentInventoryStackPortGroup = _AgentInventoryStackPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7)
)


class _AgentInventoryStackPortIpTelephonyQOSSupport_Type(Integer32):
    """Custom type agentInventoryStackPortIpTelephonyQOSSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackPortIpTelephonyQOSSupport_Type.__name__ = "Integer32"
_AgentInventoryStackPortIpTelephonyQOSSupport_Object = MibScalar
agentInventoryStackPortIpTelephonyQOSSupport = _AgentInventoryStackPortIpTelephonyQOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 1),
    _AgentInventoryStackPortIpTelephonyQOSSupport_Type()
)
agentInventoryStackPortIpTelephonyQOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackPortIpTelephonyQOSSupport.setStatus("current")
_AgentInventoryStackPortTable_Object = MibTable
agentInventoryStackPortTable = _AgentInventoryStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2)
)
if mibBuilder.loadTexts:
    agentInventoryStackPortTable.setStatus("current")
_AgentInventoryStackPortEntry_Object = MibTableRow
agentInventoryStackPortEntry = _AgentInventoryStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1)
)
agentInventoryStackPortEntry.setIndexNames(
    (0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortIndex"),
)
if mibBuilder.loadTexts:
    agentInventoryStackPortEntry.setStatus("current")
_AgentInventoryStackPortIndex_Type = Unsigned32
_AgentInventoryStackPortIndex_Object = MibTableColumn
agentInventoryStackPortIndex = _AgentInventoryStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 1),
    _AgentInventoryStackPortIndex_Type()
)
agentInventoryStackPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryStackPortIndex.setStatus("current")
_AgentInventoryStackPortUnit_Type = Unsigned32
_AgentInventoryStackPortUnit_Object = MibTableColumn
agentInventoryStackPortUnit = _AgentInventoryStackPortUnit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 2),
    _AgentInventoryStackPortUnit_Type()
)
agentInventoryStackPortUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortUnit.setStatus("current")
_AgentInventoryStackPortTag_Type = DisplayString
_AgentInventoryStackPortTag_Object = MibTableColumn
agentInventoryStackPortTag = _AgentInventoryStackPortTag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 3),
    _AgentInventoryStackPortTag_Type()
)
agentInventoryStackPortTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortTag.setStatus("current")


class _AgentInventoryStackPortConfiguredStackMode_Type(Integer32):
    """Custom type agentInventoryStackPortConfiguredStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("ethernet", 2))
    )


_AgentInventoryStackPortConfiguredStackMode_Type.__name__ = "Integer32"
_AgentInventoryStackPortConfiguredStackMode_Object = MibTableColumn
agentInventoryStackPortConfiguredStackMode = _AgentInventoryStackPortConfiguredStackMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 4),
    _AgentInventoryStackPortConfiguredStackMode_Type()
)
agentInventoryStackPortConfiguredStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackPortConfiguredStackMode.setStatus("current")


class _AgentInventoryStackPortRunningStackMode_Type(Integer32):
    """Custom type agentInventoryStackPortRunningStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("ethernet", 2))
    )


_AgentInventoryStackPortRunningStackMode_Type.__name__ = "Integer32"
_AgentInventoryStackPortRunningStackMode_Object = MibTableColumn
agentInventoryStackPortRunningStackMode = _AgentInventoryStackPortRunningStackMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 5),
    _AgentInventoryStackPortRunningStackMode_Type()
)
agentInventoryStackPortRunningStackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortRunningStackMode.setStatus("current")


class _AgentInventoryStackPortLinkStatus_Type(Integer32):
    """Custom type agentInventoryStackPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AgentInventoryStackPortLinkStatus_Type.__name__ = "Integer32"
_AgentInventoryStackPortLinkStatus_Object = MibTableColumn
agentInventoryStackPortLinkStatus = _AgentInventoryStackPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 6),
    _AgentInventoryStackPortLinkStatus_Type()
)
agentInventoryStackPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortLinkStatus.setStatus("current")
_AgentInventoryStackPortLinkSpeed_Type = Gauge32
_AgentInventoryStackPortLinkSpeed_Object = MibTableColumn
agentInventoryStackPortLinkSpeed = _AgentInventoryStackPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 7),
    _AgentInventoryStackPortLinkSpeed_Type()
)
agentInventoryStackPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortLinkSpeed.setStatus("current")
_AgentInventoryStackPortDataRate_Type = Counter32
_AgentInventoryStackPortDataRate_Object = MibTableColumn
agentInventoryStackPortDataRate = _AgentInventoryStackPortDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 8),
    _AgentInventoryStackPortDataRate_Type()
)
agentInventoryStackPortDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortDataRate.setStatus("current")
_AgentInventoryStackPortErrorRate_Type = Counter32
_AgentInventoryStackPortErrorRate_Object = MibTableColumn
agentInventoryStackPortErrorRate = _AgentInventoryStackPortErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 9),
    _AgentInventoryStackPortErrorRate_Type()
)
agentInventoryStackPortErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortErrorRate.setStatus("current")
_AgentInventoryStackPortTotalErrors_Type = Counter32
_AgentInventoryStackPortTotalErrors_Object = MibTableColumn
agentInventoryStackPortTotalErrors = _AgentInventoryStackPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 10),
    _AgentInventoryStackPortTotalErrors_Type()
)
agentInventoryStackPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryStackPortTotalErrors.setStatus("current")
_AgentInventorySFSGroup_ObjectIdentity = ObjectIdentity
agentInventorySFSGroup = _AgentInventorySFSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8)
)
_AgentInventoryStackUnitNumber_Type = Unsigned32
_AgentInventoryStackUnitNumber_Object = MibScalar
agentInventoryStackUnitNumber = _AgentInventoryStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 1),
    _AgentInventoryStackUnitNumber_Type()
)
agentInventoryStackUnitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryStackUnitNumber.setStatus("current")


class _AgentInventorySFS_Type(Integer32):
    """Custom type agentInventorySFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventorySFS_Type.__name__ = "Integer32"
_AgentInventorySFS_Object = MibScalar
agentInventorySFS = _AgentInventorySFS_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 2),
    _AgentInventorySFS_Type()
)
agentInventorySFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySFS.setStatus("current")


class _AgentInventorySFSAllowDowngrade_Type(Integer32):
    """Custom type agentInventorySFSAllowDowngrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventorySFSAllowDowngrade_Type.__name__ = "Integer32"
_AgentInventorySFSAllowDowngrade_Object = MibScalar
agentInventorySFSAllowDowngrade = _AgentInventorySFSAllowDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 3),
    _AgentInventorySFSAllowDowngrade_Type()
)
agentInventorySFSAllowDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySFSAllowDowngrade.setStatus("current")


class _AgentInventorySFSTrap_Type(Integer32):
    """Custom type agentInventorySFSTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventorySFSTrap_Type.__name__ = "Integer32"
_AgentInventorySFSTrap_Object = MibScalar
agentInventorySFSTrap = _AgentInventorySFSTrap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 4),
    _AgentInventorySFSTrap_Type()
)
agentInventorySFSTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventorySFSTrap.setStatus("current")

# Managed Objects groups

fastPathInventorySupportedUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 1)
)
fastPathInventorySupportedUnitGroup.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitIndex"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitModelIdentifier"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitDescription"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitExpectedCodeVer"))
)
if mibBuilder.loadTexts:
    fastPathInventorySupportedUnitGroup.setStatus("current")

fastPathInventoryUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 2)
)
fastPathInventoryUnitGroup.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitAssignNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitType"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitMgmtAdmin"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitHWMgmtPref"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitAdminMgmtPref"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitStatus"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDetectedCodeVer"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDetectedCodeInFlashVer"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitUpTime"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDescription"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitReplicateSTK"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitRowStatus"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitImage1Version"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitImage2Version"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitSTKname"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitActivateSTK"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDeleteSTK"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitSTKname"))
)
if mibBuilder.loadTexts:
    fastPathInventoryUnitGroup.setStatus("current")

fastPathInventorySlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 3)
)
fastPathInventorySlotGroup.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotStatus"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotPowerMode"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotAdminMode"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
)
if mibBuilder.loadTexts:
    fastPathInventorySlotGroup.setStatus("current")

fastPathInventoryCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 4)
)
fastPathInventoryCardGroup.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardIndex"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardType"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardModelIdentifier"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardDescription"))
)
if mibBuilder.loadTexts:
    fastPathInventoryCardGroup.setStatus("current")


# Notification objects

agentInventoryCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 1)
)
agentInventoryCardMismatch.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
)
if mibBuilder.loadTexts:
    agentInventoryCardMismatch.setStatus(
        "current"
    )

agentInventoryCardUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 2)
)
agentInventoryCardUnsupported.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"))
)
if mibBuilder.loadTexts:
    agentInventoryCardUnsupported.setStatus(
        "current"
    )

agentInventoryStackPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 3)
)
agentInventoryStackPortLinkUp.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortUnit"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortTag"))
)
if mibBuilder.loadTexts:
    agentInventoryStackPortLinkUp.setStatus(
        "current"
    )

agentInventoryStackPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 4)
)
agentInventoryStackPortLinkDown.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortUnit"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortTag"))
)
if mibBuilder.loadTexts:
    agentInventoryStackPortLinkDown.setStatus(
        "current"
    )

agentInventorySFSStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 5)
)
agentInventorySFSStart.setObjects(
    ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber")
)
if mibBuilder.loadTexts:
    agentInventorySFSStart.setStatus(
        "current"
    )

agentInventorySFSComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 6)
)
agentInventorySFSComplete.setObjects(
    ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber")
)
if mibBuilder.loadTexts:
    agentInventorySFSComplete.setStatus(
        "current"
    )

agentInventorySFSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 7)
)
agentInventorySFSFail.setObjects(
    ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber")
)
if mibBuilder.loadTexts:
    agentInventorySFSFail.setStatus(
        "current"
    )


# Notifications groups

fastPathInventoryNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 5)
)
fastPathInventoryNotificationsGroup.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardMismatch"),
        ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardUnsupported"))
)
if mibBuilder.loadTexts:
    fastPathInventoryNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fastPathInventoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1, 1)
)
fastPathInventoryCompliance.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "fastPathInventorySlotGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryUnitGroup"))
)
if mibBuilder.loadTexts:
    fastPathInventoryCompliance.setStatus(
        "obsolete"
    )

fastPathInventoryCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1, 2)
)
fastPathInventoryCompliance2.setObjects(
      *(("EdgeSwitch-INVENTORY-MIB", "fastPathInventorySlotGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"),
        ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryUnitGroup"))
)
if mibBuilder.loadTexts:
    fastPathInventoryCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-INVENTORY-MIB",
    **{"AgentInventoryUnitPreference": AgentInventoryUnitPreference,
       "AgentInventoryUnitType": AgentInventoryUnitType,
       "AgentInventoryCardType": AgentInventoryCardType,
       "fastPathInventory": fastPathInventory,
       "agentInventoryTraps": agentInventoryTraps,
       "agentInventoryCardMismatch": agentInventoryCardMismatch,
       "agentInventoryCardUnsupported": agentInventoryCardUnsupported,
       "agentInventoryStackPortLinkUp": agentInventoryStackPortLinkUp,
       "agentInventoryStackPortLinkDown": agentInventoryStackPortLinkDown,
       "agentInventorySFSStart": agentInventorySFSStart,
       "agentInventorySFSComplete": agentInventorySFSComplete,
       "agentInventorySFSFail": agentInventorySFSFail,
       "agentInventoryStackGroup": agentInventoryStackGroup,
       "agentInventoryStackReplicateSTK": agentInventoryStackReplicateSTK,
       "agentInventoryStackReload": agentInventoryStackReload,
       "agentInventoryStackMaxUnitNumber": agentInventoryStackMaxUnitNumber,
       "agentInventoryStackReplicateSTKStatus": agentInventoryStackReplicateSTKStatus,
       "agentInventoryStackSTKname": agentInventoryStackSTKname,
       "agentInventoryStackActivateSTK": agentInventoryStackActivateSTK,
       "agentInventoryStackDeleteSTK": agentInventoryStackDeleteSTK,
       "agentInventoryStackTemplateId": agentInventoryStackTemplateId,
       "agentInventoryUnitGroup": agentInventoryUnitGroup,
       "agentInventorySupportedUnitTable": agentInventorySupportedUnitTable,
       "agentInventorySupportedUnitEntry": agentInventorySupportedUnitEntry,
       "agentInventorySupportedUnitIndex": agentInventorySupportedUnitIndex,
       "agentInventorySupportedUnitModelIdentifier": agentInventorySupportedUnitModelIdentifier,
       "agentInventorySupportedUnitDescription": agentInventorySupportedUnitDescription,
       "agentInventorySupportedUnitExpectedCodeVer": agentInventorySupportedUnitExpectedCodeVer,
       "agentInventoryUnitTable": agentInventoryUnitTable,
       "agentInventoryUnitEntry": agentInventoryUnitEntry,
       "agentInventoryUnitNumber": agentInventoryUnitNumber,
       "agentInventoryUnitAssignNumber": agentInventoryUnitAssignNumber,
       "agentInventoryUnitType": agentInventoryUnitType,
       "agentInventoryUnitSupportedUnitIndex": agentInventoryUnitSupportedUnitIndex,
       "agentInventoryUnitMgmtAdmin": agentInventoryUnitMgmtAdmin,
       "agentInventoryUnitHWMgmtPref": agentInventoryUnitHWMgmtPref,
       "agentInventoryUnitHWMgmtPrefValue": agentInventoryUnitHWMgmtPrefValue,
       "agentInventoryUnitAdminMgmtPref": agentInventoryUnitAdminMgmtPref,
       "agentInventoryUnitAdminMgmtPrefValue": agentInventoryUnitAdminMgmtPrefValue,
       "agentInventoryUnitStatus": agentInventoryUnitStatus,
       "agentInventoryUnitDetectedCodeVer": agentInventoryUnitDetectedCodeVer,
       "agentInventoryUnitDetectedCodeInFlashVer": agentInventoryUnitDetectedCodeInFlashVer,
       "agentInventoryUnitUpTime": agentInventoryUnitUpTime,
       "agentInventoryUnitDescription": agentInventoryUnitDescription,
       "agentInventoryUnitReplicateSTK": agentInventoryUnitReplicateSTK,
       "agentInventoryUnitReload": agentInventoryUnitReload,
       "agentInventoryUnitRowStatus": agentInventoryUnitRowStatus,
       "agentInventoryUnitSerialNumber": agentInventoryUnitSerialNumber,
       "agentInventoryUnitImage1Version": agentInventoryUnitImage1Version,
       "agentInventoryUnitImage2Version": agentInventoryUnitImage2Version,
       "agentInventoryUnitSTKname": agentInventoryUnitSTKname,
       "agentInventoryUnitActivateSTK": agentInventoryUnitActivateSTK,
       "agentInventoryUnitDeleteSTK": agentInventoryUnitDeleteSTK,
       "agentInventoryUnitReplicateSTKStatus": agentInventoryUnitReplicateSTKStatus,
       "agentInventoryUnitStandby": agentInventoryUnitStandby,
       "agentInventoryUnitSFSTransferStatus": agentInventoryUnitSFSTransferStatus,
       "agentInventoryUnitSFSLastAttemptStatus": agentInventoryUnitSFSLastAttemptStatus,
       "agentInventorySlotGroup": agentInventorySlotGroup,
       "agentInventorySlotTable": agentInventorySlotTable,
       "agentInventorySlotEntry": agentInventorySlotEntry,
       "agentInventorySlotNumber": agentInventorySlotNumber,
       "agentInventorySlotStatus": agentInventorySlotStatus,
       "agentInventorySlotPowerMode": agentInventorySlotPowerMode,
       "agentInventorySlotAdminMode": agentInventorySlotAdminMode,
       "agentInventorySlotInsertedCardType": agentInventorySlotInsertedCardType,
       "agentInventorySlotConfiguredCardType": agentInventorySlotConfiguredCardType,
       "agentInventorySlotCapabilities": agentInventorySlotCapabilities,
       "agentInventoryCardGroup": agentInventoryCardGroup,
       "agentInventoryCardTypeTable": agentInventoryCardTypeTable,
       "agentInventoryCardTypeEntry": agentInventoryCardTypeEntry,
       "agentInventoryCardIndex": agentInventoryCardIndex,
       "agentInventoryCardType": agentInventoryCardType,
       "agentInventoryCardModelIdentifier": agentInventoryCardModelIdentifier,
       "agentInventoryCardDescription": agentInventoryCardDescription,
       "agentInventoryComponentGroup": agentInventoryComponentGroup,
       "agentInventoryComponentTable": agentInventoryComponentTable,
       "agentInventoryComponentEntry": agentInventoryComponentEntry,
       "agentInventoryComponentIndex": agentInventoryComponentIndex,
       "agentInventoryComponentMnemonic": agentInventoryComponentMnemonic,
       "agentInventoryComponentName": agentInventoryComponentName,
       "fastPathInventoryConformance": fastPathInventoryConformance,
       "fastPathInventoryCompliances": fastPathInventoryCompliances,
       "fastPathInventoryCompliance": fastPathInventoryCompliance,
       "fastPathInventoryCompliance2": fastPathInventoryCompliance2,
       "fastPathInventoryGroups": fastPathInventoryGroups,
       "fastPathInventorySupportedUnitGroup": fastPathInventorySupportedUnitGroup,
       "fastPathInventoryUnitGroup": fastPathInventoryUnitGroup,
       "fastPathInventorySlotGroup": fastPathInventorySlotGroup,
       "fastPathInventoryCardGroup": fastPathInventoryCardGroup,
       "fastPathInventoryNotificationsGroup": fastPathInventoryNotificationsGroup,
       "agentInventoryStackPortGroup": agentInventoryStackPortGroup,
       "agentInventoryStackPortIpTelephonyQOSSupport": agentInventoryStackPortIpTelephonyQOSSupport,
       "agentInventoryStackPortTable": agentInventoryStackPortTable,
       "agentInventoryStackPortEntry": agentInventoryStackPortEntry,
       "agentInventoryStackPortIndex": agentInventoryStackPortIndex,
       "agentInventoryStackPortUnit": agentInventoryStackPortUnit,
       "agentInventoryStackPortTag": agentInventoryStackPortTag,
       "agentInventoryStackPortConfiguredStackMode": agentInventoryStackPortConfiguredStackMode,
       "agentInventoryStackPortRunningStackMode": agentInventoryStackPortRunningStackMode,
       "agentInventoryStackPortLinkStatus": agentInventoryStackPortLinkStatus,
       "agentInventoryStackPortLinkSpeed": agentInventoryStackPortLinkSpeed,
       "agentInventoryStackPortDataRate": agentInventoryStackPortDataRate,
       "agentInventoryStackPortErrorRate": agentInventoryStackPortErrorRate,
       "agentInventoryStackPortTotalErrors": agentInventoryStackPortTotalErrors,
       "agentInventorySFSGroup": agentInventorySFSGroup,
       "agentInventoryStackUnitNumber": agentInventoryStackUnitNumber,
       "agentInventorySFS": agentInventorySFS,
       "agentInventorySFSAllowDowngrade": agentInventorySFSAllowDowngrade,
       "agentInventorySFSTrap": agentInventorySFSTrap}
)
