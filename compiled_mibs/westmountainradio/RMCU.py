# SNMP MIB module (RMCU) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\westmountainradio\RMCU
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:14 2025
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
 NotificationType,
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
    "NotificationType",
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

rr4005i = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15117, 1)
)
if mibBuilder.loadTexts:
    rr4005i.setRevisions(
        ("2017-10-11 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedDiv1000(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_Wmr_ObjectIdentity = ObjectIdentity
wmr = _Wmr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15117)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15117, 1, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Build_date_Type = DisplayString
_Build_date_Object = MibScalar
build_date = _Build_date_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 1, 3),
    _Build_date_Type()
)
build_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    build_date.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2)
)
_Analog1name_Type = DisplayString
_Analog1name_Object = MibScalar
analog1name = _Analog1name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 1),
    _Analog1name_Type()
)
analog1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog1name.setStatus("current")
_Analog1val_Type = DisplayString
_Analog1val_Object = MibScalar
analog1val = _Analog1val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 2),
    _Analog1val_Type()
)
analog1val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog1val.setStatus("current")
_Analog2name_Type = DisplayString
_Analog2name_Object = MibScalar
analog2name = _Analog2name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 3),
    _Analog2name_Type()
)
analog2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog2name.setStatus("current")
_Analog2val_Type = DisplayString
_Analog2val_Object = MibScalar
analog2val = _Analog2val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 4),
    _Analog2val_Type()
)
analog2val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog2val.setStatus("current")
_Analog3name_Type = DisplayString
_Analog3name_Object = MibScalar
analog3name = _Analog3name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 5),
    _Analog3name_Type()
)
analog3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog3name.setStatus("current")
_Analog3val_Type = DisplayString
_Analog3val_Object = MibScalar
analog3val = _Analog3val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 6),
    _Analog3val_Type()
)
analog3val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog3val.setStatus("current")
_Analog4name_Type = DisplayString
_Analog4name_Object = MibScalar
analog4name = _Analog4name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 7),
    _Analog4name_Type()
)
analog4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog4name.setStatus("current")
_Analog4val_Type = DisplayString
_Analog4val_Object = MibScalar
analog4val = _Analog4val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 8),
    _Analog4val_Type()
)
analog4val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog4val.setStatus("current")
_Analog5name_Type = DisplayString
_Analog5name_Object = MibScalar
analog5name = _Analog5name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 9),
    _Analog5name_Type()
)
analog5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog5name.setStatus("current")
_Analog5val_Type = DisplayString
_Analog5val_Object = MibScalar
analog5val = _Analog5val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 10),
    _Analog5val_Type()
)
analog5val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog5val.setStatus("current")
_Analog6name_Type = DisplayString
_Analog6name_Object = MibScalar
analog6name = _Analog6name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 11),
    _Analog6name_Type()
)
analog6name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog6name.setStatus("current")
_Analog6val_Type = DisplayString
_Analog6val_Object = MibScalar
analog6val = _Analog6val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 12),
    _Analog6val_Type()
)
analog6val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog6val.setStatus("current")
_Digout1name_Type = DisplayString
_Digout1name_Object = MibScalar
digout1name = _Digout1name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 65),
    _Digout1name_Type()
)
digout1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digout1name.setStatus("current")
_Digout1val_Type = Integer32
_Digout1val_Object = MibScalar
digout1val = _Digout1val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 66),
    _Digout1val_Type()
)
digout1val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout1val.setStatus("current")
_Digout2name_Type = DisplayString
_Digout2name_Object = MibScalar
digout2name = _Digout2name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 67),
    _Digout2name_Type()
)
digout2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digout2name.setStatus("current")
_Digout2val_Type = Integer32
_Digout2val_Object = MibScalar
digout2val = _Digout2val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 68),
    _Digout2val_Type()
)
digout2val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout2val.setStatus("current")
_Digout3name_Type = DisplayString
_Digout3name_Object = MibScalar
digout3name = _Digout3name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 69),
    _Digout3name_Type()
)
digout3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digout3name.setStatus("current")
_Digout3val_Type = Integer32
_Digout3val_Object = MibScalar
digout3val = _Digout3val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 70),
    _Digout3val_Type()
)
digout3val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout3val.setStatus("current")
_Digout4name_Type = DisplayString
_Digout4name_Object = MibScalar
digout4name = _Digout4name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 71),
    _Digout4name_Type()
)
digout4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digout4name.setStatus("current")
_Digout4val_Type = Integer32
_Digout4val_Object = MibScalar
digout4val = _Digout4val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 72),
    _Digout4val_Type()
)
digout4val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout4val.setStatus("current")
_Digout5name_Type = DisplayString
_Digout5name_Object = MibScalar
digout5name = _Digout5name_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 73),
    _Digout5name_Type()
)
digout5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digout5name.setStatus("current")
_Digout5val_Type = Integer32
_Digout5val_Object = MibScalar
digout5val = _Digout5val_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 2, 74),
    _Digout5val_Type()
)
digout5val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout5val.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3)
)
_Control_ints_ObjectIdentity = ObjectIdentity
control_ints = _Control_ints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4)
)
_Analog1val_int_Type = FixedDiv1000
_Analog1val_int_Object = MibScalar
analog1val_int = _Analog1val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 1),
    _Analog1val_int_Type()
)
analog1val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog1val_int.setStatus("current")
_Analog2val_int_Type = FixedDiv1000
_Analog2val_int_Object = MibScalar
analog2val_int = _Analog2val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 2),
    _Analog2val_int_Type()
)
analog2val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog2val_int.setStatus("current")
_Analog3val_int_Type = FixedDiv1000
_Analog3val_int_Object = MibScalar
analog3val_int = _Analog3val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 3),
    _Analog3val_int_Type()
)
analog3val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog3val_int.setStatus("current")
_Analog4val_int_Type = FixedDiv1000
_Analog4val_int_Object = MibScalar
analog4val_int = _Analog4val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 4),
    _Analog4val_int_Type()
)
analog4val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog4val_int.setStatus("current")
_Analog5val_int_Type = FixedDiv1000
_Analog5val_int_Object = MibScalar
analog5val_int = _Analog5val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 5),
    _Analog5val_int_Type()
)
analog5val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog5val_int.setStatus("current")
_Analog6val_int_Type = FixedDiv1000
_Analog6val_int_Object = MibScalar
analog6val_int = _Analog6val_int_Object(
    (1, 3, 6, 1, 4, 1, 15117, 1, 4, 6),
    _Analog6val_int_Type()
)
analog6val_int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog6val_int.setStatus("current")

# Managed Objects groups


# Notification objects

trap_auth = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 1)
)
if mibBuilder.loadTexts:
    trap_auth.setStatus(
        "current"
    )

trap_analog_over1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 2)
)
trap_analog_over1.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog1val"))
)
if mibBuilder.loadTexts:
    trap_analog_over1.setStatus(
        "current"
    )

trap_analog_over2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 3)
)
trap_analog_over2.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog2val"))
)
if mibBuilder.loadTexts:
    trap_analog_over2.setStatus(
        "current"
    )

trap_analog_over3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 4)
)
trap_analog_over3.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog3val"))
)
if mibBuilder.loadTexts:
    trap_analog_over3.setStatus(
        "current"
    )

trap_analog_over4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 5)
)
trap_analog_over4.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog4val"))
)
if mibBuilder.loadTexts:
    trap_analog_over4.setStatus(
        "current"
    )

trap_analog_over5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 6)
)
trap_analog_over5.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog5val"))
)
if mibBuilder.loadTexts:
    trap_analog_over5.setStatus(
        "current"
    )

trap_analog_over6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 7)
)
trap_analog_over6.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog6val"))
)
if mibBuilder.loadTexts:
    trap_analog_over6.setStatus(
        "current"
    )

trap_analog_under6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 23)
)
trap_analog_under6.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog6val"))
)
if mibBuilder.loadTexts:
    trap_analog_under6.setStatus(
        "current"
    )

trap_poweron = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 34)
)
trap_poweron.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_poweron.setStatus(
        "current"
    )

trap_test = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 52)
)
trap_test.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_test.setStatus(
        "current"
    )

trap_digout_inactive1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 72)
)
trap_digout_inactive1.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_inactive1.setStatus(
        "current"
    )

trap_digout_inactive2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 73)
)
trap_digout_inactive2.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_inactive2.setStatus(
        "current"
    )

trap_digout_inactive3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 74)
)
trap_digout_inactive3.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_inactive3.setStatus(
        "current"
    )

trap_digout_inactive4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 75)
)
trap_digout_inactive4.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_inactive4.setStatus(
        "current"
    )

trap_digout_inactive5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 76)
)
trap_digout_inactive5.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_inactive5.setStatus(
        "current"
    )

trap_digout_active1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 88)
)
trap_digout_active1.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_active1.setStatus(
        "current"
    )

trap_digout_active2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 89)
)
trap_digout_active2.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_active2.setStatus(
        "current"
    )

trap_digout_active3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 90)
)
trap_digout_active3.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_active3.setStatus(
        "current"
    )

trap_digout_active4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 91)
)
trap_digout_active4.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_active4.setStatus(
        "current"
    )

trap_digout_active5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 92)
)
trap_digout_active5.setObjects(
    ("RMCU", "name")
)
if mibBuilder.loadTexts:
    trap_digout_active5.setStatus(
        "current"
    )

trap_analog_urecover6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 109)
)
trap_analog_urecover6.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog6val"))
)
if mibBuilder.loadTexts:
    trap_analog_urecover6.setStatus(
        "current"
    )

trap_analog_orecover1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 120)
)
trap_analog_orecover1.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog1val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover1.setStatus(
        "current"
    )

trap_analog_orecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 121)
)
trap_analog_orecover2.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog2val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover2.setStatus(
        "current"
    )

trap_analog_orecover3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 122)
)
trap_analog_orecover3.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog3val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover3.setStatus(
        "current"
    )

trap_analog_orecover4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 123)
)
trap_analog_orecover4.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog4val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover4.setStatus(
        "current"
    )

trap_analog_orecover5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 124)
)
trap_analog_orecover5.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog5val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover5.setStatus(
        "current"
    )

trap_analog_orecover6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15117, 1, 3, 125)
)
trap_analog_orecover6.setObjects(
      *(("RMCU", "name"),
        ("RMCU", "analog6val"))
)
if mibBuilder.loadTexts:
    trap_analog_orecover6.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMCU",
    **{"FixedDiv1000": FixedDiv1000,
       "wmr": wmr,
       "rr4005i": rr4005i,
       "product": product,
       "name": name,
       "version": version,
       "build-date": build_date,
       "control": control,
       "analog1name": analog1name,
       "analog1val": analog1val,
       "analog2name": analog2name,
       "analog2val": analog2val,
       "analog3name": analog3name,
       "analog3val": analog3val,
       "analog4name": analog4name,
       "analog4val": analog4val,
       "analog5name": analog5name,
       "analog5val": analog5val,
       "analog6name": analog6name,
       "analog6val": analog6val,
       "digout1name": digout1name,
       "digout1val": digout1val,
       "digout2name": digout2name,
       "digout2val": digout2val,
       "digout3name": digout3name,
       "digout3val": digout3val,
       "digout4name": digout4name,
       "digout4val": digout4val,
       "digout5name": digout5name,
       "digout5val": digout5val,
       "traps": traps,
       "trap-auth": trap_auth,
       "trap-analog-over1": trap_analog_over1,
       "trap-analog-over2": trap_analog_over2,
       "trap-analog-over3": trap_analog_over3,
       "trap-analog-over4": trap_analog_over4,
       "trap-analog-over5": trap_analog_over5,
       "trap-analog-over6": trap_analog_over6,
       "trap-analog-under6": trap_analog_under6,
       "trap-poweron": trap_poweron,
       "trap-test": trap_test,
       "trap-digout-inactive1": trap_digout_inactive1,
       "trap-digout-inactive2": trap_digout_inactive2,
       "trap-digout-inactive3": trap_digout_inactive3,
       "trap-digout-inactive4": trap_digout_inactive4,
       "trap-digout-inactive5": trap_digout_inactive5,
       "trap-digout-active1": trap_digout_active1,
       "trap-digout-active2": trap_digout_active2,
       "trap-digout-active3": trap_digout_active3,
       "trap-digout-active4": trap_digout_active4,
       "trap-digout-active5": trap_digout_active5,
       "trap-analog-urecover6": trap_analog_urecover6,
       "trap-analog-orecover1": trap_analog_orecover1,
       "trap-analog-orecover2": trap_analog_orecover2,
       "trap-analog-orecover3": trap_analog_orecover3,
       "trap-analog-orecover4": trap_analog_orecover4,
       "trap-analog-orecover5": trap_analog_orecover5,
       "trap-analog-orecover6": trap_analog_orecover6,
       "control-ints": control_ints,
       "analog1val-int": analog1val_int,
       "analog2val-int": analog2val_int,
       "analog3val-int": analog3val_int,
       "analog4val-int": analog4val_int,
       "analog5val-int": analog5val_int,
       "analog6val-int": analog6val_int}
)
