# SNMP MIB module (ARRIS-CM-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-CM-DEVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:11 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisCmDevMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arrisCmDevMib.setRevisions(
        ("1902-11-08 00:00",
         "1902-10-29 00:00",
         "1902-10-23 00:00",
         "1902-07-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ArrsCmDevProvMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("docsisOnly", 0),
          ("fullPacketCable", 1),
          ("packetCableMinusKDC", 2),
          ("cps", 3),
          ("gupi", 4),
          ("singleMAC", 5))
    )



# MIB Managed Objects in the order of their OIDs

_ArrisCmDevMibObjects_ObjectIdentity = ObjectIdentity
arrisCmDevMibObjects = _ArrisCmDevMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1)
)
_ArrisCmDevBase_ObjectIdentity = ObjectIdentity
arrisCmDevBase = _ArrisCmDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1)
)


class _ArrisCmDevWanIsolationState_Type(Integer32):
    """Custom type arrisCmDevWanIsolationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-InActiveMode", 1),
          ("on-ActiveMode", 2))
    )


_ArrisCmDevWanIsolationState_Type.__name__ = "Integer32"
_ArrisCmDevWanIsolationState_Object = MibScalar
arrisCmDevWanIsolationState = _ArrisCmDevWanIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 1),
    _ArrisCmDevWanIsolationState_Type()
)
arrisCmDevWanIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisCmDevWanIsolationState.setStatus("current")
_ArrisCmDevSwImageName_Type = DisplayString
_ArrisCmDevSwImageName_Object = MibScalar
arrisCmDevSwImageName = _ArrisCmDevSwImageName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 2),
    _ArrisCmDevSwImageName_Type()
)
arrisCmDevSwImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisCmDevSwImageName.setStatus("current")
_ArrisCmDevSwImageBuildTime_Type = DisplayString
_ArrisCmDevSwImageBuildTime_Object = MibScalar
arrisCmDevSwImageBuildTime = _ArrisCmDevSwImageBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 3),
    _ArrisCmDevSwImageBuildTime_Type()
)
arrisCmDevSwImageBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisCmDevSwImageBuildTime.setStatus("current")
_ArrisCmDevCmSetup_ObjectIdentity = ObjectIdentity
arrisCmDevCmSetup = _ArrisCmDevCmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2)
)
_ArrisCmDevPermanentSetup_ObjectIdentity = ObjectIdentity
arrisCmDevPermanentSetup = _ArrisCmDevPermanentSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 2)
)
_ArrisCmDevOperationalSetup_ObjectIdentity = ObjectIdentity
arrisCmDevOperationalSetup = _ArrisCmDevOperationalSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3)
)
_ArrisCmDevProvMethodIndicator_Type = ArrsCmDevProvMethod
_ArrisCmDevProvMethodIndicator_Object = MibScalar
arrisCmDevProvMethodIndicator = _ArrisCmDevProvMethodIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 2),
    _ArrisCmDevProvMethodIndicator_Type()
)
arrisCmDevProvMethodIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisCmDevProvMethodIndicator.setStatus("current")
_ArrisCmDevEnableDocsis20_Type = TruthValue
_ArrisCmDevEnableDocsis20_Object = MibScalar
arrisCmDevEnableDocsis20 = _ArrisCmDevEnableDocsis20_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 3),
    _ArrisCmDevEnableDocsis20_Type()
)
arrisCmDevEnableDocsis20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisCmDevEnableDocsis20.setStatus("current")
_ArrisCmDevSalesSetup_ObjectIdentity = ObjectIdentity
arrisCmDevSalesSetup = _ArrisCmDevSalesSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 4)
)
_ArrisCmDevCmTest_ObjectIdentity = ObjectIdentity
arrisCmDevCmTest = _ArrisCmDevCmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3)
)
_ArrisCmDevManufacturingTest_ObjectIdentity = ObjectIdentity
arrisCmDevManufacturingTest = _ArrisCmDevManufacturingTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 2)
)
_ArrisCmDevOperationalTest_ObjectIdentity = ObjectIdentity
arrisCmDevOperationalTest = _ArrisCmDevOperationalTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-CM-DEVICE-MIB",
    **{"ArrsCmDevProvMethod": ArrsCmDevProvMethod,
       "arrisCmDevMib": arrisCmDevMib,
       "arrisCmDevMibObjects": arrisCmDevMibObjects,
       "arrisCmDevBase": arrisCmDevBase,
       "arrisCmDevWanIsolationState": arrisCmDevWanIsolationState,
       "arrisCmDevSwImageName": arrisCmDevSwImageName,
       "arrisCmDevSwImageBuildTime": arrisCmDevSwImageBuildTime,
       "arrisCmDevCmSetup": arrisCmDevCmSetup,
       "arrisCmDevPermanentSetup": arrisCmDevPermanentSetup,
       "arrisCmDevOperationalSetup": arrisCmDevOperationalSetup,
       "arrisCmDevProvMethodIndicator": arrisCmDevProvMethodIndicator,
       "arrisCmDevEnableDocsis20": arrisCmDevEnableDocsis20,
       "arrisCmDevSalesSetup": arrisCmDevSalesSetup,
       "arrisCmDevCmTest": arrisCmDevCmTest,
       "arrisCmDevManufacturingTest": arrisCmDevManufacturingTest,
       "arrisCmDevOperationalTest": arrisCmDevOperationalTest}
)
