# SNMP MIB module (NSCRTV-HFCEMS-OPTICALAMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\glassway\NSCRTV-HFCEMS-OPTICALAMPLIFIER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:00 2025
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

(oaIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "oaIdent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OaVendorOID_Type = ObjectIdentifier
_OaVendorOID_Object = MibScalar
oaVendorOID = _OaVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 1),
    _OaVendorOID_Type()
)
oaVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVendorOID.setStatus("optional")


class _OaOutputOpticalPower_Type(Integer32):
    """Custom type oaOutputOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaOutputOpticalPower_Type.__name__ = "Integer32"
_OaOutputOpticalPower_Object = MibScalar
oaOutputOpticalPower = _OaOutputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 2),
    _OaOutputOpticalPower_Type()
)
oaOutputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaOutputOpticalPower.setStatus("mandatory")


class _OaInputOpticalPower_Type(Integer32):
    """Custom type oaInputOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_OaInputOpticalPower_Type.__name__ = "Integer32"
_OaInputOpticalPower_Object = MibScalar
oaInputOpticalPower = _OaInputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 3),
    _OaInputOpticalPower_Type()
)
oaInputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputOpticalPower.setStatus("mandatory")
_OaPumpTable_Object = MibTable
oaPumpTable = _OaPumpTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4)
)
if mibBuilder.loadTexts:
    oaPumpTable.setStatus("mandatory")
_OaPumpEntry_Object = MibTableRow
oaPumpEntry = _OaPumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1)
)
oaPumpEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-OPTICALAMPLIFIER-MIB", "oaPumpIndex"),
)
if mibBuilder.loadTexts:
    oaPumpEntry.setStatus("mandatory")
_OaPumpIndex_Type = Integer32
_OaPumpIndex_Object = MibTableColumn
oaPumpIndex = _OaPumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 1),
    _OaPumpIndex_Type()
)
oaPumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpIndex.setStatus("mandatory")


class _OaPumpBIAS_Type(Integer32):
    """Custom type oaPumpBIAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaPumpBIAS_Type.__name__ = "Integer32"
_OaPumpBIAS_Object = MibTableColumn
oaPumpBIAS = _OaPumpBIAS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 2),
    _OaPumpBIAS_Type()
)
oaPumpBIAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpBIAS.setStatus("mandatory")


class _OaPumpTEC_Type(Integer32):
    """Custom type oaPumpTEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OaPumpTEC_Type.__name__ = "Integer32"
_OaPumpTEC_Object = MibTableColumn
oaPumpTEC = _OaPumpTEC_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 3),
    _OaPumpTEC_Type()
)
oaPumpTEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpTEC.setStatus("optional")


class _OaPumpTemp_Type(Integer32):
    """Custom type oaPumpTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_OaPumpTemp_Type.__name__ = "Integer32"
_OaPumpTemp_Object = MibTableColumn
oaPumpTemp = _OaPumpTemp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 4),
    _OaPumpTemp_Type()
)
oaPumpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpTemp.setStatus("mandatory")


class _OaNumberDCPowerSupply_Type(Integer32):
    """Custom type oaNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OaNumberDCPowerSupply_Type.__name__ = "Integer32"
_OaNumberDCPowerSupply_Object = MibScalar
oaNumberDCPowerSupply = _OaNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 5),
    _OaNumberDCPowerSupply_Type()
)
oaNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaNumberDCPowerSupply.setStatus("mandatory")


class _OaDCPowerSupplyMode_Type(Integer32):
    """Custom type oaDCPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadsharing", 1),
          ("switchedRedundant", 2),
          ("aloneSupply", 3))
    )


_OaDCPowerSupplyMode_Type.__name__ = "Integer32"
_OaDCPowerSupplyMode_Object = MibScalar
oaDCPowerSupplyMode = _OaDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 6),
    _OaDCPowerSupplyMode_Type()
)
oaDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerSupplyMode.setStatus("optional")
_OaDCPowerTable_Object = MibTable
oaDCPowerTable = _OaDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7)
)
if mibBuilder.loadTexts:
    oaDCPowerTable.setStatus("mandatory")
_OaDCPowerEntry_Object = MibTableRow
oaDCPowerEntry = _OaDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1)
)
oaDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-OPTICALAMPLIFIER-MIB", "oaDCPowerIndex"),
)
if mibBuilder.loadTexts:
    oaDCPowerEntry.setStatus("mandatory")
_OaDCPowerIndex_Type = Integer32
_OaDCPowerIndex_Object = MibTableColumn
oaDCPowerIndex = _OaDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 1),
    _OaDCPowerIndex_Type()
)
oaDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerIndex.setStatus("mandatory")


class _OaDCPowerVoltage_Type(Integer32):
    """Custom type oaDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OaDCPowerVoltage_Type.__name__ = "Integer32"
_OaDCPowerVoltage_Object = MibTableColumn
oaDCPowerVoltage = _OaDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 2),
    _OaDCPowerVoltage_Type()
)
oaDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerVoltage.setStatus("mandatory")


class _OaDCPowerCurrent_Type(Integer32):
    """Custom type oaDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaDCPowerCurrent_Type.__name__ = "Integer32"
_OaDCPowerCurrent_Object = MibTableColumn
oaDCPowerCurrent = _OaDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 3),
    _OaDCPowerCurrent_Type()
)
oaDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerCurrent.setStatus("mandatory")
_OaDCPowerName_Type = DisplayString
_OaDCPowerName_Object = MibTableColumn
oaDCPowerName = _OaDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 4),
    _OaDCPowerName_Type()
)
oaDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-OPTICALAMPLIFIER-MIB",
    **{"oaVendorOID": oaVendorOID,
       "oaOutputOpticalPower": oaOutputOpticalPower,
       "oaInputOpticalPower": oaInputOpticalPower,
       "oaPumpTable": oaPumpTable,
       "oaPumpEntry": oaPumpEntry,
       "oaPumpIndex": oaPumpIndex,
       "oaPumpBIAS": oaPumpBIAS,
       "oaPumpTEC": oaPumpTEC,
       "oaPumpTemp": oaPumpTemp,
       "oaNumberDCPowerSupply": oaNumberDCPowerSupply,
       "oaDCPowerSupplyMode": oaDCPowerSupplyMode,
       "oaDCPowerTable": oaDCPowerTable,
       "oaDCPowerEntry": oaDCPowerEntry,
       "oaDCPowerIndex": oaDCPowerIndex,
       "oaDCPowerVoltage": oaDCPowerVoltage,
       "oaDCPowerCurrent": oaDCPowerCurrent,
       "oaDCPowerName": oaDCPowerName}
)
