# SNMP MIB module (HH3C-CATV-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-CATV-TRANSCEIVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:51 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cCATVTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cCATVTransStatus_ObjectIdentity = ObjectIdentity
hh3cCATVTransStatus = _Hh3cCATVTransStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1)
)
_Hh3cCATVTransStatusScalarObjects_ObjectIdentity = ObjectIdentity
hh3cCATVTransStatusScalarObjects = _Hh3cCATVTransStatusScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1, 1)
)


class _Hh3cCATVTransState_Type(Integer32):
    """Custom type hh3cCATVTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Hh3cCATVTransState_Type.__name__ = "Integer32"
_Hh3cCATVTransState_Object = MibScalar
hh3cCATVTransState = _Hh3cCATVTransState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1, 1, 1),
    _Hh3cCATVTransState_Type()
)
hh3cCATVTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCATVTransState.setStatus("current")
_Hh3cCATVTransInputPwr_Type = Integer32
_Hh3cCATVTransInputPwr_Object = MibScalar
hh3cCATVTransInputPwr = _Hh3cCATVTransInputPwr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1, 1, 2),
    _Hh3cCATVTransInputPwr_Type()
)
hh3cCATVTransInputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwr.setUnits("dbm")
_Hh3cCATVTransOutputLevel_Type = Integer32
_Hh3cCATVTransOutputLevel_Object = MibScalar
hh3cCATVTransOutputLevel = _Hh3cCATVTransOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1, 1, 3),
    _Hh3cCATVTransOutputLevel_Type()
)
hh3cCATVTransOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLevel.setUnits("dbuv")
_Hh3cCATVTransTemperature_Type = Integer32
_Hh3cCATVTransTemperature_Object = MibScalar
hh3cCATVTransTemperature = _Hh3cCATVTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 1, 1, 4),
    _Hh3cCATVTransTemperature_Type()
)
hh3cCATVTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCATVTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCATVTransTemperature.setUnits("centigrade")
_Hh3cCATVTransceiverMan_ObjectIdentity = ObjectIdentity
hh3cCATVTransceiverMan = _Hh3cCATVTransceiverMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 2)
)
_Hh3cCATVTransCtrlScalarObjects_ObjectIdentity = ObjectIdentity
hh3cCATVTransCtrlScalarObjects = _Hh3cCATVTransCtrlScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 2, 1)
)
_Hh3cCATVTransInputPwrLowerThr_Type = Integer32
_Hh3cCATVTransInputPwrLowerThr_Object = MibScalar
hh3cCATVTransInputPwrLowerThr = _Hh3cCATVTransInputPwrLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 2, 1, 1),
    _Hh3cCATVTransInputPwrLowerThr_Type()
)
hh3cCATVTransInputPwrLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwrLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwrLowerThr.setUnits("dbm")
_Hh3cCATVTransOutputLvlLowerThr_Type = Integer32
_Hh3cCATVTransOutputLvlLowerThr_Object = MibScalar
hh3cCATVTransOutputLvlLowerThr = _Hh3cCATVTransOutputLvlLowerThr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 2, 1, 2),
    _Hh3cCATVTransOutputLvlLowerThr_Type()
)
hh3cCATVTransOutputLvlLowerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLvlLowerThr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLvlLowerThr.setUnits("dbuv")
_Hh3cCATVTransTempratureUpperThr_Type = Integer32
_Hh3cCATVTransTempratureUpperThr_Object = MibScalar
hh3cCATVTransTempratureUpperThr = _Hh3cCATVTransTempratureUpperThr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 2, 1, 3),
    _Hh3cCATVTransTempratureUpperThr_Type()
)
hh3cCATVTransTempratureUpperThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCATVTransTempratureUpperThr.setStatus("current")
_Hh3cCATVTansTrap_ObjectIdentity = ObjectIdentity
hh3cCATVTansTrap = _Hh3cCATVTansTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3)
)
_Hh3cCATVTransTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cCATVTransTrapPrefix = _Hh3cCATVTransTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cCATVTransInputPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 1)
)
hh3cCATVTransInputPwrTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwrTrap.setStatus(
        "current"
    )

hh3cCATVTransInputPwrReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 2)
)
hh3cCATVTransInputPwrReTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransInputPwr")
)
if mibBuilder.loadTexts:
    hh3cCATVTransInputPwrReTrap.setStatus(
        "current"
    )

hh3cCATVTransOutputLvlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 3)
)
hh3cCATVTransOutputLvlTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLvlTrap.setStatus(
        "current"
    )

hh3cCATVTransOutputLvlReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 4)
)
hh3cCATVTransOutputLvlReTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransOutputLevel")
)
if mibBuilder.loadTexts:
    hh3cCATVTransOutputLvlReTrap.setStatus(
        "current"
    )

hh3cCATVTransTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 5)
)
hh3cCATVTransTemperatureTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransTemperature")
)
if mibBuilder.loadTexts:
    hh3cCATVTransTemperatureTrap.setStatus(
        "current"
    )

hh3cCATVTransTemperatureReTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94, 3, 0, 6)
)
hh3cCATVTransTemperatureReTrap.setObjects(
    ("HH3C-CATV-TRANSCEIVER-MIB", "hh3cCATVTransTemperature")
)
if mibBuilder.loadTexts:
    hh3cCATVTransTemperatureReTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CATV-TRANSCEIVER-MIB",
    **{"hh3cCATVTransceiver": hh3cCATVTransceiver,
       "hh3cCATVTransStatus": hh3cCATVTransStatus,
       "hh3cCATVTransStatusScalarObjects": hh3cCATVTransStatusScalarObjects,
       "hh3cCATVTransState": hh3cCATVTransState,
       "hh3cCATVTransInputPwr": hh3cCATVTransInputPwr,
       "hh3cCATVTransOutputLevel": hh3cCATVTransOutputLevel,
       "hh3cCATVTransTemperature": hh3cCATVTransTemperature,
       "hh3cCATVTransceiverMan": hh3cCATVTransceiverMan,
       "hh3cCATVTransCtrlScalarObjects": hh3cCATVTransCtrlScalarObjects,
       "hh3cCATVTransInputPwrLowerThr": hh3cCATVTransInputPwrLowerThr,
       "hh3cCATVTransOutputLvlLowerThr": hh3cCATVTransOutputLvlLowerThr,
       "hh3cCATVTransTempratureUpperThr": hh3cCATVTransTempratureUpperThr,
       "hh3cCATVTansTrap": hh3cCATVTansTrap,
       "hh3cCATVTransTrapPrefix": hh3cCATVTransTrapPrefix,
       "hh3cCATVTransInputPwrTrap": hh3cCATVTransInputPwrTrap,
       "hh3cCATVTransInputPwrReTrap": hh3cCATVTransInputPwrReTrap,
       "hh3cCATVTransOutputLvlTrap": hh3cCATVTransOutputLvlTrap,
       "hh3cCATVTransOutputLvlReTrap": hh3cCATVTransOutputLvlReTrap,
       "hh3cCATVTransTemperatureTrap": hh3cCATVTransTemperatureTrap,
       "hh3cCATVTransTemperatureReTrap": hh3cCATVTransTemperatureReTrap}
)
