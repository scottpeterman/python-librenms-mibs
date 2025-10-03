# SNMP MIB module (TEL2N-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\2n\TEL2N-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:13:53 2025
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

tel2n = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6530)
)
if mibBuilder.loadTexts:
    tel2n.setRevisions(
        ("2015-05-01 10:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Heliosip_ObjectIdentity = ObjectIdentity
heliosip = _Heliosip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6530, 11)
)
_HipProductName_Type = OctetString
_HipProductName_Object = MibScalar
hipProductName = _HipProductName_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 1),
    _HipProductName_Type()
)
hipProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipProductName.setStatus("current")
_HipHwVersion_Type = OctetString
_HipHwVersion_Object = MibScalar
hipHwVersion = _HipHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 2),
    _HipHwVersion_Type()
)
hipHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipHwVersion.setStatus("current")


class _HipSerial_Type(OctetString):
    """Custom type hipSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_HipSerial_Type.__name__ = "OctetString"
_HipSerial_Object = MibScalar
hipSerial = _HipSerial_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 3),
    _HipSerial_Type()
)
hipSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipSerial.setStatus("current")


class _HipVersion_Type(OctetString):
    """Custom type hipVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_HipVersion_Type.__name__ = "OctetString"
_HipVersion_Object = MibScalar
hipVersion = _HipVersion_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 4),
    _HipVersion_Type()
)
hipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipVersion.setStatus("current")
_HipBootVersion_Type = OctetString
_HipBootVersion_Object = MibScalar
hipBootVersion = _HipBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 5),
    _HipBootVersion_Type()
)
hipBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipBootVersion.setStatus("current")
_HipSipTable_Object = MibTable
hipSipTable = _HipSipTable_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6)
)
if mibBuilder.loadTexts:
    hipSipTable.setStatus("current")
_HipSipEntry_Object = MibTableRow
hipSipEntry = _HipSipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1)
)
hipSipEntry.setIndexNames(
    (0, "TEL2N-MIB", "hipIndex"),
)
if mibBuilder.loadTexts:
    hipSipEntry.setStatus("current")
_HipIndex_Type = Integer32
_HipIndex_Object = MibTableColumn
hipIndex = _HipIndex_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 1),
    _HipIndex_Type()
)
hipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipIndex.setStatus("current")
_HipPhoneNumber_Type = OctetString
_HipPhoneNumber_Object = MibTableColumn
hipPhoneNumber = _HipPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 2),
    _HipPhoneNumber_Type()
)
hipPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipPhoneNumber.setStatus("current")


class _HipState_Type(Integer32):
    """Custom type hipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("goingup", 1),
          ("up", 2),
          ("goingdown", 3))
    )


_HipState_Type.__name__ = "Integer32"
_HipState_Object = MibTableColumn
hipState = _HipState_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 3),
    _HipState_Type()
)
hipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipState.setStatus("current")
_HipRegistrationAt_Type = IpAddress
_HipRegistrationAt_Object = MibTableColumn
hipRegistrationAt = _HipRegistrationAt_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 4),
    _HipRegistrationAt_Type()
)
hipRegistrationAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipRegistrationAt.setStatus("current")
_HipRegistrationTime_Type = TimeTicks
_HipRegistrationTime_Object = MibTableColumn
hipRegistrationTime = _HipRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 5),
    _HipRegistrationTime_Type()
)
hipRegistrationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hipRegistrationTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TEL2N-MIB",
    **{"tel2n": tel2n,
       "heliosip": heliosip,
       "hipProductName": hipProductName,
       "hipHwVersion": hipHwVersion,
       "hipSerial": hipSerial,
       "hipVersion": hipVersion,
       "hipBootVersion": hipBootVersion,
       "hipSipTable": hipSipTable,
       "hipSipEntry": hipSipEntry,
       "hipIndex": hipIndex,
       "hipPhoneNumber": hipPhoneNumber,
       "hipState": hipState,
       "hipRegistrationAt": hipRegistrationAt,
       "hipRegistrationTime": hipRegistrationTime}
)
