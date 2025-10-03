# SNMP MIB module (CTRON-SFPS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:23 2025
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

(sfpsChassisRipAPI,
 sfpsChassisRipTable) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsChassisRipAPI",
    "sfpsChassisRipTable")

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



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsChassisRipChassisMac_Type = OctetString
_SfpsChassisRipChassisMac_Object = MibScalar
sfpsChassisRipChassisMac = _SfpsChassisRipChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1),
    _SfpsChassisRipChassisMac_Type()
)
sfpsChassisRipChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipChassisMac.setStatus("mandatory")
_SfpsChassisRipFPPortMask_Type = OctetString
_SfpsChassisRipFPPortMask_Object = MibScalar
sfpsChassisRipFPPortMask = _SfpsChassisRipFPPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2),
    _SfpsChassisRipFPPortMask_Type()
)
sfpsChassisRipFPPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipFPPortMask.setStatus("mandatory")
_SfpsChassisRipINBPortMask_Type = OctetString
_SfpsChassisRipINBPortMask_Object = MibScalar
sfpsChassisRipINBPortMask = _SfpsChassisRipINBPortMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3),
    _SfpsChassisRipINBPortMask_Type()
)
sfpsChassisRipINBPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipINBPortMask.setStatus("mandatory")
_SfpsChassisRipModifiedTime_Type = TimeTicks
_SfpsChassisRipModifiedTime_Object = MibScalar
sfpsChassisRipModifiedTime = _SfpsChassisRipModifiedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4),
    _SfpsChassisRipModifiedTime_Type()
)
sfpsChassisRipModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipModifiedTime.setStatus("mandatory")


class _SfpsChassisRipStatus_Type(Integer32):
    """Custom type sfpsChassisRipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("dead", 3))
    )


_SfpsChassisRipStatus_Type.__name__ = "Integer32"
_SfpsChassisRipStatus_Object = MibScalar
sfpsChassisRipStatus = _SfpsChassisRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5),
    _SfpsChassisRipStatus_Type()
)
sfpsChassisRipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipStatus.setStatus("mandatory")


class _SfpsChassisRipAPIVerb_Type(Integer32):
    """Custom type sfpsChassisRipAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("add", 2),
          ("delete", 3),
          ("purgePort", 4),
          ("sendUpdate", 5),
          ("clearTable", 6),
          ("setTimer", 7))
    )


_SfpsChassisRipAPIVerb_Type.__name__ = "Integer32"
_SfpsChassisRipAPIVerb_Object = MibScalar
sfpsChassisRipAPIVerb = _SfpsChassisRipAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1),
    _SfpsChassisRipAPIVerb_Type()
)
sfpsChassisRipAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIVerb.setStatus("mandatory")
_SfpsChassisRipAPIChassisMac_Type = SfpsAddress
_SfpsChassisRipAPIChassisMac_Object = MibScalar
sfpsChassisRipAPIChassisMac = _SfpsChassisRipAPIChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2),
    _SfpsChassisRipAPIChassisMac_Type()
)
sfpsChassisRipAPIChassisMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIChassisMac.setStatus("mandatory")
_SfpsChassisRipAPIPort_Type = Integer32
_SfpsChassisRipAPIPort_Object = MibScalar
sfpsChassisRipAPIPort = _SfpsChassisRipAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3),
    _SfpsChassisRipAPIPort_Type()
)
sfpsChassisRipAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPIPort.setStatus("mandatory")
_SfpsChassisRipAPITimer_Type = Integer32
_SfpsChassisRipAPITimer_Object = MibScalar
sfpsChassisRipAPITimer = _SfpsChassisRipAPITimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4),
    _SfpsChassisRipAPITimer_Type()
)
sfpsChassisRipAPITimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsChassisRipAPITimer.setStatus("mandatory")
_SfpsChassisRipAPINumInTable_Type = Integer32
_SfpsChassisRipAPINumInTable_Object = MibScalar
sfpsChassisRipAPINumInTable = _SfpsChassisRipAPINumInTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5),
    _SfpsChassisRipAPINumInTable_Type()
)
sfpsChassisRipAPINumInTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsChassisRipAPINumInTable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-CHASSIS-MIB",
    **{"SfpsAddress": SfpsAddress,
       "sfpsChassisRipChassisMac": sfpsChassisRipChassisMac,
       "sfpsChassisRipFPPortMask": sfpsChassisRipFPPortMask,
       "sfpsChassisRipINBPortMask": sfpsChassisRipINBPortMask,
       "sfpsChassisRipModifiedTime": sfpsChassisRipModifiedTime,
       "sfpsChassisRipStatus": sfpsChassisRipStatus,
       "sfpsChassisRipAPIVerb": sfpsChassisRipAPIVerb,
       "sfpsChassisRipAPIChassisMac": sfpsChassisRipAPIChassisMac,
       "sfpsChassisRipAPIPort": sfpsChassisRipAPIPort,
       "sfpsChassisRipAPITimer": sfpsChassisRipAPITimer,
       "sfpsChassisRipAPINumInTable": sfpsChassisRipAPINumInTable}
)
