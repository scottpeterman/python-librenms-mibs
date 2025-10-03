# SNMP MIB module (NBS-META-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-META-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:19 2025
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

nbsMetaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsMetaMibGrp_ObjectIdentity = ObjectIdentity
nbsMetaMibGrp = _NbsMetaMibGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 205, 1)
)
if mibBuilder.loadTexts:
    nbsMetaMibGrp.setStatus("current")
_NbsMetaMibFeatureTableSize_Type = Integer32
_NbsMetaMibFeatureTableSize_Object = MibScalar
nbsMetaMibFeatureTableSize = _NbsMetaMibFeatureTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 1),
    _NbsMetaMibFeatureTableSize_Type()
)
nbsMetaMibFeatureTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureTableSize.setStatus("current")
_NbsMetaMibFeatureTable_Object = MibTable
nbsMetaMibFeatureTable = _NbsMetaMibFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2)
)
if mibBuilder.loadTexts:
    nbsMetaMibFeatureTable.setStatus("current")
_NbsMetaMibFeatureEntry_Object = MibTableRow
nbsMetaMibFeatureEntry = _NbsMetaMibFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1)
)
nbsMetaMibFeatureEntry.setIndexNames(
    (0, "NBS-META-MIB", "nbsMetaMibFeatureID"),
)
if mibBuilder.loadTexts:
    nbsMetaMibFeatureEntry.setStatus("current")
_NbsMetaMibFeatureID_Type = Integer32
_NbsMetaMibFeatureID_Object = MibTableColumn
nbsMetaMibFeatureID = _NbsMetaMibFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 1),
    _NbsMetaMibFeatureID_Type()
)
nbsMetaMibFeatureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureID.setStatus("current")


class _NbsMetaMibFeatureFamily_Type(DisplayString):
    """Custom type nbsMetaMibFeatureFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsMetaMibFeatureFamily_Type.__name__ = "DisplayString"
_NbsMetaMibFeatureFamily_Object = MibTableColumn
nbsMetaMibFeatureFamily = _NbsMetaMibFeatureFamily_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 2),
    _NbsMetaMibFeatureFamily_Type()
)
nbsMetaMibFeatureFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureFamily.setStatus("current")


class _NbsMetaMibFeatureName_Type(DisplayString):
    """Custom type nbsMetaMibFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsMetaMibFeatureName_Type.__name__ = "DisplayString"
_NbsMetaMibFeatureName_Object = MibTableColumn
nbsMetaMibFeatureName = _NbsMetaMibFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 3),
    _NbsMetaMibFeatureName_Type()
)
nbsMetaMibFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureName.setStatus("current")
_NbsMetaMibFeatureDesc_Type = DisplayString
_NbsMetaMibFeatureDesc_Object = MibTableColumn
nbsMetaMibFeatureDesc = _NbsMetaMibFeatureDesc_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 4),
    _NbsMetaMibFeatureDesc_Type()
)
nbsMetaMibFeatureDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureDesc.setStatus("current")


class _NbsMetaMibFeatureUnits_Type(DisplayString):
    """Custom type nbsMetaMibFeatureUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsMetaMibFeatureUnits_Type.__name__ = "DisplayString"
_NbsMetaMibFeatureUnits_Object = MibTableColumn
nbsMetaMibFeatureUnits = _NbsMetaMibFeatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 5),
    _NbsMetaMibFeatureUnits_Type()
)
nbsMetaMibFeatureUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureUnits.setStatus("current")


class _NbsMetaMibFeatureType_Type(Integer32):
    """Custom type nbsMetaMibFeatureType based on Integer32"""
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
        *(("enum", 1),
          ("string", 2),
          ("integer", 3),
          ("float", 4))
    )


_NbsMetaMibFeatureType_Type.__name__ = "Integer32"
_NbsMetaMibFeatureType_Object = MibTableColumn
nbsMetaMibFeatureType = _NbsMetaMibFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 6),
    _NbsMetaMibFeatureType_Type()
)
nbsMetaMibFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibFeatureType.setStatus("current")
_NbsMetaMibVariableTableSize_Type = Integer32
_NbsMetaMibVariableTableSize_Object = MibScalar
nbsMetaMibVariableTableSize = _NbsMetaMibVariableTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 3),
    _NbsMetaMibVariableTableSize_Type()
)
nbsMetaMibVariableTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableTableSize.setStatus("current")
_NbsMetaMibVariableTable_Object = MibTable
nbsMetaMibVariableTable = _NbsMetaMibVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4)
)
if mibBuilder.loadTexts:
    nbsMetaMibVariableTable.setStatus("current")
_NbsMetaMibVariableEntry_Object = MibTableRow
nbsMetaMibVariableEntry = _NbsMetaMibVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1)
)
nbsMetaMibVariableEntry.setIndexNames(
    (0, "NBS-META-MIB", "nbsMetaMibVariableIfIndex"),
    (0, "NBS-META-MIB", "nbsMetaMibVariableID"),
)
if mibBuilder.loadTexts:
    nbsMetaMibVariableEntry.setStatus("current")
_NbsMetaMibVariableIfIndex_Type = InterfaceIndex
_NbsMetaMibVariableIfIndex_Object = MibTableColumn
nbsMetaMibVariableIfIndex = _NbsMetaMibVariableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 1),
    _NbsMetaMibVariableIfIndex_Type()
)
nbsMetaMibVariableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsMetaMibVariableIfIndex.setStatus("current")
_NbsMetaMibVariableID_Type = Integer32
_NbsMetaMibVariableID_Object = MibTableColumn
nbsMetaMibVariableID = _NbsMetaMibVariableID_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 2),
    _NbsMetaMibVariableID_Type()
)
nbsMetaMibVariableID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsMetaMibVariableID.setStatus("current")


class _NbsMetaMibVariableCaps_Type(DisplayString):
    """Custom type nbsMetaMibVariableCaps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NbsMetaMibVariableCaps_Type.__name__ = "DisplayString"
_NbsMetaMibVariableCaps_Object = MibTableColumn
nbsMetaMibVariableCaps = _NbsMetaMibVariableCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 3),
    _NbsMetaMibVariableCaps_Type()
)
nbsMetaMibVariableCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableCaps.setStatus("current")


class _NbsMetaMibVariableDefault_Type(DisplayString):
    """Custom type nbsMetaMibVariableDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NbsMetaMibVariableDefault_Type.__name__ = "DisplayString"
_NbsMetaMibVariableDefault_Object = MibTableColumn
nbsMetaMibVariableDefault = _NbsMetaMibVariableDefault_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 4),
    _NbsMetaMibVariableDefault_Type()
)
nbsMetaMibVariableDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableDefault.setStatus("current")
_NbsMetaMibVariableJumper_Type = DisplayString
_NbsMetaMibVariableJumper_Object = MibTableColumn
nbsMetaMibVariableJumper = _NbsMetaMibVariableJumper_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 5),
    _NbsMetaMibVariableJumper_Type()
)
nbsMetaMibVariableJumper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableJumper.setStatus("current")


class _NbsMetaMibVariableOper_Type(DisplayString):
    """Custom type nbsMetaMibVariableOper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NbsMetaMibVariableOper_Type.__name__ = "DisplayString"
_NbsMetaMibVariableOper_Object = MibTableColumn
nbsMetaMibVariableOper = _NbsMetaMibVariableOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 6),
    _NbsMetaMibVariableOper_Type()
)
nbsMetaMibVariableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableOper.setStatus("current")


class _NbsMetaMibVariableAdmin_Type(DisplayString):
    """Custom type nbsMetaMibVariableAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NbsMetaMibVariableAdmin_Type.__name__ = "DisplayString"
_NbsMetaMibVariableAdmin_Object = MibTableColumn
nbsMetaMibVariableAdmin = _NbsMetaMibVariableAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 7),
    _NbsMetaMibVariableAdmin_Type()
)
nbsMetaMibVariableAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMetaMibVariableAdmin.setStatus("current")


class _NbsMetaMibVariableStatus_Type(DisplayString):
    """Custom type nbsMetaMibVariableStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NbsMetaMibVariableStatus_Type.__name__ = "DisplayString"
_NbsMetaMibVariableStatus_Object = MibTableColumn
nbsMetaMibVariableStatus = _NbsMetaMibVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 8),
    _NbsMetaMibVariableStatus_Type()
)
nbsMetaMibVariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMetaMibVariableStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-META-MIB",
    **{"nbsMetaMib": nbsMetaMib,
       "nbsMetaMibGrp": nbsMetaMibGrp,
       "nbsMetaMibFeatureTableSize": nbsMetaMibFeatureTableSize,
       "nbsMetaMibFeatureTable": nbsMetaMibFeatureTable,
       "nbsMetaMibFeatureEntry": nbsMetaMibFeatureEntry,
       "nbsMetaMibFeatureID": nbsMetaMibFeatureID,
       "nbsMetaMibFeatureFamily": nbsMetaMibFeatureFamily,
       "nbsMetaMibFeatureName": nbsMetaMibFeatureName,
       "nbsMetaMibFeatureDesc": nbsMetaMibFeatureDesc,
       "nbsMetaMibFeatureUnits": nbsMetaMibFeatureUnits,
       "nbsMetaMibFeatureType": nbsMetaMibFeatureType,
       "nbsMetaMibVariableTableSize": nbsMetaMibVariableTableSize,
       "nbsMetaMibVariableTable": nbsMetaMibVariableTable,
       "nbsMetaMibVariableEntry": nbsMetaMibVariableEntry,
       "nbsMetaMibVariableIfIndex": nbsMetaMibVariableIfIndex,
       "nbsMetaMibVariableID": nbsMetaMibVariableID,
       "nbsMetaMibVariableCaps": nbsMetaMibVariableCaps,
       "nbsMetaMibVariableDefault": nbsMetaMibVariableDefault,
       "nbsMetaMibVariableJumper": nbsMetaMibVariableJumper,
       "nbsMetaMibVariableOper": nbsMetaMibVariableOper,
       "nbsMetaMibVariableAdmin": nbsMetaMibVariableAdmin,
       "nbsMetaMibVariableStatus": nbsMetaMibVariableStatus}
)
